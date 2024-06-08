# Python код для чтения изображения
import cv2

# Для чтения изображения с диска мы используем
# функцию cv2.imread, в нижеприведенном методе,
img = cv2.imread("image/1.png", cv2.IMREAD_COLOR)
print(img)
