import datetime

pacientes = []
registros = {}

def registrar_paciente():
    print("\n--- Menú Registro de Paciente ---")
    try:
        run = int(input("Ingrese el Run: "))
    except:
        print("El run ingresado está sin de formato válido (numero entre 3999999 a 22000000)\n\n")
        return
    if run < 3999999 or run > 22000000:
        print("El run ingresado está sin de formato válido (numero entre 3999999 a 22000000)\n\n")
        return

    nombre = input("Ingrese el Nombre: ")
    apellidos = input("Ingrese los Apellidos: ")
    direccion = input("Ingrese la Dirección: ")
    correo = input("Ingrese el Correo: ")
    if "@" not in correo:
        print("El correo ingresado está sin de formato válido")
        return
    temp = False
    while(temp):
        if edad < 1 or edad > 90:
            print("La edad ingresada está fuera dde rango")
        else: return
    edad = int(input("Ingrese la Edad: "))
    

    genero = input("Ingrese el Género (M/F/Otro): ").upper()
    if genero not in ['M', 'F', 'OTRO']:
        print("Ingrese el género en el formato solicitado ('M', 'F' o 'Otro').")
        return

    estado_salud = input("Escriba el seguro de salud ('Particular', 'Isapre' o 'Fonasa'): ").capitalize()
    if estado_salud not in ['Particular', 'Isapre', 'Fonasa']:
        print("El seguro de Salud debe ser 'Particular', 'Isapre' o 'Fonasa'.")
        return

    paciente = {
        "Run": run,
        "Nombre": nombre,
        "Apellidos": apellidos,
        "Dirección": direccion,
        "Correo": correo,
        "Edad": edad,
        "Género": genero,
        "Estado de Salud": estado_salud
    }

    pacientes.append(paciente)
    registros[run] = []
    print("Paciente registrado con éxito.")


def atencion_paciente():
    print("\n--- Menú Atención de Paciente ---")
    run = int(input("Ingrese el Run del paciente: "))
    
    if run not in registros:
        print("Paciente no encontrado en el sistema.")
        return

    fecha = input("Ingrese la fecha de la visita (Formato Fecha dia-mes-año): ")
    observaciones = input("Ingrese observaciones de la visita: ")
    registro = f"Fecha: {fecha}, Observaciones: {observaciones}"
    registros[run].append(registro)
    print("Atención registrada con éxito.")


def consultar_paciente():
    print("\n--- Menú Consulta de Paciente ---")
    run = int(input("Ingrese el Run del paciente a consultar: "))
    if run in registros:
        paciente = [p for p in pacientes if p['Run'] == run][0]
        print("Datos del Paciente:")
        print(f" ° Run: {paciente['Run']}")
        print(f" ° Nombre: {paciente['Nombre']} {paciente['Apellidos']}")
        print(f" ° Dirección: {paciente['Dirección']}")
        print(f" ° Correo: {paciente['Correo']}")
        print(f" ° Edad: {paciente['Edad']} años")
        print(f" ° Género: {paciente['Género']}")
        print(f" ° Estado de Salud: {paciente['Estado de Salud']}")
        
        # Muestra los registros de atención
        print("\nRegistros de Atención:")
        if registros[run]:
            for i, registro in enumerate(registros[run], start=1):
                print(f" ° Registro {i}:")
                print("    - ",registro)
        else:
            print(" ° Sin atenciones registradas en el sistema.")
    else:
        print("Paciente no encontrado en el sistema.\n")


def main():
    while True:
        print("\n----------------------------------------\n")
        print("Menú:")
        print("1. Registrar Paciente")
        print("2. Atención Paciente")
        print("3. Consultar Paciente")
        print("4. Salir")
        opcion = input("Elija una opción: ")

        if opcion == '1':
            registrar_paciente()
        elif opcion == '2':
            atencion_paciente()
        elif opcion == '3':
            consultar_paciente()
        elif opcion == '4':           
            fecha = datetime.datetime.now()

            # Imprime la fecha actual en un formato legible
            print(fecha)
            print("\nintegrantes:")
            print(" ° Gabriel Silva")
            print(" ° Adriel Barrientos")
            print("Asignatura: Lenguajes de programación")



            resp = input("\nRealmente desea salir? ('Si' para salir): ").capitalize()
            if resp == "Si":          
                print("Gracias por usar el sistema.")
                break
            else:
                print("Voliendo al menú proncipal")
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
