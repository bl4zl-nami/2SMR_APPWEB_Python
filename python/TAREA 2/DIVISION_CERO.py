#Iván Jiménez Álvarez
#30/09/2024
#Este programa pide 2 numeros enteros y que calcule la division si es exacta o no, y si es cero lo dice que no se puede dividir por el
print("DIVISOR DE NÚMEROS") 
A = eval(input("Escribe el dividendo "))
B = eval(input("Escribe el divisor "))

if A and B == 0:
    print("No se puede dividir por cero crack")
elif A%B == 0:
    print("la division es exacta. Cociente", A/B)
else:
    print("La division no es exacta. Cociente", round(A/B) ,"Resto", round(A%B))
