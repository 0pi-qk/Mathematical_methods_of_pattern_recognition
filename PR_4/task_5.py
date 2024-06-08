import qrcode

# Данные, для которых вы хотите создать QR-код
# Здесь мы используем URL веб-сайта
data = "https://www.makeuseof.com/"

# Имя файла изображения QR-кода
QRCodefile = "image/CustomisedBorderQRCode.png"

# Создание объекта QRCode с заданной шириной границы
qrObject = qrcode.QRCode(border=10)

# Добавление данных в QR-код
qrObject.add_data(data)

# Компиляция данных в массив QR-кода
qrObject.make()

# Создание изображения QR-кода
image = qrObject.make_image()

# Сохранение изображения в файл
image.save(QRCodefile)
