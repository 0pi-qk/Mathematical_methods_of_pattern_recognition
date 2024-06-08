# Программа на Python - сопоставление функция
import cv2

# Чтение запросов изображения как query_img и обучающего изображения. Это запросное изображение
# то, что вам нужно найти на обучающем изображении.
query_img = cv2.imread('image/1.png')
train_img = cv2.imread('image/1.png')

# Преобразование в оттенки серого
query_img_bw = cv2.cvtColor(query_img, cv2.COLOR_BGR2GRAY)
train_img_bw = cv2.cvtColor(train_img, cv2.COLOR_BGR2GRAY)

# Инициализация детектора ORB
orb = cv2.ORB_create()

# Обнаружение ключевых точек и вычисление дескрипторов для запросного и обучающего изображений
queryKeypoints, queryDescriptors = orb.detectAndCompute(query_img_bw, None)
trainKeypoints, trainDescriptors = orb.detectAndCompute(train_img_bw, None)

# Инициализация матчера для сопоставления ключевых точек, а затем сопоставление ключевых точек
matcher = cv2.BFMatcher()
matches = matcher.match(queryDescriptors, trainDescriptors)

# нарисовать совпадения на конечном изображении содержащем оба изображения. Функция drawMatches()
# принимает оба изображения и ключевые точки и выводит сопоставленное запросное изображение с
# его обучающим изображением
final_img = cv2.drawMatches(query_img, queryKeypoints, train_img, trainKeypoints, matches[:20], None)
final_img = cv2.resize(final_img, (1000, 650))

# Показать конечное изображение
cv2.imshow("Matches", final_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
