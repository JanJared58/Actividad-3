def evaluar_polinomio(coeficientes, x):
    resultado = 0
    n = len(coeficientes) - 1

    for coef in coeficientes:
        resultado += coef * (x ** n)
        n -= 1

    return resultado


coeficientes = [2, -6, 2, -1] 
x = 3
valor_polinomio = evaluar_polinomio(coeficientes, x)
print(f"El valor del polinomio en x = {x} es: {valor_polinomio}")

