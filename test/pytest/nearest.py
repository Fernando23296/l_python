def nearest_square(num):
    '''
    Retorna el valor cuadrado mas cercano 
    que es menor o igual que el numero.
    '''
    root = 0
    while (root + 1) ** 2 <=num:
        root += 1
    return root ** 2