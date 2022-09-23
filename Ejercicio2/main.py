
from src.Arbol import Arbol

def frontera(nodo):
    if nodo.getIzquierdo() is None and nodo.getDerecho() is None:
        print(nodo.getDato())
    if nodo.getIzquierdo() is not None:
        frontera(nodo.getIzquierdo())
    if nodo.getDerecho() is not None:
        frontera(nodo.getDerecho())

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

    frontera(arbol.getRaiz())