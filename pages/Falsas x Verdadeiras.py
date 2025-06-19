import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Distribuição: Notícias Verdadeiras vs Falsas")

fake_df = pd.read_csv("Fake.csv")
true_df = pd.read_csv("True.csv")

qtd_falsas = len(fake_df)
qtd_verdadeiras = len(true_df)

labels = ["Verdadeiras", "Falsas"]
valores = [qtd_verdadeiras, qtd_falsas]
cores = ["#4169E1", "#8A2BE2"]  # Azul e Roxo

fig, ax = plt.subplots(figsize=(6, 6), facecolor="#1E1E1E")
ax.set_facecolor("#1E1E1E")

wedges, texts, autotexts = ax.pie(
    valores,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90,
    colors=cores,
    textprops={'color': 'white'}
)
ax.axis("equal")

st.pyplot(fig)

with st.expander("Comentário"):
    st.write("""
    Este gráfico de pizza apresenta a proporção entre notícias verdadeiras e falsas no conjunto de dados analisado. 

    As **notícias verdadeiras** representam uma parcela menor, enquanto as **notícias falsas** são mais numerosas, indicando um possível viés no volume de dados coletados.

    Essa diferença pode refletir tanto a facilidade de produção e disseminação de notícias falsas quanto um foco maior da base em detectar esse tipo de conteúdo. É um ponto importante a ser considerado na hora de treinar modelos de machine learning, pois o desequilíbrio pode afetar a performance e a imparcialidade das previsões.
    """)

