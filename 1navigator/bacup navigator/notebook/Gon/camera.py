import numpy as np
import cv2

imagem = cv2.VideoCapture(0)

m = False

while True:
    _, imageFrame = imagem.read()
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)  # Mudança para BGR2HSV para câmeras OpenCV

    if not m:
        m = True
        altura, largura, _ = imageFrame.shape
        meio = (int(largura / 2), int(altura / 2))

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
            imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Cor vermelha (BGR)
            cv2.putText(imageFrame, "Vermelho", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 2)
            red_center = (x + w // 2, y + h // 2)
            cv2.line(imageFrame, red_center, meio, (0, 0, 255), 2)  # Linha vermelha
            distancia = ((2.2 * 10.5) / h)
            print(distancia)

    # Exibindo o resultado
    cv2.imshow("Vermelho detectado", imageFrame)

    # Terminando o programa
    if cv2.waitKey(10) & 0xFF == ord('q'):
        imagem.release()
        cv2.destroyAllWindows()
        break
