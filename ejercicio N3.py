def operacion():
    print('Ingrese 2 numeros para saber cual es el mayor de ellos dos')
    num1=int(input('primer numero: '))
    num2=int(input('segunto numero: '))
    if num1>num2:
        print(f'{num1} es mayor que {num2}')
    else:
        print(f'{num2} es mayor que {num1}')
operacion()