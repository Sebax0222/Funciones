# 1-sumaDeElementosEnUnaLista
# def suma_de_numeros(numeros):
#     suma = 0
#     for numero in numeros:
#         suma += numero 
#     return suma
    
# lista_de_numeros = [1, 2, 3, 4, 5]
# total = suma_de_numeros(lista_de_numeros)

# print("La suma de la lista de números es : ", total)

# 2-VerificarParidad

# def par_impar(numero):
#     if numero % 2 == 0:
#         print("par")
#     else:
#         print("impar")
        
# numero = 6
# resultado = par_impar(numero)

# 3-Diccionario para estudiantes

# estudiantes = {}

# def agregar_estudiante(nombre, edad, calificaciones):
#     estudiantes[nombre] = {'edad': edad, 'calificaciones': calificaciones}
#     print(f"Estudiante {nombre} agregado con éxito.")

# def eliminar_estudiante(nombre):
#     if nombre in estudiantes:
#         del estudiantes[nombre]
#         print(f"Estudiante {nombre} eliminado con éxito.")
#     else:
#         print(f"No se encontró al estudiante {nombre}.")

# def mostrar_informacion_estudiante(nombre):
#     if nombre in estudiantes:
#         info_estudiante = estudiantes[nombre]
#         print(f"Información del estudiante {nombre}:")
#         print(f"Edad: {info_estudiante['edad']}")
#         print(f"Calificaciones: {info_estudiante['calificaciones']}")
#     else:
#         print(f"No se encontró al estudiante {nombre}.")

# agregar_estudiante("Juan", 20, [90, 85, 95])
# agregar_estudiante("María", 22, [88, 92, 89])
# mostrar_informacion_estudiante("Juan")

# eliminar_estudiante("Pedro")
# mostrar_informacion_estudiante("Pedro")


# 4- Invertir una lista

# def invertir_lista(lista):
#     # Opción 1: Utilizando el método reverse()
#     # lista.reverse()

#     # Opción 2: Utilizando la técnica de rebanado [::-1]
#     lista = lista[::-1]

#     return lista

# # Ejemplo de uso
# mi_lista = [1, 2, 3, 4, 5]
# lista_invertida = invertir_lista(mi_lista)

# print("Lista original:", mi_lista)
# print("Lista invertida:", lista_invertida)

# 5- Validacion de parentesis

# def paréntesis_balanceados(cadena):
#     pila = []
#     paréntesis = {')': '(', '}': '{', ']': '['}

#     for carácter in cadena:
#         if carácter in paréntesis.values():
#             pila.append(carácter)
#         elif carácter in paréntesis.keys():
#             if not pila or pila.pop() != paréntesis[carácter]:
#                 return False

#     return not pila

# cadena1 = "({[()]})"
# cadena2 = "({[()]}"
# cadena3 = "({[()]}"

# print(paréntesis_balanceados(cadena1))  
# print(paréntesis_balanceados(cadena2))  
# print(paréntesis_balanceados(cadena3))  

# 6- Cola de tareas

# class ColaDeTareas:
#     def __init__(self):
#         self.tareas = []

#     def agregar_tarea(self, tarea):
#         self.tareas.append(tarea)
#         print(f"Tarea '{tarea}' agregada a la cola.")

#     def eliminar_tarea_mas_antigua(self):
#         if self.tareas:
#             tarea_eliminada = self.tareas.pop(0)
#             print(f"Tarea '{tarea_eliminada}' eliminada.")
#         else:
#             print("La cola de tareas está vacía.")

#     def mostrar_tareas(self):
#         print("Cola de tareas:", self.tareas)


# # Ejemplo de uso
# cola_tareas = ColaDeTareas()

# cola_tareas.agregar_tarea("Hacer la compra")
# cola_tareas.agregar_tarea("Estudiar para el examen")
# cola_tareas.agregar_tarea("Preparar la presentación")

# cola_tareas.mostrar_tareas()

# cola_tareas.eliminar_tarea_mas_antigua()
# cola_tareas.mostrar_tareas()

# cola_tareas.eliminar_tarea_mas_antigua()
# cola_tareas.mostrar_tareas()


