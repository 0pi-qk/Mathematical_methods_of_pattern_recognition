import qrcode

# Данные, для которых вы хотите создать QR-код
# Здесь мы используем URL веб-сайта
data = "https://www.makeuseof.com/"

# Имя файла изображения QR-кода
QRCodefile = "image/CustomisedBGColorQRCode.png"

# Создание объекта QRCode
qrObject = qrcode.QRCode()

# Добавление данных в QR-код
qrObject.add_data(data)

# Компиляция данных в массив QR-кода
qrObject.make()

# Создание изображения QR-кода с заданным цветом фона
image = qrObject.make_image(back_color="blue")

# Сохранение изображения в файл
image.save(QRCodefile)
