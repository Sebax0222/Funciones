    
def suma_enteros(numero):
    sumaEntero = 0
    
    for x in range(2, numero + 1, 2):
        sumaEntero += x
    return sumaEntero
     
print(suma_enteros(5))