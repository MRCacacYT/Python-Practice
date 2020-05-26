
def  peso():
    marte = 1.5
    jupiter = 3
    tierra = 9.1
    peso_user = int(input('cual es tu peso? '))
    print('ahora elige un planeta: 1 es tierra, 2 es marte, 3 es jupiter')
    respuesta = int(input('escribe tu respuesta: '))

    if respuesta == 1:
        print(f'tu peso en la tierra es de {peso_user}')
    elif respuesta == 2:
        peso_user = peso_user * marte
        print(f'tu peso en marte es de {peso_user} ')
    elif respuesta == 3:
        peso_user = peso_user * jupiter
        print(f'tu peso en jupiter es {peso_user}')
    else:
        print(f'chingas a toda tu madre')

peso()