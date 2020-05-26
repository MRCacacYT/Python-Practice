# busca en todos los elementos
# el peor caso es que el numero sea muy largo
import random

def busqueda(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break

    return match

if __name__ == '__main__':
    tamano_de_lista = int(input('de que tamano sera la lista: '))
    objetivo = int(input('que numero quieres encontrar? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

    encontrado = busqueda(lista, objetivo)
    print(lista)
    print(f'el elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
