"""
# mientras contador sea menor a 100
contador = 0
while contador < 100:
    print("La cuenta es: ", contador)
    # incrementamos 10
    contador += 10

# mientras respuesta sea distinto a detener, volver a preguntar
respuesta = ""
while respuesta != "detener":
    respuesta = input("Ingrese un texto")
"""


# máximo de participantes
participantes_max = int(input("Cuantos participantes? \n"))
print("El sistema ha sido configurado para aceptar", participantes_max,
      "participantes a partir de ahora el ordenador queda preparado para recibirlos\n")

cantidad_participantes = 0
# mientras que la cantidad de participantes sea menor a los maximos
while cantidad_participantes < participantes_max:
    # pedir datos del participante
    nombre = input("Ingrese su nombre: \n")
    email = input("Ingrese su email: \n")
    print("Hola ", nombre, "su email es ", email,
          " desea confirmar la inscripción?\n")
    print("Para confirmar \"SI\", o escriba 'NO' para rechazar")
    respuesta = input()
    print("")

    # convertimos respuesta a minuscula
    respuesta = respuesta.lower()

    # si respuesta es que si, inscribimos
    if respuesta == "si":
        print("***************************************")
        print("* Gracias, confirmamos su inscripción *")
        print("***************************************\n\n\n")
        print("SU NUMERO DE PARTICIPANTE ES " +
              str(cantidad_participantes)+"\n\n\n")

        # sumamos participante en la variable para la siguiente iteración del while
        cantidad_participantes += 1

    # si la respuesta es no, cancelamos
    else:
        print("*******************")
        print("Operación cancelada")
        print("*******************\n")

print("Cantidad máxima alcanzada")
