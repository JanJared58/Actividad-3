import random

def juego_adivinanza():
    numero_objetivo = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido al juego de adivinanza!")
    print("Estoy pensando en un número entre 1 y 100. ¡Intenta adivinarlo!")

    while True:
        intento = int(input("Introduce tu adivinanza: "))
        intentos += 1

        if intento < numero_objetivo:
            print("El número es mayor. Intenta de nuevo.")
        elif intento > numero_objetivo:
            print("El número es menor. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

juego_adivinanza()
