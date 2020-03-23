paciente = {"nombre": "Juan", "edad": 32, "peso": 70.5,
            "fuma": False, "clinica": "Lorem ipsum dolor sit amet"}
print(paciente["nombre"])

# OBTENER VALOR:
paciente.get("edad")
print(paciente)

# ELIMINAR VALOR Y GUARDAR:  Selecciona el valor de la posición 1 y la elimina (la guarda en la variable)
valor = paciente.pop("edad")
print(paciente)

# ACTUALIZAR VALOR: Método1: Le pasamos el nuevo valor (lo pone al final)
paciente.update({"edad": 18})
print(paciente)

# ACTUALIZAR VALOR: Método 2: Le pasamos el nuevo valor (lo pone al final)
paciente["edad"] = 18
print(paciente)

# BUSCAR DENTRO DE DICCIONARIO: Está peso dentro de paciente? True or False
print("peso" in paciente)


# ARRAY DE DICCIONARIOS PACIENTES
paciente1 = {"nombre": "Manolo", "edad": 42, "peso": 70.5,
             "fuma": False, "clinica": "Lorem ipsum dolor sit amet"}
paciente2 = {"nombre": "Eugenio", "edad": 23, "peso": 70.5,
             "fuma": False, "clinica": "Lorem ipsum dolor sit amet"}
paciente3 = {"nombre": "Juan", "edad": 32, "peso": 70.5,
             "fuma": False, "clinica": "Lorem ipsum dolor sit amet"}

pacientes = [paciente1, paciente2, paciente3]
print(pacientes)

# CREAMOS LISTA
demo = ["uno", "dos", "tres"]

# RECORRER LISTA (Bucle for)
for x in range(len(demo)):  # len --> devuelve total elementos lista
    print(demo[x])


# RECORRER DICCIONARIO (Bucle for)
# 2 variables: k --> clave | v --> value
for k, v in paciente1.items():
    print("Clave: ", k, " | Valor: ", v)
    print("********************************\n")
    if(k == "edad" and v < 33):
        print("Encontramos un paciente menor de 33")
