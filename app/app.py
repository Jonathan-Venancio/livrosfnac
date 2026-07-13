import streamlit as st
from PIL import Image

from barcode_utils import gerar_barcode
from ocr import ler_imagem

st.set_page_config(page_title="Leitor de EAN")

st.title("📚 Leitor de Lista de Livros")

arquivo = st.file_uploader(
    "Envie uma foto da folha",
    type=["jpg", "jpeg", "png"]
)

if arquivo:

    imagem = Image.open(arquivo)

    st.image(imagem)

    with st.spinner("Lendo imagem..."):

        produtos = ler_imagem(imagem)

    st.success(f"{len(produtos)} produtos encontrados")

    for produto in produtos:

        st.divider()

        st.subheader(produto["descricao"])

        st.write(produto["ean"])

        codigo = gerar_barcode(produto["ean"])

        st.image(codigo)