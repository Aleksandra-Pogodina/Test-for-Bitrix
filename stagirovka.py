import cv2
import numpy as np


# Размеры видео

width, height = 100, 100


# Длительность видео в секундах

duration = 3

# Текст бегущей строки
print("введите текст")
text = input()

# Создание пустого видео
video = cv2.VideoWriter("running_text.mp4", cv2.VideoWriter_fourcc(*"XVID"), 30, (width, height))


# Создание изображения с текстом

font = cv2.FONT_HERSHEY_SIMPLEX #шрифт изображения

image = np.zeros((height, width, 3), dtype=np.uint8) #создаём пустое изображение

x = width #координата нижнего левого угла начала текста (x)

y = int(height/ 2) #координата нижнего левого угла начала текста (y)

color = (0,124,255) #цвет текста

thickness = 2 #толщина линий букв

image = cv2.putText(image, text, (x, y), font, 1, color, thickness)


# Генерация видео с бегущей строкой
count = int(duration * 30)  # 30 кадров в секунду
for i in range(count):
    x -= 2  # Сдвигаем текст 
    frame = np.copy(image)
    frame = cv2.putText(frame, text, (x, y), font, 1, color, thickness)
    video.write(frame)
    
# Закрытие видеофайла
video.release()
