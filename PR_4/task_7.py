import cv2

# Инициализация камеры
cap = cv2.VideoCapture(0)

# Инициализация детектора QR-кодов OpenCV
detector = cv2.QRCodeDetector()

while True:
    # Чтение изображения с камеры 
    _, img = cap.read()

    # Обнаружение и декодирование QR-кода
    data, vertices_array, _ = detector.detectAndDecode(img)

    # Проверка, есть ли QR-код на изображении
    if vertices_array is not None:
        if data:
            print("Обнаружен QR-код, данные:", data)

    # Отображение результата
    cv2.imshow("Qr scanner", img)

    # Выход из цикла при нажатии клавиши 'q'
    if cv2.waitKey(1) == ord("q"):
        break

# Освобождение ресурса камеры и закрытие всех окон
cap.release()
cv2.destroyAllWindows()
