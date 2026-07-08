from rapidocr_onnxruntime import RapidOCR

engine=RapidOCR()

def extrair_produtos(linhas):

    produtos=[]

    for linha in linhas:

        ean_img=linha[:,0:270]

        nome_img=linha[:,280:]

        ean=engine(ean_img)

        nome=engine(nome_img)

        if ean:

            produtos.append({
                "ean":ean[0][1],
                "nome":nome[0][1]
            })

    return produtos