# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio
numero_1 = int(input("ingresar primer numero:\n"))
numero_2 = int(input("ingresar segundo numero:\n"))

while True:

    opcion = str(input("""Ingrese la operación a realizar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
- fin \n"""))

    if opcion == "+":
        print("la suma de la operacion es", numero_1+numero_2)
    elif opcion == "-":
        print("la resta de la operacion es", numero_1+numero_2)
    elif opcion == "*":
        print("la multiplicacion de la operacion es", numero_1+numero_2)
    elif opcion == "/":
        print("la division de la operacion es", numero_1+numero_2)
    elif opcion == "**":
        print("la potencia de la operacion es", numero_1+numero_2)
    elif opcion == "fin":
        print("terminamos!")
        break
    else: 
        print("ERROR")





