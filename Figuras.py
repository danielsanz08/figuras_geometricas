class figura_geometrica:
    def __init__(self, nombre: str, area:float):
        
        self.nombre=nombre
        self.area=area 
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre:str):
        self._nombre=nombre
    
    @property
    def  area(self):
        return self._area
    
    @area.setter
    def area(self,area: float):
        self._area=area
    
    @staticmethod
    def calcular_area(self):
        print(f"Esta es una figura generica, no puedo calcular el area...")
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Area: {self.area}"