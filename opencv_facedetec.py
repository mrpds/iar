import face_recognition
import imutils
import pickle
import time
import cv2
import os

# Найти путь к файлу xml, содержащему файл базу
cascPathface = os.path.dirname(
    cv2.__file__) + "/data/haarcascade_face.xml"
# Загрузить harcaascade в каскадный классификатор
faceCascade = cv2.CascadeClassifier(cascPathface)
# Загрузить известные лица и вложения, сохраненные в последнем файле
data = pickle.loads(open('face_enc', "rb").read())
# Найдите путь к изображению, на котором вы хотите обнаружить лицо, и передайте его сюда
image = cv2.imread(Path - to - img)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# Преобразовать изображение в оттенки серого для haarcascade
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray,
                                     scaleFactor=1.1,
                                     minNeighbors=5,
                                     minSize=(60, 60),
                                     flags=cv2.CASCADE_SCALE_IMAGE)

# вычисляем эмбеддинги для каждого лица
encodings = face_recognition.face_encodings(rgb)
names = []
for encoding in encodings:
    # Сравните кодировки с кодировками в данных["encodings"]
    # Совпадения содержат массив с логическими значениями и значением True для встраивания, которое близко соответствует
    # и False для остальных
    matches = face_recognition.compare_faces(data["encodings"],
                                             encoding)
    # Установить имя = неизвестно, если ни одна кодировка не соответствует
    name = "Unknown"
    # Проверяем, нашли ли мы совпадение
    if True in matches:
        # Находим позиции, в которых мы получаем True и сохраняем их
        matchedIdxs = [i for (i, b) in enumerate(matches) if b]
        counts = {}
        # Цикл по совпадающим индексам и сохранение количества для каждого распознанного лица
        for i in matchedIdxs:
            # Проверьте имена в соответствующих индексах, которые мы сохранили
            name = data["names"][i]
            # Увеличить количество для имени, которое мы получили
            counts[name] = counts.get(name, 0) + 1
            # Установить имя, которое имеет наибольшее количество
            name = max(counts, key=counts.get)

        # Обновить список имен
        names.append(name)
        # Цикл по распознанным лицам
        for ((x, y, w, h), name) in zip(faces, names):
            # Масштабируем координаты лица
            # Нарисовать предсказанное имя лица на изображении
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, name, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                        0.75, (0, 255, 0), 2)
    cv2.imshow("Frame", image)
    cv2.waitKey(0)