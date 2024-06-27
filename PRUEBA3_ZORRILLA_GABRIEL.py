import os
os.system("cls")
vehiculos=[]
#funcion para grabar vehiculo
def grabar_vehiculo():
    tipo = input("Ingrese el tipo de vehículo (Automovil, Camión, Camioneta o Moto): \n")
    patente = input("Ingrese la patente del vehículo EJ(ABCD12):\n ")
    if patente=="M"or patente=="N"or patente=="Ñ":
        patente = input("Patente invalida. Ingrese nuevamente (4 consonantes sin M, N, Ñ): ")
    marca = input("Ingrese la marca del vehículo: \n")
    if len(marca)>2 and len(marca)<16:
        print("guardado correctamente")
    else:
        marca=input("ingrese una marca correcta")
        
    precio = float(input("Ingrese el precio del vehículo: \n"))
    if precio >= 5000000:
        print("Error: El precio del vehículo debe ser mayor a $5,000,000.")
        return
    fecha_registro = input("Ingrese la fecha cuando se registro el vehículo (DD/MM/AAAA): \n")
    rut_dueño = input("Ingrese el RUT del dueño: \n")
    nombre_dueño = input("Ingrese el nombre del dueño:\n ")
    tiene_multa = input("¿Tiene multa? (SI/NO): ").lower()
    
    monto_multa = None

    fecha_multa = None
    
    if tiene_multa == "si":
        monto_multa = float(input("Ingrese el monto de la multa: "))
        fecha_multa = input("Ingrese la fecha de la multa (DD/MM/AA): ")
    elif tiene_multa=="no":
        print("bien hecho,puedes seguir")
    
    vehiculo={
         "tipo": tipo,
        "patente": patente,
        "marca": marca,
        "precio": precio,
        "fecha_registro": fecha_registro,
        "rut_dueño": rut_dueño,
        "nombre_dueño": nombre_dueño,
        "tiene_multa":tiene_multa,
        "monto_multa":monto_multa,
        "fecha_multa":fecha_multa,
    }
    vehiculos.append(vehiculo)
    print("vehiculo registrado correctamente")

#funcion para buscar vehiculo
def buscar_vehiculo():
    patente_buscar = input("Ingrese la patente del vehículo que busca: \n").upper()
    encontrado = False

    for vehiculo in vehiculos:
        if vehiculo["patente"] == patente_buscar:
            print("Información del vehículo:\n")
            print(f"Tipo: {vehiculo['tipo']}")
            print(f"Patente: {vehiculo['patente']}")
            print(f"Marca: {vehiculo['marca']}")
            print(f"Precio: {vehiculo['precio']}")
            print(f"Fecha de Registro: {vehiculo['fecha_registro']}")
            print(f"RUN del dueño: {vehiculo['rut_dueño']}")
            print(f"Nombre del dueño: {vehiculo['nombre_dueño']}")
            print(f"Multa: {vehiculo['tiene_multa']}")
            print(f"Monto multa: {vehiculo['monto_multa']}")
            print(f"Fecha de la multa:{vehiculo['fecha_multa']}")
            encontrado = True
            break

    if not encontrado:
        print("Vehículo no encontrado")
#menu principal

while True:
    print("Bienvenido a autos seguro")
    print("Menu de opciones\n")
    print("1)Grabar")
    print("2)Buscar auto")
    print("3)Imprmir certificados ")
    print("4)salir")
    
    try:
        op=int(input("Ingrese una opcion: \n"))
    except:
        op=0
    if op==1:
        grabar_vehiculo()
    if op==2:
        buscar_vehiculo()
    if op==3:
        buscar_patente=input("ingrese la patente del vehiculo que busca:\n")
        for vehiculo in vehiculos:
            if vehiculo["patente"] == buscar_patente:
                print(f"Patente: {vehiculo['patente']}")
                print("1)Emision de contaminante: muy alto")
                print("2)Amotaciones pendientes: muchas")
                print(f"3)Multa: {vehiculo['tiene_multa']}")
                print(f"4)Monto multa: {vehiculo['monto_multa']}")
        
    if op==4:
        print("saliendo del programa")
        break
    else:
        print("***")
    