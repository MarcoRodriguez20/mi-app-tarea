def producto(nombre, cantidad=1, precio=10):
    return cantidad * precio

if opcion == "Producto con valores predeterminados":
    nombre_producto = st.text_input("Nombre del producto")
    cantidad = st.number_input("Cantidad", value=1)
    precio = st.number_input("Precio por unidad", value=10)
    if st.button("Calcular precio total"):
        st.write(f"El precio total es: {producto(nombre_producto, cantidad, precio)}")