#7 - Contar Elementos unicos

# def contar_elementos_unicos(lista):
#     # Utiliza un conjunto para almacenar elementos únicos
#     elementos_unicos = set(lista)
#     # Devuelve la cantidad de elementos únicos
#     return len(elementos_unicos)

# # Ejemplo de uso
# mi_lista = [1, 2, 3, 4, 2, 3, 5, 6, 7, 7, 8]
# cantidad_unicos = contar_elementos_unicos(mi_lista)

# print(f"La lista {mi_lista} tiene {cantidad_unicos} elementos únicos.")

#8 - Comprobación de Palíndromos

# def es_palindromo(palabra):
#     # Elimina los espacios en blanco y convierte a minúsculas para hacer la comparación más robusta
#     palabra = palabra.replace(" ", "").lower()
#     # Compara la palabra con su versión invertida
#     return palabra == palabra[::-1]

# # Ejemplo de uso
# palabra1 = "reconocer"
# palabra2 = "python"

# print(f"'{palabra1}' es un palíndromo: {es_palindromo(palabra1)}")
# print(f"'{palabra2}' es un palíndromo: {es_palindromo(palabra2)}")

# 9- Pila de historial de navegación

# class HistorialNavegacion:
#     def __init__(self):
#         self.pila_paginas = []

#     def agregar_pagina(self, pagina):
#         self.pila_paginas.append(pagina)
#         print(f"Se agregó la página '{pagina}' al historial.")

#     def retroceder_pagina(self):
#         if len(self.pila_paginas) > 1:
#             pagina_actual = self.pila_paginas.pop()
#             pagina_anterior = self.pila_paginas[-1]
#             print(f"Retrocediendo de '{pagina_actual}' a '{pagina_anterior}'.")
#         else:
#             print("No hay páginas anteriores en el historial.")

#     def mostrar_historial(self):
#         print("Historial de navegación:", self.pila_paginas)


# # Ejemplo de uso
# historial = HistorialNavegacion()

# historial.agregar_pagina("www.ejemplo1.com")
# historial.agregar_pagina("www.ejemplo2.com")
# historial.agregar_pagina("www.ejemplo3.com")

# historial.mostrar_historial()

# historial.retroceder_pagina()
# historial.mostrar_historial()

# historial.retroceder_pagina()
# historial.mostrar_historial()

# 10- Diccionario de frecuencia

# def frecuencia_elementos(lista):
#     diccionario_frecuencia = {}

#     for elemento in lista:
#         # Incrementa la frecuencia si el elemento ya está en el diccionario, o crea una nueva entrada
#         diccionario_frecuencia[elemento] = diccionario_frecuencia.get(elemento, 0) + 1

#     return diccionario_frecuencia

# # Ejemplo de uso
# mi_lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# resultado = frecuencia_elementos(mi_lista)

# print("Lista:", mi_lista)
# print("Frecuencia de elementos:", resultado)


# 11- Multiplicacion de matrices 

# def multiplicar_matrices(matriz1, matriz2):
#     # Verifica si las matrices son multiplicables
#     if len(matriz1[0]) != len(matriz2):
#         raise ValueError("Las matrices no son multiplicables debido a dimensiones incompatibles.")

#     # Inicializa la matriz resultante con ceros
#     resultado = [[0 for _ in range(len(matriz2[0]))] for _ in range(len(matriz1))]

#     # Realiza la multiplicación de matrices
#     for i in range(len(matriz1)):
#         for j in range(len(matriz2[0])):
#             for k in range(len(matriz2)):
#                 resultado[i][j] += matriz1[i][k] * matriz2[k][j]

#     return resultado

# # Ejemplo de uso
# matriz_A = [[1, 2, 3], [4, 5, 6]]
# matriz_B = [[7, 8], [9, 10], [11, 12]]

# resultado_multiplicacion = multiplicar_matrices(matriz_A, matriz_B)

# print("Matriz A:")
# for fila in matriz_A:
#     print(fila)

# print("\nMatriz B:")
# for fila in matriz_B:
#     print(fila)

