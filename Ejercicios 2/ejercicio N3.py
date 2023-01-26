print('Ingrese 2 numeros para saber cual es el mayor de ellos dos')
def operacion(a,b):
    if a>b:
        print(f'{a} es mayor que {b}')
    else:
        print(f'{b} es mayor que {a}')
m=int(input('primer numero: '))
n=int(input('segunto numero: '))
operacion(m,n)