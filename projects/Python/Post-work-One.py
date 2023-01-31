'''
Ejercicio 7.1
 Una familia, formada por 4 hijos y el matrimonio, va al cine.
 Si cada entrada vale $80 pesos,
 ¿Cuantó tienen que pagar?,
 si para pagar las entradas la madre entrega un billete de $500,
 ¿cuanto tendrán que devolverle?  
'''
costoEntrada = 80
nPersonas = 4 + 2 #Hijos + matrimonio
# ¿Cuantó tienen que pagar?
total = costoEntrada * nPersonas
print("Respuesta 1.1:", total)

# ¿Cuanto tendrán que devolverle?  
print("Respuesta 1.2:", 500 - total)

'''
Ejercicio 7.2
Un padre murió dejando cuatro hijos. Estos se repartieron sus bienes de la
manera siguiente:
El primero agarró la mitad de la fortuna, menos 3000 pesos.
El segundo agarró un tercio de ella, menos 1000 pesos.
El tercero agarró exactamente un cuarto de los bienes.
El cuarto cogió 600 pesos, más la quinta parte de los bienes.
¿Cuál era la fortuna total, y qué cantidad recibió cada uno de los hijos?  
'''

# f = (f/2 - 3000) + (f/3 - 1000) + (f/4) + (f/5 + 600)
suma = -3000 - 1000 + 600
coef = 1/2 + 1/3 + 1/4 + 1/5
# f = suma + coef*f
# suma = f*(coef - 1)
# f = suma/(coef - 1)
print("Respuesta 2.1:", suma / (coef - 1))

'''
 Ejercicio 7.3

Tres ciclistas recorren una pista circular. El primero tarda
32 minutos, el segundo 40 minutos y el tercero 44
minutos. Si salieron juntos a las 7h, ¿a qué hora
coincidirán, por primera vez?
'''

# La primera vez que coinciden es a las 7h.

# La segunda vez que coinciden es el minimo comun multiplo de sus tiempos.
# mcm(a, b) = (a * b) / mcd(a, b)

import math
a, b, c = 32, 40, 44
print("Respuesta 3.1:", (a*b*c)/math.gcd(math.gcd(a, b), c))

