import cv2
import numpy as np

def extrair_produtos(imagem):
    produtos = []
    
    try:
        detector = cv2.barcode_BarcodeDetector()
        decoded_info, _, _ = detector.detectAndDecode(imagem)
        
        if decoded_info is not None:
            for ean in decoded_info:
                if ean and len(ean) == 13 and ean.isdigit():
                    produtos.append({
                        "ean": ean,
                        "nome": f"Produto {ean}"
                    })
    except Exception as e:
        print(f"Erro ao detectar código de barras: {e}")
    
    return produtos