import matplotlib.pyplot as plt
import numpy as np

def matriz_rotacion_2d(angulo):
  angulo = np.radians(angulo)
  cos_theta = np.cos(angulo)
  sin_theta = np.sin(angulo)

  matriz_rotacion = np.array([[cos_theta, -sin_theta],
                              [sin_theta, cos_theta]])
  
  return matriz_rotacion

while True:
    
    try:       
        
        while True:
            x = int(input('Ingrese valor de x (de -100 a 100): '))
            if not -100 < x < 100:
                print('\nPor favor ingrese valor desde -100 a 100: ')
            else:
                y = int(input('\nIngrese valor de y (de -100 a 100): '))
                if not -100 < y < 100:
                    print('\nPor favor ingrese un valor desde -100 a 100:')
                else:
                    angulo = int(input('\nIngrese un ángulo (de -360° a 360°): '))
                    if not -360 < angulo < 360:
                        print('\nPor favor ingrese un valor desde -360° a 360°: ')                  
                    else:
                        vector = (x,y)
                        matriz_rotada=matriz_rotacion_2d(angulo)
                        vector_rotado = np.dot(matriz_rotada,vector)
                        
                        break                        
                        
        while True:
            x1 = int(input('\nIngrese valor de desplazamiento en x e y (desde -100 a 100):\nValor de X: '))
            if not -100 < x1 < 100:
                print('\nPor favor ingrese un valor desde -100 a 100:')
            else:
                y1 = int(input('\nIngrese valor de desplazamiento en x e y(desde -100 a 100):\nValor de Y:'))
                if not -100 < y1 < 100:
                    print('\nPor favor ingrese un valor desde -100 a 100: ')
                else:
                    vector_desplazado = (x1,y1)
                    break
        
        resultado= np.round(vector_rotado+vector_desplazado)
        print(f'\nEl resultado de rotar x={x} e y={y} a un ángulo de {angulo}° y desplazarlo a x1={x1} e y1={y1} es: {resultado}')
            
    except ValueError:
        print('\nIngrese un valor válido.\n')
