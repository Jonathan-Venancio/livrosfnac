import streamlit as st
from PIL import Image

from modules.image import preparar_imagem
from modules.table import detectar_linhas
from modules.parser import extrair_produtos
from modules.ui import mostrar_produtos

st.set_page_config(layout="wide")

st.title("Leitor de Lista de Livros")

arquivo = st.file_uploader(
    "Escolha uma foto",
    type=["jpg","jpeg","png"]
)

if arquivo:

    imagem = Image.open(arquivo)

    imagem = preparar_imagem(imagem)

    linhas = detectar_linhas(imagem)

    produtos = extrair_produtos(linhas)

    mostrar_produtos(produtos)