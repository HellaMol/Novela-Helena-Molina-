

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
        eleccion = 2
    elif(respuesta == "B"):
        eleccion_milo = -1
    return float(puntos_de_conexion_milo + eleccion)

"""
========Contador Eli========
"""
puntos_de_conexion_eli = 0
def contador_eli(respuesta_eli):
    if(respuesta_eli == "A"):
        eleccion = 2
    elif(respuesta_eli == "B"):
        eleccion = -1
    return float(puntos_de_conexion_eli + eleccion)

"""
========Contador Arath========
"""
puntos_de_conexion_arath = 0
def contador_arath(respuesta_arath):
    if(respuesta_arath == "A"):
        eleccion = 2
    elif(respuesta_arath == "B"):
        eleccion = -1
    return float(puntos_de_conexion_arath + eleccion)

"""
========Contador Marisa========
"""
puntos_de_conexion_marisa = 0
def contador_marisa(respuesta_marisa):
    if(respuesta_marisa == "A"):
        eleccion = 2
    elif(respuesta_marisa == "B"):
        eleccion = -1
    return float(puntos_de_conexion_marisa + eleccion)
"""
========Inventario========
"""

inventario = []

def agregar_inventario_boost():
        inventario.append(respuesta_boost)
        return inventario
    
def agregar_inventario_item(respuesta_sn_item):
    if (respuesta_sn_item == "Sí"):
        inventario.append(respuesta_item) and respuesta_item.append(respuesta_item)
        print ("Se agregó al inventario")
        return inventario
    else:
        print("De acuerdo")

"""
========Inventario========
"""

items_totales = []
def num_items(items_totales):
    cont = 0
    for respuesta_item in items_totales:
        cont = cont + 1
    return cont
    

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
========Mapa========
"""



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
puntos_de_conexion = contador(respuesta)
print("Puntos de conexión:",puntos_de_conexion,"\n")

if puntos_de_conexion == -1:
    print("Oh no, eso no es lo que hace un%s buen%s amig%s. Tendrás que ser penalizado.\n"%(f,y,y))

print("De acuerdo, intentémoslo de nuevo. Ahora la situación será diferente.")
print("Uno de tus comañeros de escuela no entiende la tarea y te pide ayuda. Tú...\n")
print("A: Lo ayudarías y resolverías todas las dudas que el tenga. o B: Lo ignorarías, no es tu problema.")

respuesta = str(input())
puntos_de_conexion = contador(respuesta)
print("Puntos de conexión:",puntos_de_conexion,"\n")

if puntos_de_conexion > 0 :
    print("Veo que estás entendiendo de que va esto.¡Muy bien!\n")
if puntos_de_conexion < 0:
    print("Deberías plantearte en tomar cursos sobre relaciones interpersonales amig%s."%(y))

print("Cómo viste, en la vida tus decisiones importan, si eres bueno tus puntos de conexión subirán y cosas buenas pasarán...\n""De lo contrario, vivirás consecuencias catastróficas. No digas que no te lo advertí.\n")
print("¿No hay dudas? Perfecto. Que la diversión comience.\n")

"""
========Día 1========
"""

print("Es hoy, el primer día en la Universidad X.¿Qué llevarás contigo?")
print("Objetos: computadora gamer, marcadores posca, libro desgastado de Freud o almohada de ajolote.")

respuesta_boost = str(input())
agregar_inventario_boost()
print(inventario)

print("Excelente decisión, cómo podrás ver arriba está tu inventario, podrás acceder a el\n""(con una funcion que aún no existe) y usar los objetos que encuentres ")
print("Ya estás en la Universidad X, una persona bajita se acerca a ti y te mira con ojos tímidos.\n""No puedes evitar sentir ternura")

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

#En este avance terminé de escribir unas funciones, decidí ocupar un día por personaje para no alargar el proyecto, el quinto será donde se revela el final. Asimismo ya están presentes las listas, próximamente pondré listas anidadas. La historia la estoy escribiendo en un documento aparte
exit()