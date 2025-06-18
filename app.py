import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    url_fake = "https://drive.google.com/uc?export=download&id=1Yjbj1aEZdsfAAMmTILPKUKhIJBvQ8f9f"
    url_true = "https://drive.google.com/uc?export=download&id=16GUK2Tozv5jWPMZ6tfjTRgPyYUJ2-NaB"
    fake = pd.read_csv(url_fake)
    true = pd.read_csv(url_true)
    fake["label"] = "Fake"
    true["label"] = "Real"
    df = pd.concat([fake, true], ignore_index=True)
    return df

df = load_data()

st.title("Trabalho final") 
st.title("introdução à Ciência de Dados")

st.markdown("<hr>", unsafe_allow_html=True)

st.write("## CIADM1A-CIA001-20251")

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("### 👨‍🏫 Professor:")
st.markdown("**Alexandre Vaz Roriz**")

st.markdown("### 👥 Alunos:")
st.markdown("**Victor De Melo** e **Henrique Coutinho**")

st.markdown("<hr>", unsafe_allow_html=True)

texto = """
<div style='text-align: justify'>
O problema das fake news é um dos maiores desafios da atualidade, impactando diretamente a sociedade, a política e a economia. 
A propagação de informações falsas pode gerar desinformação, pânico e manipulação de opinião pública. Por isso, a criação de ferramentas automatizadas que auxiliem na identificação rápida e confiável dessas notícias é fundamental.
Neste trabalho, apresentamos um aplicativo interativo desenvolvido em Streamlit com o objetivo de oferecer uma ferramenta eficiente para a detecção de notícias falsas (fake news). 
Utilizando um conjunto de dados robusto disponível no Kaggle, realizamos uma análise detalhada e aplicamos técnicas de aprendizado de máquina para classificar notícias em verdadeiras ou falsas.
</div>
"""

st.markdown(texto, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("## 📌 Funcionalidades do Aplicativo")

# Upload dos Dados
st.markdown("""
<div style="
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 10px;
    background-color: #2c2c2c;">
  <h4>📥 Upload dos Dados</h4>
  <p>Permite carregar arquivos <code>.csv</code> com notícias verdadeiras e falsas para análise detalhada.</p>
</div>
""", unsafe_allow_html=True)

# Análise e Visualização dos Gráficos
st.markdown("""
<div style="
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 10px;
    background-color: #2c2c2c;">
  <h4>📊 Análise Visual com Gráficos</h4>
  <p>Gráficos interativos mostram a distribuição das notícias por categorias, datas e regiões, facilitando a compreensão dos dados.</p>
</div>
""", unsafe_allow_html=True)

# Navegação Multi-páginas
st.markdown("""
<div style="
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 10px;
    background-color: #2c2c2c;">
  <h4>🗂️ Navegação Multi-páginas</h4>
  <p>Menu lateral para acessar páginas separadas com gráficos e análises específicas, permitindo foco em cada tema.</p>
</div>
""", unsafe_allow_html=True)

# Comentários Explicativos
st.markdown("""
<div style="
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 10px;
    background-color: #2c2c2c;">
  <h4>💬 Comentários Explicativos</h4>
  <p>Cada gráfico acompanha uma seção expansível com explicações e insights, facilitando a interpretação dos resultados.</p>
</div>
""", unsafe_allow_html=True)

# Atualização e Exportação dos Resultados
st.markdown("""
<div style="
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 10px;
    background-color: #2c2c2c;">
  <h4>💾 Exportação dos Resultados</h4>
  <p>Opção para baixar os dados analisados com previsões e classificações para uso externo e documentação.</p>
</div>
""", unsafe_allow_html=True)

st.write("#### clique no menu lateral esquerdo para saber mais das nossas análises")


