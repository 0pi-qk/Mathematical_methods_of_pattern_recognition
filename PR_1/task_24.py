# Программа на Python3 для рисования прямоугольника на сплошном изображении
import numpy as np
import cv2

# Создание черного изображения с 3 каналами RGB и беззнаковым целочисленным типом данных
img = np.zeros((400, 400, 3), dtype="uint8")

# Создание прямоугольника
cv2.rectangle(img, (30, 30), (300, 200), (0, 255, 0), 5)

# Отображение изображения
cv2.imshow('dark', img)

# Ожидание закрытия окна с изображением
cv2.waitKey(0)
cv2.destroyAllWindows()
