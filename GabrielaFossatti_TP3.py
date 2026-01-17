# """TP N° 3"""
# """Trabajo practico de estructuras de datos simples"""

"""1) Meter los números del 1 al 20 en una lista y mostrarla en pantalla. Hacer lo mismo
para un rango de números indicado por un usuario. """

lista=[]
for i in range (1,21):
    lista.append(i)
print(lista)

#CON NUMERO PEDIDO POR EL USUARIO

numero=int(input("Ingrese un número:"))
lista=[]

for i in range(1,numero+1):
    lista.append(i)
print(lista)


"""2) Pide un número y guarda en una lista su tabla de multiplicar hasta el 10. Por

ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50 """

numero=int(input("Ingrese un número: "))
lista=[]

for i in range(1,11):
    lista.append(numero*i)
print(lista)

"""3) Pide una cadena (string) por teclado, mete los caracteres en una lista sin repetir
caracteres. """

palabra=input("Ingrese una palabra: ")
lista=[]

for i in range(len(palabra)):
    repetido=False
    for j in range(len(lista)):
        if palabra[i]==lista[j]:
            repetido=True
    if repetido==False:
        lista.append(palabra[i])
print(lista)

"""4) Pide una cadena (string) por teclado, mete los caracteres en una lista sin espacios. """

palabra=input("Ingrese una palabra: ")
lista=[]

for i in range(len(palabra)):
    if palabra[i]!= " ":
        lista.append(palabra[i])
print(lista)

"""5) Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite."""

tupla=(1,2,5,4,7,8,9,4,1,2,5,6,7,1,2,3,6,4,5,6,6,8,2,7)
numero_buscado=int(input("Ingrese un numero: "))
contador=0

for i in range(len(tupla)):
    if tupla[i]==numero_buscado:
        contador=contador+1
print(f"El número {numero_buscado} se repite {contador} veces")
        
"""6) Crea una tupla con los meses del año, pedir números al usuario. Si el numero esta entre 1 y la longitud máxima de la tupla,
muestra el contenido de esa posición sino muestra un mensaje de error.
El programa termina cuando el usuario introduce un cero"""

tupla=("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")

posicion=int(input("Ingrese un número: "))
if posicion==0:
     print("Programa finalizado")
else:
    while posicion!=0:
        if posicion>= 1 and posicion<= len(tupla):
            print(f"El mes ingresado es {tupla[posicion-1]}")
        else:
            print("Error, elija otro número")
        posicion=int(input("Ingrese otro número: "))
    print("Programa finalizado")
    
"""7) Crea una tupla con números e indica el número con mayor valor y el que menor tenga."""
tupla=(1,5,6,3,2,88,5,4,1,2,5,45,41,5,7,98,5,15,5,23,1,5,6,54,1)
mayor=tupla[0]
menor=tupla[0]
for i in range(len(tupla)):
    if tupla[i]>mayor:
        mayor=tupla[i]
    elif tupla[i]<menor:
        menor=tupla[i]
print(f"El número mayor es {mayor} y el número menor es {menor}")

"""8. Escribir un programa que vaya solicitando al usuario que ingrese nombres.
- Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
- Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente. El usuario puede utilizar la cadena "*", para salir del programa"""


diccionario={"Barry Allen":1314551123,"Dracy Fitzwilliam":44113255812,"Charles Bingley":442055553491,"Hazel Levesque":19075553482,"Piper McLean":1405555672}


while True:
    nombre=(input("Ingrese un nombre o * para salir: "))
    if nombre=="*":
        break
    if nombre in diccionario:
        print(f"El número telefonico de {nombre} es {diccionario[nombre]}")
        consulta=(input("¿Desea modificarlo? SI/NO: "))
        if consulta.upper()=="SI":
            nuevo_numero=int(input("Ingrese el nuevo número: "))
            diccionario[nombre]=nuevo_numero
        elif consulta.upper()=="NO":
            print("El número no sera modificado")
    else:
        telefono=int(input("El nombre no existe. Ingrese el teléfono: "))
        diccionario[nombre]=telefono
        print("Contacto agregado a la agenda")



"""9)Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar.
Por último, muestra los números ordenados de menor a mayor. """

lista=[]

while True:
    numero=int(input("Ingrese un número o 0 para salir: "))
    if numero==0:
        break
    lista.append(numero)
for i in range (len(lista)):
    for j in range(len(lista)-1):
        if lista[j]>lista[j+1]:
            guardar=lista[j]
            lista[j]=lista[j+1]
            lista[j+1]=guardar
print(lista)

"""10)Lo mismo que el anterior, pero ordenando de mayor a menor. """    

lista=[]

while True:
    numero=int(input("Ingrese un número o 0 para salir: "))
    if numero==0:
        break
    lista.append(numero)
for i in range (len(lista)):
    for j in range(len(lista)-1):
        if lista[j]<lista[j+1]:
            guardar=lista[j]
            lista[j]=lista[j+1]
            lista[j+1]=guardar
            
print(lista)

"""11)Codificador Morse: Desarrolle un programa en Python que permita al usuario escribir un mensaje y convertirlo a código Morse.
Muestre el mensaje codificado de manera tal que haya una letra en Morse por línea,
y separe las palabras con dos líneas en blanco. Por ejemplo, "hola mundo" se mostraría:
.... --- .-.. .- / -- ..- -. -.. ---"""

codigo_morse= {"a":".-","b": "-...","c":"-.-.","d":"-..","e":".","f":"..-.", "g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..", "m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.", "s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--", "z":"--.."}

mensaje=input("Ingrese un mensaje: ").lower()
for letra in mensaje:
    if letra==" ":
        print()
        print()
    else:
        print(codigo_morse[letra])
