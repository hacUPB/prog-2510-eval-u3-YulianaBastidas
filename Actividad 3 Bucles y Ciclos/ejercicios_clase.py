# Escribe un programa que solicite al usuario ingresar un número entero positivo. Luego, utiliza un bucle while para imprimir la tabla de multiplicar de ese número, desde 1 hasta 10. Por ejemplo, si el usuario ingresa el número 5, el programa debería imprimir:
numero = int(input("Ingresa un número entero positivo: "))

contador = 1
while contador <= 10:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1

 # Ejercicio 4:

numeros_pares = []

n = int(input("Ingrese el no. de números pares requeridos: "))
for i in range(n):
    numeros_pares.append(i*2)
print("los",n, "numeros pares son:",numeros_pares)


# Ejercicio 7: Programa de Conversión de Temperatura

print("Tabla de Conversión de Temperatura")
print("----------------------------------")
print("Celsius (°C)  |  Fahrenheit (°F)")
print("----------------------------------")

for celsius in range(0, 101, 10): # recorremos de 1 a 100 saltando cada 10
    fahrenheit = ((celsius * 9/5) + 32)
    print( celsius,"(C°)","|",  fahrenheit,"(F°)"  )