import streamlit as st
from PIL import Image
import numpy as np

from modules.image import preparar_imagem
from modules.parser import extrair_produtos
from modules.ui import mostrar_produtos

st.set_page_config(layout="wide")

st.title("Leitor de Códigos de Barras")

arquivo = st.file_uploader(
    "Escolha uma foto",
    type=["jpg","jpeg","png"]
)

if arquivo:
    imagem = Image.open(arquivo)
    
    st.image(imagem, caption="Imagem original", use_container_width=True)
    
    imagem_array = preparar_imagem(imagem)
    
    produtos = extrair_produtos(imagem_array)
    
    if produtos:
        st.success(f"Encontrados {len(produtos)} códigos de barras!")
        mostrar_produtos(produtos)
    else:
        st.warning("Nenhum código de barras encontrado na imagem.")