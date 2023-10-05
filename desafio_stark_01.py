""" Luego de analizar el set de datos correspondiente resolver el Desafío #01:

A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
fuerza (MÁXIMO)
C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
(MÍNIMO)
D. Recorrer la lista y determinar el peso promedio de los superhéroes
masculinos (PROMEDIO)
E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
género) los cuales su fuerza supere a la fuerza promedio de todas las
superhéroes de género femenino
NOTA: Se debe construir un menú en el que se sea posible acceder a cada una de
las opciones (A-E) """

from data_stark import lista_personajes

while True:
    print('Menu de opciones')
    print('Opcion A - Imprimir los datos de cada superheroe.')
    print('Opcion B - Mostrar peso del superheroe con mayor fuerza.')
    print('Opcion C - Mostrar nombre e identidad del superheroe mas bajo.')
    print('Opcion D - Mostrar promedio del peso de los superheroes masculinos.')
    print('Opcion E - Mostrar nombre y peso que supere la fuerza promedio de las superheroes de genero femenino. ')
    print('Opcion F - Salir.')

    respuesta = input('Ingrese la opcion deseada: ').upper()

    if respuesta == "A":
        contador = 0
        for personaje in lista_personajes:
            contador += 1
            print(f'Personaje n° {contador}\n{personaje}\n')
    elif respuesta == "B":
        fuerza_max = None
        for personaje in lista_personajes:
            identidad = personaje['identidad']
            peso = round(float(personaje['peso']), 1)
            fuerza = int(personaje['fuerza'])
            if fuerza_max == None or fuerza > fuerza_max:
                fuerza_max = fuerza
                peso_identidad_max = f'la identidad del mas fuerte es: {identidad}, y su peso es: {peso} Kg. '

        print(peso_identidad_max)
    elif respuesta == "C":
        altura_min = None
        for personaje in lista_personajes:
            identidad = personaje['identidad']
            nombre = personaje['nombre']
            altura = round(float(personaje['altura']))
            if altura_min == None or altura < altura_min:
                altura_min = altura
                nombre_identidad_min = f'El nombre del heroe mas bajo es {nombre} y su identidad es {identidad} '
        print(nombre_identidad_min)

    elif respuesta == "D":
        # D
        contador = 0
        acumulador_peso = 0
        for personaje in lista_personajes:
            contador += 1
            peso = round(float(personaje['peso']), 1)
            acumulador_peso += peso
        promedio_peso = acumulador_peso / contador
        mensaje = f'La suma de los pesos es {round(acumulador_peso,1)} Kg. Hay {contador} heroes.\nel promedio es: {round(promedio_peso ,1)} Kg.'
        print(mensaje)
    elif respuesta == "E":
        # E.
        promedio_fuerza_f = 0
        acumulador_fuerza_f = 0
        contador_heroe_f = 0
        for personaje in lista_personajes:
            nombre = personaje['nombre']
            peso = round(float(personaje['peso']), 1)
            fuerza = int(personaje['fuerza'])
            genero = personaje['genero']
            if genero == 'F':
                contador_heroe_f += 1
                acumulador_fuerza_f = acumulador_fuerza_f + fuerza
                promedio_fuerza_f = acumulador_fuerza_f / contador_heroe_f
            if fuerza > promedio_fuerza_f:
                nombre_mas_fuertes = nombre
                peso_mas_fuerte = peso
                print(
                    f'Nombre: {nombre_mas_fuertes} , peso: {peso_mas_fuerte} kg.')
    elif respuesta == "F":
        break
