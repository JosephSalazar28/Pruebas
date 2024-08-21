# Ejemplo de Listas
frutas = ["manzana", "banana", "cereza"]

# Acceder a un elemento de la lista
print("Lista - Elemento en la posición 1:", frutas[1])  # Imprime "banana"

# Añadir un nuevo elemento a la lista
frutas.append("naranja")
print("Lista después de añadir 'naranja':", frutas)  # Imprime ["manzana", "banana", "cereza", "naranja"]

# Eliminar un elemento de la lista
frutas.remove("cereza")
print("Lista después de eliminar 'cereza':", frutas)  # Imprime ["manzana", "banana", "naranja"]

# Modificar un elemento de la lista
frutas[0] = "pera"
print("Lista después de modificar el primer elemento:", frutas)  # Imprime ["pera", "banana", "naranja"]

# Ejemplo de Tuplas
colores = ("rojo", "verde", "azul")

# Acceder a un elemento de la tupla
print("\nTupla - Elemento en la posición 2:", colores[2])  # Imprime "azul"

# Desempaquetar una tupla
rojo, verde, azul = colores
print("Tupla desempaquetada - rojo:", rojo)  # Imprime "rojo"
print("Tupla desempaquetada - verde:", verde)  # Imprime "verde"
print("Tupla desempaquetada - azul:", azul)  # Imprime "azul"

# Ejemplo de Diccionarios
estudiante = {
    "nombre": "Juan",
    "edad": 21,
    "carrera": "Ingeniería"
}

# Acceder a un valor del diccionario usando su clave
print("\nDiccionario - Valor de la clave 'nombre':", estudiante["nombre"])  # Imprime "Juan"

# Añadir un nuevo par clave-valor
estudiante["universidad"] = "UDistrital"
print("Diccionario después de añadir 'universidad':", estudiante)  # Imprime {'nombre': 'Juan', 'edad': 21, 'carrera': 'Ingeniería', 'universidad': 'UNAM'}

# Modificar un valor existente
estudiante["edad"] = 22
print("Diccionario después de modificar 'edad':", estudiante)  # Imprime {'nombre': 'Juan', 'edad': 22, 'carrera': 'Ingeniería', 'universidad': 'UNAM'}

# Eliminar un par clave-valor
del estudiante["carrera"]
print("Diccionario después de eliminar 'carrera':", estudiante)  # Imprime {'nombre': 'Juan', 'edad': 22, 'universidad': 'UNAM'}
