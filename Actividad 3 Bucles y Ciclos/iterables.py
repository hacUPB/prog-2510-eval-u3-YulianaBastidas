# 1. Agregar Elementos a una Lista



# Insertamos un elemento al final de la lista con append
frutas = ["mango", "banano", "pera"]
frutas.append("piña")
print(frutas)

# Agregamos un elemento en una posición deseada

frutas.insert(3, "sandía")
print(frutas)


# Extender la lista con otra lista

frutas.extend(["manzana", "uva"]) # se agregan al final de la lista también
print(frutas)



# 2. Eliminar Elementos de una Lista



numeros = [5, 456, 78, 90, 1]
numeros.remove(5) # eliminamos el número 5
print(numeros)

valor_eli = numeros.pop(1) # eliminamos el número en la posición 1
print(valor_eli)

numeros.clear() # borramos todos los elementos de la lista "numeros"
print(numeros)

print("Valor Eliminado:", valor_eli) # mostramos que numero eliminamos con .pop


# 3. Ordenar y Revertir una Lista



nombres = ["Miguel", "Laura", "Mark", "Cris"]

# Ordenar la lista alfabéticamente (ascendente)
nombres.sort()
print(nombres)

# Ordenar la lista alfabéticamente en orden descendente
nombres.sort(reverse=True)
print(nombres)


nombres.reverse() # revertimos el orden de la lista
print(nombres)


# 4. Contar y Encontrar Elementos en una Lista



colores = ["pink", "brown", "yellow", "turquese", "gray"]

# Contar la cantidad de veces que aparece un elemento
cantidad_pink = colores.count("pink")
print("Cantidad de pink:",cantidad_pink)
# Encontrar el índice de un elemento
indice_gray = colores.index("gray") # para saber en que posición está 
print("Índice de gray:", indice_gray)



# Cadenas de caracteres


# Método upper() - Convertir a Mayúsculas:

texto = "susie"
en_mayusculas = texto.upper()
print(en_mayusculas) 

# Método lower() - Convertir a Minúsculas:

text = "ReNaTo"
en_min = text.lower()
print(en_min)

# Método capitalize() - Capitalizar la Primera Letra:

palabra = "propiedad"
capitalizado = palabra.capitalize()
print(capitalizado)


# Método replace() - Reemplazar Subcadena:

frase = "Susie es asombrosa"
reemplazado = frase.replace("asombrosa", "pequeña")
print(reemplazado) 


# Método split() - Dividir en Lista de Subcadenas:

parrafo = "Hallo, wie gehts?"
palabras = parrafo.split(" ")
print(palabras)  

# Método strip() - Eliminar Espacios en Blanco:

txto = "    hola   "
limpio = txto.strip()
print(limpio)  


# EJERCICIO: 


# Solicitar al usuario una frase de al menos 30 palabras
frase = input("Ingresa una frase con al menos 30 palabras: ")

# Contar cuantas palabras hay en la frase
cantidad_pal = len(frase.split())
print(cantidad_pal)

# Contar cuantos carácteres hay, incluyendo espacios en blanco hay en el texto
cantidad_caracteres = len(frase)
print(cantidad_caracteres)

# Contar los carácetres sin espacios

caracteres_sin_espacios = len(frase.replace(" ", ""))
print(caracteres_sin_espacios)

# Contar cuantas veces se repite la vocal a y la vocal e
letras_a = frase.lower().count("a")
letras_e = frase.lower().count("e")
print("Numero de letras a:",letras_a)
print("Numero de letras e:",letras_e)

