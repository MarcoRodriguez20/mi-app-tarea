def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

if opcion == "Área de un triángulo":
    base = st.number_input("Base del triángulo", value=0)
    altura = st.number_input("Altura del triángulo", value=0)
    if st.button("Calcular área"):
        st.write(f"El área del triángulo es: {calcular_area_triangulo(base, altura)}")
