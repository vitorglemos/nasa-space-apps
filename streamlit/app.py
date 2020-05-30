import streamlit as st
import pandas as pd


def main():
    st.title('Track Covid-19')
    imagem = st.file_uploader('Upload your file', type='png')
    if imagem is not None:
        st.image(imagem)


if __name__ == '__main__':
    main()
