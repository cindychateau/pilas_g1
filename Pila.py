from Nodo import Nodo

class Pila:
    def __init__(self):
        self.top = None
    
    #Ingresa un nuevo valor en mi pila
    #Pila-> top: None
    #nuevoNodo -> nodo1 -> A next: None
    #A.next = None
    #top = A

    #nuevoNodo -> nodo3 -> C next: None
    #C.next = A
    #top = C
    def push(self, nuevoNodo):
        #1.- El next de mi nuevoNodo sea el top que teníamos antes
        nuevoNodo.next = self.top
        self.top = nuevoNodo

    #Imprime toda la pila en orden
    #Pila -> top: A, C, B
    #aux = A
    #IMPRIMO A
    #aux = C
    #IMPRIMO C
    #aux = B
    #IMPRIMO B
    #aux = None
    def imprimePila(self):
        aux = self.top
        while aux != None:
            print(aux.valor)
            aux = aux.next

    #Elimina el nodo de más arriba
    #Pila -> top: A, C, B
    #aux = A
    #top= A.next = C
    #A.next = None
    #Pila -> top: C, B
    def pop(self):
        aux = self.top
        if aux != None:
            self.top = aux.next
            aux.next = None
