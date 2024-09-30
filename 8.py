def numeros_pares_e_impares(lista):
    pares = [n for n in lista if n % 2 == 0]
    impares = [n for n in lista if n % 2 != 0]
    return pares, impares

if opcion == "Números pares e impares":
    numeros = st.text_area("Introduce una lista de números separados por comas")
    if st.button("Separar pares e impares"):
        lista_numeros = [int(x) for x in numeros.split(",") if x.strip().isdigit()]
        pares, impares = numeros_pares_e_impares(lista_numeros)
        st.write(f"Números pares: {pares}")
        st.write(f"Números impares: {impares}")
