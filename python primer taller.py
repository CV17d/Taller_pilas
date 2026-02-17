# 1. Declaración e inicialización
# a. Lista unidimensional de tamaño 5
lista_uni = ["Python", "Java", "C++", "JavaScript", "PHP"]

# b. Lista bidimensional de tamaño 3x3
lista_bi = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# ---------------------------------------------------------
# 2. Acceso a elementos
# a. Segundo elemento del array unidimensional (índice 1)
print(f"Segundo elemento (1a): {lista_uni[1]}")

# b. Elemento de la segunda fila y segunda columna (índice [1][1])
print(f"Elemento fila 2, col 2 (1b): {lista_bi[1][1]}")

# ---------------------------------------------------------
# 3. Inserción y eliminación
# a. Insertar "Estructura de datos" en la posición 3
# Nota: insert(índice, valor). La posición 3 es el índice 3.
lista_uni.insert(3, "Estructura de datos")
print(f"Lista uni tras inserción: {lista_uni}")

# b. Eliminar el elemento de la tercera fila y tercera columna
# Usamos 'del' o pop() en los índices [2][2]
valor_eliminado = lista_bi[2].pop(2)
print(f"Lista bi tras eliminar {valor_eliminado} en [2][2]: {lista_bi}")

# ---------------------------------------------------------
# 4. Búsqueda de elementos
# a. Buscar "Estructura de datos" y devolver su índice
indice_uni = lista_uni.index("Estructura de datos")
print(f"Índice de 'Estructura de datos': {indice_uni}")

# b. Buscar un valor en la segunda fila (lista_bi[1]) y devolver su índice
valor_a_buscar = 50
indice_bi = lista_bi[1].index(valor_a_buscar)
print(f"El valor {valor_a_buscar} en la fila 2 está en la columna (índice): {indice_bi}")
