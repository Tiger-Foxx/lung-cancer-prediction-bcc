# Fonction de Prédiction BCC - Documentation

## Description Générale
Cette documentation décrit une fonction Python avancée pour la prédiction du carcinome basocellulaire (BCC) à partir d'images dermoscopiques et de métadonnées patient. Cette fonction est le résultat d'un processus d'exploration et d'entraînement approfondi sur plusieurs modèles de machine learning.

## Contexte du Projet
Le projet initial comportait plusieurs phases :
1. **Phase exploratoire** : Analyse des métadonnées et des images
   - Traitement et encodage des variables catégorielles (localisation)
   - Standardisation des variables numériques (âge)
   - Création de datasets fusionnés (images + métadonnées)

2. **Phase d'entraînement** : 
   - Création de multiples modèles (Random Forest, Logistic Regression, Decision Tree)
   - Entraînement sur différentes versions des données :
     - Images 8x8 en noir et blanc
     - Images 8x8 en RGB
     - Images 28x28 en noir et blanc
     - Images 28x28 en RGB

## Structure des Données
La fonction travaille avec deux types de données :
1. **Images** :
   - Format d'entrée flexible (n'importe quelle taille)
   - Conversion automatique en 8x8 ou 28x28
   - Support des images en couleur et noir et blanc

2. **Métadonnées** :
   - Âge du patient
   - Localisation de la lésion
   - Autres variables pertinentes identifiées lors de l'analyse exploratoire

## Installation et Prérequis

### Structure des Dossiers Requise
```
votre_projet/
├── models/
│   ├── RANDOM FOREST/
│   ├── LOGISTIC REGRESSION/
│   ├── DESCISION THREE/
│   └── model_logreg_28RGB.pkl
├── votre_script.py
```

### Dépendances Python
```python
numpy
pandas
scikit-learn
PIL
opencv-python
```

## Utilisation de la Fonction

### Paramètres
- `image_path` (str) : Chemin vers l'image à analyser
- `age` (int/float) : Âge du patient
- `localization` (str) : Localisation de la lésion
- `size` (str, optionnel) : Taille désirée ('8x8' ou '28x28')
- `model_type` (str, optionnel) : Type de modèle ('rf', 'lr', 'dt', ou 'all')

### Exemple d'Utilisation
```python
from prediction_bcc import predict_bcc

resultat = predict_bcc(
    image_path="chemin/vers/image.jpg",
    age=65,
    localization="face",
    size="28x28",
    model_type="all"
)
```

### Valeurs de Retour
- Prédiction binaire (0/1)
- Probabilité de la prédiction
- Métriques détaillées si model_type='all'

## Gestion des Erreurs
La fonction inclut une gestion robuste des erreurs pour :
- Fichiers image invalides ou manquants
- Formats d'image non supportés
- Valeurs de métadonnées invalides
- Modèles manquants ou corrompus

## Notes Importantes
1. Les modèles doivent être placés dans les dossiers appropriés
2. Les images sont automatiquement prétraitées
3. Les métadonnées sont automatiquement standardisées
4. La fonction choisit automatiquement le meilleur modèle selon le type d'image

## Performances et Limitations
- Temps de traitement variable selon la taille de l'image
- Nécessité d'avoir tous les modèles PKL disponibles
- Dépendance à la qualité des images d'entrée

## Support Technique
Pour toute question ou problème, contacter l'équipe de développement.