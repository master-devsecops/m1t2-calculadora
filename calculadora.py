# Función para sumar dos números
def suma(a, b):
    return a + b

# Función para restar dos números
def resta(a, b):
    return a - b

# Función para multiplicar dos números
def multiplicacion(a, b):
    return a * b

# Función para dividir dos números
def division(a, b):
    if b == 0:
        return "No es posible dividir entre cero"
    return a / b

while True:
    print("Opciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Elige una opción (1/2/3/4/5): ")

    if opcion == '5':
        print("¡Adiós!")
        break

    if opcion not in ('1', '2', '3', '4'):
        print("Opción no válida")
        continue

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        print("Resultado:", suma(num1, num2))
    elif opcion == '2':
        print("Resultado:", resta(num1, num2))
    elif opcion == '3':
        print("Resultado:", multiplicacion(num1, num2))
    elif opcion == '4':
        print("Resultado:", division(num1, num2))

