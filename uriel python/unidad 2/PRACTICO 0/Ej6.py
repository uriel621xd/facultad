import numpy as np

vector = np.arange(24)

num3 = vector[3] 
num7 = vector[7]
num13 = vector[13]
num23 = vector[23]

suma = num3 + num7 + num13 + num23

vector[3]=suma
vector[7]=suma
vector[13]=suma
vector[23]=suma

matriz = vector.reshape(2,4,3)

print(matriz)