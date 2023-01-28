class Producto:
    # Constructor de clase
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        
    def __str__(self):
        a=self.codigo.split(sep="-")
        return (f"""el nombre del producto es {self.nombre} y su codigo es {self.codigo}
        el pais de origen es {a[0]} y su lote es {a[1]}""")

produc1=Producto('Palomitas','ARGENTINA-0001-2023')
print(produc1)

