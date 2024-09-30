def informacion_personal(**kwargs):
    return kwargs

if opcion == "Información personal con **kwargs":
    nombre = st.text_input("Nombre")
    edad = st.number_input("Edad", value=0)
    direccion = st.text_input("Dirección")
    if st.button("Mostrar información"):
        st.write(informacion_personal(nombre=nombre, edad=edad, direccion=direccion))
