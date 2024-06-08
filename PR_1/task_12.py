# Программа на Python для иллюстрации арифметической операции побитового исключающего ИЛИ двух изображений
import cv2

# указывается путь к входным изображениям и изображения загружаются с помощью команды imread
img1 = cv2.imread('image/4.png')
img2 = cv2.imread('image/5.png')

# применяется cv2.bitwise_xor к входным изображениям с заданными параметрами
dest_xor = cv2.bitwise_xor(img1, img2, mask=None)

# окно, отображающее выходное изображение с операцией побитового исключающего ИЛИ на входных изображениях
cv2.imshow('Bitwise XOR', dest_xor)

# Освобождение памяти, занятой изображениями
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()