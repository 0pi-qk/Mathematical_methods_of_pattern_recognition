import qrcode

# Данные, для которых вы хотите создать QR-код
# Здесь мы используем URL веб-сайта
data = "https://www.makeuseof.com/"

# Имя файла изображения QR-кода
QRCodefile = "image/CustomisedFillColorQRCode.png"

# Создание объекта QRCode
qrObject = qrcode.QRCode()

# Добавление данных в QR-код
qrObject.add_data(data)

# Компиляция данных в массив QR-кода
qrObject.make()

# Создание изображения QR-кода с заданным цветом заполнения
image = qrObject.make_image(fill_color="red")

# Сохранение изображения в файл
image.save(QRCodefile)
