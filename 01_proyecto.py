import random

try:
    N = int(input("Ingrese el tamaño de la matriz cuadrada: "))
    if N <= 0:
        raise ValueError("El tamaño debe ser un número entero positivo.")
except ValueError:
    print("ERROR: Debe ingresar un número entero positivo.")
    exit()

# Generación de la matriz
matriz = []
for i in range(N):
    fila = []
    for j in range(N):
        fila.append(random.randint(0, 9))
    matriz.append(fila)

# Imprimir la matriz
print("Matriz generada:")
for fila in matriz:
    print(fila)

# Calcular la suma de cada fila y columna
sumas_filas = []
sumas_columnas = []
for fila in matriz:
    suma_fila = sum(fila)
    sumas_filas.append(suma_fila)

for j in range(N):
    suma_columna = sum(matriz[i][j] for i in range(N))
    sumas_columnas.append(suma_columna)

# Imprimir la suma de cada fila y columna
print("Suma de cada fila:")
for i, suma_fila in enumerate(sumas_filas):
    print(f"Fila {i+1}: {suma_fila}")

print("Suma de cada columna:")
for j, suma_columna in enumerate(sumas_columnas):
    print(f"Columna {j+1}: {suma_columna}")


