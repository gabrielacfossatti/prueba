"""TRABAJO PRACTICO 2"""

"""1) Pida un número al usuario y determine si es par o impar."""

NUMERO=int(input("INGRESE UN NUMERO: "))
if NUMERO%2==0:
    print(f"EL {NUMERO} INGRESADO ES PAR")
else: 
    print(f"EL {NUMERO} INGRESADO ES IMPAR")

"""2) Escriba una cadena if-elif-else que determine el estado de vida de una persona.
• Si la persona tiene menos de 2 años, muestre un mensaje que diga que es un bebe.
• Si tiene al menos 2 años, pero menos de 4, muestre que es un infante.
• Si tiene al menos 4, pero menos de 12, muestre que es un niño.
• Si tiene al menos 13, pero menos de 20, muestre que es un adolescente.
• Si tiene al menos 20 pero menos de 65, muestre que es un adulto.
• Si tiene 65 o más, muestre que es un anciano."""

edad=int(input("Ingrese edad: "))
if edad<2:
    print(f"Esta persona de {edad} año/s es un bebé")
elif edad>=2 and edad<4:
    print(f"Esta persona de {edad} años aún es un infante")
elif edad>=4 and edad<=12:
    print(f"Esta persona de {edad} años es un/a niño/a")
elif edad>=13 and edad<20:
    print(f"Esta persona de {edad} años es adolescente")
elif edad>=20 and edad<65:
    print(f"Esta persona de {edad} años es adulto/a")
else:
    print(f"Esta persona de {edad} años es anciano/a")


# """3) Cree un ciclo que nunca termine y ejecútelo. Puede probarlo haciendo que muestre algo en pantalla por cada pasada del ciclo. 
# Para finalizarlo, presione Ctrl-C o el comando para detener la ejecución correspondiente a su editor"""

# while True:
#     print("⚠️  Deterner con Ctrl + C  ⚠️")

"""4) Escriba un programa que contenga dos ciclos while anidados que muestre los enteros del 1 al 100, 
diez números por línea, como se muestra abajo:
1 2 3 4 5 6 7 8 9 10
11 12 13 14 15 16 17 18 19 20
21 22 23 24 25 26 27 28 29 30
. . 91 92 93 94 95 96 97 98 99 100"""
contador=1
while contador<=100:
    contadorlinea=1
    while contadorlinea<=10:
        print(contador,end=" ")
        contador=contador+1
        contadorlinea=contadorlinea+1
    print()

"""5) Resuelva el ejercicio anterior usando solo un ciclo while"""

contador=1
while contador<=100:
    print(contador,end=" ")
    if contador%10==0:
        print()
    contador=contador+1



