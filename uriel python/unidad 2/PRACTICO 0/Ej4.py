import numpy as np

matriz_entrada_4x3 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

C1_F1 = matriz_entrada_4x3[0,0] #lo que contenga el lugar del número 1
C2_F1 = matriz_entrada_4x3[2,2]+matriz_entrada_4x3[3,2] #lo que contenga la suma del lugar n° 9 + n°12
C1_F2 = matriz_entrada_4x3[1,1] #lo que contenga el lugar del número 5
C2_F2 = matriz_entrada_4x3[3,0]*matriz_entrada_4x3[3,1]*matriz_entrada_4x3[3,2] #lo que contenga la multiplicación de todo lo que está en la última fila

vector = np.array([C1_F1,C2_F1,C1_F2,C2_F2])

matriz_salida_2x2 = vector.reshape(2,2)

print('Su matriz de 2x2 es:\n',matriz_salida_2x2)