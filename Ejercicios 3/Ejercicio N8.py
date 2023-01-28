while (True):
    try:
        from ejercicion5.Division import division
        from ejercicion5.Suma import suma
        import os
        m=int(input('ingrese el primer numero: '))
        n=int(input('ingrese el segundo numero: '))
        suma(m,n)
        division(m,n)
    except Exception as e:
        print('Error =>',e)
    else:
        print('la ruta del directorio de trabajo',os.getcwd() )
    finally:
        print('el proceso ha terminado')
        break
    
    
        