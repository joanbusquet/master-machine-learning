"""
70% helado
20% pastel
10% flan
"""

stock = input("Ingrese el postre encontrado: ")  # dato que ingresa

if stock == "helado":
    print("Recuerda comprar las cucharas desechables, por cierto, no olvides el hielo")
elif stock == "pastel":
    print("Recuerda comprar platos desechables")
elif stock == "flan":
    print("Recuerda comprar salsa de caramelo")
else:
    print("Espero que no se enfaden tus amigos")
