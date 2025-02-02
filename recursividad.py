'''utlizando recursion hare un algoritmo el cual le entregara a un profesor un escrito y el lo revisara.
 el profesor no lo puede aceptar hasta que el alumno hago bien su trabajo.'''


#Enunciado: crea una funcion factorial utilizando recursion. Con la formula R(n) = n * R(n-1)
def factorial(number: int):
  if number == 1:
    return 1  
  return number * factorial(number -1)
  
#print(factorial(5))

#5 - 4, 4 -3, 3- 2, 2-1, 1
#2x 1 = 2, 3x2 = 6, 4x6 = 24, 5x24 = 120 
'''
orden de stack
Llamadas (apilando):
factorial(5)
    factorial(4)
        factorial(3)
            factorial(2)
                factorial(1)  ← Caso base

Resolviendo (desapilando):
                factorial(1) = 1
            factorial(2) = 2 × 1 = 2
        factorial(3) = 3 × 2 = 6
    factorial(4) = 4 × 6 = 24
factorial(5) = 5 × 24 = 120
'''
#Enunciado:
#Escribe una función recursiva que calcule la suma de los primeros n números naturales.
def suma_numeros_naturales(number: int):
  if number == 1:
    return 1
  return number + suma_numeros_naturales(number - 1)

#print(suma_numeros_naturales(5))

#5, 5-1=4, 4-1=3, 3-1=2, 2-1=1, 1
#1, 2+1=3, 3+3=6, 4+6=10, 10+5= 15
'''
llamadas stack
suma(5)
  suma(4)
    suma(3)
      suma(2)
        suma(1) -> caso base
        unstack
        suma(1) = 1
      suma(2) = 2+1 = 3
    suma(3) = 3+3 = 6
  sumas(4) = 4+6 = 10
sumas(5) = 5 + 10 = 15
'''

def fibonacci(number: int):
  if number == 0:
    return 0
  elif number == 1:
    return 1
  return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(6))