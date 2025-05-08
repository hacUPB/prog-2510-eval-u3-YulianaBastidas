# 9.
# MENÚ DE OPERACIONES
while True:
    print("=== MENÚ DE OPERACIONES ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Ir al menú de postres")
    print("6. Salir")

    opcion = input("Elija una opción (1-6): ")

    match opcion:
        case '1' | '2' | '3' | '4':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            match opcion:
                case '1':
                    print("Resultado:", num1 + num2)
                case '2':
                    print("Resultado:", num1 - num2)
                case '3':
                    print("Resultado:", num1 * num2)
                case '4':
                    if num2 == 0:
                        print("Error: No se puede dividir por cero.")
                    else:
                        print("Resultado:", num1 / num2)

        case '5':
            # ======= MENÚ DE POSTRES =======
            while True:
                print("\n=== MENÚ DE POSTRES ===")
                print("1. Pastel de Chocolate")
                print("2. Torta Red Velvet")
                print("3. Cheesecake de Limón")
                print("4. Torta de Banano")
                print("5. Tiramisú")

                postre = input("Elija una opción (1-5): ")

                match postre:
                    case '1':
                        print("El pastel de chocolate está hecho con cacao 100% puro, cubierto con ganache y relleno de crema de avellanas.")
                    case '2':
                        print("La torta Red Velvet tiene un suave sabor a cacao y vainilla, con crema de queso como cobertura.")
                    case '3':
                        print("El cheesecake de limón es cremoso y refrescante, con una base de galleta y ralladura de limón natural.")
                    case '4':
                        print("La torta de banano es húmeda y dulce, preparada con banano maduro y un toque de canela.")
                    case '5':
                        print("El tiramisú es un postre italiano con capas de bizcocho, café, queso mascarpone y cacao espolvoreado.")
                    case _:
                        print("Opción no válida.")

                continuar_postre = input("¿Desea pedir otro postre? (s/n): ")
                if continuar_postre.lower() != 's':
                    print("Regresando al menú de operaciones...\n")
                    break

        case '6':
            print("Saliendo del programa...")
            break

        case _:
            print("Opción no válida. Intenta de nuevo.")

    continuar = input("¿Desea realizar otra operación o ir al menú de postres? (s/n): ")
    if continuar.lower() != 's':
        print("Gracias por usar el programa. ¡Hasta pronto!")
        break


# 10.

# Verificar contraseña:

contraseña_correcta = "1234"

cont_ingresada = input("Ingresa la contraseña: ")

if cont_ingresada == contraseña_correcta:
    print("Acceso concedido")
else:
    print("Acceso denegado")


# Clasificar calificaciones:


nota = float(input("Ingresa tu nota (0 a 5): "))

if nota < 0 or nota > 5:
    print("Nota fuera de rango.")
elif nota <= 2:
    print("Baja")
elif nota <= 4:
    print("Media")
else:  # nota == 5
    print("Alta")


# Operación aritmética:


num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operador = input("Elige una operación (+, -, *, /): ")

match operador:
    case '+':
        print("Resultado:", num1 + num2)
    case '-':
        print("Resultado:", num1 - num2)
    case '*':
        print("Resultado:", num1 * num2)
    case '/':
        if num2 == 0:
            print("Error: No se puede dividir por cero.")
        else:
            print("Resultado:", num1 / num2)
    case _:
        print("Operación no válida.")


