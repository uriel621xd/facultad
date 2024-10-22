import matplotlib.pyplot as plt

def dibujar_vector(vector, color):
  # Crear una figura y un eje
  fig, ax = plt.subplots()

  # Establecer los límites de los ejes
  plt.xlim(-10, 10)
  plt.ylim(-10, 10)

  # Crear una grilla
  plt.grid(color='lightgray', linestyle='-', linewidth=0.5)

  # Dibujar el vector como una flecha
  plt.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color=color)

  # Mostrar la gráfica
  plt.show()

# Ejemplo de uso:
vector = (9, 1)
color = 'blue'
dibujar_vector(vector, color)