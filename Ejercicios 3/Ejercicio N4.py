class Catalogo:
    def __init__(self,productos=[]):
        self.productos=productos
    def __str__(self):
        return f'{self.productos}'
    productos=[]
    def agregar(self,p):
        self.productos.append(p)
    def mostrar(self):
        for p in self.productos:
            print(p)
pro1=Catalogo('Aceites y líquidos')
pro2=Catalogo('Neumáticos')
pro3=Catalogo('Filtros')
pro1.mostrar()

print("""Bienvenido a Ferreterias Sabrosas LLantas
            ¿Que desea realizar?
            a)Revisar el catalogo de productos
            b)Ingresar productos""")
m=input("elija una opcion: ")

