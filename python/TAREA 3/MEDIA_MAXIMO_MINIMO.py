#Iván Jiménez Álvarez
#10/10/2024
#Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y escriba el mayor, el menor y la media aritmética.


print("MAYOR, MENOR Y MEDIA ARIGMETICA")

NUM = eval(input("Cuantos valores va a introducir? "))
numero = []

if  NUM<0:
    print("Imposible!!!")

else:
    for n in range(NUM):
        numero1 = eval(input("Escribe el número: "))
        numero.append(numero1)

    menor = min(numero)
    mayor = max(numero)
    media = sum(numero) // NUM

print("El número más grande es:", mayor)
print("El número más pequeño es:", menor )
print("La media de los números es:", media)