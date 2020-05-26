# partir un problema en problemas mas pequenos
# las clases permiten crear mayores absatracciones en forma de componentes
# cada clase se encarga de una parte del problema y el programa se vuelve mas acil de mantener

class Automovil:
    def __init__(self, modelo, marca, color, blindaje):
        self.blindaje = blindaje
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en reposo'
        self._motor = Motor(cilindros=4)

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado = 'en movimiento'

class Motor:
    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass
