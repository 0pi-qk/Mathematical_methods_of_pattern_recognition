# Программа на Python для иллюстрации адаптивного порогового преобразования на изображении
import cv2

# указывается путь к входному изображению и изображение загружается с помощью команды imread
image1 = cv2.imread('image/1.png')

# применение cv2.cvtColor к входному изображению с заданными параметрами для преобразования изображения в оттенки серого
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

# применение различных адаптивных пороговых методов к входному изображению
thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 199, 5)
thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 199, 5)

# окна, отображающие выходные изображения с соответствующими адаптивными пороговыми методами, примененными к входному изображению
cv2.imshow('Adaptive Mean', thresh1)
cv2.imshow('Adaptive Gaussian', thresh2)

# Освобождение памяти, занятой изображениями
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
