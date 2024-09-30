import streamlit as st

def saludar(nombre):
    return f"Hola, {nombre}!"

def sumar(a, b):
    return a + b

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def calcular_precio_final(precio, descuento=10, impuesto=16):
    precio_descuento = precio * (1 - descuento / 100)
    precio_final = precio_descuento * (1 + impuesto / 100)
    return precio_final

def sumar_lista(lista):
    return sum(lista)

def producto(nombre, cantidad=1, precio=10):
    return cantidad * precio

def numeros_pares_e_impares(lista):
    pares = [n for n in lista if n % 2 == 0]
    impares = [n for n in lista if n % 2 != 0]
    return pares, impares

def multiplicar_todos(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado if args else 1

def informacion_personal(**kwargs):
    return kwargs

def calculadora_flexible(num1, num2, operacion="suma"):
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicacion":
        return num1 * num2
    elif operacion == "division":
        return num1 / num2 if num2 != 0 else "No se puede dividir por cero"

st.title("Tablero de Ejercicios Sobre Funciones Marco Contreras")

st.sidebar.title("Navegación")
opcion = st.sidebar.selectbox("Selecciona un ejercicio", 
                              ("Saludo simple", 
                               "Suma de dos números", 
                               "Área de un triángulo",
                               "Calculadora de descuento",
                               "Suma de una lista",
                               "Producto con valores predeterminados",
                               "Números pares e impares",
                               "Multiplicación con *args",
                               "Información personal con **kwargs",
                               "Calculadora flexible"))

#1
if opcion == "Saludo simple":
    st.header("1. Saludo simple")
    nombre = st.text_input("Introduce tu nombre")
    if st.button("Saludar"):
        st.write(saludar(nombre))

#2
elif opcion == "Suma de dos números":
    st.header("2. Suma de dos números")
    num1 = st.number_input("Número 1", value=0)
    num2 = st.number_input("Número 2", value=0)
    if st.button("Sumar"):
        st.write(f"La suma es: {sumar(num1, num2)}")

#3
elif opcion == "Área de un triángulo":
    st.header("3. Área de un triángulo")
    base = st.number_input("Base del triángulo", value=0)
    altura = st.number_input("Altura del triángulo", value=0)
    if st.button("Calcular área"):
        st.write(f"El área del triángulo es: {calcular_area_triangulo(base, altura)}")

#4
elif opcion == "Calculadora de descuento":
    st.header("4. Calculadora de descuento")
    precio = st.number_input("Precio original", value=0)
    descuento = st.number_input("Descuento (%)", value=10)
    impuesto = st.number_input("Impuesto (%)", value=16)
    if st.button("Calcular precio final"):
        st.write(f"El precio final es: {calcular_precio_final(precio, descuento, impuesto)}")

#5
elif opcion == "Suma de una lista":
    st.header("5. Suma de una lista de números")
    numeros = st.text_area("Introduce una lista de números separados por comas")
    if st.button("Sumar lista"):
        lista_numeros = [int(x) for x in numeros.split(",") if x.strip().isdigit()]
        st.write(f"La suma de la lista es: {sumar_lista(lista_numeros)}")

#6
elif opcion == "Producto con valores predeterminados":
    st.header("6. Producto con valores predeterminados")
    nombre_producto = st.text_input("Nombre del producto")
    cantidad = st.number_input("Cantidad", value=1)
    precio = st.number_input("Precio por unidad", value=10)
    if st.button("Calcular precio total"):
        st.write(f"El precio total es: {producto(nombre_producto, cantidad, precio)}")

#7
elif opcion == "Números pares e impares":
    st.header("7. Números pares e impares")
    numeros = st.text_area("Introduce una lista de números separados por comas")
    if st.button("Separar pares e impares"):
        lista_numeros = [int(x) for x in numeros.split(",") if x.strip().isdigit()]
        pares, impares = numeros_pares_e_impares(lista_numeros)
        st.write(f"Números pares: {pares}")
        st.write(f"Números impares: {impares}")

#8
elif opcion == "Multiplicación con *args":
    st.header("8. Multiplicación con *args")
    numeros = st.text_area("Introduce los números a multiplicar separados por comas")
    if st.button("Multiplicar"):
        lista_numeros = [int(x) for x in numeros.split(",") if x.strip().isdigit()]
        st.write(f"El resultado es: {multiplicar_todos(*lista_numeros)}")

#9
elif opcion == "Información personal con **kwargs":
    st.header("9. Información personal con **kwargs")
    nombre = st.text_input("Nombre")
    edad = st.number_input("Edad", value=0)
    direccion = st.text_input("Dirección")
    if st.button("Mostrar información"):
        st.write(informacion_personal(nombre=nombre, edad=edad, direccion=direccion))

#10
elif opcion == "Calculadora flexible":
    st.header("10. Calculadora flexible")
    num1 = st.number_input("Número 1", value=0)
    num2 = st.number_input("Número 2", value=0)
    operacion = st.selectbox("Operación", ["suma", "resta", "multiplicacion", "division"])
    if st.button("Calcular"):
        st.write(f"Resultado: {calculadora_flexible(num1, num2, operacion)}")
