import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv')

print(car_data.head(20))

st.header("Histograma del conteo de vehículos por cantidad de uso")
start_button = st.button("Crear un histograma")
if start_button:
    st.write('Creación de un histograma para la cantidad de vehículos por marca de cuentakilómetros')
    fig = px.histogram(car_data, x="odometer", nbins=50, width=800, height=600)
    st.plotly_chart(fig, use_container_width=True)

st.header('Gráfico de dispersión del precio de los vehículos por cantidad de uso')
start_button_2 = st.button("Crear un gráfico de dispersión")
if start_button_2:
    st.write("Creación de un gráfico de dispersión para el precio de vehículos por marca de cuentakilómetros")
    fig_2 = px.scatter(car_data, x="odometer", y="price", width=800, height=600)
    st.plotly_chart(fig_2, use_container_width=True)

condition = car_data.groupby("condition")["price"].mean()
condition_df = condition.reset_index()
st.header('Gráfico de barras de promedio de precio de vehículos por condición de uso')
build_bar_graph = st.checkbox("Construir gráfico de barras")
if build_bar_graph:
    st.write("Creación de un gráfico de barras para el precio promedio de vehículos por su condición de uso")
    fig_3 = px.bar(condition_df, x="condition", y="price", width=800, height=600)
    st.plotly_chart(fig_3, use_container_width=True)