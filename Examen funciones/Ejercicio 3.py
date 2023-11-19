
import random

def juegoAdivinar():
    aleatorio = random.randint (1,100)
    adivina = None
    intentos = 0


    print('----- Inicia el juego ----')

    while adivina != aleatorio:
        adivina = int(input('Ingresa un número: '))
        if adivina < aleatorio:
            print('Demasiado bajo')
        else:
            print('Demasiado alto')
            
        intentos += 1 
    
    print(f'Ganaste - Tu número de intentos fueron:  {intentos}')
       
juegoAdivinar()