# CODE:18
# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 3.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Objetizo:
Realizar un programa que solicite ingresar
tres valores decimales de temperatura
De las temperaturas ingresadas se determinará:
1 - ¿Cuál es suma de todas las temperaturas ingresadas?
2 - ¿Cuál es el promedio de las temperaturas ingresadas?

IMPORTANTE: Para ordenar las temperaturas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.

Alumno:
- Deberá solicitar tres números decimales por consola,
cada nuḿero de temperatura lo debe almacenar
en variables llamadas:
-> temperatura_1
-> temperatura_2
-> temperatura_3

Utilizando el operador suma o el operador incremento
deberá almacenar la suma de todas las temperaturas
ingresadas en una nueva variable llamada "temperatura_total"

Luego, mediante el uso de la variable "temperatura_total"
y teniendo en cuenta que se ingresaron tres temperaturas.
Deberá calcular el promedio de todas las temperaturas
y almacenar el resultado en una variable llamada
"temperatura_promedio"

- Al final imprimir en pantalla la variable 
  temperatura_promedio
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
temperatura_1= float(input("Ingrese la primer temperatura: "))
temperatura_2= float(input("Ingrese la segunda temperatura: "))
temperatura_3= float(input("Ingrese la tercer temperatura: "))

if temperatura_1>temperatura_2>temperatura_3:
    temperatura_max=temperatura_1
elif temperatura_2>temperatura_3:
    temperatura_max=temperatura_2
else:
    temperatura_max=temperatura_3

if temperatura_1<temperatura_2<temperatura_3:
    temperatura_min=temperatura_1
elif temperatura_2<temperatura_3:
    temperatura_min=temperatura_2
else:
    temperatura_min=temperatura_3

if temperatura_min<temperatura_1<temperatura_max:
    temperatura_media=temperatura_1
elif temperatura_min<temperatura_2<temperatura_max:
    temperatura_media=temperatura_2
else:
    temperatura_media=temperatura_3

print("Temperatura maxima= ",temperatura_max)
print("Temperatura media= ",temperatura_media)
print("Temperatura minima= ",temperatura_min)

suma_temperaturas= temperatura_max+temperatura_media+temperatura_min
print("La suma de las temperaturas es: ", suma_temperaturas)

promedio_temperaturas=round(suma_temperaturas/3,2)
print("El promedio de las temperaturas es: ", promedio_temperaturas)

