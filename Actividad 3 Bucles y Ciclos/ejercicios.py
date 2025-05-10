# Creamos una lista mutable
lista1 = [1, 2, 3]

# Asignamos la lista a otra variable
lista2 = lista1

# Modificamos la lista2
lista2.append(4)

# Imprimimos ambas listas
print("Lista 1:", lista1)
print("Lista 2:", lista2)

lista3 = [434, "Susie", 1088]
print(lista3)
lista3.append(4756)


# Creamos una cadena de caracteres
cadena1 = "Hola"

# Asignamos la cadena a otra variable
cadena2 = cadena1

# Intentamos modificar la cadena2 (esto generará un error)
try:
    cadena2 += " Mundo"
except TypeError as e:
    print(f"Error: {e}")

# Imprimimos ambas cadenas
print("Cadena 1:", cadena1)
print("Cadena 2:", cadena2)


# lista con top 5 de canciones favoritas

canciones_fav = ["Superman", "Cinnamon Girl", "Everybody Wants To Rule The World", "Unholy", "Back To Black"]
cantantes_cfav = ["Eminem", "Lana Del Rey", "Tears For Fears", "Sam Smith", "Amy Winehouse"]

indice = 0
while indice < 5:
    print(f"{canciones_fav[indice]} la interpreta {cantantes_cfav[indice]}")
    indice += 1
# Con este código inicializamos en 0 y vamos hasta 5, ya que tanto canciones como cantantes fav solo tenemos 4