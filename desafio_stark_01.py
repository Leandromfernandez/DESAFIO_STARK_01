""" Luego de analizar el set de datos correspondiente resolver el Desafío #01:

A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe

B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO).

C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO).

D. Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)-

E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio 
de todas las superhéroes de género femenino.

NOTA: Se debe construir un menú en el que se sea posible acceder a cada una de las opciones (A-E) """

from data_stark import lista_personajes

#A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
for personaje in lista_personajes:
    nombre_personajes = personaje['nombre']
    identidad_personaje = personaje['identidad']
    empresa_personaje = personaje['empresa']
    altura_personaje = float(personaje['altura'])
    peso_personaje = float(personaje['peso'])
    genero_personaje = personaje['genero']
    color_ojos_personaje = personaje['color_ojos']
    color_pelo_personaje = personaje['color_pelo']
    fuerza_personaje = personaje['fuerza']
    inteligencia_personaje = personaje['inteligencia']
                                  
    print(f'nombre: {nombre_personajes}\nidentidad: {identidad_personaje}\nempresa: {empresa_personaje}\naltura: {altura_personaje} Cm.\npeso: {peso_personaje} kg.\ngenero: {genero_personaje}\ncolor de ojos: {color_ojos_personaje}\ncolor de pelo: {color_pelo_personaje}\nfuerza: {fuerza_personaje}\ninteligencia: {inteligencia_personaje}\n')
    
 
#B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO).
peso_max = None
for personaje in lista_personajes:
    identidad = personaje['identidad']
    peso = personaje['peso']
    peso = float(peso)
    if peso_max == None or peso > peso_max:
        peso_max = peso
        nombre_peso_max = personaje['nombre']

#C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO).
altura_min = None
for personaje in lista_personajes:
    identidad = personaje['identidad']
    nombre = personaje['nombre']
    altura = float(personaje['altura'])
    altura = round(altura ,1)
    if altura_min == None or altura < altura_min:
        altura_min = altura
        identidad_altura_min = personaje['identidad']
        nombre_altura_min = personaje['nombre']

#D. Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)-
acumuluador_peso_masculino = 0
contador_masculino = 0
for personaje in lista_personajes:
    if personaje['genero'] == "M":
        contador_masculino += 1
        peso = round(float(personaje['peso']) , 2)
        acumuluador_peso_masculino = acumuluador_peso_masculino + peso
        promedio_peso_masculino = acumuluador_peso_masculino / contador_masculino

#E.Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) 
# los cuales su fuerza supere a la fuerza promedio 
# de todas las superhéroes de género femenino.
contador_femenino = 0
acumuluador_fuerza_femenina = 0

for personaje in lista_personajes: 
    if personaje['genero'] == "F":
        contador_femenino += 1
        fuerza_femenina = int(personaje['fuerza'])
        acumuluador_fuerza_femenina += fuerza_femenina
        promedio_fuerza_femenino = acumuluador_fuerza_femenina / contador_femenino
    if int(personaje['fuerza']) > promedio_fuerza_femenino:
        print(f'el nombre es {personaje["nombre"]} y su peso: {personaje["peso"]} Kg.')

print(f'promedio fuerza femenina: {promedio_fuerza_femenino}')





        






print(f'El mas pesado es {nombre_peso_max} y pesa: {peso_max} Kg.')
print(f'El nombre del mas bajo es {nombre_altura_min}, su identidad es {identidad_altura_min} y mide: {altura_min} Cm.' )
print(f'El promedio del peso de los masculinos es: {promedio_peso_masculino} Kg.')

  