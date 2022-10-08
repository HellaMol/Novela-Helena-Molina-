

"""
========Contador tutorial========
"""
puntos_de_conexion = 0
def contador(respuesta):
    if(respuesta == "A"):
        eleccion = 2
    elif(respuesta == "B"):
        eleccion = -1
    return float(puntos_de_conexion + eleccion)

"""
========Contador Milo========
"""
puntos_de_conexion_milo = 0
def contador_milo(respuesta_milo):
    if(respuesta_milo == "A"):
        eleccion_milo = 2
    elif(respuesta == "B"):
        eleccion_milo = -1
    return float(puntos_de_conexion_milo + eleccion_milo)

"""
========Contador Eli========
"""
puntos_de_conexion_eli = 0
def contador_eli(respuesta_eli):
    while True:
        if(respuesta_eli == "A"):
            eleccion_eli = 2
        elif(respuesta_eli == "B"):
            eleccion_eli = -1
        return float(puntos_de_conexion_eli + eleccion_eli)

"""
========Contador Arath========
"""
puntos_de_conexion_arath = 0
def contador_arath(respuesta_arath):
    if(respuesta_arath == "A"):
        eleccion_arath = 2
    elif(respuesta_arath == "B"):
        eleccion_arath = -1
    return float(puntos_de_conexion_arath + eleccion_arath)

"""
========Contador Marisa========
"""
puntos_de_conexion_marisa = 0
def contador_marisa(respuesta_marisa):
    if(respuesta_marisa == "A"):
        eleccion_marisa = 2
    elif(respuesta_marisa == "B"):
        eleccion_marisa = -1
    return float(puntos_de_conexion_marisa + eleccion_marisa)
"""
========Inventario========
"""
Cosas_de_gamer = []
Cosas_de_artista = []
Cosas_de_nerd = []
Cosas_de_deportista = []
Inventario = [[Cosas_de_gamer],[Cosas_de_artista],[Cosas_de_nerd],[Cosas_de_deportista]]

def agregar_inventario_boost():
    if (respuesta_boost == "marcadores posca" or respuesta_boost == "computadora gamer" or respuesta_boost == "libro desgastado de Freud" or respuesta_boost == "almohada de ajolote"):
        Inventario.append(respuesta_boost)
        return Inventario
    
def agregar_inventario_item(respuesta_sn_item):
    if (respuesta_sn_item == "Sí"):
        respuesta_item = str(input("Escribe el nombre del objeto: "))
        if (respuesta_item == "audífonos de gatitos" or respuesta_item == "tarjeta STOM" or respuesta_item == "figura de acción"):
            if (respuesta_item not in Inventario):
                Cosas_de_gamer.append(respuesta_item) and items_totales.append(respuesta_item)
                print ("Se agregó al inventario")
                return Inventario
            else:
                print("No hagas trampa, ese objeto ya lo tienes -_-")
        elif (respuesta_item == "pincel de Bob Gross" or respuesta_item == "tableta Wecom" or respuesta_item == "CD inspirador"):
            if (respuesta_item not in Inventario):
                Cosas_de_artista.append(respuesta_item) and items_totales.append(respuesta_item)
                print ("Se agregó al inventario")
                return Inventario
            else:
                print("No hagas trampa, ese objeto ya lo tienes -_-")
        elif (respuesta_item == "libro de existencialismo" or respuesta_item == "sudoku" or respuesta_item == "1001 ensayos sobre la psicosis"):
            if (respuesta_item not in Inventario):
                Cosas_de_nerd.append(respuesta_item) and items_totales.append(respuesta_item)
                print ("Se agregó al inventario")
                return Inventario
            else:
                print("No hagas trampa, ese objeto ya lo tienes -_-")
        elif (respuesta_item == "tapete de yoga" or respuesta_item == "revista" or respuesta_item == "powerace"):
            if (respuesta_item not in Inventario):
                Cosas_de_deportista.append(respuesta_item) and items_totales.append(respuesta_item)
                print ("Se agregó al inventario")
                return Inventario
            else:
                print("No hagas trampa, ese objeto ya lo tienes -_-")
    elif (respuesta_sn_item == "No"):
        print("De acuerdo")

"""
========Logro por conseguir todos los items========
"""

items_totales = []
def num_items(items_totales):
    cont = 0
    for respuesta_item in items_totales:
        cont = cont + 1
    return cont
    
def logro_completado():
    if num_items(items_totales) == 12:
        print("¡Felicidades, conseguiste todos los objetos del juego!")
    else:
        print("Bien jugado.")
"""
========Boost========
"""

def boost():
    if "marcadores posca" in inventario:
        return (puntos_de_conexion_milo + 2.25)
    elif "computadora gamer" in inventario:
        return (puntos_de_conexion_eli + 2.25)
    elif "libro desgastado de Freud" in inventario:
        return (puntos_de_conexion_arath + 2.25)
    elif "almohada de ajolote" in inventario:
        return (puntos_de_conexion_marisa + 2.25)

"""
========Elilge tu nombre========
"""

