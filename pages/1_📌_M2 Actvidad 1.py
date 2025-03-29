import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import json

st.set_page_config(page_icon="📌", layout="wide")
st.title("Momento 2 - Actividad 1")

st.header("Descripción de la actividad")
st.markdown("""
En esta actividad trabajamos con diferentes formas de estructurar y visualizar datos en Python.
Utilizamos Pandas para manejar diccionarios, listas de diccionarios, listas de listas y series, así como 
para cargar información desde archivos CSV y JSON. Además, realizamos una consulta a una base de datos SQLite 
y mostramos los resultados en Streamlit.
""")

st.header("Objetivos de aprendizaje")
st.markdown("""
- Objetivo: Familiarizarse con la creación de DataFrames en Pandas y mostrarlos usando Streamlit.
""")

st.header("Solución")

# 1️⃣ DataFrame desde un Diccionario
st.subheader("📚 DataFrame de Libros (Diccionario)")
st.markdown("Se creó un DataFrame a partir de un diccionario de Python con información sobre libros.")
data_dict = {
    "Título": ["1984", "Cien años de soledad", "El principito"],
    "Autor": ["George Orwell", "Gabriel García Márquez", "Antoine de Saint-Exupéry"],
    "Año de Publicación": [1949, 1967, 1943],
    "Género": ["Distopía", "Realismo mágico", "Infantil"]
}
df_dict = pd.DataFrame(data_dict)
st.dataframe(df_dict)

st.code('''data_dict = {
    "Título": ["1984", "Cien años de soledad", "El principito"],
    "Autor": ["George Orwell", "Gabriel García Márquez", "Antoine de Saint-Exupéry"],
    "Año de Publicación": [1949, 1967, 1943],
    "Género": ["Distopía", "Realismo mágico", "Infantil"]
}
df_dict = pd.DataFrame(data_dict)
st.dataframe(df_dict)''', language="python")

# 2️⃣ DataFrame desde una Lista de Diccionarios
st.subheader("🌍 Información de Ciudades (Lista de Diccionarios)")
st.markdown("Se creó un DataFrame desde una lista de diccionarios con datos de ciudades.")
data_cities = [
    {"Nombre": "Nueva York", "Población": 8419600, "País": "EE.UU."},
    {"Nombre": "Tokio", "Población": 13929286, "País": "Japón"},
    {"Nombre": "Londres", "Población": 9304000, "País": "Reino Unido"}
]
df_cities = pd.DataFrame(data_cities)
st.dataframe(df_cities)

st.code('''data_cities = [
    {"Nombre": "Nueva York", "Población": 8419600, "País": "EE.UU."},
    {"Nombre": "Tokio", "Población": 13929286, "País": "Japón"},
    {"Nombre": "Londres", "Población": 9304000, "País": "Reino Unido"}
]
df_cities = pd.DataFrame(data_cities)
st.dataframe(df_cities)''', language="python")

# 3️⃣ DataFrame desde una Lista de Listas
st.subheader("🛒 Productos en Inventario (Lista de Listas)")
st.markdown("Se estructuró un DataFrame a partir de una lista de listas con información de productos en inventario.")
data_products = [
    ["Laptop", 1200, 50],
    ["Teléfono", 700, 100],
    ["Tablet", 300, 75]
]
df_products = pd.DataFrame(data_products, columns=["Producto", "Precio", "Stock"])
st.dataframe(df_products)

st.code('''data_products = [
    ["Laptop", 1200, 50],
    ["Teléfono", 700, 100],
    ["Tablet", 300, 75]
]
df_products = pd.DataFrame(data_products, columns=["Producto", "Precio", "Stock"])
st.dataframe(df_products)''', language="python")

