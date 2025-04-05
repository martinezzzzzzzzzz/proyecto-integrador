import streamlit as st
import pandas as pd 
import io

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")

# Título de la app
st.title("Explorador de estudiantes - Colombia")

# Carga del dataset
df = pd.read_csv("data/estudiantes_colombia.csv")

# Mostrar el dataframe completo
st.subheader("Vista completa del dataset")
st.dataframe(df)

# Mostrar las primeras 5 filas
st.header("Primeras 5 filas del dataframe")
st.write(df.head())

# Mostrar las últimas 5 filas
st.header("Últimas 5 filas del dataframe")
st.write(df.tail())

# Mostrar resumen con info()
st.header("Información del dataset")
buffer = io.StringIO()
df.info(buf=buffer)
info_str = buffer.getvalue()
st.text(info_str)

# Mostrar estadísticas con describe()
st.header("Estadísticas del dataset")
st.write(df.describe())

# Seleccionar columnas específicas
st.header("Seleccionar columnas específicas")
columnas = st.multiselect(
    "Selecciona las columnas que quieres visualizar",
    df.columns.tolist(),
    default=["nombre", "edad", "promedio"] if all(col in df.columns for col in ["nombre", "edad", "promedio"]) else df.columns[:3]
)
st.write(df[columnas])

# Filtro por promedio
if "promedio" in df.columns:
    st.header("Filtrar estudiantes por promedio")
    valor_min, valor_max = float(df["promedio"].min()), float(df["promedio"].max())
    promedio_min = st.slider("Mostrar estudiantes con promedio mayor a:", min_value=valor_min, max_value=valor_max, value=valor_min)
    df_filtrado = df[df["promedio"] > promedio_min]
    st.write(df_filtrado)
else:
    st.warning("La columna 'promedio' no está disponible en el dataset.")

