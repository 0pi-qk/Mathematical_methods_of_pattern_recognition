import cv2


def ORB(image_path):
    # Загрузка изображения
    img = cv2.imread(image_path)

    # Создание объекта детектора ORB
    orb = cv2.ORB_create()

    # Нахождение особых точек и описаний признаков на изображении
    keypoints, descriptors = orb.detectAndCompute(img, None)

    # Отмечаем найденные особые точки на исходном изображении
    img_keypoints = cv2.drawKeypoints(img, keypoints, None)

    # Выводим изображение с отмеченными особыми точками
    cv2.imshow("Image with keypoints (ORB)", img_keypoints)

    # Вывод количества найденных особых точек
    print("Found %d keypoints using ORB" % len(keypoints))

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Пути к изображениям
    image_paths = ['image/people.jpg', 'image/fruits.jpg']

    # Обработка изображений
    for image_path in image_paths:
        ORB(image_path)
