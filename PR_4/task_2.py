import qrcode
import numpy as np

# Данные, для которых вы хотите создать QR-код
# Здесь мы используем URL веб-сайта
data = "https://www.makeuseof.com/"

# Имя файла изображения QR-кода
QRCodefile = "image/CustomisedImgBoxQRCode.png"

# Создание объекта QRCode
qrObject = qrcode.QRCode(version=1, box_size=12)

# Добавление данных в QR-код
qrObject.add_data(data)

# Компиляция данных в массив QR-кода
qrObject.make()

# Создание изображения QR-кода
image = qrObject.make_image()

# Сохранение изображения в файл
image.save(QRCodefile)

# Печать размера изображения (версия)
print("Размер изображения QR-кода (версия):")
print(np.array(qrObject.get_matrix()).shape)
