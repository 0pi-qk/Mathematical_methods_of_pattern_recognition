# Программа на Python для объяснения метода cv2.rotate()
import cv2

# путь
path = 'image/1.png'

# Чтение изображения в режиме по умолчанию
src = cv2.imread(path)

# Название окна, в котором отображается изображение
window_name = 'test_4'

# Использование метода cv2.rotate()
# Используя cv2.ROTATE_90_CLOCKWISE повернуть на 90 градусов по часовой стрелке
image = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)

# Отображение изображения
cv2.imshow(window_name, image)
cv2.waitKey(0)
