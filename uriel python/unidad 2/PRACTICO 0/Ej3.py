import numpy as np

primer_vector = np.random.rand(10)
primer_vector = np.round(primer_vector * 10)
componente_mas_alto = np.max(primer_vector)
indice = np.argmax(primer_vector)


segundo_vector = np.arange(0,10)
concatenado = np.concatenate((primer_vector,segundo_vector))
matriz_2x10 = concatenado.reshape(2,10)
print('\nVECTOR RANDOM:\n',primer_vector)
print('\nEL COMPONENTE MÁS ALTO DEL VECTOR RANDOM:\n',componente_mas_alto)
print('\nEL ÍNDICE DEL COMPONENTE MAS ALTO:\n',indice)
print('\nSEGUNDO VECTOR DESDE 0 A 9:\n',segundo_vector)
print('\nLOS DOS VECTORES CONCATENADOS:\n',concatenado)
print('\nMATRIZ DE 2x10:\n',matriz_2x10)