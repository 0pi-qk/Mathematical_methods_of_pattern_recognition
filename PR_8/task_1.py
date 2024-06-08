import cv2

# Загружаем набор данных для распознавания лица
face_cascade = cv2.CascadeClassifier('xml/haarcascade_frontalface_default.xml')

# Загружаем изображение, на котором нужно найти лицо 
img = cv2.imread('media/people.jpg')

# Преобразуем изображение в оттенки серого
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Используем фильтры Хаара для поиска лица на изображении
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Отмечаем найденные лица на изображении
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Выводим результат
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
