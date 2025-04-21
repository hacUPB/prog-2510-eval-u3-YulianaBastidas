def suma(a, b):
	resultado = a + b
	return resultado


#Llamando a la función
numero1 = 46458
numero2 = 14909
resultado_suma = suma(numero1, numero2)
print(f"{numero1} + {numero2} = {resultado_suma}")


lista = [6, 8, 6, 6, 7]
print(lista)
lista.sort() # sort es un método de las listas, asociado al objeto
print(lista)

resultado = sum(lista)
print(resultado)



def mcd(num, den):
	if num <= den:
		menor = num
	else:
		menor = den
	for divisor in range(menor, 0, -1):
		if num % divisor == 0 and den % divisor == 0:
			max_com_div = divisor
			break
	return max_com_div

def imprime_fraccion(num, den, maximo):
	pass

# función principal
def main():
	numerador = int(input("Ingrese el numerador:"))
	denominador = int(input("Ingrese el denominador:"))
	maximo = mcd(numerador, denominador)
	print(f"M.C.D = {maximo}")
	
# Punto de entrada del programa
if __name__ == "__main__":
	main()
	