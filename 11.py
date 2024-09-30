def calculadora_flexible(num1, num2, operacion="suma"):
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicacion":
        return num1 * num2
    elif operacion == "division":
        return num1 / num2 if num2 != 0 else "No se puede dividir por cero"

if opcion == "Calculadora flexible":
    num1 = st.number_input("Número 1", value=0)
    num2 = st.number_input("Número 2", value=0)
    operacion = st.selectbox("Operación", ["suma", "resta", "multiplicacion", "division"])
    if st.button("Calcular"):
        st.write(f"Resultado: {calculadora_flexible(num1, num2, operacion)}")
