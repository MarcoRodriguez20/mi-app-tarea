def calcular_precio_final(precio, descuento=10, impuesto=16):
    precio_descuento = precio * (1 - descuento / 100)
    precio_final = precio_descuento * (1 + impuesto / 100)
    return precio_final

if opcion == "Calculadora de descuento":
    precio = st.number_input("Precio original", value=0)
    descuento = st.number_input("Descuento (%)", value=10)
    impuesto = st.number_input("Impuesto (%)", value=16)
    if st.button("Calcular precio final"):
        st.write(f"El precio final es: {calcular_precio_final(precio, descuento, impuesto)}")
