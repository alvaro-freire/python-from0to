import numpy as np

# Matriz a partir de lista de listas.
mat1 = np.array([[2.3, 5.1],
                [8.1, 1.4]])

print("\nMatriz a partir de listas.\n", mat1)

# Matriz a partir de funciones de Numpy.
mat2 = np.zeros((2, 2))
print("\nMatriz a partir de funciones de Numpy.\n", mat2)

# Matriz a partir de tabla de datos.
iris = np.loadtxt('./iris.csv', skiprows=1, delimiter=',')
print("\nMatriz a partir de archivo de datos.\n", iris.shape)

# Calculamos la media para todos los valores.
print(np.mean(iris[:5, :]))

# Calculamos la media para todas las columnas.
print(np.mean(iris, axis=0))

X = iris[:, :4]
Y = iris[:, 4]

print(type(X), X.shape)
print(type(Y), Y.shape)

# Añade una nueva dimensión en el eje de las columas.
print(Y[:, np.newaxis].shape)

# Cambiamos la forma de la matriz para que tenga una segunda dimensión.
print(Y.reshape(len(Y), 1).shape)

# Añade una dimensión al eje que indiquemos.
print(np.expand_dims(Y, axis=1).shape)

# E incluso podemos evitar perder la segunda dimensión al crear la matriz Y si en vez de s
# la columna con un único índice, lo hacemos como rango.
print(iris[:, 4].shape)
print(iris[:, 4:5].shape)