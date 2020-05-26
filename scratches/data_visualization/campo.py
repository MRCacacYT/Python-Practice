
class Campo:

    def __int__(self):
        self.coordenada_de_borrachos = {}

    def anadir_borracho(self, borracho, coordenada):
        self.borracho = borracho
        self.coordenada_de_borrachos[borracho] = coordenada

    def mover_borracho(self, borracho):
        delta_x, delta_y = borracho.camina()
        coordenada_actual = self.coordenada_de_borrachos[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)

        self.coordenadas_de_borrachos[borracho] = nueva_coordenada

    def obtener_coordenada(self, borracho):
        return self.coordenada_de_borrachos[borracho]

    