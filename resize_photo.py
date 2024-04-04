import os
import cv2
import numpy as np
# Chemin vers le répertoire contenant les images
directory = "alphabet/"
output_directory="alphabet_resize/"


# Créer le répertoire de sortie s'il n'existe pas déjà
if not os.path.exists(output_directory):
    os.makedirs(output_directory)


# # Redimensionnement souhaité
# desired_width = 200
# desired_height =200
desired_width = 100
desired_height =100

# Créer le répertoire de sortie s'il n'existe pas déjà
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Parcourir le répertoire principal
for subdir in os.listdir(directory):
    subdir_path = os.path.join(directory, subdir)
    # Vérifier si le chemin est un sous-répertoire
    if os.path.isdir(subdir_path):
        # Créer un sous-répertoire correspondant dans le répertoire de sortie
        output_subdir = os.path.join(output_directory, subdir)
        if not os.path.exists(output_subdir):
            os.makedirs(output_subdir)
        # Parcourir les fichiers dans le sous-répertoire
        for filename in os.listdir(subdir_path):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                # Chemin complet de l'image d'entrée
                input_filepath = os.path.join(subdir_path, filename)
                # Charger l'image
                img = cv2.imread(input_filepath)
                # Redimensionner l'image
                resized_img = cv2.resize(img, (desired_width, desired_height))
                # Appliquer un filtre pour rendre l'image plus nette
                sharpened_img = cv2.filter2D(resized_img, -1, kernel=np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]]))
                # Chemin de sortie pour l'image redimensionnée et nette
                output_filepath = os.path.join(output_subdir, filename)
                # Enregistrer l'image redimensionnée et nette
                cv2.imwrite(output_filepath, sharpened_img)


cv2.destroyAllWindows()