
class Nodo:
    __izq = None
    __der = None
    __clave = None

    def __init__(self, clave):
        self.__clave = clave
        self.__der = None
        self.__izq = None
    
    def getIzquierdo(self):
        return self.__izq

    def getDerecho(self):
        return self.__der

    def getDato(self):
        return self.__clave

    def setDato(self, clave):
        self.__clave = clave

    def setDerecho(self, clave):
        self.__der = clave

    def setIzquierdo(self, clave):
        self.__izq = clave


