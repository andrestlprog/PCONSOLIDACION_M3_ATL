#FILTRANDO DATOS:
#INSTRUCCIONES: Lee con atención cada uno de los requerimientos que se presentan a continuación, y desarrolla la prueba de acuerdo con lo solicitado.
#DESCRIPCIÓN: Dada la siguiente lista de nombres: Harry Houdini, Newton, David Blaine, Hawking, Messi, Teller, Einstein, Pele, Juanes.
#Y sabiendo que Harry Houdini, David Blaine y Teller son magos. Y también que Newton, Hawking y Einstein son científicos. Debemos separar los nombres en tres grupos: magos, científicos y otros; y escribir una función llamada hacer_grandioso(), que modifique la lista de magos añadiendo la frase ‘El gran‘ antes del nombre de cada mago. Crear una función llamada imprimir_nombres(), que imprime el nombre de cada persona de la lista.
#Finalmente, imprimir en pantalla la lista completa de nombres antes de ser modificados; luego imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes.

nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

magos = ["Harry Houdini", "David Blaine", "Teller"]

cientificos = ["Newton", "Hawking", "Einstein"]

otros = ["Messi", "Pele", "Juanes"]

hacer_grandioso = [["El Gran", magos[0]], ["El Gran", magos[1]] ,["El Gran", magos[2]]]

print(nombres)

imprimir_nombres = print(hacer_grandioso)

print(cientificos)

print(otros)