import matplotlib.pyplot as plt
import numpy as np

def matriz_rotacion_2d(angulo):
  angulo = np.radians(angulo)
  cos_theta = np.cos(angulo)
  sin_theta = np.sin(angulo)

  matriz_rotacion = np.array([[cos_theta, -sin_theta],
                              [sin_theta, cos_theta]])
  
  return matriz_rotacion

def dibujar_vector(vector, vector_rotado):
   # Crear una figura y un eje
  fig, ax = plt.subplots()

  # Establecer los límites de los ejes
  plt.xlim(-15, 15)
  plt.ylim(-15, 15)

  # Crear una grilla
  plt.grid(color='lightgray', linestyle='-', linewidth=0.5)

  # Dibujar el vector como una flecha
  plt.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='blue')
  plt.quiver(0, 0, vector_rotado[0], vector_rotado[1], angles='xy', scale_units='xy', scale=1, color='red')
  # Mostrar la gráfica
  plt.show()
  


print('### EJERCICIO 3 - Solicitar un vector y rotarlo x grados. Dibujar el vector de azul y el vector rotado de rojo.\n')

while True:
    try:
        x = float(input('Ingrese valor de x (de -10 a 10): '))
        while -10.0<= x <=10.0:
            y = float(input('\nIngrese valor de y (de -10 a 10): '))
            while -10.0<= y <=10.0:
                angulo = float(input('\nIngrese un ángulo (de -360° a 360°): '))
                while -360.00<= angulo <=360.00:
                    matriz_rotacion = matriz_rotacion_2d(angulo)
                    vector = (x,y)
                    vector_rotado = np.dot(matriz_rotacion,vector)
                    print('\nDibujando vectores...\nVector azul = Vector original\nVector rojo = Vector rotado')
                    dibujar_vector(vector,vector_rotado)
                    break
                else:
                    print('\nPor favor ingrese un valor desde -360° a 360°: ')
            else:
                print('\nPor favor ingrese un valor desde -10 a 10: ')
        else:
            print('\nPor favor ingrese un valor desde -10 a 10: ')    
          
        
    except ValueError:
        print('\nPor favor ingrese un valor válido.\n')