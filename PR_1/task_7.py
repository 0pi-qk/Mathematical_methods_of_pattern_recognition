# Программа на Python для объяснения метода cv2.cvtColor()
import cv2


# путь
path = 'image/1.png'

# Чтение изображения в режиме по умолчанию
src = cv2.imread(path)

# Название окна, в котором отображается изображение
window_name = 'test_7'

# Использование метода cv2.cvtColor()
# Используя код преобразования цветового пространства cv2.COLOR_BGR2GRAY
image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# Отображение изображения
cv2.imshow(window_name, image)

cv2.waitKey(0)
cv2.destroyAllWindows()
