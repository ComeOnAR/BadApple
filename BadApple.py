import cv2
from PIL import Image
import requests
from io import BytesIO
import time

def image_to_ascii(image):
    image = image.convert('L')

    ascii_chars = "@%#*+=-:. "

    new_width = 100
    aspect_ratio = image.height / image.width
    new_height = int(new_width * aspect_ratio)
    image = image.resize((new_width, new_height))

    ascii_image = ""
    for y in range(new_height):
        for x in range(new_width):
            pixel_value = image.getpixel((x, y))
            ascii_image += ascii_chars[pixel_value // 32]  # 256 / 8 = 32
        ascii_image += "\n"  # Add newline after each row

    return ascii_image

video_url = "https://github.com/ComeOnAR/BadApple/raw/main/BadApple.mp4"
cap = cv2.VideoCapture(video_url)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    ascii_frame = image_to_ascii(frame_pil)

    # print("\033[H\033[J")

    print(ascii_frame)

    time.sleep(1/30)

cap.release()
