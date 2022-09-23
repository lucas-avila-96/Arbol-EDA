from src.classNodo import Nodo

class Arbol:
    __raiz = None

    def __init__(self):
        self.__raiz = None

    def insertar(self, x):
        self.__insertar(x, self.__raiz)

    def __insertar(self, valor, subArbol):
        if self.__raiz is None:
            self.__raiz = Nodo(valor)
        else:
            if subArbol.getDato() == valor:
                print('ya existe')
            else:
                if valor < subArbol.getDato():
                    if subArbol.getIzquierdo() is not None:
                        self.__insertar(valor, subArbol.getIzquierdo())
                    else:
                        nuevoNodo = Nodo(valor)
                        subArbol.setIzquierdo(nuevoNodo)
                else:
                    if subArbol.getDerecho() is not None:
                        self.__insertar(valor, subArbol.getDerecho())
                    else:
                        nuevoNodo = Nodo(valor)
                        subArbol.setDerecho(nuevoNodo)

    def hoja(self, x):
        esHoja = False
        if self.__raiz is not None:
            hoja = self.__buscar(x, self.__raiz)
            if hoja.getIzquierdo() is None and hoja.getDerecho() is None:
                esHoja = True
        return esHoja
    
    def hijo(self, x, z):
        esHijoIzq = z.getIzquierdo().getDato() == x.getDato()
        esHijoDer = z.getDerecho().getDato() == x.getDato()
        return esHijoIzq or esHijoDer
            
    def padre(self, x, z):
        esHijoIzq = z.getIzquierdo().getDato() == x.getDato()
        esHijoDer = z.getDerecho().getDato() == x.getDato()
        return esHijoIzq or esHijoDer
    '''
    def camino(self, x, z):
        if self.__raiz is not None:
            r1 = self.__buscar(x, self.__raiz)
            r2 = self.__buscar(z, r1)
        if r2 is not None:
            self.__inOrden(r1)
    '''

    def grado(self, subArbol):
        grado = 0
        if subArbol.getIzquierdo() is not None or subArbol.getDerecho() is not None:
            grado = 1
        if subArbol.getIzquierdo() is not None and subArbol.getDerecho() is not None:
            grado = 2
        return grado
        
    def buscar(self, valor):
        if self.__raiz is not None:
            return self.__buscar(valor, self.__raiz)

    def __buscar(self, valor, subArbol):
        if valor == subArbol.getDato():
            return subArbol
        elif valor < subArbol.getDato() and subArbol.getIzquierdo() is not None:
            return self.__buscar(valor, subArbol.getIzquierdo())
        elif valor > subArbol.getDato() and subArbol.getDerecho() is not None:
            return self.__buscar(valor, subArbol.getDerecho())

    def inOrden(self): 
        if self.__raiz is not None: 
            print('in Orden')
            self.__inOrden(self.__raiz) 
    
    def __inOrden(self, subArbol): 
        if subArbol is not None:
            self.__inOrden(subArbol.getIzquierdo())
            print(str(subArbol.getDato()) + ' ')
            self.__inOrden(subArbol.getDerecho())
    
    def preOrden(self): 
        if self.__raiz is not None: 
            print('Pre Orden')
            self.__preOrden(self.__raiz)
    
    def __preOrden(self, subArbol): 
        if subArbol is not None:
            self.__preOrden(subArbol.getIzquierdo())
            print(str(subArbol.getDato()) + ' ')
            self.__preOrden(subArbol.getDerecho())
    
    def postOrden(self): 
        if self.__raiz is not None: 
            print('Post Orden')
            self.__postOrden(self.__raiz) 
    
    def __postOrden(self, subArbol): 
        if subArbol is not None:
            self.__postOrden(subArbol.getIzquierdo())
            self.__postOrden(subArbol.getDerecho())
            print(str(subArbol.getDato()) + ' ')


    def maximo(self, nodo):
        if nodo.getDerecho() is None:
            return nodo
        return self.maximo(nodo.getDerecho())
 
    def suprimir(self, valor):
        if self.__raiz is not None:
            return self.__suprimir(self.__raiz, valor)

    def __suprimir(self, subArbol, valor):
        if subArbol == None: 
            return None
        elif valor < subArbol.getDato():
            self.__suprimir(subArbol.getIzquierdo(), valor)
        elif valor > subArbol.getDato(): 
            self.__suprimir(subArbol.getDerecho(), valor)
        if subArbol.getDato() == valor:
            if self.grado(subArbol) == 0:
                pass
            elif self.grado(subArbol) == 1:
                if subArbol.getIzquierdo() == None:
                    subArbol.setDato(subArbol.getDerecho().getDato())
                    subArbol.setDerecho(None)
                elif subArbol.getDerecho() == None:
                    subArbol.setDato(subArbol.getIzquierdo().getDato())
                    subArbol.setIzquierdo(None)
            elif self.grado(subArbol) == 2:
                temp = self.maximo(subArbol.getIzquierdo())
                subArbol.setDato(temp.getDato())
                self.__suprimir(subArbol.getIzquierdo(), temp.getDato()) 


    def __nivel(self, nodo, valor, nivel):
        if nodo == None:
            return 0
        if nodo.getDato() == valor:
            return nivel
        result = self.__nivel(nodo.getIzquierdo(), valor, nivel + 1)
        if result != 0:
            return result
        result = self.__nivel(nodo.getDerecho(), valor, nivel + 1)
        return result
 
 
    def nivel(self, valor):
        return self.__nivel(self.__raiz, valor, 1)

    def __altura(self, nodo):
        if nodo == None:
            return 0
        altIzq = self.__altura(nodo.getIzquierdo())
        altDer = self.__altura(nodo.getDerecho())
        return max(altIzq, altDer) + 1

    def altura(self):
        return self.__altura(self.__raiz)





