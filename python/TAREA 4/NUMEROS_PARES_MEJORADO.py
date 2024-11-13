#Iván Jiménez Álvarez
#10/10/2024
#Mejore la usabilidad del programa anterior haciendo que la pregunta se repita si el usuario no contesta S, s, N o n.

print("CUENTA PARES (2)")

CONT = 0 
CONTI = "S"

while CONTI == "S" or CONTI == "s":
    numero = int(input("Escriba un número par: "))

    if numero % 2 == 0:  
        print(numero, "es un número par.")
        CONT += 1
    else:
        print(numero, "no es un número válido. Inténtelo de nuevo.")

    CONTI = input("¿Quiere escribir otro número par? (S/N): ")
    while CONTI != "S" and CONTI != "s" and CONTI != "N" and CONTI != "n":
        print("Respuesta no válida. Debe contestar S o N.")
        CONTI = input("¿Quiere escribir otro número par? (S/N): ")

print("Ha escrito", CONT, "números pares.")