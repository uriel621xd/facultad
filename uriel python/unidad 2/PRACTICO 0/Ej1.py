import numpy as np

vector = np.array([1,3,6])
matriz = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

print(f'\nSu vector es: {vector}')
print(f'\nEl shape del vector es:{vector.shape}')
print(f'\nSu matriz es: \n{matriz}')
print(f'\nEl shape de su matriz es:{(matriz.shape)}')

resultado = np.dot(vector,matriz)

print(f'\nEl resultado de la multiplicación del vector y la matriz es: {resultado}')
print(f'\nEl shape del resultado es: {resultado.shape}')