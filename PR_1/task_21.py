# Программа на Python - контуры изображения
import cv2

# Загрузка изображения с тремя черными квадратами
image = cv2.imread('image/1.png')
cv2.waitKey(0)

# Преобразование в оттенки серого
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Поиск границ с помощью алгоритма Canny
edged = cv2.Canny(gray, 30, 200)
cv2.waitKey(0)

# Поиск контуров
contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.imshow('Canny Edges After Contouring', edged)
cv2.waitKey(0)

print("Number of Contours found = " + str(len(contours)))

# Нарисовать все контуры
# -1 означает рисование всех контуров
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
