biblioteca={
    "categoria": ["Novela","Novela","Novela rosa","Terror","Tragedia","Epico","Novela","Novela","Realismo","Novela",],
    "titulo": ["Las mil y una noches","Don Quijote de la Mancha","Orgullo y prejuicio","Frankenstein o el moderno Prometeo","Cumbres borrascosas","Moby Dick","Grandes esperanzas","Mujercitas","Madame Bovary","Crimen y castigo",],
    "autor": ["anonimo","Miguel de Cervantes","Jane Austen","Mary Shelley","Emily Bronte","Herman Melville","Charles Dickens","Louisa May Alcott","Gustave Flaubert","Fiodor Dostoyevski",],
    "estado": ["prestado","prestado","prestado","disponible","disponible","disponible","disponible","prestado","disponible","disponible",]
}
print("""Buenos días, bienvenido a la biblioteca 'libros para piTUCOS del perú' ¿que desea realizar?
    a) Revisar el catalogo de la libreria y su estado
    b) Consultar la los generos
    c) Ver la relación de usuarios
    d) inscribirse a la biblioteca""")
opcion=input("elija una opcion: ")
if opcion=="a":
       print(f'te ofrecemos {biblioteca[0]}')


