# Ejercicio 002
'''
Haz un programa que diga el resto de la division de un numero cuando se divide.
El programa debe solicitar un numero al usuario y luego escribir 3 lineas diciendo el resto a dividir entre 2, 3 y 5
'''

nums = [2, 3, 5]
n = int(input("Ingresa un numero: "))
for i in nums:
    print(i, "/", n, " = ", i // n, "\tEl residuo es: ", i % n, sep = "")
