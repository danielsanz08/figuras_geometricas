from Figuras import figura_geometrica
import math

class circulo(figura_geometrica):
    # Atributo de clase y constante

    def __init__(self, radio: float = 0):
        super().__init__("Circulo", area=0)
        self._radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, radio: float):
        self._radio = radio

    def calcular_area(self):
        if self._radio == 0:
            print(f"No se ha establecido un radio...")
            return False
        else:
            self.area = math.pi * (self._radio ** 2)

    def __str__(self):
        return f"Nombre: {self.nombre}, Area: {self.area}, Radio: {self._radio}"
