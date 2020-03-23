# ARRAY DE DICCIONARIOS PACIENTES
paciente1 = {"nombre": "Manolo", "edad": 42, "peso": 70.5,
             "fuma": False, "clinic": "Lorem ipsum"}
paciente2 = {"nombre": "Eugenio", "edad": 23, "peso": 70.5,
             "fuma": False, "clinic": "Lorem ipsum"}
paciente3 = {"nombre": "Juan", "edad": 32, "peso": 70.5,
             "fuma": False, "clinic": "Lorem ipsum"}

pacientes = [paciente1, paciente2, paciente3]
print(pacientes)


# RECORRER LISTA (Bucle for)
for x in range(len(pacientes)):  # len --> devuelve total elementos lista
    print("")
    print("------------------------------")
    print("--- DICCIONARIO NUMERO ", x+1, " ---")
    print("CLAVE\t\tVALOR\t\t<33\t\t\n")

    # RECORRER DICCIONARIO (Bucle for)
    # 2 variables: k --> clave | v --> value
    for k, v in pacientes[x].items():
        print(k, "\t\t", v)
        if(k == "edad" and v < 33):
            menor = "✔️"
        else:
            menor = ""
        print(k, "\t\t", v, "\t\t", menor)
