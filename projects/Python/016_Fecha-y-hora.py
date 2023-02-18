# Fecha y hora
import datetime
ahora = datetime.datetime.now()
print(ahora)
nacimiento = datetime.datetime(2001, 9, 5)
print(nacimiento)
edad = ahora - nacimiento
print(edad)
birthday = nacimiento.strftime('%d-%m') # %y 01; %Y 2001
print(birthday)
""" Permament clock
while True:
    print('\r', datetime.datetime.now(), sep = '', end = '')
"""