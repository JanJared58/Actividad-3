
def mostrar_mensaje(nombre, edad=18):
    print(f"Hola {nombre}, tienes {edad} años.")

nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad (o deja en blanco para asumir 18): ")

edad = int(edad) if edad else 18

mostrar_mensaje(nombre, edad)
