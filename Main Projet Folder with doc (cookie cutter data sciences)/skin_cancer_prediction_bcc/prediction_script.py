import os
import numpy as np
import pandas as pd
from PIL import Image
import pickle
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import cv2
import warnings
from typing import Union, Tuple, Dict, Optional, List
import logging
import re


def extraire_premier_nombre(chaine):
    nombre = ""
    for caractere in chaine:
        if caractere.isdigit():
            nombre += caractere
        elif nombre:
            break
    return int(nombre) if nombre else None


# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PreprocesseurImage:
    """Classe pour gérer le prétraitement des images."""

    @staticmethod
    def redimensionner_image(image: np.ndarray, taille: str) -> np.ndarray:
        """Redimensionne l'image à la taille spécifiée."""
        dimensions = int(taille.split('x')[0])
        return cv2.resize(image, (dimensions, dimensions), interpolation=cv2.INTER_AREA)

    @staticmethod
    def normaliser_image(image: np.ndarray) -> np.ndarray:
        """Normalise les valeurs des pixels."""
        return image.astype('float32') / 255.0

    @staticmethod
    def determiner_type_image(image: np.ndarray) -> str:
        """Détermine si l'image est en couleur ou noir et blanc."""
        return 'RGB' if len(image.shape) == 3 else 'L'

    @staticmethod
    def convertir_format(image: np.ndarray) -> np.ndarray:
        """Convertit l'image en format approprié pour le modèle."""
        return image.flatten()


class PreprocesseurMetadonnees:
    """Classe pour gérer le prétraitement des métadonnées."""

    def __init__(self):
        self.scaler = MinMaxScaler()
        self.localisations = [
            'acral', 'back', 'chest', 'ear', 'face', 'foot', 'genital',
            'hand', 'lower extremity', 'neck', 'scalp', 'trunk',
            'unknown', 'upper extremity'
        ]

    def encoder_localisation(self, localisation: str) -> np.ndarray:
        """Encode la localisation en format one-hot."""
        encodage = np.zeros(len(self.localisations))
        try:
            index = self.localisations.index(localisation.lower())
            encodage[index] = 1
        except ValueError:
            warnings.warn(f"Localisation '{localisation}' inconnue. Utilisation de 'unknown'.")
            index = self.localisations.index('unknown')
            encodage[index] = 1
        return encodage

    def standardiser_age(self, age: float) -> float:
        """Standardise l'âge du patient."""
        return self.scaler.fit_transform([[age]])[0][0]


class GestionnairePrediction:
    """Classe principale pour gérer les prédictions."""

    def __init__(self):
        self.preprocesseur_image = PreprocesseurImage()
        self.preprocesseur_metadonnees = PreprocesseurMetadonnees()
        self.modeles = {}
        self.chemin_base_modeles = '../models'

    def charger_modele(self, type_modele: str, taille: str, type_image: str) -> object:
        """Charge le modèle approprié selon les paramètres."""
        taille1Chiffre = extraire_premier_nombre(taille)
        nom_fichier = f"model_{type_modele}_{taille1Chiffre}{type_image}.pkl"

        if type_modele == 'lr' or type_modele == 'logreg':
            chemin = os.path.join(self.chemin_base_modeles, 'LOGISTIC REGRESSION', nom_fichier)
        elif type_modele == 'rf':
            chemin = os.path.join(self.chemin_base_modeles, 'RANDOM FOREST', nom_fichier)
        elif type_modele == 'dt':
            chemin = os.path.join(self.chemin_base_modeles, 'DESCISION THREE', nom_fichier)
        else:
            raise ValueError(f"Type de modèle non supporté: {type_modele}")

        try:
            with open(chemin, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Modèle non trouvé: {chemin}")

    def preparer_donnees(
            self,
            chemin_image: str,
            age: float,
            localisation: str,
            taille: str
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Prépare les données pour la prédiction."""
        # Traitement de l'image
        image = cv2.imread(chemin_image)
        if image is None:
            raise ValueError(f"Impossible de lire l'image: {chemin_image}")

        image_redim = self.preprocesseur_image.redimensionner_image(image, taille)
        image_norm = self.preprocesseur_image.normaliser_image(image_redim)
        type_image = self.preprocesseur_image.determiner_type_image(image_norm)
        image_finale = self.preprocesseur_image.convertir_format(image_norm)

        # Traitement des métadonnées
        age_std = self.preprocesseur_metadonnees.standardiser_age(age)
        loc_encoded = self.preprocesseur_metadonnees.encoder_localisation(localisation)

        # Combinaison des données
        return np.concatenate([image_finale, [age_std], loc_encoded])

    def predire(
            self,
            chemin_image: str,
            age: float,
            localisation: str,
            taille: str = '28x28',
            type_modele: str = 'all'
    ) -> Dict:
        """Fonction principale de prédiction."""
        resultats = {}

        try:
            X = self.preparer_donnees(chemin_image, age, localisation, taille)

            if type_modele == 'all':
                modeles = ['logreg', 'rf', 'dt']
            else:
                modeles = [type_modele]

            for modele in modeles:
                clf = self.charger_modele(modele, taille, 'RGB')
                proba = clf.predict_proba([X])[0]
                prediction = clf.predict([X])[0]

                resultats[modele] = {
                    'prediction': bool(prediction),
                    'probabilite': float(proba[1]),
                    'confiance': f"{proba[1] * 100:.2f}%"
                }

            if type_modele != 'all':
                return resultats[type_modele]

            return resultats

        except Exception as e:
            logger.error(f"Erreur lors de la prédiction: {str(e)}")
            raise


def predict_bcc(
        chemin_image: str,
        age: float,
        localisation: str,
        taille: str = '28x28',
        type_modele: str = 'all'
) -> Dict:
    """
    Fonction principale pour la prédiction de BCC.

    Args:
        chemin_image (str): Chemin vers l'image à analyser
        age (float): Âge du patient
        localisation (str): Localisation de la lésion
        taille (str, optional): Taille désirée ('8x8' ou '28x28'). Défaut '28x28'
        type_modele (str, optional): Type de modèle ('rf', 'lr', 'dt', 'all'). Défaut 'all'

    Returns:
        Dict: Résultats de la prédiction
    """
    try:
        gestionnaire = GestionnairePrediction()
        resultats = gestionnaire.predire(chemin_image, age, localisation, taille, type_modele)

        # Affichage des résultats
        if type_modele == 'all':
            print("\n=== Résultats de la prédiction BCC ===")
            for modele, res in resultats.items():
                print(f"\nModèle {modele.upper()}:")
                print(f"Prédiction: {'BCC détecté' if res['prediction'] else 'Pas de BCC'}")
                print(f"Confiance: {res['confiance']}")
        else:
            print("\n=== Résultat de la prédiction BCC ===")
            print(f"Prédiction: {'BCC détecté' if resultats['prediction'] else 'Pas de BCC'}")
            print(f"Confiance: {resultats['confiance']}")

        return resultats

    except Exception as e:
        print(f"\nErreur lors de la prédiction: {str(e)}")
        raise


# Exemple
if __name__ == "__main__":
    try:
        resultat = predict_bcc(
            chemin_image="data/test.png",
            age=65,
            localisation="face",
            taille="28x28",
            type_modele="all"
        )
        print("\nPrédiction réussie!")
    except Exception as e:
        print(f"Erreur: {str(e)}")