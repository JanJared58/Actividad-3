#7.- calcular mediana

def mediana(lista):
    lista.sort()
    n=len(lista)
    if n%2!=0:
        return lista[n//2]
    else:
        return (lista[n // 2 - 1] + lista[n // 2]) / 2
 
lista=[]
op='s'

while op=='s':
    num=int(input("Ingrese el numero: "))
    lista.append(num)
    op=input("¿Desea a agregar otro numero a la lista?(s/n): ")

print(f"La mediana de la lista es: {mediana(lista)}") 
