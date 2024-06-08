# Программа на Python для демонстрации эрозии и дилатации изображений.
import cv2
import numpy as np

# Чтение входного изображения
img = cv2.imread('image/1.png', 0)

# Создание матрицы размером 5x5 в качестве ядра
kernel = np.ones((5, 5), np.uint8)

# Первый параметр - исходное изображение, ядро - это матрица, с которой выполняется
# операция свертки, и третий параметр - количество итераций, которые определяют, насколько
# вы хотите сужать/расширять данное изображение.
img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('Input', img)
cv2.imshow('Erosion', img_erosion)
cv2.imshow('Dilation', img_dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
