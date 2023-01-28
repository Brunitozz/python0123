def direccion():
    import os
    print(os.path.splitext(os.path.basename(__file__))[0])
    
