# Программа на Python для иллюстрации простого типа порогового преобразования на изображении
import cv2

# указывается путь к входному изображению и изображение загружается с помощью команды imread
image1 = cv2.imread('image/1.png')

# применение cv2.cvtColor к входному изображению с заданными параметрами для преобразования изображения в оттенки серого
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

# применение различных пороговых методов к входному изображению все пиксели со значением выше 120 будут установлены в 255
ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

# окна, отображающие выходные изображения с соответствующими пороговыми методами, примененными к входным изображениям
cv2.imshow('Binary Threshold', thresh1)
cv2.imshow('Binary Threshold Inverted', thresh2)
cv2.imshow('Truncated Threshold', thresh3)
cv2.imshow('Set to 0', thresh4)
cv2.imshow('Set to 0 Inverted', thresh5)

# Освобождение памяти, занятой изображениями
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
