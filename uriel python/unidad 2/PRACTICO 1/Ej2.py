import numpy as np

def matriz_rotacion_2d(angulo):
  
  cos_theta = np.cos(angulo)
  sin_theta = np.sin(angulo)

  matriz_rotacion = np.array([[cos_theta, -sin_theta],
                             [sin_theta, cos_theta]])
  
  return matriz_rotacion


angulo = 50
# Ángulo de rotación en radianes
angulo = np.radians(angulo)
# Obtener la matriz de rotación
matriz_rotacion = matriz_rotacion_2d(angulo)

print(matriz_rotacion)