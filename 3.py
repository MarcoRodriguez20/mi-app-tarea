def sumar(a, b):
    return a + b

if opcion == "Suma de dos números":
    num1 = st.number_input("Número 1", value=0)
    num2 = st.number_input("Número 2", value=0)
    if st.button("Sumar"):
        st.write(f"La suma es: {sumar(num1, num2)}")
