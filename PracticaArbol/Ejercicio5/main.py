
from src.huffman import Huffman

if __name__ == '__main__':
    file = open('Ejercicio5/src/texto.txt')

    huffman = Huffman()

    huffman.crearArbolHuffman(file)
    raiz = huffman.getRaiz()
    huffman.preOrden(raiz)