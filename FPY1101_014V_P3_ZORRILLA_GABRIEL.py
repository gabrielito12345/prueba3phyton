import random
import os
os.system("cls")

class Vehiculo:
    def __init__(self, tipo, patente, marca, precio, muchas, fecha_registro, run_dueno, nombre_dueno):
        self.tipo = tipo
        self.patente = patente
        self.marca = marca
        self.precio = precio
        self.muchas = muchas
        self.fecha_registro = fecha_registro
        self.run_dueno = run_dueno
        self.nombre_dueno = nombre_dueno

    def __str__(self):
        return f"Tipo: {self.tipo}\nPatente: {self.patente}\nMarca: {self.marca}\nPrecio: {self.precio}\nMultas: {self.muchas}\nFecha de Registro: {self.fecha_registro}\nDueño: {self.nombre_dueno} (RUT: {self.run_dueno})\n"

class Programa:
    def __init__(self):
        self.vehiculos = []
#menu de opciones
    def menu(self):
        while True:
            print("Menú ")
            print("1) Grabar vehículo:\n")
            print("2) Buscar vehículo por patente:\n")
            print("3) Imprimir certificados\n")
            print("4) Salir del programa\n")
            try:
                opcion = input("Ingrese una opción (1-4):\n ")
            except:
                opcion = 0
            if opcion == "1":
                self.grabar_vehiculo()
            elif opcion == "2":
                self.buscar_vehiculo()
            elif opcion == "3":
                self.imprimir_certificados()
            elif opcion == "4":
                print("BYE ")
                break
            else:
                print("Opción no valida. Ingrese una opcion valida.")
# grabar informacion
    def grabar_vehiculo(self):
        tipo = input("Ingrese el tipo de vehículo (Automovil, Camión, Camioneta, Moto): \n")
        patente = input("Ingrese la patente del vehículo, excepto(M,N,Ñ): (ej:ABCD12)  \n")
        marca = input("Ingrese la marca del vehículo: \n")
        precio = float(input("Ingrese el precio del vehículo debe ser mayor a $5.000.000: \n"))
        muchas = int(input("Ingrese la cantidad de multas del vehículo: \n"))
        fecha_registro = input("Ingrese la fecha de registro del vehículo:(DD\MM\AA)\n ")
        run_dueno = input("Ingrese el RUT del dueño sin putnos ni guion: \n")
        nombre_dueno = input("Ingrese el nombre del dueño: \n")

        # Validando condiciones
        if self.validar_patente(patente) and len(marca) >= 2 and len(marca) <= 25 and precio > 5000000:
            vehiculo = Vehiculo(tipo, patente, marca, precio, muchas, fecha_registro, run_dueno, nombre_dueno)
            self.vehiculos.append(vehiculo)
            print("Vehículo guardado correctamente.")
        else:
            print("Error: Verifique la patente antes de grabar el vehículo.")

    def validar_patente(self, patente):
        # Verificando patente 
        if len(patente) == 6:
            letras = patente[:4]
            numeros = patente[4:]
            if letras.isalpha() and numeros.isdigit():
                # restricciones de letras
                if letras[2] not in ['M', 'N', 'R']:
                    return True
        return False

    def buscar_vehiculo(self):
        patente_buscar = input("Ingrese la patente del vehículo a buscar: \n")
        encontrado = False
        for vehiculo in self.vehiculos:
            if vehiculo.patente == patente_buscar:
                print(" Información del Vehículo ")
                print(vehiculo)
                encontrado = True
                break
        if not encontrado:
            print("Vehículo no encontrado.")

    def imprimir_certificados(self):
        for vehiculo in self.vehiculos:
            # valores aleatorios para certificados
            emision_contaminantes = random.randint(1500, 3500)
            amotaciones_vigentes = random.randint(1500, 3500)
            multas = random.randint(1500, 3500)

            print(f" Certificados para Vehículo {vehiculo.patente} ")
            print(f"1. Emisión de contaminantes: {emision_contaminantes}")
            print(f"2. ANotaciones vigentes: {amotaciones_vigentes}")
            print(f"3. Multas: {multas}")
            print(f"Nombre del dueño: {vehiculo.nombre_dueno}")
            print(f"RUT del dueño: {vehiculo.run_dueno}")
            print()

if __name__ == "__main__":
    programa = Programa()
    programa.menu()
