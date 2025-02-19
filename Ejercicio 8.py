#8.- Palindromo 
def palindromo (texto):

    texto = texto.replace(" ", "").lower()
    if texto==texto[::-1]:
        return print("Es un palindromo")
    else: 
        return print("No es un palindromo")

texto= input("Ingrese el texto: ")
palindromo(texto)