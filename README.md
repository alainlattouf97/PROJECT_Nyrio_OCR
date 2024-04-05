# Projet de Contrôle de Robot avec Détection de Caractères

Ce projet vise à contrôler les mouvements d'un robot en Python tout en intégrant une étape de détection de caractères à l'aide de techniques de reconnaissance optique de caractères (OCR). Deux approches pour la détection de caractères sont comparées : un modèle SVM et PyTesseract d'une part, et un modèle CNN avec PyTesseract d'autre part.

## Contenu du Projet

- `vision.py`: Script Python pour controler le robot niryo pour le tri des pieces en 
- `ocr.ipynb`: Implémentation de la détection de caractères avec un modèle CNN.
- `ocr_2.ipynb`: Implémentation de la détection de caractères avec un modèle SVM.
- `alpabet_resize/`: Répertoire contenant les données d'entraînement et de test pour les modèles OCR. avec des tailles      d'images modifiés
- `alpabet/`: Répertoire contenant les données d'entraînement et de test pour les modèles OCR.
- `requirements.txt`: Liste des dépendances Python nécessaires pour exécuter le projet.

## requirements
dans ce projet il faut installer les librairies suivante:

pip install numpy tensorflow scikit-learn opencv-python matplotlib pytesseract


## Installation

1. Cloner ce dépôt :

```bash
git clone https://github.com/votre-utilisateur/projet-robot-detection-caracteres.git
cd projet-robot-detection-caracteres