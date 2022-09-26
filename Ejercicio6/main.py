
from src.MonticuloBinario import MonticuloBinario


if __name__ == '__main__':
    m = MonticuloBinario(100)

    m.insertar(10)
    m.insertar(20)
    m.insertar(35)
    m.insertar(50)
    m.insertar(1)

    m.eliminarMenor()

    print(m)