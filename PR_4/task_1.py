import qrcode

# Данные, для которых вы хотите создать QR-код
# Здесь мы используем URL веб-сайта
data = "https://www.makeuseof.com/"

# Имя файла изображения QR-кода
# Измените его на желаемое имя файла
QRCodefile = "image/MUOQRCode.png"

# Генерация QR-кода
QRimage = qrcode.make(data)

# Сохранение изображения в файл
QRimage.save(QRCodefile)