# print("\nResultado de la multiplicación:")
# for fila in resultado_multiplicacion:
#     print(fila)

# 12- Ordenar una lista de palabras

# def ordenar_alfabeticamente(lista_palabras):
#     return sorted(lista_palabras)

# # Ejemplo de uso
# mi_lista = ["manzana", "pera", "banana", "uva", "kiwi"]
# lista_ordenada = ordenar_alfabeticamente(mi_lista)

# print("Lista original:", mi_lista)
# print("Lista ordenada alfabéticamente:", lista_ordenada)

# 13- Verificacion de numeros primos

# def es_primo(numero):
#     # Verifica si el número es menor o igual a 1 (los números primos son mayores que 1)
#     if numero <= 1:
#         return False
#     # Verifica si el número es divisible por algún número entre 2 y la raíz cuadrada del número + 1
#     for i in range(2, int(numero**0.5) + 1):
#         if numero % i == 0:
#             return False
#     # Si no se encontraron divisores, el número es primo
#     return True

# # Ejemplo de uso
# numero1 = 17
# numero2 = 4

# print(f"{numero1} es primo: {es_primo(numero1)}")
# print(f"{numero2} es primo: {es_primo(numero2)}")

# 14- Calculadora con operaciones basicas

# def suma(a, b):
#     return a + b

# def resta(a, b):
#     return a - b

# def multiplicacion(a, b):
#     return a * b

# def division(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Error: No se puede dividir entre cero."

# # Función principal para realizar la operación seleccionada
# def calcular(operacion, a, b):
#     if operacion == "suma":
#         return suma(a, b)
#     elif operacion == "resta":
#         return resta(a, b)
#     elif operacion == "multiplicacion":
#         return multiplicacion(a, b)
#     elif operacion == "division":
#         return division(a, b)
#     else:
#         return "Operación no válida."

# # Ejemplo de uso
# num1 = 10
# num2 = 5

# # Suma
# resultado_suma = calcular("suma", num1, num2)
# print(f"Suma: {num1} + {num2} = {resultado_suma}")

# # Resta
# resultado_resta = calcular("resta", num1, num2)
# print(f"Resta: {num1} - {num2} = {resultado_resta}")

# # Multiplicación
# resultado_multiplicacion = calcular("multiplicacion", num1, num2)
# print(f"Multiplicación: {num1} * {num2} = {resultado_multiplicacion}")

# # División
# resultado_division = calcular("division", num1, num2)
# print(f"División: {num1} / {num2} = {resultado_division}")

# 15- Conversion de unidades

# def km_a_millas(kilometros):
#     # Factor de conversión de kilómetros a millas
#     factor_conversion = 0.621371
#     return kilometros * factor_conversion

# def millas_a_km(millas):
#     # Factor de conversión de millas a kilómetros
#     factor_conversion = 1.60934
#     return millas * factor_conversion

# def celsius_a_fahrenheit(celsius):
#     # Fórmula de conversión de Celsius a Fahrenheit
#     return (celsius * 9/5) + 32

# def fahrenheit_a_celsius(fahrenheit):
#     # Fórmula de conversión de Fahrenheit a Celsius
#     return (fahrenheit - 32) * 5/9

# # Ejemplo de uso
# distancia_km = 10
# temperatura_celsius = 25

# # Conversión de kilómetros a millas
# distancia_millas = km_a_millas(distancia_km)
# print(f"{distancia_km} kilómetros es igual a {distancia_millas:.2f} millas")

# # Conversión de millas a kilómetros
# distancia_km_nueva = millas_a_km(distancia_millas)
# print(f"{distancia_millas} millas es igual a {distancia_km_nueva:.2f} kilómetros")

# # Conversión de Celsius a Fahrenheit
# temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
# print(f"{temperatura_celsius} grados Celsius es igual a {temperatura_fahrenheit:.2f} grados Fahrenheit")

# # Conversión de Fahrenheit a Celsius
# temperatura_celsius_nueva = fahrenheit_a_celsius(temperatura_fahrenheit)
# print(f"{temperatura_fahrenheit} grados Fahrenheit es igual a {temperatura_celsius_nueva:.2f} grados Celsius")