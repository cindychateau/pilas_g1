from Nodo import Nodo
from Pila import Pila

nodo1 = Nodo('A')
nodo2 = Nodo('B')
nodo3 = Nodo('C')

pila = Pila() #top: None

pila.push(nodo1) #top: nodo1
pila.imprimePila()
print('---------')

pila.push(nodo3) #top: nodo3
pila.imprimePila()
print('---------')

pila.push(nodo2)
pila.imprimePila()
print('---------')

pila.pop()
pila.imprimePila()
print('---------')

pila.pop()
pila.imprimePila()
print('---------')

# Crear una función que recibe como parámetro un string. Este string contiene una 
# fórmula matemática. La función debe de validar que los parentesis, corchetes y llaves
# sean correctos y tengan una estructura y orden válido. Retorna True si la validación 
# es exitosa, False de lo contrario
# ( 1 + 2 ) * ( 6 * 4 ) => True
# ( x + [z-3] * { 4 + 5 * (y - 7)} ) => True
# ( x + z / [ y * z} + 7 ) => False


