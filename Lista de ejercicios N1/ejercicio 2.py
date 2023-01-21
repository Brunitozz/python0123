lista=[1,8,9,6,7,1,3,5,10,4,7]
print(f'la lista de numeros es la siguiente: {lista}')
for i in range(11):
    if lista[i]%2==0:
        print(f'el numero {lista[i]} es multiplo de 2')