import cv2


def SIFT(image_path):
    # Загрузка изображения
    img = cv2.imread(image_path)

    # Создание объекта детектора SIFT
    sift = cv2.SIFT_create()

    # Нахождение особых точек и описаний признаков на изображении
    keypoints, descriptors = sift.detectAndCompute(img, None)

    # Отмечаем найденные особые точки на исходном изображении
    img_keypoints = cv2.drawKeypoints(img, keypoints, None)

    # Выводим изображение с отмеченными особыми точками
    cv2.imshow("Image with keypoints (SIFT)", img_keypoints)

    # Вывод количества найденных особых точек
    print("Found %d keypoints using SIFT" % len(keypoints))

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Пути к изображениям
    image_paths = ['image/people.jpg', 'image/fruits.jpg']

    # Обработка изображений
    for image_path in image_paths:
        SIFT(image_path)
