print('lista de 15 personas con sus respectivas edades: ')
personas=[["Ezequiel",4],["Claudia",19],["Norma",6],["Liliana",7],["Víctor",12],['Liliana',10],["Mirta",18],["Ricardo",14],["Carlos",8],["Juana",3],["Nicolás",6],["Silvia",18],["Claudio",20],["Sergio",5],["Martín",7]]
print(personas)
for i in range(14):
    if personas[i][1]>=18:
        print(f'{personas[i][0]} es mayor de edad')
