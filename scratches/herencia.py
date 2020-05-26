# herencia, permite modelar una jerarquia de clases
# permite compartir comportamiento comun en la jerarquia
# al padre se le conoce como sperclase y al hijo como subclase

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):                  # aqui es donde se hereda

    def __init__(self, lado):
        super().__init__(lado, lado )          # obtuvimos acceso directo a la super clase

if __name__ == '__main__':
    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area())