print("Elige tu nombre:")

n = str(input())

while True:
    print("Escribe tu pronombre:ella,él o elle")
    pronombre_jugador=input()
    if pronombre_jugador == "ella":
        y = "a"
        z = "la"
        f = "a"
        break
    elif pronombre_jugador == "él":
        y = "o"
        z = "el"
        v = "e"
        f = ""
        break
    elif pronombre_jugador == "elle":
        y = "x"
        f = "x"
        break
    else:
        print("Pronombres disponibles por el momento: él, ella, elle (lamento las molestias >_< )")
    continue

"""
========Tutorial========
"""

print("Hola %s ¿list%s para la aventura?\n"%(n,y))
print("Comencemos por lo básico. Tú eres %s, un%s estudiante de nuevo ingreso en la Universidad X. No conoces a nadie… aún."%(n,f))
print("Pero no te preocupes, esta es tu historia, tendrás el poder de elegir y fortalecer los vínculos que hagas.\n")
print("Mira, practiquemos un poco la toma decisiones.")
print("Supongamos que tu mejor amigo está triste,¿Qué harías para hacerlo sentirse mejor?\n")
print("A: Darle un abrazo para reconfortarlo. o B: Burlarte de sus sentimientos.")

respuesta = str(input())
print("Puntos de conexión:",contador(respuesta),"\n")

if puntos_de_conexion == -1:
    print("Oh no, eso no es lo que hace un%s buen%s amig%s. Tendrás que ser penalizad%.\n"%(f,y,y,y))

print("De acuerdo, intentémoslo de nuevo. Ahora la situación será diferente.")
print("Uno de tus compañeros de escuela no entiende la tarea y te pide ayuda. Tú...\n")
print("A: Lo ayudarías y resolverías todas las dudas que él tenga. o B: Lo ignorarías, no es tu problema.")

respuesta = str(input())
print("Puntos de conexión:",contador(respuesta),"\n")

if puntos_de_conexion > 0 :
    print("Veo que estás entendiendo de que va esto.¡Muy bien!\n")
if puntos_de_conexion < 0:
    print("Deberías plantearte en tomar cursos sobre relaciones interpersonales amig%s."%(y))

print("Cómo viste, en la vida tus decisiones importan, si eres bueno tus puntos de conexión subirán y cosas buenas pasarán...\n""De lo contrario, vivirás consecuencias catastróficas. No digas que no te lo advertí.\n")
print("¿No hay dudas? Perfecto. Que la diversión comience.\n")

"""
========Día 1========
"""
print("====Día 1====")
print("Es hoy, el primer día en la Universidad X.¿Qué llevarás contigo?")
print("(Recuerda que para asegurar un mejor funcionamiento debes copiar y pegar la respuesta o copiarla sin errores :D)")
print("Objetos: 1. computadora gamer, 2. marcadores posca, libro desgastado de Freud o almohada de ajolote.")

respuesta_boost = str(input())
agregar_inventario_boost()
print(Inventario)

print("Excelente decisión, cómo podrás ver arriba está tu inventario, podrás acceder a el en ciertos puntos de la historia y usar los objetos que encuentres.")
print("Ya estás en la Universidad X, una persona bajita se acerca a ti y te mira con ojos tímidos.\n""No puedes evitar sentir ternura")
print("Eli: Hola, ¿sabes dónde está el salón 6103? Soy nueva aquí y no tengo ni idea de dónde es mi clase.")
print("Es la personita más adorable que has visto. Llena de pecas y el cabello esponjado y ondulado. Claro que vas ayudarla, ¿no?")
print("A: Por supuesto que sí, no la culpo por no entender la rara enumeración de los salones. o B: No, no tengo tiempo que perder voy tarde a clases.")

respuesta = str(input())
print("Puntos de conexión:",contador(respuesta),"\n")

if respuesta == "A" :
    print("Le explicas a Eli que el primer número indica el número de edificio, el segundo señala el piso y los dos últimos el número de salón")
    print("Eli: ¡Muchas, muchas, muuuuuuuchaaas graciaaas! No tenía ni idea de que eras alguien tan amable <3.")
if respuesta == "B" :
    print("Te rehusas a explicarle a Eli y la ignoras friamente mientras te alejas con pasos largos para llegar a tiempo. Por suerte aún no es tarde para reconsiderar tus acciones.")

print("TU-RU-RU-RUUUUU, has encontrado audífonos de gatitos en tu camino a clase. ¿Quieres agregarlos a tu inventario?")

respuesta_sn_item = str(input("Sí o No: "))
print(agregar_inventario_item(respuesta_sn_item))

"""
========Día 2========
"""

"""
========Día 3========
"""

"""
========Día 4========
"""

"""
========Día 5 (Final)========
"""

#En este avance actualicé el inventario para hacerlo una lista anidada o matriz. Sobre funciones importantes me faltan poner ciclos while para cuando haya una respuesta incorrecta o no disponible al igual que una función para remover los items cuando estos se regalen a los personajes. Por otro lado, falta terminar de escribir la historia.
exit()