import string
from src.classNodo import Nodo

class Huffman:
    __raiz = None

    def __init__(self):
        __raiz = None
    
    def crearArbolHuffman(self, file):
        texto = ''
        nodos = []
        for line in file:
            texto += line

        diccionario = dict()
        for i in range(len(texto)):
            if texto[i] in diccionario:
                diccionario[texto[i]] += 1
            else:
                diccionario[texto[i]] = 1

        for clave, valor in diccionario.items():
            nodos.append(Nodo(clave, valor))

        nodos.sort()

        while len(nodos) >= 2:
            sumChar = nodos[0].getDato() + nodos[1].getDato()
            sumFrec = nodos[0].getFrecuencia() + nodos[1].getFrecuencia()
            nuevoNodo = Nodo(sumChar, sumFrec)
            nuevoNodo.setDerecho(nodos[0])
            nuevoNodo.setDerecho(nodos[1])
            nodos.pop(0)
            nodos.pop(0)
            nodos.append(nuevoNodo)

        self.__raiz = nodos[0]

    def preOrden(self, subArbol):
        if subArbol is not None:
            self.preOrden(subArbol.getIzquierdo())
            print(str(subArbol.getDato()) + ' ')
            self.preOrden(subArbol.getDerecho())

    def getRaiz(self):
        return self.__raiz

        





        