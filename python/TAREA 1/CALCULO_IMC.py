#Iván Jiménez Álvarez
#30/09/2024
#Este programa hace que con el peso y altura de una persona te da su masa corporal
print("CÁLCULO DEL ÍNDICE DE MASA CORPORAL (IMC)")
X1 = input("Cuanto pesas? ")
X2 = input("Cuanto mides? ")
X1 = eval(X1)
X2 = eval(X2)
print("Tu IMC es", round(X1 / (X2 ** 2)))