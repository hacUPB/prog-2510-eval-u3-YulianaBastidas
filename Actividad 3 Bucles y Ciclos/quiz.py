calificaciones = [] # ya que el código no funcionaba bien mejor decidí agregar "nota" como mi variable de entrada para después agregar las calificaciones a mi lista vacía y después ya proceder con los cálculos necesarios


while True:
    try: # arregle indentación con el try, el try y except van de la mano, no lo había agregado en el código del quiz
        nota = float(input("Ingrese sus calificaciónes:"))  
        
        if nota == -1:
            break  

        if 0.0 <= nota <= 5.0:
            calificaciones.append(nota)  
        else:
            print("Error: La calificación debe estar entre 0.0 y 5.0")

    except ValueError:
        print("Error") # hice el cambio según lo que el profe me dijo que averiguara
n = len(calificaciones)
# miro que queda mejor agregar otro if para de ahí ya evaluar el promedio
if n > 0:
    promedio = (sum(calificaciones) / n) # Le cambié porque en el quiz le puse .sum
    print(f"Promedio de calificaciones: {promedio}")
    print(f"No.de calificaciones: {n}")
else:
    print("Las notas no son válidas")