# 4️⃣ DataFrame desde Series
st.subheader("👥 Datos de Personas (Series)")
st.markdown("Se creó un DataFrame a partir de Series de Pandas con datos de personas.")
nombres = pd.Series(["Carlos", "Ana", "Pedro"])
edades = pd.Series([25, 30, 35])
ciudades = pd.Series(["Madrid", "Barcelona", "Sevilla"])
df_series = pd.DataFrame({"Nombre": nombres, "Edad": edades, "Ciudad": ciudades})
st.dataframe(df_series)

st.code('''nombres = pd.Series(["Carlos", "Ana", "Pedro"])
edades = pd.Series([25, 30, 35])
ciudades = pd.Series(["Madrid", "Barcelona", "Sevilla"])
df_series = pd.DataFrame({"Nombre": nombres, "Edad": edades, "Ciudad": ciudades})
st.dataframe(df_series)''', language="python")

# 5️⃣ Consulta a SQLite
st.subheader("📊 Datos desde SQLite")
st.markdown("Se realizó una consulta a una base de datos SQLite para extraer información de estudiantes.")
conn = sqlite3.connect("data/estudiantes.db")
try:
    df_sqlite = pd.read_sql("SELECT * FROM estudiantes", conn)
    st.dataframe(df_sqlite)
except Exception as e:
    st.error("Error al consultar la base de datos. Asegúrate de que la tabla existe.")
    st.write(e)
conn.close()

st.code('''conn = sqlite3.connect("data/estudiantes.db")
df_sqlite = pd.read_sql("SELECT * FROM estudiantes", conn)
st.dataframe(df_sqlite)
conn.close()''', language="python")

# 6️⃣ DataFrame desde un Archivo Excel
st.subheader("📄 Datos desde Excel")
st.markdown("Se cargó un DataFrame desde un archivo Excel (`data.xlsx`).")
excel_filename = "data/data.xlsx"
try:
    df_excel = pd.read_excel(excel_filename, engine="openpyxl")
    st.dataframe(df_excel)
except FileNotFoundError:
    st.error(f"El archivo {excel_filename} no existe. Asegúrate de crearlo y guardarlo en el proyecto.")

st.code('''df_excel = pd.read_excel("data/data.xlsx", engine="openpyxl")
st.dataframe(df_excel)''', language="python")

# 7️⃣ DataFrame desde un archivo JSON
st.subheader("📄 Datos desde JSON")
st.markdown("Se cargó un DataFrame desde un archivo JSON (`data.json`).")
json_filename = "data/data.json"
try:
    df_json = pd.read_json(json_filename)
    st.dataframe(df_json)
except (FileNotFoundError, ValueError):
    st.error(f"El archivo {json_filename} no existe o está vacío.")

st.code('''df_json = pd.read_json("data/data.json")
st.dataframe(df_json)''', language="python")

# 8️⃣ DataFrame desde una URL (Archivo CSV en línea)
st.subheader("🌍 Datos desde URL (CSV en línea)")
st.markdown("Se cargó un DataFrame desde un archivo CSV alojado en línea con datos abiertos.")

csv_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"  # URL de un CSV público
try:
    df_url = pd.read_csv(csv_url)
    st.dataframe(df_url)
except Exception as e:
    st.error("No se pudo cargar el archivo CSV desde la URL.")
    st.write(e)

st.code('''csv_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
df_url = pd.read_csv(csv_url)
st.dataframe(df_url)''', language="python")


st.code('''df_json = pd.read_json("data.json")
st.dataframe(df_json)''', language="python")

# 9️⃣ DataFrame desde un array de NumPy
st.subheader("🔢 Datos desde NumPy")
st.markdown("Se creó un DataFrame a partir de un array de NumPy con datos numéricos.")
data_numpy = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df_numpy = pd.DataFrame(data_numpy, columns=["A", "B", "C"])
st.dataframe(df_numpy)

st.code('''data_numpy = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df_numpy = pd.DataFrame(data_numpy, columns=["A", "B", "C"])
st.dataframe(df_numpy)''', language="python")
