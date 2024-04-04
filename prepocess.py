import numpy as np
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
import cv2
import os
from resize_photo import *
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
from pytesseract import *

image_test_ancien_dir = "camera_image_ancien/"
images_ancien_rgb = []

# Obtenez la liste des fichiers dans le répertoire
file_list = os.listdir(image_test_ancien_dir)

# Parcourez chaque fichier dans le répertoire
for filename in file_list:
    # Chemin complet vers le fichier
    image_path = os.path.join(image_test_ancien_dir, filename)
    
    # Lire l'image
    image_rgb = cv2.imread(image_path)
    
    # Ajouter l'image à la liste
    images_ancien_rgb.append(image_rgb)

image_test_nouv_dir = "camera_image_nouveau/"
images_nouveau_rgb = []

# Obtenez la liste des fichiers dans le répertoire
file_list = os.listdir(image_test_nouv_dir)

# Parcourez chaque fichier dans le répertoire
for filename in file_list:
    # Chemin complet vers le fichier
    image_path = os.path.join(image_test_nouv_dir, filename)
    
    # Lire l'image
    image_rgb = cv2.imread(image_path)
    
    # Ajouter l'image à la liste
    images_nouveau_rgb.append(image_rgb)


for image in images_nouveau_rgb[:1]:
    # Convertir en niveaux de gris
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Appliquer un seuillage avec un seuil haut
    _, thresholded = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Appliquer une opération de fermeture
    kernel = np.ones((100, 100), np.uint8)
    closing = cv2.morphologyEx(thresholded, cv2.MORPH_CLOSE, kernel)

    # Trouver les contours des objets
    contours, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contours_sorted = sorted(contours, key=cv2.contourArea, reverse=True)

    # Calculer la surface de chaque objet
    for contour in contours_sorted:
        area = cv2.contourArea(contour)
        print("Surface de l'objet:", area)

        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Découper l'image avec les contours
        cropped_contours = image[y:y+h, x:x+w]

        # Calculer l'histogramme des niveaux de gris
        hist = cv2.calcHist([image], [0], None, [256], [0, 256])

        # Dessiner les contours sur l'image
        image_with_contours = image.copy()
        cv2.drawContours(image_with_contours, contours, -1, (0, 255, 255), 2)

        # Afficher les images côte à côte en utilisant subplot
        plt.figure(figsize=(15, 5))

        # Afficher l'image originale
        plt.subplot(1, 3, 1)
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title('Image Originale')

        # Afficher l'image avec les contours détectés
        plt.subplot(1, 3, 2)
        plt.imshow(cv2.cvtColor(cropped_contours, cv2.COLOR_BGR2RGB))
        plt.title('Image avec Contours')

        # Afficher l'histogramme des niveaux de gris
        plt.subplot(1, 3, 3)
        plt.plot(hist, color='black')
        plt.title("Histogramme de Niveaux de Gris")
        plt.xlabel("Niveau de Gris")
        plt.ylabel("Nombre de Pixels")
        plt.xlim([0, 256])

        plt.show()
