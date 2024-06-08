import cv2
import numpy as np


def segment_image(image_path, k_value):
    # Загрузите изображение
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Unable to load image {image_path}")
        return

    # Преобразуйте изображение в массив NumPy и измените его форму
    pixel_vals = img.reshape((-1, 3))
    pixel_vals = np.float32(pixel_vals)

    # Установите параметры для кластеризации k-means
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85)

    # Выполните кластеризацию k-means
    _, labels, centers = cv2.kmeans(pixel_vals, k_value, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Преобразуйте метки в форму, которую можно использовать для создания маски сегментации
    labels = labels.reshape((img.shape[0], img.shape[1]))

    # Преобразуем центры в uint8
    centers = np.uint8(centers)

    # Создайте маску сегментации
    segmented_img = centers[labels.flatten()]
    segmented_img = segmented_img.reshape(img.shape)

    # Отобразите результат
    cv2.imshow(f'Segmented Image k={k_value}', segmented_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Пути к изображениям
    image_paths = ['image/people.jpg', 'image/fruits.jpg']

    # Значения K для эксперимента
    k_values = [2, 3, 5]

    # Обработка изображений
    for image_path in image_paths:
        for k_value in k_values:
            segment_image(image_path, k_value)

