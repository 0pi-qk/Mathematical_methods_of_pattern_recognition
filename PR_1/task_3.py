# Программа на Python для объяснения метода cv2.imwrite()
import cv2

image_path = 'image/1.png'
# Использование метода cv2.imread() для чтения изображения

img = cv2.imread(image_path)

# Название файла
filename = 'image/savedImage.jpg'

# Использование метода cv2.imwrite()
# Сохранение изображения
cv2.imwrite(filename, img)

# Чтение и отображение сохраненного изображения
img = cv2.imread(filename)
cv2.imshow("test_3", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
