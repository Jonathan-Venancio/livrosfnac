import streamlit as st

from .barcode import gerar

def mostrar_produtos(produtos):

    for produto in produtos:

        st.divider()

        st.subheader(produto["nome"])

        st.write(produto["ean"])

        st.image(gerar(produto["ean"]))