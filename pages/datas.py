import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carrega os dados
st.title("Evolução a cada 4 meses nas notícias falsas")
url_fake = "https://drive.google.com/uc?export=download&id=1Yjbj1aEZdsfAAMmTILPKUKhIJBvQ8f9f"
url_true = "https://drive.google.com/uc?export=download&id=16GUK2Tozv5jWPMZ6tfjTRgPyYUJ2-NaB"

df_fake = pd.read_csv(url_fake)
df_true = pd.read_csv(url_true)

# --- GRÁFICO DE FAKE ---
df_fake["date"] = pd.to_datetime(df_fake["date"], errors="coerce")
fake_contagem = df_fake["date"].value_counts().sort_index()

fig1, ax1 = plt.subplots(figsize=(10, 5), facecolor="#1E1E1E")
ax1.set_facecolor("#1E1E1E")
ax1.plot(fake_contagem.index, fake_contagem.values, color="#8A2BE2")
ax1.set_title("Notícias falsas por data", color="white")
ax1.tick_params(axis='x', rotation=45)
ax1.tick_params(axis='both', colors='white')
ax1.set_xlabel("Data", color="white")
ax1.set_ylabel("Quantidade", color="white")
st.pyplot(fig1)

with st.expander("Comentários - Notícias Falsas"):
    st.write("""
    Este gráfico apresenta a evolução diária da quantidade de notícias falsas publicadas ao longo do tempo.
    """)

# --- GRÁFICO DE VERDADEIRAS ---
st.title("Evolução a cada 3 meses nas notícias verdadeiras")
df_true["date"] = pd.to_datetime(df_true["date"], errors="coerce")
true_contagem = df_true["date"].value_counts().sort_index()

fig2, ax2 = plt.subplots(figsize=(10, 5), facecolor="#1E1E1E")
ax2.set_facecolor("#1E1E1E")
ax2.plot(true_contagem.index, true_contagem.values, color="#4169E1")
ax2.set_title("Notícias verdadeiras por data", color="white")
ax2.tick_params(axis='x', rotation=45)
ax2.tick_params(axis='both', colors='white')
ax2.set_xlabel("Data", color="white")
ax2.set_ylabel("Quantidade", color="white")
st.pyplot(fig2)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título
st.title("Volume de Notícias (13 a 20 de Janeiro de 2016)")

url_fake = "https://drive.google.com/uc?export=download&id=1Yjbj1aEZdsfAAMmTILPKUKhIJBvQ8f9f"
url_true = "https://drive.google.com/uc?export=download&id=16GUK2Tozv5jWPMZ6tfjTRgPyYUJ2-NaB"

df_fake = pd.read_csv(url_fake)
df_true = pd.read_csv(url_true)

# Conversão para datetime
df_fake['date'] = pd.to_datetime(df_fake['date'], errors='coerce')
df_true['date'] = pd.to_datetime(df_true['date'], errors='coerce')

# Filtro por intervalo de datas
start_date = pd.to_datetime("2016-01-13")
end_date = pd.to_datetime("2016-01-20")

fake_range = df_fake[(df_fake['date'] >= start_date) & (df_fake['date'] <= end_date)]
true_range = df_true[(df_true['date'] >= start_date) & (df_true['date'] <= end_date)]

# Contagem por dia
fake_counts = fake_range['date'].dt.date.value_counts().sort_index()
true_counts = true_range['date'].dt.date.value_counts().sort_index()

# Preparar os dados para o gráfico
datas = sorted(set(fake_counts.index).union(set(true_counts.index)))
valores_fake = [fake_counts.get(data, 0) for data in datas]
valores_true = [true_counts.get(data, 0) for data in datas]

# Gráfico
fig, ax = plt.subplots(figsize=(10, 4), facecolor="#1E1E1E")
ax.set_facecolor("#1E1E1E")

ax.bar(datas, valores_true, label="Verdadeiras", color="#0ABAB5")
ax.bar(datas, valores_fake, bottom=valores_true, label="Falsas", color="#003366")

ax.set_ylabel("Quantidade de notícias", color="white")
ax.set_xlabel("Data", color="white")
ax.set_title("Distribuição de Notícias por Dia", color="white")
ax.tick_params(colors="white")
ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))

st.pyplot(fig)

with st.expander("Comentários"):
    st.markdown("""
    Durante o intervalo de 13 a 20 de janeiro de 2016, observamos um volume relativamente equilibrado entre notícias falsas e verdadeiras. 
    A variação diária sugere que ambos os tipos de notícias eram publicadas constantemente, sem picos muito acentuados.

    É interessante notar que em alguns dias a quantidade de notícias verdadeiras supera a de falsas, o que pode indicar um período de maior cobertura factual — possivelmente relacionado a eventos relevantes da época.

    """)