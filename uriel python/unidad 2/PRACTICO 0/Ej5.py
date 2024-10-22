import numpy as np

matriz_2x3 = np.array([[1,2,3],
                   [4,5,6]])

matriz_3x2 = matriz_2x3.reshape(3,2)

matriz_2x3_transpuesta = matriz_2x3.transpose()

print('\nMatriz 2x3:\n',matriz_2x3)
print('\nMatriz 3x2:\n',matriz_3x2)
print('\nMatriz 2x3 transpuesta:\n',matriz_2x3_transpuesta)