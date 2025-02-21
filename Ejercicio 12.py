def calcular_moda(lista_numeros):
    frecuencia = {}
    max_frecuencia = 0
    modas = []

    for numero in lista_numeros:
        if numero in frecuencia:
            frecuencia[numero] += 1
        else:
            frecuencia[numero] = 1

        if frecuencia[numero] > max_frecuencia:
            max_frecuencia = frecuencia[numero]
            modas = [numero]
        elif frecuencia[numero] == max_frecuencia:
            modas.append(numero)

    return modas

# Pedir al usuario que ingrese los números
numeros_usuario = input("Ingresa una lista de números separados por comas: ")
lista = [int(numero) for numero in numeros_usuario.split(',')]

moda = calcular_moda(lista)
print(f"La(s) moda(s) es/son: {moda}")
