# README : Notebook d’Entraînement pour la Prédiction de BCC (Basal Cell Carcinoma)

## **Introduction**
Ce notebook est dédié à l’entraînement de différents modèles de machine learning pour la prédiction du cancer de type BCC (Basal Cell Carcinoma) à partir de données fusionnées entre des images et des métadonnées traitées. Cette phase est cruciale pour analyser les performances des modèles sur plusieurs ensembles de données, comparer leurs métriques, et préparer une évaluation exhaustive.



## **Résumé de la Phase Exploratoire**
1. **Objectif de la phase exploratoire :**  
   - Examiner les métadonnées fournies, identifier les colonnes pertinentes, et nettoyer les données.
   - Standardiser les formats et valeurs, notamment pour des colonnes comme l'âge, les localisations anatomiques, et les labels.

2. **Traitement des métadonnées :**  
   - Les colonnes inutiles ou redondantes ont été supprimées (par exemple, apres analyse nous avons pu voir que la donnee du sexe de l'individus n'est pas tres pertinente pour predire son cancer de la peau ).
   - Certaines colonnes ont été encodées sous forme de variables binaires (comme les localisations anatomiques).

3. **Fusion des données :**  
   - Les ensembles de métadonnées nettoyés ont été fusionnés avec des datasets contenant les pixels des images (par exemple, des images en niveaux de gris ou en couleurs).
   - Les nouveaux fichiers CSV générés combinent des informations visuelles et contextuelles, prêts pour l’entraînement des modèles.

4. **Nouveaux datasets générés :**  
   - Chaque dataset représente un type spécifique d’image (8x8 ou 28x28, en niveaux de gris ou RGB).
   - **Exemples de fichiers :**
     - `Meta_Data_Processed_8L.csv` : Images 8x8 en niveaux de gris avec métadonnées.
     - `Meta_Data_Processed_28RGB.csv` : Images 28x28 en RGB avec métadonnées.



## **Objectif de ce Notebook**
### **1. Entraînement des modèles pour la prédiction de BCC**
   - La variable cible est `is_bcc` (0 : non-BCC, 1 : BCC). Les colonnes non pertinentes à cette tâche, comme `label`, seront supprimées pour éviter les redondances.

### **2. Évaluation poussée des performances des modèles**
   - Plusieurs algorithmes seront testés (ex. : Random Forest, SVM, Réseaux Neuronaux, etc.).
   - Les métriques incluront :
     - Accuracy
     - Précision, rappel, F1-score
     - Courbes ROC et AUC
   - Comparaison des performances sur les 4 datasets (28x28 et 8x8, niveaux de gris et RGB).



## **Structure des Données**
Les fichiers CSV contiennent :
1. **Colonnes de pixels :**  
   - Représentent les valeurs des pixels des images, préalablement non standardisées (elles seront normalisées avant l’entraînement).
   - Exemple : `pixel0000, pixel0001, ..., pixel0063` pour des images 8x8.

2. **Colonnes de métadonnées :**
   - `age` : Âge du patient.
   - `localization_*` : Localisation anatomique, encodée sous forme binaire.
   - `is_bcc` : Cible pour la classification.

---

## **Étapes du Notebook**
1. **Chargement et Prétraitement des Données**
   - Chargement des fichiers CSV.
   - Suppression des colonnes inutiles ou redondantes (`label`).
   - Normalisation des colonnes de pixels (exemple : division par 255 pour les mettre entre 0 et 1).

2. **Séparation des Données**
   - Division en ensembles d’entraînement et de test.
   - Stratification pour garantir une répartition équilibrée de la variable cible.

3. **Entraînement des Modèles**
   - Test de différents algorithmes :

4. **Évaluation des Modèles**
   - Métriques calculées pour chaque modèle.
   - Analyse des courbes ROC.
   - Comparaison des performances entre modèles et entre datasets.

5. **Sauvegarde des Modèles**
   - Les modèles entraînés seront enregistrés au format `.pkl` pour une utilisation ultérieure.
   - Exemple : `model_rf_8L.pkl` pour un modèle Random Forest sur le dataset 8x8 en niveaux de gris.


## **Résultats Attendus**
- Identifier le modèle le plus performant pour la prédiction de BCC.
- Comprendre l’impact des différentes résolutions (8x8 vs 28x28) et des formats (niveaux de gris vs RGB) sur les performances.
- Préparer une documentation exhaustive pour l’intégration future de ces modèles.


## **Fichiers Produits**
1. **Fichiers de sortie :**
   - Modèles entraînés sous forme de fichiers `.pkl`.
   - Rapports d’évaluation pour chaque modèle (sauvegardés en fichiers texte ou CSV).

2. **Fichiers intermédiaires :**
   - Graphiques de visualisation des courbes ROC.
   - Logs d’entraînement pour la traçabilité.