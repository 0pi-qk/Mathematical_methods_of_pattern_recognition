# Программа на Python для смещения изображения
import cv2
import numpy as np

image = cv2.imread('image/1.png')

# Хранение высоты и ширины изображения
height, width = image.shape[:2]
quarter_height, quarter_width = height / 4, width / 4

# Матрица преобразования
T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])

# Используем warpAffine для трансформации изображения с использованием матрицы T
img_translation = cv2.warpAffine(image, T, (width, height))

cv2.imshow('Translation', img_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()
