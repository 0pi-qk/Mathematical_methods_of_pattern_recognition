# Программа на Python для размытия изображения
import cv2

# чтение изображения
image = cv2.imread('image/1.png')

# отображение исходного изображения
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# применение гауссовского размытия
Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow('Gaussian Blurring', Gaussian)
cv2.waitKey(0)

# применение медианного размытия
median = cv2.medianBlur(image, 5)
cv2.imshow('Median Blurring', median)
cv2.waitKey(0)

# применение двустороннего размытия
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Blurring', bilateral)
cv2.waitKey(0)

# закрытие всех окон
cv2.destroyAllWindows()
