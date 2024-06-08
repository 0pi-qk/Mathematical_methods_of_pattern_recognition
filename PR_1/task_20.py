# Программа на Python - двусторонняя фильтрация
import cv2

# Чтение изображения
img = cv2.imread('image/1.png')

# Применение двустороннего фильтра с параметрами d = 15,
# sigmaColor = sigmaSpace = 100
bilateral = cv2.bilateralFilter(img, 15, 100, 100)

# Отображение выходного изображения
cv2.imshow('Bilateral', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
