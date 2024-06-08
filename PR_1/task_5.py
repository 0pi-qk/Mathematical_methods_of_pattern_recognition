# Программа на Python для вращения изображения под любым углом
import cv2

path = 'image/1.png'

# Чтение изображения с диска.
img = cv2.imread(path)

# Форма изображения в пикселях.
(rows, cols) = img.shape[:2]

# getRotationMatrix2D создает матрицу, необходимую для преобразования. Мы хотим матрицу для поворота относительно центра на 45 градусов без масштабирования.
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)

# Применяем аффинное преобразование к изображению.
res = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow("GeeksforGeeks", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
