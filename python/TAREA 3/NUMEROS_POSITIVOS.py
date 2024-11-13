#Iván Jiménez Álvarez
#10/10/2024
#Este programa te pide que escribas la cantidad de números positivos que se tienen que escribir y a continuación pida números hasta que se haya escrito la cantidad de números positivos indicada

print("NÚMEROS POSITIVOS")
def solicitar_numeros_positivos():
    cantidad = int(input("Escriba la cantidad de números a escribir: "))
    
    while cantidad <= 0:
        print("La cantidad debe ser mayor que 0. Inténtelo de nuevo.")
        cantidad = int(input("Escriba la cantidad de números a escribir: "))
    
    CONTP = 0
    CONTT = 0

    while CONTT < cantidad:
        numero = int(input("Escriba un número: "))
        CONTT += 1
        
        if numero > 0:
            CONTP += 1

    print("Ha escrito " + str(CONTT) + " números, de los cuales " + str(CONTP) + " son positivos.")

solicitar_numeros_positivos()