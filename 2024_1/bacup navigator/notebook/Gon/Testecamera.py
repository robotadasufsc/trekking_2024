import numpy as np
import cv2

imagem = cv2.VideoCapture(0)

m = False

def distancia(imageFrame,m):
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    if not m:
        m = True
        altura, largura, _ = imageFrame.shape

    # Definindo a faixa de cor vermelha
    red_lower = np.array([0, 120, 70], np.uint8)
    red_upper = np.array([10, 255, 255], np.uint8)
    red_mask1 = cv2.inRange(hsvFrame, red_lower, red_upper)

    red_lower = np.array([170, 120, 70], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red_mask2 = cv2.inRange(hsvFrame, red_lower, red_upper)

    red_mask = red_mask1 + red_mask2

    # Aplicando operações morfológicas
    kernel = np.ones((5, 5), "uint8")
    red_mask = cv2.dilate(red_mask, kernel)

    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:
            x, y, w, h = cv2.boundingRect(contour)
            altura_objeto = h
            distancia = ((2.2 * 14) / h)
            print(f"Altura do objeto na camera: {altura_objeto}, Distância: {distancia}")


while True:

    _, imageFrame = imagem.read()

    distancia(imageFrame,m)