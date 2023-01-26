texto="""Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.
Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un
impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos
y los mezcló de tal manera que logró hacer un libro de textos especimen."""

print(texto.split(sep=" "))
print(" ".join(texto))
m=input("¿que palabra o letra desea contar?: ")
print(texto.count(m))
n=input("que palbra desea buscar?: ")
print("la palabra que esta buscando esta en el caracter: ",texto.find(n))

print("\nlas palabras en mayuscula: ", texto.upper())
print("\nlas palabras en minuscula: ",texto.lower())