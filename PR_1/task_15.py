# Программа на Python для обнаружения границ
import cv2

FILE_NAME = 'image/1.png'

# Чтение изображения с диска.
img = cv2.imread(FILE_NAME)

# Обнаружение границ с помощью алгоритма Canny.
edges = cv2.Canny(img, 100, 200)

# Отображение изображения с обнаруженными границами.
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
