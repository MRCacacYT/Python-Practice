import random
import time

def busqueda_binaria(lista, comienzo, final, objetivo, iter_bin=0):
    iter_bin += 1
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:
        return (False, iter_bin)

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return (True, iter_bin)
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, iter_bin)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, iter_bin)

def busqueda_lineal(lista, objetivo, iter_lin=0):
    match = False

    for elemento in lista:
        iter_lin += 1
        if elemento == objetivo:
            match = True
            break

    return (match, iter_lin)


if __name__ == '__main__':
    tamano_de_lista = int(input(' de que tamano es la lisata? '))
    objetivo = int(input('que nuemero quieres econtrar: '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

    (encontrado, iter_bin) = busqueda_binaria(lista, 0, len(lista), objetivo)
    (encontrado, iter_lin) = busqueda_lineal(lista, objetivo)

    print(lista)
    print(f'el elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'iteraciones en busqeuda lineal: {iter_lin}')
    print(f'iteraciones en busqueda bienaria: {iter_bin}')
