# Examen.parcial
PREGUNTA 1

Realiza los siguientes ejercicios en un fichero llamado Ejercicio1.py:
*Convertir la variable "var_1" en todas las letras mayúsculas y en minúsculas (var_1 = "Módulo 1 de Python ")

*Consulta el tamaño o la longitud de la variable "var_1" y calcula la división de ese numero entre "7" redondeado a 4 decimales

*Realiza una función llamada funcion1  que calcule siguiente operación para que el resultado final sea igual a cero (0) //12 - (4 * 2) - (2 + 2)
*Realiza una función llamada funcion2 para que calcule la siguiente operación para que el resultado final sea igual a catorce (14)// 12 - 4 * (2 - 2) + 2
*Realiza una función llamda funcion3 para pedir al usuario que introduzca su edad, y después imprimir en la pantalla si es meyor de edad o no
Adjuntar archivo

PREGUNTA 2

Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre de un alumno y la nota de un exámen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?

Nombre Apellido ha sacado un Nota de nota.

Ayuda

Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: cadena[::-1]

cadena = "zeréP nauJ,01"

Adjuntar archivoNinguno archivo selec.
1 puntos   

PREGUNTA 3

Realiza un programa llamado multiplicador.py que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:

Guarda en una variable numero_magico el valor 12345679 (sin el 8)
Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
Multiplica el numero_usuario por 9 en sí mismo
Multiplica el numero_magico por el numero_usuario en sí mismo
Finalmente muestra el valor final del numero_magico por pantalla
Adjuntar archivoNinguno archivo selec.
1 puntos   

PREGUNTA 4

En este ejercicio se os pide crear un fichero llamado listasCEU.py que realice las siguientes funcionnes


Define una lista que contenga al menos 4 elementos de todos los tipos de valores permitidos en Python.
Selecciona cada dos elementos (uno si otro no) desde el final de la lista.
Cambia solamente la posición del primer elemento con el último elemento de la lista.
Elimina el último elemento de la lista modificada en el paso anterior.
Crea una nueva lista con la repetición de los elemento de la lista guardada en el paso anterior.

Adjuntar archivoNinguno archivo selec.
2 puntos   

PREGUNTA 5

Crea un script llamado descomposicion.py que realice las siguientes tareas:

Debe tomar 1 argumento que será un número entero positivo.
En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.
El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número 3287:

python descomposicion.py 3647

El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo:

0007

0080

0200

1000

Pista

Que el valor sea un número no significa necesariamente que deba serlo para formatearlo. Necesitarás jugar muy bien con los índices y realizar muchas conversiones entre tipos cadenas, números y viceversa

Adjuntar archivoNinguno archivo selec.
2 puntos   

PREGUNTA 6

Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:

Borrar los elementos duplicados.
Ordenar la lista de mayor a menor.
Eliminar todos los números impares.
Realizar una suma de todos los números que quedan.
Añadir como primer elemento de la lista la suma realizada.
Devolver la lista modificada.
Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista, tal que así:
nueva_lista = modificar(lista)

print( nueva_lista[0] == sum(nueva_lista[1:]) )

True

Recordatorio

La función sum(lista) devuelve una suma de los elementos de una lista.

Adjuntar archivoNinguno archivo selec.
2 puntos   

PREGUNTA 7

Crea un Script llamado recorrido.py que realice las siguientes funciones:

Recorre el listado del ejemplo y realiza las siguientes operaciones: [18, 50, 210, 80, 145, 333, 70, 30]

Imprimr el número en caso de que sea múltiplo de 10 y menor que 200
Parar el programa si llega a un número mayor que 300
Adjuntar archivoNinguno archivo selec.

[19:51, 26/10/2022] +34 684 28 90 48: cadena = "zeréP nauJ,01"

# Completa el ejercicio aquí
l = cadena[::-1].split(',')
print( l[1] + " ha sacado un " + l[0] + " de nota")
 numero_magico = 12345679
numero_usuario = int( input( "Introduce un entero (1-9): "))
numero_usuario *= 9
numero_magico *= numero_usuario
print( numero_magico)
[19:51, 26/10/2022] +34 684 28 90 48: 3
[19:52, 26/10/2022] +34 684 28 90 48: lista_1 = ["h","o","l","a","","m","u","n","d","o"]
lista_2 = ["h","o","l","a","","l","u","n","a"]

lista_3 = []

for letra in lista_1:
    if letra in lista_2 and letra not in lista_3:
        lista_3.append(letra)

print(lista_3)
[19:52, 26/10/2022] +34 684 28 90 48: 4
[19:52, 26/10/2022] +34 684 28 90 48: def ordenar(c):
    return c['prioridad']

cola = [
    {'tarea2' : 'comprar', 'prioridad' : '2'},
    {'tarea1' : 'Python', 'prioridad' : '1'},
    {'tarea4' : 'comer', 'prioridad' : '4'},
    {'tarea3' : 'jugar', 'prioridad' : '3'},
]

cola.sort(key=ordenar)
print(cola[0]['tarea1'], cola[1]['tarea2'], cola[2]['tarea3'],cola[3]['tarea4'])
[19:52, 26/10/2022] +34 684 28 90 48: 5
[19:53, 26/10/2022] +34 684 28 90 48: print("Introduce un número entero positivo de 4 cifras para que sea descompuesto")

num = input("Tu número: ")
if len(num) != 4:
    print("Tu número no es válido")
else:
    for c in range(3, -1, -1):
        res = num[c]
        if c == 0:
            n ="1000"
            m = n.replace("1", res)
            print(m)
        elif c == 1:
            n ="0100"
            m = n.replace("1", res)
            print(m)
        elif c == 2:
            n ="0010"
            m = n.replace("1", res)
            print(m)
        elif c == 3:
            n ="0001"
            m = n.replace("1", res)
            print(m)