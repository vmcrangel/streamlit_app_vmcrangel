import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Categorias mais frequentes")

# Carregando os dados
df_fake = pd.read_csv("Fake.csv")
df_true = pd.read_csv("True.csv")

# Adiciona uma coluna para indicar o tipo
df_fake["label"] = "Fake"
df_true["label"] = "True"

# Junta os dois DataFrames
df_all = pd.concat([df_fake, df_true])

# Agrupa por subject e label
contagem = df_all.groupby(["subject", "label"]).size().unstack().fillna(0)

# Ordena pelo total
contagem["Total"] = contagem.sum(axis=1)
contagem = contagem.sort_values(by="Total", ascending=False)

# Remove a coluna auxiliar "Total"
contagem = contagem.drop(columns="Total")

# Cores para fake (roxo) e true (azul)
colors = ["#8A2BE2", "#4169E1"]  # roxo e azul

# Gráfico de barras agrupadas
fig, ax = plt.subplots(figsize=(10, 6), facecolor="#1E1E1E")
ax.set_facecolor("#1E1E1E")

contagem.plot(kind="bar", ax=ax, color=colors)

ax.set_title("Distribuição de notícias por categoria (subject)", color="white")
ax.set_ylabel("Quantidade de notícias", color="white")
ax.set_xlabel("Categoria", color="white")
ax.tick_params(axis='x', rotation=45, labelcolor='white')
ax.tick_params(axis='y', colors='white')
ax.legend(["Fake", "True"], facecolor="#1E1E1E", labelcolor='white')

st.pyplot(fig)


with st.expander("Comentários"):
    st.write("""
    O campo **`categorias`** representa o tema central de cada notícia, classificando o conteúdo em categorias específicas como política, economia, saúde, entre outras.  

    Essa categorização é fundamental para entender o contexto e a área de interesse das notícias, permitindo análises segmentadas que identificam padrões distintos entre notícias verdadeiras e falsas.  

    Ao observar a distribuição de fake news e notícias verdadeiras por categoria, conseguimos perceber quais temas são mais suscetíveis à desinformação, auxiliando no direcionamento de estratégias para combate a fake news.  

    Essa visão detalhada é essencial para estudos que buscam compreender o comportamento da desinformação e seus impactos em diferentes setores da sociedade.
    """)

st.markdown("---")
    

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Categorias com mais notícias falsas e verdadeiras")

# Carregando os dados
df_fake = pd.read_csv("Fake.csv")
df_true = pd.read_csv("True.csv")

# Contagem dos subjects para fake e true
cont_fake = df_fake['subject'].value_counts()
cont_true = df_true['subject'].value_counts()

# Seleciona top 7 para visualização melhor
top_fake = cont_fake.head(7)
top_true = cont_true.head(7)

# Cores frias para fake (tons de azul e roxo)
colors_fake = ['#4B8BBE', '#306998', '#284B8B', '#6A5ACD', '#483D8B', '#4169E1', '#1E90FF']

# Cores frias para true (tons de verde e azul)
colors_true = ['#3CB371', '#2E8B57', '#20B2AA', '#008080', '#4682B4', '#5F9EA0', '#66CDAA']

# --- Gráfico fake news ---

fig1, ax1 = plt.subplots(figsize=(10,4), facecolor="#1E1E1E")
ax1.set_facecolor("#1E1E1E")

wedges1, texts1, autotexts1 = ax1.pie(
    top_fake,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors_fake,
    textprops={'color':'white'},
    labels=None  # remove labels do gráfico
)

# Legenda à direita
ax1.legend(
    wedges1, 
    top_fake.index, 
    title="Categorias",
    loc="center left",
    bbox_to_anchor=(1, 0.5),
    fontsize=10,
    title_fontsize=12,
    facecolor="#1E1E1E",
    edgecolor="none",
    labelcolor="white"
)

ax1.set_title("Top categorias - Notícias Falsas", color='white')

st.pyplot(fig1)

# --- Gráfico true news ---

fig2, ax2 = plt.subplots(figsize=(10,4), facecolor="#1E1E1E")
ax2.set_facecolor("#1E1E1E")

wedges2, texts2, autotexts2 = ax2.pie(
    top_true,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors_true,
    textprops={'color':'white'},
    labels=None  # remove labels do gráfico
)

# Legenda à direita
ax2.legend(
    wedges2, 
    top_true.index, 
    title="Categorias",
    loc="center left",
    bbox_to_anchor=(1, 0.5),
    fontsize=10,
    title_fontsize=12,
    facecolor="#1E1E1E",
    edgecolor="none",
    labelcolor="white"
)

ax2.set_title("Top categorias - Notícias Verdadeiras", color='white')

st.pyplot(fig2)

with st.expander("Comentários"):
    st.write("""
    Estes gráficos destacam as categorias mais frequentes nas notícias falsas e verdadeiras, revelando quais temas são mais explorados em cada grupo.

    **Categorias com mais notícias verdadeiras:**
    - politicnews
    - worldnews

    **Categorias com mais notícias falsas:**
    - news
    - politics
    - left-news
    - government news
    - US_news
    - Middle-east
    """)