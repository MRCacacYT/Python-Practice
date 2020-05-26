# manejo de errores como exepciones estilo try catch en JS

def divide_lista(lista, divisor):
    try:
        return[i / divisor for i in lista]
    except ZeroDivisionError as e:
        return lista

lista = list(range(10))
divisor = 0

print(divide_lista(lista, divisor))