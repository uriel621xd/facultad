import numpy as np

vector = np.arange(0,5.5,0.5)
matriz_ceros = np.zeros([4,4])
matriz_unos = np.ones([3,4])
matriz_identidad = np.identity(3)
matriz_random = np.random.rand(2,3)

print(f'\nMatriz de ceros: \n{matriz_ceros}')
print(f'\nMatriz de unos:\n{matriz_unos}')
print(f'\nMatriz de identidad: \n{matriz_identidad}')
print(f'\nMatriz random: \n{matriz_random}')
print(f'\nVector de 0 hasta 5 con saltos de 0.5: \n{vector}')
print(f'\nTamaño del vector: \n{len(vector)}')