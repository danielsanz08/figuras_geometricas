from circulo import circulo
import Figuras
from Triangulo import triangulo
if __name__ =="__main__":

    mi_circulo= circulo()
    mi_circulo.radio=25
    print(mi_circulo.calcular_area())
    print(mi_circulo)
        

    mi_triangulo = triangulo(altura=78, base=25)
    mi_triangulo.calcular_area_triangulo()
    print(mi_triangulo.area)
    print(mi_triangulo)