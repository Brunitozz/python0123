def ejericio2():
    texto="""Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.
    Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un
    impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos
    y los mezcló de tal manera que logró hacer un libro de textos especimen."""

    print("texto separado por el '' (espacio):\n")
    print(texto.split(sep=" "))
    print("\ntexto unido por el '' (espacio):\n")
    print(" ".join(texto))
    m=input("\n¿que palabra o letra desea contar?: ")
    print(texto.count(m))
    n=input("que palabra desea buscar?: ")
    print("la palabra que esta buscando esta en el caracter: ",texto.find(n))

    print("\nLAS PALABRAS EN MAYUSCULA: ", texto.upper())
    print("\nLAS PALABRAS EN MINUSCULA: ",texto.lower())
    return
