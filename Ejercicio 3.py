numeros = input("Introduce dos números separados por espacio: ").split()

num1 = int(numeros[0])
num2 = int(numeros[1])

producto = lambda a, b: a * b

resultado = producto(num1, num2)

print(f"El producto de los números {num1} y {num2} es: {resultado}")
