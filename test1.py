print("Hola Mundo!\n")
List1 = ["hola","mundo","!"]
print(List1)

# List2 = List1  #referencia la lista, no es una copia
List2 = List1[:]  # clona la lista, es una copia

List1[0] = "Hello"
List1[1] = "World"
# imprime nueva lista

print("Lista 1: ", List1)
print("Lista 2: ", List2)

print("Fin del programa!")
