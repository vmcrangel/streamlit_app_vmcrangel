import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

st.title("Ocorrência de Termos Específicos nos Títulos")

url_fake = "https://drive.google.com/uc?export=download&id=1Yjbj1aEZdsfAAMmTILPKUKhIJBvQ8f9f"
url_true = "https://drive.google.com/uc?export=download&id=16GUK2Tozv5jWPMZ6tfjTRgPyYUJ2-NaB"

# Carrega os arquivos CSV da web
df_fake = pd.read_csv(url_fake)
df_true = pd.read_csv(url_true)
# Função para processar e extrair palavras
def extrair_palavras(textos):
    todas = " ".join(textos).lower()
    todas = re.sub(r'[^a-zA-Z]', ' ', todas)  # remove pontuações
    palavras = todas.split()
    return Counter(palavras)

# Extrair palavras dos títulos
palavras_fake = extrair_palavras(df_fake['title'])
palavras_true = extrair_palavras(df_true['title'])

# Termos que queremos analisar
termos = ['trump', 'obama', 'clinton', 'russia', 'china', 'hillary', 'biden', 'email']

# Criar listas com as contagens
cont_fake = [palavras_fake.get(palavra, 0) for palavra in termos]
cont_true = [palavras_true.get(palavra, 0) for palavra in termos]

# Gráfico de barras
fig, ax = plt.subplots(figsize=(10, 5), facecolor='#1e1e1e')
ax.set_facecolor('#1e1e1e')

x = range(len(termos))
ax.bar(x, cont_fake, width=0.4, label='Falsas', color='#8A2BE2', align='center')
ax.bar([i + 0.4 for i in x], cont_true, width=0.4, label='Verdadeiras', color='#1E90FF', align='center')

# Customização
ax.set_xticks([i + 0.2 for i in x])
ax.set_xticklabels(termos, rotation=45, color='white')
ax.set_ylabel("Ocorrências", color='white')
ax.set_title("Ocorrência de Termos Específicos nos Títulos", color='white')
ax.legend(loc='upper right')
ax.tick_params(colors='white')

st.pyplot(fig)

with st.expander("Comentários"):
    st.write("""
    Esse gráfico mostra como certos nomes e temas políticos aparecem de forma diferente em notícias falsas e verdadeiras.
    
    - Termos como **'trump'** e **'hillary'** são recorrentes em ambos os grupos, sugerindo foco político.
    - Já termos como **'email'** e **'russia'** aparecem mais em notícias falsas, indicando temas sensacionalistas ou polêmicos.
    - A distribuição sugere que a desinformação se aproveita de temas com alto apelo emocional e político.
    """)

st.markdown("---")

import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

st.title("Similaridade entre Notícias")

# Carregar dados
df_fake = pd.read_csv("Fake.csv")
df_true = pd.read_csv("True.csv")

# Adicionar rótulo de classe
df_fake['label'] = 'Falsa'
df_true['label'] = 'Verdadeira'

# Juntar os dados
df = pd.concat([df_fake, df_true], ignore_index=True)

# Usar apenas uma amostra para visualização rápida
df_sample = df.sample(500, random_state=42)

# Vetorizar os textos com TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
X = vectorizer.fit_transform(df_sample['text'])

# Redução de dimensionalidade com PCA
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X.toarray())

# Plot
fig, ax = plt.subplots(figsize=(10, 6), facecolor='#1e1e1e')
ax.set_facecolor('#1e1e1e')

cores = {'Falsa': '#8A2BE2', 'Verdadeira': '#1E90FF'}

for classe in df_sample['label'].unique():
    indices = df_sample['label'] == classe
    ax.scatter(X_reduced[indices, 0], X_reduced[indices, 1],
               label=classe, alpha=0.6, color=cores[classe])

ax.set_title("Distribuição de Similaridade entre Notícias", color='white')
ax.set_xlabel("Componente 1", color='white')
ax.set_ylabel("Componente 2", color='white')
ax.tick_params(colors='white')
ax.legend()

st.pyplot(fig)

with st.expander("Comentários"):
    st.write("""
    Este gráfico mostra como os textos das notícias se distribuem com base em sua similaridade textual. 
    
    - Observamos que as **notícias verdadeiras** e **falsas** tendem a formar agrupamentos diferentes, 
      indicando que seus conteúdos têm padrões distintos.
    - Isso sugere que modelos de machine learning conseguem captar diferenças reais no estilo de escrita e 
      vocabulário entre os dois tipos de notícia.
    """)