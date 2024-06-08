import cv2

# Имя файла изображения QR-кода
filename = "image/MUOQRCode.png"

# Чтение изображения QR-кода
image = cv2.imread(filename)

# Инициализация детектора QR-кодов cv2
detector = cv2.QRCodeDetector()

# Обнаружение и декодирование QR-кода
data, vertices_array, binary_qrcode = detector.detectAndDecode(image)

# Если QR-код обнаружен, выводим данные
if vertices_array is not None:
    print("Данные QR-кода:")
    print(data)
else:
    print("Произошла ошибка")
