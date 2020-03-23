# máximo de participantes
participantes_max = int(input("Cuantos participantes? \n"))
print("El sistema ha sido configurado para aceptar", participantes_max,
      "participantes a partir de ahora el ordenador queda preparado para recibirlos\n")

# hacemos un bucle que nos pida los datos de todos los participantes
for x in range(participantes_max):
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
        print("SU NUMERO DE PARTICIPANTE ES "+str(x+1)+"\n\n\n")
    # si la respuesta es no, cancelamos
    else:
        print("*******************")
        print("Operación cancelada")
        print("*******************\n")

print("Cantidad máxima alcanzada")
