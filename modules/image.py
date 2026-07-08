import cv2
import numpy as np

def preparar_imagem(img):
    img = np.array(img)
    
    # Converter para escala de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    # Aumentar contraste para melhor detecção de código de barras
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    gray = clahe.apply(gray)
    
    return gray