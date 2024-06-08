import cv2
import numpy as np

# Чтение левого и правого изображений.
imgL = cv2.imread("image/im0.jpg", 0)
imgR = cv2.imread("image/im1.jpg", 0)

# Проверка, были ли успешно загружены изображения.
if imgL is None or imgR is None:
    print("Не удалось загрузить изображения.")
    exit()

# Настройка параметров для алгоритма StereoSGBM.
minDisparity = 0
numDisparities = 256
blockSize = 2
disp12MaxDiff = 6
uniquenessRatio = 4
speckleWindowSize = 2
speckleRange = 8

# Создание объекта алгоритма StereoSGBM.
stereo = cv2.StereoSGBM_create(minDisparity=minDisparity,
                               numDisparities=numDisparities,
                               blockSize=blockSize,
                               disp12MaxDiff=disp12MaxDiff,
                               uniquenessRatio=uniquenessRatio,
                               speckleWindowSize=speckleWindowSize,
                               speckleRange=speckleRange)

# Вычисление диспаритета с использованием алгоритма StereoSGBM.
disp = stereo.compute(imgL, imgR).astype(np.float32)
disp = cv2.normalize(disp, 0, 255, cv2.NORM_MINMAX)

# Отображение карты диспаратности.
cv2.imshow("disparity", disp)
cv2.waitKey(0)
cv2.destroyAllWindows()
