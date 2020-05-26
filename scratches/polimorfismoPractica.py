class Electronico:

    def __init__(self, nombre = None, precio = None, marca = None):
        self._nombre = nombre
        self._precio = precio
        self._marca = marca

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca


    def Encendido(self):
        print(f"El dispositivo {self.nombre} se activo correctamente")


class Computadora(Electronico):

    def __init__(self,nombre, precio, marca, procesador = None, nucleos = None, t_grafica = None, m_board = None):
        super().__init__(nombre,precio,marca)
        self.procesador = procesador
        self._nucleos = nucleos
        self.t_grafica = t_grafica
        self.m_board = m_board

    @property
    def nucleos(self):
        return  self._nucleos

    @nucleos.setter
    def nucleos(self, nucleos):
        self._nucleos = nucleos

    def Encendido(self):
        print(f"Encendio la PC {self.nombre} con exito")

    def Tareas(self, nombre, n_nucleos):
        print(f"Esta realizando la tarea {nombre} con {n_nucleos}  nucleos asignados\n")

class Laptop(Computadora):

    def __init__(self,nombre, precio, marca):
        super().__init__(nombre,precio,marca)
        pass


if __name__ == '__main__':
    r2d2 = Electronico('R2 - D2', 999.999, '¿?')
    compu = Computadora('The Power',1000,'Varios','Core i5 5000', 4, 'gtx 1060', 'Aorus B450')
    lap = Laptop('RGB',1500,'MSI')

    r2d2.Encendido()
    print(f'Con precio de {r2d2.precio} y pertenece a {r2d2.marca}\n')

    compu.Encendido()
    print(f'Con precio de {compu.precio} con especificaciones {compu.procesador}, {compu.nucleos},\n '
          f'con una TG {compu.t_grafica} y una mother {compu.m_board}')
    compu.Tareas('Jugar Fornite',2)

    print(f'''{lap.nombre}
{lap.precio}
{lap.marca}
{lap.procesador}
{lap.nucleos}
{lap.m_board}''')