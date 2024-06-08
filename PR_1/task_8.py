# Программа на Python для иллюстрации арифметической операции сложения двух изображений
import cv2

# указывается путь к входным изображениям и изображения загружаются с помощью команды imread
image1 = cv2.imread('image/2.png')
image2 = cv2.imread('image/3.png')

# применяется cv2.addWeighted к входным изображениям с заданными параметрами
weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)

# окно, отображающее выходное изображение с взвешенной суммой
cv2.imshow('test_8', weightedSum)

# Освобождение памяти, занятой изображениями
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
