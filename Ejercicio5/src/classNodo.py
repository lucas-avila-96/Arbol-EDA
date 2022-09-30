
class Nodo:
    __char = None
    __frec = None
    __izq = None
    __der = None

    def __init__(self, char, frec):
        self.__char = char
        self.__frec = frec
        self.__der = None
        self.__izq = None
    
    def __gt__(self, otro):
        return self.__frec > otro.getFrecuencia()

    def getIzquierdo(self):
        return self.__izq
    
    def getFrecuencia(self):
        return self.__frec

    def setFrecuencia(self, frec):
        self.__frec = frec

    def getDerecho(self):
        return self.__der

    def getDato(self):
        return self.__char

    def setDato(self, char):
        self.__char = char

    def setDerecho(self, char):
        self.__der = char

    def setIzquierdo(self, char):
        self.__izq = char
    
