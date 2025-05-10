def SimulacionSatelite(altitudInicial, coefArrastre, altitudMinSeguridad):
  #Define las variables iniciales
  altitud_actual = altitudInicial
  coeficiente_arrastre = coefArrastre
  orbita = 0
  #Simula la perdida de altitud siempre y cuando la altitud actual sea mayor a la altitud minima de seguridad
  while altitud_actual > altitudMinSeguridad:
    #Incrementa la orbita
    orbita = orbita + 1
    #Calcula altitud Perdida
    altitudPerdida = coeficiente_arrastre * altitud_actual
    #Actualiza la altitud actual
    altitud_actual = altitud_actual - altitudPerdida
    #Incrementa el coeficiente de arrastre
    coeficiente_arrastre += 0.0001

    print("Órbita", orbita, "Altitud actual =", altitud_actual, "km,", "Coeficiente de arrastre =", coeficiente_arrastre)

    #Si la altitud perdida es muy muy muy pequeña, decimos que esta en una orbita estable.
    #El valor es arbitrario
    if(altitudPerdida < 0.01):
      print("Órbita estable en", orbita, "con altitud de :", altitud_actual)
      return

  print("El satélite ha reingresado en la atmósfera terrestre después de",orbita," órbitas.")

# Solicita al usuario los datos necesarios
altitud_inicial = float(input("Ingrese la altitud inicial del satélite (en kilómetros): "))
coeficiente_arrastre = float(input("Introduzca el coeficiente de arrastre inicial: "))
altitud_minima_segura = float(input("Ingrese la altitud mínima segura (en kilómetros): "))

print("Simulando la desintegración orbital...")
SimulacionSatelite(altitud_inicial, coeficiente_arrastre, altitud_minima_segura)

# Pausa para evitar que la consola se cierre
input("\nPresiona Enter para salir.")


# video en youtube: https://youtu.be/NyTYiXNEmX8
