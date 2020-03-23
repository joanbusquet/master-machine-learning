# calcula()  # NO FUNCIONA! Se tiene que declarar antes la función de llamarla!

# PRIMERO: Definimos función

# FUNCIONES SIN PARÁMETROS


def calcula():
    calculo = 43 * 12 * 80
    coeficiente = 45 * 3.1416

    calculo = calculo / 7
    calculo = calculo * coeficiente
    calculo = "El resultado es: " + str(calculo)
    print(calculo)


calcula()  # DESPUES: Ejecutamos función


# FUNCIONES CON PARÁMETROS
def calcula_valor(mensaje, numero1, numero2):
    resultado = numero1 + numero2
    calculo = mensaje + str(resultado)
    print(calculo)


calcula_valor("El cálculo es: ", 4, 9)


# FUNCIONES CON RETORNO
def calcula_valor2(numero1, numero2):
    resultado = numero1 + numero2
    return resultado


resultado1 = calcula_valor2(9, 858)
print(resultado1)

# FUNCIONES CON DOS RETORNOS


def calcula_valor3(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    return suma, resta


resultado_suma, resultado_resta = calcula_valor3(9, 858)
print("SUMA: " + str(resultado_suma))
print("RESTA: " + str(resultado_resta))

# FUNCIONES CON ESTRUCTURAS DE CONTROL


def calcula_valor4(numero1, numero2, comando):
    if(comando == "+"):
        resultado = numero1 + numero2
    elif(comando == "-"):
        resultado = numero1 - numero2

    return resultado


resultado2 = calcula_valor4(9, 858, "+")
print(resultado2)
