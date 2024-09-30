def sumar_lista(lista):
    return sum(lista)

if opcion == "Suma de una lista":
    numeros = st.text_area("Introduce una lista de números separados por comas")
    if st.button("Sumar lista"):
        lista_numeros = [int(x) for x in numeros.split(",") if x.strip().isdigit()]
        st.write(f"La suma de la lista es: {sumar_lista(lista_numeros)}")
