sabores = ["chocolate", "crema americana", "vainilla", True, 3, 20.93]
sabores2 = ['dulce de leche', 'fresa']

print(sabores)  # Imprimimos array
print(sabores[3])  # Imprimimos array posicion 3 (2 sin contar el 0)

# ELIMINAR VALOR Y GUARDAR:  Selecciona el valor de la posición 1 y la elimina (la guarda en la variable)
elemento_eliminado = sabores.pop(1)
print(elemento_eliminado)
print(sabores)

# AGREGAR VALOR AL FINAL: Agrega al final de la array
sabores.append("esto es el ultimo")
print(sabores)

# INSERTAR NUEVO ELEMENTO EN LA POSICION X (Params: POSICION, OBJETO)
sabores.insert(1, "objeto insertado")
print(sabores)

# SE FUSIONA NUEVO ARRAY DENTRO DE ARRAY
sabores.extend(sabores2)
print(sabores2)

# ELIMINAR VALOR SIN GUARDAR POR VALOR (OJO: Solo la primera vez que lo encuentra)
sabores.remove("vainilla")
print(sabores)
