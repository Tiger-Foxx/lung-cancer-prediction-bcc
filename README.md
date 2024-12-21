# Lung-Cancer-Prediction-BCC

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Ce projet vise à développer un modèle d'apprentissage automatique capable de détecter le cancer de la peau, avec un focus initial sur le carcinome basocellulaire (BCC). L'objectif est également d'étendre la détection à d'autres types de cancers de la peau si possible.  




# **Détection de Cancer de la Peau via Machine Learning**

## **Description du Projet**  
Ce projet vise à développer un modèle d'apprentissage automatique capable de détecter le cancer de la peau, avec un focus initial sur le carcinome basocellulaire (BCC). L'objectif est également d'étendre la détection à d'autres types de cancers de la peau si possible.  

Nous nous engageons à appliquer les meilleures pratiques en science des données, notamment l'utilisation de la structure **Cookiecutter Data Science** et une collaboration optimisée via GitHub.  

---

## **Objectifs Principaux**  
1. Créer un modèle de détection performant pour le BCC à partir d'images.  
2. Étendre la détection à plusieurs types de cancers de la peau.  
3. Assurer une organisation rigoureuse et une reproductibilité totale du projet.  

---

## **Structure du Projet**  
Ce projet suit la structure Cookiecutter Data Science :  

```
├── data/                 # Données brutes, intermédiaires et finales  
├── notebooks/            # Explorations et analyses en Jupyter  
├── src/                  # Code source du projet (prétraitement, modèles, etc.)  
├── models/               # Modèles entraînés et résultats  
├── reports/              # Graphiques, résultats et documentation finale  
├── tests/                # Scripts de tests pour valider le code  
├── requirements.txt      # Liste des dépendances Python  
└── README.md             # Documentation principale  
```  

Chaque dossier contient un fichier `README.md` pour décrire son rôle et son contenu.  

---

## **Prérequis**  
### **1. Configuration de l’Environnement**  
1. Installez Python 3.9 ou supérieur.  
2. Clonez ce dépôt :  
   ```bash
   git clone https://github.com/votre-repo/cancer-detection.git
   cd cancer-detection
   ```  
3. Installez les dépendances :  
   ```bash
   pip install -r requirements.txt
   ```  

### **2. Structure Cookiecutter**  
Ce projet utilise la structure **Cookiecutter Data Science**. Familiarisez-vous avec son organisation [ici](https://drivendata.github.io/cookiecutter-data-science/).  

---

## **Démarrage**  
### **1. Préparation des Données**  
- Placez les données brutes dans le dossier `data/raw`.  
- Exécutez le script de prétraitement dans `src/preprocessing/` pour générer des données prêtes à l’emploi dans `data/processed`.  

### **2. Exploration et Visualisation**  
- Les carnets Jupyter sont disponibles dans le dossier `notebooks/`.  

### **3. Entraînement du Modèle**  
- Lancez le script principal dans `src/models/train_model.py` :  
   ```bash
   python src/models/train_model.py
   ```  

---

## **Organisation et Collaboration**  
### **Bonnes Pratiques GitHub**  
- **Branches dédiées :** Travaillez sur une branche spécifique pour chaque tâche (ex. : `feature/data-preprocessing`).  
- **Commits clairs :** Expliquez brièvement vos modifications.  
- **Pull Requests :** Faites valider vos modifications par un membre de l'équipe avant de fusionner dans `main`.  

### **Documentation**  
- Mettez à jour le fichier `README.md` si vous ajoutez de nouvelles étapes ou outils.  

---

## **Ressources et Références**  
- Cookiecutter Data Science : [Guide officiel](https://drivendata.github.io/cookiecutter-data-science/)  
- Dataset utilisé : [Lien vers la source du dataset]  
- Frameworks :  
  - TensorFlow / PyTorch (à confirmer selon votre choix)  
  - Pandas, NumPy, Matplotlib pour les analyses  

---

## **Prochaines Étapes**  
1. Finaliser la formalisation mathématique du problème.  
2. Prétraiter les données et explorer leur distribution.  
3. Construire et entraîner le modèle de classification initial.  

---

## **Contact**  
Pour toute question ou contribution, contactez [Donfack Pascal Arthur](mailto:donfackarthur750@gmail.com) ou ouvrez une issue sur ce dépôt.

--- 

Ce fichier README pourra évoluer avec l'avancement du projet. 😊


## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         lung_cancer_prediction_bcc and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── lung_cancer_prediction_bcc   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes lung_cancer_prediction_bcc a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------


> "Le renard sait que la voie du succès est pavée de travail, de persévérance... et parfois de lignes de code." 🦊💻

---


