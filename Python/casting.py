num1 = input("Ingrese un número: ")
num2 = input("Ingrese otro número: ")

# Casting de variable (transformar de tipo)
num1 = int(num1)
num2 = int(num2)

print(num1 + num2)

# Int
entero = int(777)
print(type(entero))

# Flotante
flotante = float("43,44")
print(type(flotante))

# Boolean
booleano = bool("True")  # Se guarda True como string convertido a boolean

# Booleano como entero
booleano_como_entero = int(False)  # Devuelve 0

# Entero a booleano
entero_como_booleano = bool(1)  # Devuelve True
# Devuelve True (cualquiera que no sea 0 es true)
entero_como_booleano = bool(9999)
