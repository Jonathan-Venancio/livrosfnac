import io
import re

import requests
from PIL import Image

API_KEY = "K84127887388957"

OCR_URL = "https://api.ocr.space/Parse/Image"


def comprimir_imagem(imagem, limite=1024 * 1024):

    imagem = imagem.convert("RGB")

    largura, altura = imagem.size

    while True:

        for qualidade in range(95, 15, -5):

            buffer = io.BytesIO()

            imagem.save(
                buffer,
                format="JPEG",
                quality=qualidade,
                optimize=True
            )

            if buffer.tell() <= limite:
                buffer.seek(0)
                return buffer

        largura = int(largura * 0.9)
        altura = int(altura * 0.9)

        imagem = imagem.resize(
            (largura, altura),
            Image.LANCZOS
        )


def extrair_produtos(parsed_results):

    palavras = []

    for pagina in parsed_results:

        overlay = pagina.get("TextOverlay", {})

        for linha in overlay.get("Lines", []):

            top = linha["MinTop"]

            for palavra in linha["Words"]:

                palavras.append({
                    "texto": palavra["WordText"].strip(),
                    "left": palavra["Left"],
                    "top": top
                })

    # Agrupa palavras pela mesma linha (Top parecido)
    linhas = {}

    tolerancia = 8

    for p in palavras:

        encontrou = False

        for y in list(linhas.keys()):

            if abs(y - p["top"]) <= tolerancia:
                linhas[y].append(p)
                encontrou = True
                break

        if not encontrou:
            linhas[p["top"]] = [p]

    produtos = []

    for y in sorted(linhas.keys()):

        linha = sorted(linhas[y], key=lambda x: x["left"])

        textos = [x["texto"] for x in linha]

        # ignora cabeçalho
        if any(t.upper() == "EAN" for t in textos):
            continue

        if any("DESCRI" in t.upper() for t in textos):
            continue

        ean = None

        descricao = []

        for palavra in linha:

            texto = palavra["texto"]

            numeros = re.sub(r"\D", "", texto)

            if len(numeros) == 13:
                ean = numeros
            else:
                descricao.append(texto)

        if ean and descricao:

            produtos.append({
                "ean": ean,
                "descricao": " ".join(descricao)
            })

    return produtos


def ler_imagem(imagem):

    imagem = comprimir_imagem(imagem)

    resposta = requests.post(
        OCR_URL,
        headers={
            "apikey": API_KEY
        },
        files={
            "filename": (
                "imagem.jpg",
                imagem,
                "image/jpeg"
            )
        },
        data={
            "language": "por",
            "OCREngine": 2,
            "isOverlayRequired": True
        },
        timeout=60
    )

    resposta.raise_for_status()

    dados = resposta.json()

    if dados.get("IsErroredOnProcessing"):
        raise Exception(str(dados.get("ErrorMessage")))

    return extrair_produtos(dados["ParsedResults"])