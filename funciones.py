def enumeracion_exh():
    objetivo = int(input('Escribe un numero: '))
    respuesta = 0

    while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de  {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} No tiene raiz cuadrada Exacta')

def aproximacion():
    objetivo = int(input('Escribe un numero: '))
    epsilon = 0.01#que tan preciso queremos ser
    paso = epsilon**2#que tanto nos acercamos en cada iteración
    respuesta = 0.0#variable que almacenara la respuesta

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'no se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def busqueda_binaria():
    objetivo = int(input('escoge un numero: '))
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo ) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}, respuesta1={respuesta**2 - objetivo}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo ) / 2

    print(f'La raíz cuadrada de {objetivo} es {respuesta}')

print('¡Bienvenido!')
print('¡Calcule la raíz cuadrada de un numero con base a estos algoritmos!\n')
print('1 Enumeracion exhaustiva \n' 
      '2 Aproximación de valores \n'
      '3 Busqueda binaria\n')
num = int(input('Seleccione una opción: '))

if num == 1:
    print('Bienvenido al algoritmo de Enumeración exhaustiva \n')
    enumeracion_exh()
elif num == 2:
    print('Bienvenido al algoritmo de aproximación de valores \n')
    aproximacion()
elif num == 3:
    print('Bienvenido al algoritmo de busqueda binaria \n')
    busqueda_binaria()
else:
    print("No selecciono ninguna de las opciones, vuelva a intentarlo")
