
from src.Arbol import Arbol

'''
a) Mostrar el nodo padre y el nodo hermano, de un nodo previamente ingresado por 
teclado; éste puede o no existir en el árbol.
b) mostrar la cantidad de nodos del árbol en forma recursiva.
c) Mostrar la altura de un árbol.
d) Mostrar los sucesores de un nodo ingresado previamente por teclado.

'''

def sucesores(nodo):
    if nodo.getIzquierdo():
        print(nodo.getIzquierdo().getDato())
    if nodo.getDerecho():
        print(nodo.getDerecho().getDato())

def mostrarPadre():
    pass


def mostrarHermano(nodo):
    pass


def nroNodos(nodo):
    if nodo == None:
        return 0
    else:
        i = 0
        d = 0
        if nodo.getIzquierdo() != None:
            i = nroNodos(nodo.getIzquierdo())
        if nodo.getDerecho() != None:
            d = nroNodos(nodo.getDerecho())
        return 1 + i + d

if __name__ == '__main__':
    arbol = Arbol()
    arbol.insertar(10)
    arbol.insertar(5)
    arbol.insertar(3)
    arbol.insertar(7)
    arbol.insertar(4)
    arbol.insertar(1)
    arbol.insertar(8)
    arbol.insertar(12)
    arbol.insertar(15)
    '''
    print(arbol.altura())
    print(nroNodos(arbol.getRaiz()))
    
    sucesores(arbol.buscar(3))
    '''
    
