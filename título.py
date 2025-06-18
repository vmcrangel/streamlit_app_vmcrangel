import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Distribuição do tamanho dos títulos das notícias")

# Carregar dados
df_fake = pd.read_csv("Fake.csv")
df_true = pd.read_csv("True.csv")

# Função para contar número de palavras em cada título
def contar_palavras(titulo):
    if pd.isna(titulo):
        return 0
    return len(titulo.split())

# Criar colunas com o tamanho dos títulos
df_fake['titulo_tamanho'] = df_fake['title'].apply(contar_palavras)
df_true['titulo_tamanho'] = df_true['title'].apply(contar_palavras)

# Plotar histograma com matplotlib
fig, ax = plt.subplots(figsize=(10,5), facecolor="#1E1E1E")
ax.hist(df_fake['titulo_tamanho'], bins=30, alpha=0.7, label='Fake News', color='#306998')
ax.hist(df_true['titulo_tamanho'], bins=30, alpha=0.7, label='True News', color='#6A5ACD')

ax.set_facecolor("#1E1E1E")
ax.tick_params(colors='white')
ax.set_title('Distribuição do tamanho dos títulos (nº de palavras)', color='white')
ax.set_xlabel('Número de palavras no título', color='white')
ax.set_ylabel('Frequência', color='white')
ax.legend(facecolor='#1E1E1E', edgecolor='white', labelcolor='white')

st.pyplot(fig)

with st.expander("Comentários"):
    st.write("""
    Observamos que a maioria dos títulos, tanto de notícias falsas quanto verdadeiras, concentra-se em uma faixa semelhante de palavras, entre 5 e 15.  
    Títulos de notícias falsas tendem a ser um pouco mais curtos, enquanto as verdadeiras apresentam uma leve variação para títulos mais longos.  
    Essa diferença pode indicar estratégias distintas na criação dos títulos para atrair leitores.
    """)

st.markdown("---")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

st.title("Palavras-chave exclusivas nos títulos")

# Carregar dados
df_fake = pd.read_csv("Fake.csv")
df_true = pd.read_csv("True.csv")

def limpar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r'[^a-zA-Z\s]', '', texto)  # Remove pontuação e números
    return texto

def extrair_palavras(titulos):
    palavras = []
    for titulo in titulos:
        texto_limpo = limpar_texto(titulo)
        palavras.extend(texto_limpo.split())
    return set(palavras)

# Extrair palavras únicas de fake e true
palavras_fake = extrair_palavras(df_fake['title'])
palavras_true = extrair_palavras(df_true['title'])

# Palavras exclusivas em fake e true
exclusivas_fake = palavras_fake - palavras_true
exclusivas_true = palavras_true - palavras_fake

# Contagem de palavras exclusivas
def contar_palavras_exclusivas(titulos, exclusivas):
    palavras = []
    for titulo in titulos:
        texto_limpo = limpar_texto(titulo)
        palavras.extend([p for p in texto_limpo.split() if p in exclusivas])
    return Counter(palavras).most_common(15)

top_exclusivas_fake = contar_palavras_exclusivas(df_fake['title'], exclusivas_fake)
top_exclusivas_true = contar_palavras_exclusivas(df_true['title'], exclusivas_true)

# Separar palavras e contagens
palavras_fake, contagens_fake = zip(*top_exclusivas_fake) if top_exclusivas_fake else ([], [])
palavras_true, contagens_true = zip(*top_exclusivas_true) if top_exclusivas_true else ([], [])

# Gráfico exclusivas fake
fig1, ax1 = plt.subplots(figsize=(10,5), facecolor="#1E1E1E")
ax1.barh(palavras_fake[::-1], contagens_fake[::-1], color='#306998')
ax1.set_facecolor("#1E1E1E")
ax1.tick_params(axis='x', colors='white')
ax1.tick_params(axis='y', colors='white')
ax1.set_title("Palavras exclusivas em títulos de notícias falsas", color='white')
st.pyplot(fig1)

# Gráfico exclusivas true
fig2, ax2 = plt.subplots(figsize=(10,5), facecolor="#1E1E1E")
ax2.barh(palavras_true[::-1], contagens_true[::-1], color='#6A5ACD')
ax2.set_facecolor("#1E1E1E")
ax2.tick_params(axis='x', colors='white')
ax2.tick_params(axis='y', colors='white')
ax2.set_title("Palavras exclusivas em títulos de notícias verdadeiras", color='white')
st.pyplot(fig2)

with st.expander("comentários"):
    st.write("""
    As palavras exclusivas encontradas nos títulos de notícias falsas e verdadeiras revelam padrões interessantes. 

    Nas notícias falsas, palavras como termos sensacionalistas ou específicos de teorias conspiratórias tendem a aparecer, indicando uma tentativa de chamar atenção ou gerar controvérsia. Isso pode explicar por que certas palavras não aparecem em notícias verdadeiras, que costumam ser mais factuais e formais.

    Já nas notícias verdadeiras, as palavras exclusivas geralmente estão relacionadas a contextos jornalísticos tradicionais, como locais geográficos, eventos oficiais e termos técnicos, refletindo a abordagem mais cuidadosa e informativa dessas publicações.

    Essa distinção sugere que a análise de palavras-chave exclusivas pode ajudar a diferenciar os tipos de notícias com base no estilo e no conteúdo abordado.
    """)
