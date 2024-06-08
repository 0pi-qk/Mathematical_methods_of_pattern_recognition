import cv2

# Загрузка изображения в оттенках серого
img = cv2.imread('image/1.jpg', 0)

# Применение алгоритма Canny для обнаружения границ
threshold1 = 120
threshold2 = 250
edges = cv2.Canny(img, threshold1, threshold2)

# Вывод изображения с границами
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
