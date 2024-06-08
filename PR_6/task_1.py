import cv2
import numpy as np


def process_image(image_path, threshold_value):
    # Загрузите изображение
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: unable to load image '{image_path}'")
        return

    # Преобразуйте изображение в оттенки серого
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Примените пороговое значение для сегментации
    _, thresh = cv2.threshold(gray_img, threshold_value, 255, cv2.THRESH_BINARY)

    # Примените морфологические операции для улучшения сегментации
    kernel = np.ones((5, 5), np.uint8)
    morph_img = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # Выполните сегментацию путем нахождения контуров объектов на изображении
    contours, _ = cv2.findContours(morph_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Нарисуйте контуры на исходном изображении
    segmented_img = img.copy()
    cv2.drawContours(segmented_img, contours, -1, (0, 255, 0), 2)

    # Отобразите результат
    cv2.imshow(f'Segmented Image - Threshold {threshold_value}', segmented_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Пути к изображениям
    image_paths = ['image/people.jpg', 'image/fruits.jpg']

    # Значения порога
    threshold_values = [100, 150, 200, 250]

    # Обработка изображений
    for image_path in image_paths:
        for threshold_value in threshold_values:
            process_image(image_path, threshold_value)
