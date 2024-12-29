# CV Comparator

## Description

CV Comparator est un projet qui analyse les CV par rapport aux exigences d'un emploi en utilisant des techniques de traitement du langage naturel (NLP). Le projet utilise des modèles de machine learning pour évaluer la pertinence des compétences et des expériences des candidats par rapport aux exigences d'un poste.

## Fonctionnalités

- Analyse des compétences des CV par rapport aux compétences requises.
- Évaluation de la pertinence des titres de poste.
- Classement des CV en fonction de leur adéquation avec les exigences de l'emploi.

## Technologies Utilisées

- Python
- Django
- Sentence Transformers
- Scikit-learn
- PyPDF2

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

- Python 3.x
- pip (ou conda si vous utilisez Anaconda)

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/adamfutur/cv_comparator.git
   cd cv_comparator
   ```

2. Créez un environnement virtuel (optionnel mais recommandé) :

   ```bash
   python -m venv venv
   ```

3. Activez l'environnement virtuel :

   - Sur Windows :
     ```bash
     venv\Scripts\activate
     ```
   - Sur macOS/Linux :
     ```bash
     source venv/bin/activate
     ```

4. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

   > **Remarque** : Assurez-vous d'avoir un fichier `requirements.txt` dans votre projet avec toutes les dépendances nécessaires.

## Utilisation

1. Lancez le serveur Django :

   ```bash
   python manage.py runserver
   ```

2. Accédez à l'application via votre navigateur à l'adresse suivante :

   ```
   http://127.0.0.1:8000/
   ```

3. Téléchargez un CV et entrez les exigences de l'emploi pour voir les résultats de l'analyse.

## Contribuer

Les contributions sont les bienvenues ! Si vous souhaitez contribuer à ce projet, veuillez suivre ces étapes :

1. Forkez le projet.
2. Créez une nouvelle branche (`git checkout -b feature/YourFeature`).
3. Apportez vos modifications et validez-les (`git commit -m 'Add some feature'`).
4. Poussez vers la branche (`git push origin feature/YourFeature`).
5. Ouvrez une Pull Request.

## Auteurs

- Adam IMLOUL - [GitHub](https://github.com/adamfutur)

## License

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.
