# Cepeda Miramontes Darrell Ramsés0
## NC 0030

import cv2
import numpy as np

# Cargar imagen
imagen = cv2.imread("orangutan.jpg")

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detectar bordes
bordes = cv2.Canny(gris, 100, 200)

# Mostrar imagen original
cv2.imshow("Orangutan Original", imagen)

# Mostrar imagen en escala de grises
cv2.imshow("Escala de Grises", gris)

# Mostrar bordes
cv2.imshow("Bordes", bordes)

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()

print("Programa realizado por Cepeda Darrell NC 0030")