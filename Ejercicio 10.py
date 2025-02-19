#10.- maximo comun divisor

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a=int(input("Ingrese el primer numero: "))
b= int(input("Ingrese el segundo numero: "))

print("El máximo comun divisor es: "+ str(mcd(a,b)))