from Figuras import figura_geometrica

class triangulo(figura_geometrica):
    def __init__(self, altura: float,base: float):
        super().__init__("Triangulo", area=0)
        self._altura= altura
        self._base= base
    
    @property
    
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, altura:float):
        self._altura= altura
    
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, base: float):
        self._base= base
        
    def calcular_area_triangulo(self):
        if self.base==0 or self.altura ==0:
            print(f"No se puede calcular")
        else:
            self.area= (self.base*self.altura)/2
    def __str__(self):
        return f"Nombre: {self.nombre}, Area: {self.area}, Base: {self._base}, altura. {self.altura}"