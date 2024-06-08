# Программа на Python для иллюстрации арифметической операции побитового отрицания для входного изображения
import cv2

# указывается путь к входным изображениям и изображения загружаются с помощью команды imread
img1 = cv2.imread('image/4.png')
img2 = cv2.imread('image/5.png')

# применяется cv2.bitwise_not к входному изображению с заданными параметрами
dest_not1 = cv2.bitwise_not(img1, mask=None)
dest_not2 = cv2.bitwise_not(img2, mask=None)

# окна, отображающие выходное изображение с операцией побитового отрицания на первом и втором входных изображениях
cv2.imshow('Bitwise NOT on image 1', dest_not1)
cv2.imshow('Bitwise NOT on image 2', dest_not2)

# Освобождение памяти, занятой изображениями
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
