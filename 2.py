def saludar(nombre):
    return f"Hola, {nombre}"

if opcion == "Saludo simple":
    nombre = st.text_input("Introduce tu nombre")
    if st.button("Saludar"):
        st.write(saludar(nombre))
