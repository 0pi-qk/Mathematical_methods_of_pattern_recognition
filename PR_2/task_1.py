import cv2
import numpy as np
import glob

# Определение размеров шахматной доски
CHECKERBOARD = (6, 9)

# Критерии остановки
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Координаты 3D точек в реальном мире
objectp3d = np.zeros((1, CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
objectp3d[0, :, :2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)

# Извлечение пути к изображениям
images = glob.glob("image\*.jpg")

for filename in images:
    # Векторы для 3D точек и 2D точек
    threedpoints = []
    twodpoints = []

    image = cv2.imread(filename)

    if image is None:
        print(f"Не удалось загрузить изображение: {filename}")
        continue

    print(f"Загружено изображение: {filename}")

    # Отображение исходного изображения
    cv2.imshow('Original Image', image)

    grayColor = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Найдите углы на шахматной доске
    ret, corners = cv2.findChessboardCorners(grayColor, CHECKERBOARD,
                                             cv2.CALIB_CB_ADAPTIVE_THRESH +
                                             cv2.CALIB_CB_FAST_CHECK +
                                             cv2.CALIB_CB_NORMALIZE_IMAGE)

    if ret:
        threedpoints.append(objectp3d)

        corners2 = cv2.cornerSubPix(grayColor, corners, (11, 11), (-1, -1), criteria)
        twodpoints.append(corners2)

        img = image.copy()
        img = cv2.drawChessboardCorners(img, CHECKERBOARD, corners2, ret)

        cv2.imshow("Ret on img", img)
    else:
        print(f"Углы, не найденные на изображении: {filename}")

    # Калибровка камеры
    ret, matrix, distortion, r_vecs, t_vecs = cv2.calibrateCamera(threedpoints, twodpoints, grayColor.shape[::-1], None,
                                                                  None)

    # Вывод параметров камеры
    print("Матрица камеры:")
    print(matrix)

    print("Коэффициент искажения:")
    print(distortion)

    print("Векторы вращения:")
    print(r_vecs)

    print("Векторы перевода:")
    print(t_vecs)

    # Исправление искажений на изображении
    undistorted_image = cv2.undistort(image, matrix, distortion, None, matrix)

    # Проекция 3D точек в 2D используя найденные векторы вращения и перевода
    # Использования одного набора r_vec и t_vec
    r_vec = r_vecs[0]
    t_vec = t_vecs[0]

    # Определение 3D точек в пространстве
    object_points = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]], dtype=np.float32)

    # Проекция точек в 2D плоскость изображения
    projected_points, _ = cv2.projectPoints(object_points, r_vec, t_vec, matrix, distortion)

    for point in projected_points:
        # Рисование точек на изображении
        cv2.circle(undistorted_image, (int(point[0][0]), int(point[0][1])), 5, (0, 255, 0), -1)

    # Отображение исходного и исправленного изображений
    cv2.imshow('Undistorted Image with Projected Points', undistorted_image)
    cv2.waitKey(0)

cv2.destroyAllWindows()
