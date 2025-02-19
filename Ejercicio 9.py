#9.- Segundo mayor
def segundo_mayor(lista):
    n=len(lista)
    lista.sort()
    segundo=lista[n-2]
    return segundo

lista=[]
op='s'

while op=='s':
    num=int(input("Ingrese el numero: "))
    lista.append(num)
    op=input("¿Desea a agregar otro numero a la lista?(s/n): ")

num=segundo_mayor(lista)
print(f"El segundo numero mayor de la lista es: {num}")