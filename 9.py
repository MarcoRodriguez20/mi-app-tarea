def multiplicar_todos(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

if opcion == "Multiplicación con *args":
    numeros = st.text_area("Introduce los números a multiplicar separados por comas")
    if st.button("Multiplicar"):
        lista_numeros = [int(x) for x in numeros.split(",") if x.strip().isdigit()]
        st.write(f"El resultado es: {multiplicar_todos(*lista_numeros)}")
