#Iván Jiménez Álvarez
#10/10/2024
#Escriba un programa que pida números pares mientras el usuario indique que quiere seguir introduciendo números. Para indicar que quiere seguir escribiendo números, el usuario deberá contestar S o s a la pregunta.


print("CUENTA PARES (1)")

CONT = 0 
continuar = "S"

while continuar == "S" or continuar == "s":
    numero = int(input("Escriba un número par: "))

    if numero % 2 == 0:  
        numero = int(numero)
        if numero % 2 == 0:
            print(numero, "es un número par.")
            CONT += 1
        else:
            print(numero, "no es un número par. Inténtelo de nuevo.") 
    else:
        print(numero, "no es un número válido. Inténtelo de nuevo.")

    continuar = input("¿Quiere escribir otro número par? (S/N): ")

print("Ha escrito", CONT, "números pares.")