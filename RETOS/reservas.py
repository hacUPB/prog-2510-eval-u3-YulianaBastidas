import random

def obtener_informacion_usuario():
    titulo = input("Ingrese su título (Sr. o Sra.): ").strip()
    nombre = input("Ingrese su nombre: ").strip()
    apellido = input("Ingrese su apellido: ").strip()
    print(f"{titulo} {nombre} {apellido}, ¡Bienvenido a FastFast Airlines!\n")
    return titulo, nombre, apellido

def seleccionar_vuelo():
    # Ciudades disponibles
    ciudades_disponibles = ["Medellín", "Bogotá", "Cartagena"]
    
    # Matriz de distancias entre ciudades 
    distancias = {
        ("Medellín", "Bogotá"): 240,
        ("Medellín", "Cartagena"): 461,
        ("Bogotá", "Cartagena"): 657
    }

    print("Ciudades disponibles: Medellín, Bogotá, Cartagena")

    # Validar ciudad de origen
    while True:
        origen = input("Ingrese la ciudad de origen: ").strip().capitalize()
        if origen in ciudades_disponibles:
            break
        print("Error: Ciudad no válida. Intente nuevamente.")

    # Validar ciudad de destino
    while True:
        destino = input("Ingrese la ciudad de destino: ").strip().capitalize()
        if destino in ciudades_disponibles and destino != origen:
            break
        print("Error: Ciudad no válida o es la misma que el origen. Intente nuevamente.")

    # Buscar la distancia en ambas direcciones
    distancia = distancias.get((origen, destino)) or distancias.get((destino, origen))

    # Validar día de la semana
    dias_validos = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    while True:
        dia_semana = input("Ingrese el día de la semana en que desea viajar: ").strip().lower()
        if dia_semana in dias_validos:
            break
        print("Error: Día no válido. Intente nuevamente.")

    # Validar día del mes
    while True:
        try:
            dia_mes = int(input("Ingrese el día del mes (1-30): "))
            if 1 <= dia_mes <= 30:
                break
            else:
                print("Error: El día del mes debe estar entre 1 y 30.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")

    # Calcular precio según distancia y día de la semana
    if distancia < 400:
        precio = 79900 if dia_semana in ["lunes", "martes", "miércoles", "jueves"] else 119900
    else:
        precio = 156900 if dia_semana in ["lunes", "martes", "miércoles", "jueves"] else 213000

    return origen, destino, dia_semana, dia_mes, precio

def asignar_asiento():
    while True:
        preferencia = input("Prefiere asiento en el pasillo, junto a la ventana o sin preferencia? ").strip().lower()
        if preferencia in ["pasillo", "ventana", "sin preferencia"]:
            break
        print("Error: Opción no válida. Debe elegir 'pasillo', 'ventana' o 'sin preferencia'.")

    if preferencia == "pasillo":
        letra_asiento = "C"
    elif preferencia == "ventana":
        letra_asiento = "A"
    else:
        letra_asiento = "B"

    numero_asiento = random.randint(1, 29)
    asiento = f"{numero_asiento}{letra_asiento}"
    return asiento

def main():
    titulo, nombre, apellido = obtener_informacion_usuario()
    origen, destino, dia_semana, dia_mes, precio = seleccionar_vuelo()
    asiento = asignar_asiento()

    print("Reserva confirmada:")
    print(f"Pasajero: {titulo} {nombre} {apellido}")
    print(f"Origen: {origen}")
    print(f"Destino: {destino}")
    print(f"Fecha: {dia_semana.capitalize()} {dia_mes}")
    print(f"Precio: ${precio:,}")
    print(f"Asiento: {asiento}")

if __name__ == "__main__":
    main()


# videos que ayudaron:
# https://youtu.be/_C7Uj7O5o_Q?si=lPGuBer6E566swiE
# https://youtu.be/rnUkxgJK4Qg?si=TJ0jsbfq4dMJqQbI

