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
            x1 = float(input('\nIngrese valor de desplazamiento en x e y (desde -100 a 100):\nValor de X: '))
            if not -100 < x1 < 100:
                print('\nPor favor ingrese un valor desde -100 a 100:')
            else:
                y1 = float(input('\nIngrese valor de desplazamiento en x e y(desde -100 a 100):\nValor de Y:'))
                if not -100 < y1 < 100:
                    print('\nPor favor ingrese un valor desde -100 a 100: ')
                else:
                    vector_desplazado = (x1,y1)
                    break

        while True:
            x = float(input('Ingrese valor de x (de -100 a 100): '))
            if not -100 < x < 100:
                print('\nPor favor ingrese valor desde -100 a 100: ')
            else:
                y = float(input('\nIngrese valor de y (de -100 a 100): '))
                if not -100 < y < 100:
                    print('\nPor favor ingrese un valor desde -100 a 100:')
                else:
                    angulo = float(input('\nIngrese un ángulo (de -360° a 360°): '))
                    if not -360 < angulo < 360:
                        print('\nPor favor ingrese un valor desde -360° a 360°: ')                  
                    else:
                        vector = (x,y)
                        matriz_rotada=matriz_rotacion_2d(angulo)
                        
                        break 
                    
        vector_desplazado = np.dot(vector, vector_desplazado)
        resultado = np.round(vector_desplazado*matriz_rotada)           
        #resultado = np.array(vector_desplazado,vector_rotado)
        print(f'\nEl resultado de desplazar a x={x} e y={y} a x1={x1} a y1={y1} y rotarlo a {angulo}° es: {resultado}')
        
    except ValueError:
        print('\nIngrese un valor válido.\n')
