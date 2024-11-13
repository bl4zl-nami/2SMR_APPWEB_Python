#Iván Jiménez Álvarez
#30/09/2024
#Este programa pide 2 numeros enteros y que calcule la division si es exacta o no
print("DIVISOR DE NÚMEROS") 
A = input("Escribe el dividendo ")
B = input("Escribe el divisor ")
A = eval(A)
B = eval(B)
if A%B == 0:
    print("la division es exacta. Cociente", A/B)
else:
    print("La division no es exacta. Cociente", round(A/B) ,"Resto", round(A%B))
