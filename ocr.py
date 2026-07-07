import easyocr
import re

reader = easyocr.Reader(['pt', 'en'])


def ler_imagem(imagem):

    resultado = reader.readtext(imagem)

    produtos = []

    ean = None
    descricao = None

    for item in resultado:

        texto = item[1].strip()

        if re.fullmatch(r"\d{13}", texto):

            ean = texto

        elif len(texto) > 4:

            descricao = texto

        if ean and descricao:

            produtos.append({
                "ean": ean,
                "descricao": descricao
            })

            ean = None
            descricao = None

    return produtos