#Iván Jiménez Álvarez
#10/10/2024
#Este programa ecribe un programa que pide dos números enteros y escriba la suma de todos los enteros desde el primer número hasta el segundo

num1 = int(input("Introduce el primer número entero: "))
num2 = int(input("Introduce el segundo número entero: "))

if num1 < 0 or num2 < 0:
    print("No se permiten números negativos.")
elif num1 == num2:
    print("Los números no pueden ser iguales.")
else:
    suma = sum(range(num1, num2 + 1))
    print("La suma de todos los enteros desde", num1, "hasta", num2, "es:", suma)