import streamlit as st

st.title("Tablero de Ejercicios de Python")


st.sidebar.title("Navegación")
opcion = st.sidebar.selectbox("Selecciona un ejercicio", 
                              ("Saludo simple", 
                               "Suma de dos números", 
                               "Área de un triángulo",
                               "Calculadora de descuento",
                               "Suma de una lista",
                               "Producto con valores predeterminados",
                               "Números pares e impares",
                               "Multiplicación con *args",
                               "Información personal con **kwargs",
                               "Calculadora flexible"))


if opcion == "Saludo simple":
    st.header("1. Saludo simple")
    nombre = st.text_input("Introduce tu nombre")
    if st.button("Saludar"):
        st.write(f"Hola, {nombre}!")
