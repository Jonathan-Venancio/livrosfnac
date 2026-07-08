from pyzbar import pyzbar
import cv2

def extrair_produtos(imagem):
    produtos = []
    
    decoded_objects = pyzbar.decode(imagem)
    
    for obj in decoded_objects:
        ean = obj.data.decode('utf-8')
        
        if len(ean) == 13 and ean.isdigit():
            produtos.append({
                "ean": ean,
                "nome": f"Produto {ean}"
            })
    
    return produtos