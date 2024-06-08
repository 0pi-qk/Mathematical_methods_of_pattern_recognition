# Программа на Python для иллюстрации арифметической операции вычитания пикселей двух изображений
import cv2

# указывается путь к входным изображениям и изображения загружаются с помощью команды imread
image1 = cv2.imread('image/2.png')
image2 = cv2.imread('image/3.png')

# применяется cv2.subtract к входным изображениям с заданными параметрами
sub = cv2.subtract(image1, image2)

# окно, отображающее выходное изображение с вычитанным изображением
cv2.imshow('Subtracted Image', sub)

# Освобождение памяти, занятой изображениями
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
