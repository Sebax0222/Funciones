def puntaciones(puntuacion):

        if puntuacion >= 90:
            print('Sobresaliente')
        elif puntuacion >= 80 and puntuacion <= 89:
            print('Bueno')
        elif puntuacion >= 70 and puntuacion <= 79:
            print('Satisfactorio')
        elif puntuacion >= 60 and puntuacion <= 69:
            print('Necesita mejorar')
        else:
            print('Reprobado')

print(puntaciones(90))