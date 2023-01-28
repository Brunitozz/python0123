def ejericio4():

    class Producto:
        def __init__(self, articulo) -> None:
            self.articulo=articulo
            print('el producto es: ', self.articulo)
            pass
    class Catalogo:
        mercancia=[]
        def __init__(self,mercancia=[]):
            self.mercancia=mercancia
        def agregar(self,m):
            self.mercancia.append(m)
        def mostrar(self):
            for m in self.mercancia:
                return m

    arti1=Producto('neumaticos')
    mer1=Catalogo([arti1])
    mer1.mostrar()

    mer1.agregar(Producto('aceites'))
    mer1.mostrar()
