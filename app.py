import streamlit as st
import pandas as pd
import plotly.express as px

archivo_excel = pd.read_excel("Data.xlsx")


st.title("Aplicación Móvil")
st.sidebar.title("Parámetros")

seleccionador = st.sidebar.selectbox("Seleccione un módulo", ["Módulo 1", "Módulo 2", "Módulo 3"])

if seleccionador == "Módulo 1":
    st.write("Usted esta en el Módulo 1")
    st.write(archivo_excel)
    figura = px.line_3d(archivo_excel,x="Eje X",y="Eje Y",z="Eje Z")
    st.write(figura)

elif seleccionador == "Módulo 2":
    st.write("Usted esta en el Módulo 2")
else: 
    st.write("Usted esta en el Módulo 3")
