import cv2

# Загрузка видеофайла и создание объекта видеопотока
video = cv2.VideoCapture('media/video.mp4')

# Создание объекта фонового вычитания
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    # Чтение кадра видеопотока
    ret, frame = video.read()

    # Проверка на конец видео
    if not ret:
        break

    # Применение алгоритма вычитания фона
    fgmask = fgbg.apply(frame)

    # Поиск контуров на двоичной карте переднего плана
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Если есть контуры
    if contours:
        # Извлечение контура с максимальной площадью
        max_contour = max(contours, key=cv2.contourArea)

        # Получение координат и размеров прямоугольника, описывающего контур
        x, y, w, h = cv2.boundingRect(max_contour)

        # Отображение кадра со слежением за объектом
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Отображение кадра
    cv2.imshow('frame', frame)

    # Если нажата клавиша 'q', выйти из цикла
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Освобождение ресурсов
video.release()
cv2.destroyAllWindows()
