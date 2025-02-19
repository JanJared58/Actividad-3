#6.- Invertir una cadena 

def invertido(texto):

    invert= texto[::-1]

    return invert

texto= input("Ingrese el texto: ")
print(f"El texto invertido es: {invertido(texto)}") 
