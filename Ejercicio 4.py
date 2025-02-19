#4.- Factorial
def factorial(num):
   result=1
   while num > 0:
     result = result * num
     num = num - 1
   return result

num = int(input("Ingrese un numero: "))

while num<1:
   print("Ingrese un numero valido")
   num = int(input("Ingrese un numero: "))

print("El factorial es: " + str(factorial(num)))