import os  # importamos librería de sistema de python para poder limpiar pantalla con comando "CLEAN"

print("*********************************************************")
print("Bienvenidos al sistema de historias clinicas del Hospital")
print("*********************************************************\n")

# VARIABLES GLOBALES
running = True
database = list()  # creamos lista vacía

# FUNCIONES


def show_menu():
    print("\t\t⚪  1- Cargar paciente")
    print("\t\t⚪  2- Buscar paciente")
    print("\t\t⚪  3- Listar pacientes")
    print("\t\t⚪  4- Salir")
    print("")
    response = input("INGRESE UNA OPCIÓN > ")

    # limpiamos la pantalla cada vez que seleccionamos una opción
    os.system('clear')

    return response


def response_validate(r):
    validated = False
    num_res = 0

    if r.isdigit():  # comprobar si el texto es un numero
        num_res = int(r)  # convertimos el dígito texto a numero
        if num_res > 0 and num_res <= 5:  # comprobamos si el dígito está dentro del rango admitido
            validated = True
            msg = "Está en rango"
        else:
            msg = "Está fuera de rango"
    else:
        msg = "Entrada incorrecta"
    return validated, num_res, msg


    # MAIN LOOP
while running:
    # mostramos menu
    response = show_menu()

    # llamamos a la funcion para validar el digito introducido
    validated, num_res, msg = response_validate(response)
    if validated:
        if num_res == 1:  # cargar paciente nuevo
            name = input("Ingrese el nombre del paciente: ")
            history = input("Ingrese la historia clinica del paciente: ")

            # guardamos los datos del paciente introducido
            paciente = {"nombre": name, "historia": history}

            # insertamos al final de la lista database
            database.append(paciente)
        elif num_res == 2:
            name = input("Ingrese el nombre del paciente: ")

            finded = True
            # recorremos la lista database (donde se almacenan los pacientes)
            for x in range(len(database)):

                # Si el key es nombre y el valor (lo pasamos a minusculas para mejorar la busqueda) es el mismo que el nombre introducido para buscar
                if database[x]["nombre"].lower() == name.lower():
                    # encontrado ok y mostramos la historia clinica de este
                    print("\nPaciente encontrado! | H. CLINICA: ",
                          database[x]["historia"], "\n")
                else:  # no encontrado!
                    finded = False
            if not finded:
                print("Paciente no encontrado")

        elif num_res == 3:
            print("\n****************************")
            print("*** LISTADO DE PACIENTES ***")
            print("****************************\n")
            for x in range(len(database)):
                print("Nombre: ".ljust(10), database[x]["nombre"],  # rjust = tamaño detereminado de la columna
                      "\t Historial Cli: ".ljust(10), database[x]["historia"])
                print("\n")

        else:
            # cortamos la ejecución del programa (del bucle While)
            running = False
    else:
        print("")
        print("ERROR!: ", msg)
        print("")

print("")
print("Aplicación finalizada")
print("")
