import cv2
import numpy as np

def preparar_imagem(img):

    img=np.array(img)

    gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    gray=cv2.GaussianBlur(gray,(3,3),0)

    gray=cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        25,
        15
    )

    return gray