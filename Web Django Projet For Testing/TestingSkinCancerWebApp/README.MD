# Détecteur BCC - Application de détection du cancer de la peau

Cette application utilise l'intelligence artificielle pour détecter le cancer de la peau de type BCC (Carcinome basocellulaire) à partir d'images dermatologiques.

## Prérequis

- Python 3.8 ou supérieur
- Un navigateur web moderne
- Connexion Internet (pour le chargement des styles)

## Installation et lancement rapide

1. Décompressez l'archive du projet dans un dossier de votre choix

2. **Méthode simple (recommandée)** :
   - Double-cliquez sur `setup_and_run.py`
   - L'application s'installera et se lancera automatiquement dans votre navigateur

3. **Méthode manuelle (si la méthode simple ne fonctionne pas)** :
   ```bash
   # Création de l'environnement virtuel
   python -m venv venv

   # Activation de l'environnement virtuel
   # Sur Windows :
   venv\Scripts\activate
   # Sur Linux/Mac :
   source venv/bin/activate

   # Installation des dépendances
   pip install -r requirements.txt

   # Migrations Django
   python manage.py migrate

   # Collection des fichiers statiques
   python manage.py collectstatic --noinput

   # Lancement du serveur
   python manage.py runserver
   ```

## Structure des dossiers

```
project/
│
├── models/                    # Modèles de prédiction
│   ├── LOGISTIC REGRESSION/  
│   ├── RANDOM FOREST/
│   └── DECISION TREE/
│
├── static/                   # Fichiers statiques
├── templates/               # Templates HTML
├── manage.py               # Script Django
├── requirements.txt        # Dépendances Python
└── setup_and_run.py       # Script d'installation automatique
```

## Utilisation

1. Une fois l'application lancée, accédez à : http://127.0.0.1:8000
2. Uploadez une image de la lésion à analyser
3. Remplissez les informations requises (âge, localisation)
4. Sélectionnez le type de modèle à utiliser
5. Cliquez sur "Lancer l'analyse"

## Support

En cas de problème :
1. Vérifiez que Python 3.8+ est bien installé
2. Vérifiez que les modèles sont bien présents dans le dossier `models/`
3. Essayez la méthode d'installation manuelle

## Notes importantes

- Les modèles de prédiction doivent être placés dans le dossier `models/` avant le lancement
- L'application nécessite une connexion Internet pour le chargement des styles Tailwind