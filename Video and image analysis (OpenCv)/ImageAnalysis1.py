import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./data/img/montre1.jpg',cv2.IMREAD_GRAYSCALE) #IMREAD_COLOR = 1 , IMREAD_UNCHANGED = -1, IMREAD_GRAYSCALE = 0
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# affichage avec la librarie matplotlib
"""
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([200,300,400],[100,200,300],'c', linewidth=5) # dessiner une ligne sur l'image 
plt.show()
"""
cv2.imwrite('./data/img/montregray.png',img) # écrire l'image sur le disque . 