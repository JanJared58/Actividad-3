#5.- calcular promedio
def promedio(lista):
    suma=0
    for n in range(0,len(lista)):
        suma= suma+ lista[n]

    promedio=suma/len(lista)

    return promedio
lista=[]
op='s'

while op=='s':
    num=int(input("Ingrese el numero: "))
    lista.append(num)
    op=input("¿Desea a agregar otro numero a la lista?(s/n): ")
res= promedio(lista)
print("Su promedio es de: "+ str(res))