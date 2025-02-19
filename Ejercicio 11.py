#11.- Determinante 3x3

def obtener_matriz_3x3():
    matriz = []
    for i in range(3):
        fila = []
        for j in range(3):
            valor = float(input(f"Ingresa el valor para la posición ({i+1},{j+1}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def determinante_matriz_3x3(matriz):
    det = (matriz[0][0] * (matriz[1][1] * matriz[2][2] - matriz[1][2] * matriz[2][1])) - \
          (matriz[0][1] * (matriz[1][0] * matriz[2][2] - matriz[1][2] * matriz[2][0])) + \
          (matriz[0][2] * (matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0]))

    return det

matriz_usuario = obtener_matriz_3x3()

det = determinante_matriz_3x3(matriz_usuario)

print(f"El determinante de la matriz es: {det}")