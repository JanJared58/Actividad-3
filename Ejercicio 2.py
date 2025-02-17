def sumar(*args):
    return sum(args)

numeros = input("Introduce los números separados por espacios: ")

numeros_lista = []
for numero in numeros.split():
    numeros_lista.append(int(numero))


resultado = sumar(*numeros_lista)

print(f"La suma de los números es: {resultado}")
