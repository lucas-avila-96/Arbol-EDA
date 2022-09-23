
from src.Arbol import Arbol

'''
a) Mostrar el nodo padre y el nodo hermano, de un nodo previamente ingresado por 
teclado; éste puede o no existir en el árbol.
b) mostrar la cantidad de nodos del árbol en forma recursiva.
c) Mostrar la altura de un árbol.
d) Mostrar los sucesores de un nodo ingresado previamente por teclado.

'''
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
    
    print(arbol.altura())
    print(arbol.nroNodos(arbol.getRaiz()))

    clave = int(input('Ingrese una clave para buscar'))
    nodo = arbol.buscar(clave)
    arbol.sucesores(nodo)
    padre = arbol.getPadre(arbol.getRaiz(), 1)
    print(padre.getDato())
    hermano = arbol.getHermano(arbol.getRaiz(), 5)
    print(hermano.getDato())
    
    if hermano != None:
        print(hermano.getDato())
    else:
        print('No tiene hermano')
