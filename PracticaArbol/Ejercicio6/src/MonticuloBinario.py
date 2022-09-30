import numpy as np


class MonticuloBinario:
    __items = None

    def __init__(self, tamano):
        self.__items = np.empty(tamano, dtype=int)
        self.__items[0] = 1

    def insertar(self, x):
        i = self.__items[0]
        self.__items[i] = x
        self.__items[0] += 1
        while i // 2 >= 1:
            if self.__items[i] < self.__items[i // 2]:
                aux = self.__items[i // 2]
                self.__items[i // 2] = self.__items[i]
                self.__items[i] = aux
            i = i // 2

    def hijoMenor(self, i):
        if i * 2 + 1 > self.__items[0]:
            return i * 2
        else:
            if self.__items[i * 2] < self.__items[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def eliminarMenor(self):
        tam = self.__items[0] # tamaño
        valorSacado = self.__items[1]
        self.__items[1] = self.__items[tam]
        self.__items[0] -= 1
        i = 1
        while (i * 2) <= tam:
            hijoMenor = self.hijoMenor(i)
            if self.__items[i] > self.__items[hijoMenor]:
                aux = self.__items[i]
                self.__items[i] = self.__items[hijoMenor]
                self.__items[hijoMenor] = aux
            i = hijoMenor
        return valorSacado

    def __str__(self):
        out = ''
        for i in range(self.__items[0]):
            out += str(self.__items[i]) + '->'
        return out
