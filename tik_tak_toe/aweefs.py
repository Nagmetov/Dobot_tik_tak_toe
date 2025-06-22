import cv2
import numpy as np

# Загрузка изображения
image = cv2.imread("svsa.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Улучшение изображения
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150)  # Детектор краев Canny

# Утолщение линий
kernel = np.ones((2, 2), np.uint8)
dilated = cv2.dilate(edges, kernel, iterations=1)

# Поиск контуров
contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Упрощение контуров (без сильного упрощения)
simplified_contours = []
for cnt in contours:
    epsilon = 0.01 * cv2.arcLength(cnt, True)  # Меньше упрощение
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    simplified_contours.append(approx)

# Создание маски контуров для просмотра
contour_image = np.zeros_like(gray)
cv2.drawContours(contour_image, simplified_contours, -1, 255, 1)

# Просмотр результата
contour_image_resized = cv2.resize(contour_image, (500, 500))
cv2.imshow("Contours", contour_image_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Преобразование координат
ROBOT_AREA_WIDTH_MM = 80
ROBOT_AREA_HEIGHT_MM = 80

# Константы для новой системы координат
CENTER_X_MM = 210  # Новое значение X для центра
CENTER_Y_MM = -10  # Новое значение Y для центра


def pixel_to_robot_coords(x_pixel, y_pixel, img_width, img_height):
    # Перевод пикселей в миллиметры
    x_robot = (x_pixel / img_width) * ROBOT_AREA_WIDTH_MM
    y_robot = (1 - y_pixel / img_height) * ROBOT_AREA_HEIGHT_MM

    # Смещение относительно нового центра
    x_centered = x_robot - (ROBOT_AREA_WIDTH_MM / 2) + CENTER_X_MM
    y_centered = y_robot - (ROBOT_AREA_HEIGHT_MM / 2) + CENTER_Y_MM

    return round(x_centered, 1), round(y_centered, 1)


# Получение списка координат с учётом нового центра
coordinates = []
for cnt in simplified_contours:
    contour_points = []
    for point in cnt:
        x, y = point[0]
        rx, ry = pixel_to_robot_coords(x, y, image.shape[1], image.shape[0])  # Используем реальные размеры изображения
        contour_points.append((rx, ry))
    coordinates.append(contour_points)

# Сохранение координат в файл
with open("contour_coordinates.txt", "w") as f:
    for contour in coordinates:
        for point in contour:
            f.write(f"{point[0]},{point[1]}\n")
        f.write("---\n")  # Разделитель контуров

print("Координаты сохранены в файл contour_coordinates.txt")