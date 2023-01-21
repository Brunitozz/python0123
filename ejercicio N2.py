biblioteca={
    "categoria": ["Novela","Novela","Novela rosa","Terror","Tragedia","Epico","Novela","Novela","Realismo","Novela",],
    "titulo": ["Las mil y una noches","Don Quijote de la Mancha","Orgullo y prejuicio","Frankenstein o el moderno Prometeo","Cumbres borrascosas","Moby Dick","Grandes esperanzas","Mujercitas","Madame Bovary","Crimen y castigo",],
    "autor": ["anonimo","Miguel de Cervantes","Jane Austen","Mary Shelley","Emily Bronte","Herman Melville","Charles Dickens","Louisa May Alcott","Gustave Flaubert","Fiodor Dostoyevski",],
    "estado": ["prestado","prestado","prestado","disponible","disponible","disponible","disponible","prestado","disponible","disponible",],
    "usuarios":["Juanito","Maria del Barrio","fulano sultano" ]
}
print("""Buenos días, bienvenido a la biblioteca 'libros para piTUCOS del perú' ¿que desea realizar?
    a) Revisar el catalogo de la libreria y su estado
    b) Consultar la los generos
    c) Ver la relación de usuarios
    d) inscribirse a la biblioteca""")
while True:
    opcion=input("elija una opcion: ")
    if opcion=="a":
        while True:
            print("\nLos libros siguientes con su titulo y su estado: ")
            for i in range(10):
                print(i,biblioteca["titulo"][i] +" ("+ biblioteca["estado"][i]+")")
            opinion=int(input("\ncual desea leer? escribalo con su respectivo numero: "))
            if biblioteca["estado"][opinion]=="prestado":
                print("\n ELIJA UNO QUE ESTE DISPONIBLE!!!!")
            elif biblioteca["estado"][opinion]=="disponible":
                biblioteca["estado"][opinion]="prestado"
                print("gracias por elegirnos\n")
                for a in range(10): 
                    print(f'{a} {biblioteca["titulo"][a]} ({biblioteca["estado"][a]}) ')
                break
            else:
                print("ingrese un numero correcto")
    elif opcion=="b":
        print("\ntenemos los siguientes generos con su respectivo titulo: ")
        for i in range(10):
            print(i,biblioteca["titulo"][i] +" ("+ biblioteca["categoria"][i]+")"+" ("+ biblioteca["estado"][i]+")")
    elif opcion=="c":
        print("\naqui los siguientes usuarios: ")
        for i in range(len(biblioteca["usuarios"])):
            print(i,biblioteca["usuarios"][i])
    elif opcion=="d":
        m=input("Escriba su apodo por aqui:\n")
        biblioteca["usuarios"].append(m)
        print("registrado con exito!!!")
        for i in range(len(biblioteca["usuarios"])):
            print(i, biblioteca["usuarios"][i])
        break
    else:
        print("CARACTER INCORRECTO!!!!!!!!!!")



