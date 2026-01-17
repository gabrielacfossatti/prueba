"""TRABAJO PRACTICO 1"""

"""1) Almacene un mensaje en una variable e imprímalo en pantalla.
Después cambie el valor del mensaje e imprímalo nuevamente."""

# texto1 = "¡Hola! Bienvenido/a"
# print(texto1)

texto1 = "¡Hola! Estas a punto de empezar"
print(texto1)

"""2) Almacene el nombre de una persona en una variable, imprima un mensaje para esa persona."""

texto3 = input("Ingrese un nombre: ")
print("Estas a punto de comenzar " + texto3)

"""3) El número ocho: Escriba una suma, resta, multiplicación y división que resulten cada una en el número ocho.
Asegúrese de utilizar la función print() para ver los resultados en pantalla."""

#SUMA
suma1 = 3
suma2 = 5
print(suma1+suma2)

#RESTA
resta1= 12
resta2=4
print(resta1-resta2)

#MULTIPLICACION
multiplicacion1=4
multiplicacion2=2
print(multiplicacion1*multiplicacion2)

#DIVISION
division1=24
division2=3
print(division1/division2)

"""4) Cree cuatro variables llamadas mi_entero, mi_decimal, mi_string y mi_booleano. 
Asigne a cada variable un valor del tipo que le corresponda. Luego muestre en pantalla el tipo de cada variable usando la función type() combinando todo con la función print()"""

mi_entero=7
mi_decimal=7.5
mi_string="¡Arya necesita salir a pasear!"
mi_booleano=True

print(type(mi_entero))
print(type(mi_decimal))
print(type(mi_string))
print(type(mi_booleano))

"""5) Escriba un programa que acepte un numero decimal como entrada y lo imprima sin lugares decimales."""

numero=float(input("Ingrese un numero decimal: "))
numero2=int(numero)
print(numero2)

"""6. Escriba un programa que le pida al usuario que ingrese nombre y edad. 
Luego muestre un mensaje donde le informe el año en que va a cumplir 100."""

nombre=input("Ingrese su nombre:")
edad=int(input("Ingrese su edad:"))
año_cumple100= 2025 + (100 - edad)
print(f"Hola {nombre} vas a cumplir 100 años en el año {año_cumple100}")

"""7. Escriba un programa que permita convertir una temperatura en Celsius a la escala Fahrenheit. La fórmula es:
Fahrenheit = (9.0/5.0) x Celsius + 32"""

Celsius=int(input("Ingrese la temperatura actual:"))
Fahrenheit=(9.0/5.0)*Celsius+32
print(f"{Celsius}°C equivalen a {Fahrenheit}°F")

