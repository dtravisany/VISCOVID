#agregamos streamlit para nuestro servidor 
import streamlit as st
#agregamos pandas para cargar los datos
import pandas as pd
#agregamos numpy
import numpy as np
#importar matplotlib pyplot

import matplotlib.pyplot as plt


# Embellecemos con seaborn
import seaborn as sns

sns.set_style("darkgrid")


#Título de la app.
st.title("Visualizador de COVID-19 Chile")

#Texto

st.markdown("### Bienvenido al visualizador")
st.markdown("Para iniciar seleccione su región y categoría")

df = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto3/TotalesPorRegion.csv")

#agregaremos 2 columnas:

col1,col2=st.columns(2)

#st.dataframe(df)
with col1:
    region = st.radio("Región", df.Region.unique())
    st.markdown("Su seleccion es: "+region)
with col2: 
    categoria = st.radio("Categoría", df.Categoria.unique())
    st.markdown("Su seleccion es: "+categoria)

#ilocs=df.iloc[:,2:-1]
super_filtro=df[(df.Region==region)&(df.Categoria==categoria)]
#st.table(ilocs.head(10))
#st.dataframe(super_filtro)
fig,ax = plt.subplots()
to_plot=super_filtro.iloc[:,2:-1]
#st.table(to_plot)

ax.plot(to_plot.T)
ax.set_title(region)
ax.set_ylabel(categoria)
ax.set_xlabel("Fecha")

xs= np.arange(0,super_filtro.shape[1]-2,30)
plt.xticks(xs,rotation=90)

st.pyplot(fig)


