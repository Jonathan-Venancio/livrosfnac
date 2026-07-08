def detectar_linhas(img):

    altura=img.shape[0]

    largura=img.shape[1]

    inicio=190

    fim=930

    passo=48

    linhas=[]

    y=inicio

    while y<fim:

        linhas.append(img[y:y+passo,:])

        y+=passo

    return linhas