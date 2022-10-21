from time import sleep
"""ISe importa la libreria de tiempo para usar la función de sleep"""

import sys
""" Se importar la libreria de sys,
donde se usara la función de flush"""


"""
========Funcion texto========
"""

"""Funcion para hacer aparecer el texto a determinada velocidad
obtenido de: https://es.stackoverflow.com/questions/25901/
como-imprimir-una-cadena-de-texto-con-pausas-entre-cada-
letra-impresa-en-python"""


def text(texto, speed):
    """
    Uso de biblioteca, uso de funciones que
    recibe: string de texto,velocidad de texto
    imprime cada letra segun la velocidad
    devuelve: texto impreso según la velocidad.
    """
    for c in texto:
        print(c, end='')
        sys.stdout.flush()
        sleep(speed)


"""
========Contador tutorial========
"""

puntos_de_conexion = 0


def contador(respuesta):
    """
    Funcion que recibe variable respuesta
    y dependiendo del string, regresa: variable
    puntos_de_conexion con un valor 2 o -1.
    """
    global puntos_de_conexion
    while respuesta != "A" and respuesta != "B":
        print("Escribe una respuesta disponible A o B:")
        respuesta = str(input())
    if (respuesta == "A"):
        eleccion = 2
        puntos_de_conexion = puntos_de_conexion + eleccion
        return float(puntos_de_conexion)
    elif (respuesta == "B"):
        eleccion = -1
        puntos_de_conexion = puntos_de_conexion + eleccion
        return float(puntos_de_conexion)


"""
========Contador Milo========
"""

puntos_de_conexion_milo = 0.0
eleccion_milo = 0.0


def contador_milo():
    """
    Funcion que solicita respuesta_milo
    y dependiendo del valor regresa: variable
    puntos_de_conexion_eli con un valor 2 o -1.
    """
    global puntos_de_conexion_milo
    global eleccion_milo
    respuesta_milo = str(input())
    if respuesta_milo != "A" and respuesta_milo != "B":
        print("Escribe una respuesta disponible A o B:")
        return contador_milo()
    elif (respuesta_milo == "A"):
        eleccion_milo = 2.0
        puntos_de_conexion_milo = puntos_de_conexion_milo + eleccion_milo
        return puntos_de_conexion_milo
    elif (respuesta_milo == "B"):
        eleccion_milo = -1.0
        puntos_de_conexion_milo = puntos_de_conexion_milo + eleccion_milo
        return puntos_de_conexion_milo


"""
========Contador Eli========
"""

puntos_de_conexion_eli = 0.0
eleccion_eli = 0.0


def contador_eli():
    """
    Funcion que solicita respuesta_eli
    y dependiendo del valor regresa: variable
    puntos_de_conexion_eli con un valor 2 o -1.
    """
    global puntos_de_conexion_eli
    global eleccion_eli
    respuesta_eli = str(input())
    if respuesta_eli != "A" and respuesta_eli != "B":
        print("Escribe una respuesta disponible A o B:")
        return contador_eli()
    elif (respuesta_eli == "A"):
        eleccion_eli = 2.0
        puntos_de_conexion_eli = puntos_de_conexion_eli + eleccion_eli
        return puntos_de_conexion_eli
    elif (respuesta_eli == "B"):
        eleccion_eli = -1.0
        puntos_de_conexion_eli = puntos_de_conexion_eli + eleccion_eli
        return puntos_de_conexion_eli


"""
========Inventario========
"""

cosas_de_gamer = []  # type: cosas_de_gamer[str]
cosas_de_artista = []  # type: cosas_de_artista[str]
inventario = [[cosas_de_gamer], [cosas_de_artista]]  # type: inventario[str]
items_totales = []


def agregar_inventario_boost(respuesta_boost):
    """
    Funcion que recibe variable respuesta_boost
    y dependiendo del string, se agrega a
    la lista inventario y regresa: la lista
    inventario con el string.
    """
    while respuesta_boost != "marcadores posca" and\
            respuesta_boost != "computadora gamer":
        print("""Objetos disponibles:
        computadora gamer o marcadores posca""")
        respuesta_boost = str(input())
    if (respuesta_boost == "marcadores posca" or
            respuesta_boost == "computadora gamer"):
        inventario.append(respuesta_boost)
        return inventario


def agregar_inventario_item(respuesta_sn_item):
    """
    Funcion que recibe variable respuesta_sn_item
    y dependiendo del string que se ingrese,
    no agrega respuesta_item al inventario y regresa
    texto string 'De acuerdo' o solicita designar
    el valor de respuesta_item y agrega
    respuesta_item al inventario y regresa lista
    inventario con el valor de respuesta_item.
    """
    while respuesta_sn_item != "Si" and respuesta_sn_item != "No":
        print("Escribe una respuesta disponible Si o No:")
        respuesta_sn_item = str(input())
    if (respuesta_sn_item == "Si"):
        respuesta_item = str(input("Escribe el nombre del objeto: "))
        while respuesta_item != "audifonos de gatito" and\
                respuesta_item != "tarjeta STOM" and\
                respuesta_item != "figura de accion" and\
                respuesta_item != "pincel de Bob Gross" and\
                respuesta_item != "tableta Wecom" and\
                respuesta_item != "CD inspirador":
            print("""Objeto inexistente o no disponible,
            por favor escribe correctamente el nombre del objeto:""")
            respuesta_item = str(input("Escribe el nombre del objeto: "))
        if (respuesta_item == "audifonos de gatito" or
                respuesta_item == "tarjeta STOM" or
                respuesta_item == "figura de accion"):
            if (respuesta_item not in inventario):
                cosas_de_gamer.append(respuesta_item)
                items_totales.append(respuesta_item)
                print("Se agrego al inventario")
                return inventario
            else:
                print("Ese objeto ya lo tienes -_-")
        elif (respuesta_item == "pincel de Bob Gross" or
                respuesta_item == "tableta Wecom" or
                respuesta_item == "CD inspirador"):
            if (respuesta_item not in inventario):
                cosas_de_artista.append(respuesta_item)
                items_totales.append(respuesta_item)
                print("Se agrego al inventario")
                return inventario
            else:
                print("Ese objeto ya lo tienes -_-")
    elif (respuesta_sn_item == "No"):
        return "De acuerdo"


"""
========Logro por conseguir todos los items========
"""


def num_items(items_totales):
    """
    Funcion que recibe la lista items_totales
    y cuenta la cantidad de valores dentro de
    la lista y regresa: la cantidad
    total contada.
    """
    cont = 0
    for x in items_totales:
        cont = cont + 1
    return cont


def logro_completado():
    """
    Funcion que compara el resultado
    de la funcion num_items(items_totales)
    con la cantidad total de posibles
    valores dentro de la lista item_totales
    regresando: diferentes textos strings
    si se tienen 6 valores o no.
    """
    if num_items(items_totales) == 6:
        return ("¡Felicidades, conseguiste todos los objetos del juego!")
    else:
        return ("Bien jugado.")


"""
========Boost========
"""


def boost():
    """
    Funcion que busca si existe un valor en la
    lista inventario y si existe
    sumará 2.25 a puntos_de_conexion_milo
    o a puntos_de_conexion_eli y regresa:
    puntos_de_conexion_milo
    o puntos_de_conexion_eli dependiendo
    del valor que sea enontrado en la lista
    inventario.
    """
    global puntos_de_conexion_eli
    global puntos_de_conexion_milo
    if "marcadores posca" in inventario:
        puntos_de_conexion_milo = puntos_de_conexion_milo + 2.25
        return puntos_de_conexion_milo
    elif "computadora gamer" in inventario:
        puntos_de_conexion_eli = puntos_de_conexion_eli + 2.25
        return puntos_de_conexion_eli


"""
========Finales========
"""


def maximo(destino):
    """
    Funcion que recibe lista
    destino y busca el valor
    más grande dentro de la lista
    y regresa: el valor maximo
    de la lista
    """
    max = destino[0]
    for i in destino:
        if i > max:
            max = i
    return max


def final(max):
    """
    Funcion que recibe valor max
    y dependiendo del valor maximo
    se obtiene un final posible en
    el juego.
    """
    if max >= 5.0 and max == (puntos_de_conexion_milo):
        return ("""
        El ultimo dia no te encuentras a nadie de las
        personas que mas destacaron en tu semana.
        Sin embargo, cuando te diriges a tu auto,
        una voz te llama y te detienes.
        Milo: Hey, espera, se que no me has dicho tu nombre
        y que no nos conocemos bien.
        Es solo que, quiero conocerte mas.
        ¿Crees... que podriamos ser amigos y hablar sobre arte?""")
    elif max >= 5.0 and max == (puntos_de_conexion_eli):
        return ("""
        El ultimo dia no te encuentras a nadie de las
        personas que mas destacaron en tu semana.
        Sin embargo, cuando te diriges a tu auto,
        una voz te llama y te detienes.
        Eli: Umm hola, solo queria agradecerte
        por ser tan amable conmigo,
        me gustaria saber si podriamos pasar mas
        tiempo junt%ss y quizas
        jugar videojuegos o algo asi.""" % (y))
    elif maximo(destino) < 5.0:
        return ("""
        El ultimo dia no te encuentras a nadie
        de las personas que mas destacaron en tu
        semana. Te diriges a tu auto sin nadie que
        te acompañe. Por tus crimenes de guerra
        te has quedado sin amigos.
        Pero no te preocupes, despues de todo solo es un juego.""")


"""
========Elilge tu nombre========
"""

print("Elige tu nombre:")

n = str(input())

"""
Permite al jugador elegir su pronombre
"""

print("Escribe tu pronombre: ella, el o elle")
pronombre_jugador = input()
while pronombre_jugador != "ella" and\
        pronombre_jugador != "el" and pronombre_jugador != "elle":
    print("""Pronombres disponibles por el momento: el, ella, elle
(lamento las molestias >_< ). Escribe una opcion disponible:""")
    pronombre_jugador = input()
if pronombre_jugador == "ella":
    y = "a"
    z = "la"
    f = "a"
elif pronombre_jugador == "el":
    y = "o"
    z = "el"
    v = "e"
    f = ""
elif pronombre_jugador == "elle":
    y = "x"
    f = "x"


"""
========Tutorial========
"""

text1 = ("""Hola %s ¿list%s para la aventura?\n""" % (n, y))
text(text1, 0.03)
text2 = ("""Comencemos por lo básico. Tu eres %s, un%s estudiante
de nuevo ingreso en la Universidad X.
No conoces a nadie… aun.\n""" % (n, f))
text(text2, 0.03)
text3 = ("""Pero no te preocupes, esta es tu historia,
tendras el poder de elegir y fortalecer los vinculos que hagas.\n""")
text(text3, 0.03)
text4 = ("""Mira, practiquemos un poco la toma decisiones.\n""")
text(text4, 0.03)
text5 = ("""Supongamos que tu mejor amigo esta triste,¿que harias
para hacerlo sentirse mejor?\n""")
text(text5, 0.03)
text6 = ("""A: Darle un abrazo para reconfortarlo.
B: Burlarte de sus sentimientos.\n""")
text(text6, 0.03)

respuesta = str(input())
print("Puntos de conexion:", contador(respuesta), "\n")

if puntos_de_conexion == -1:
    text7 = ("""Oh no, eso no es lo que hace un%s buen%s amig%s.
Tendras que ser penalizad%s.\n""" % (f, y, y, y))
    text(text7, 0.03)

text8 = ("""\nEl numero de arriba son los puntos de conexion que vas
teniendo a lo largo de la historia con los personajes y dependiendo
de tus acciones estos bajaran o subiran.
De acuerdo, intentemoslo de nuevo.
Ahora la situacion será diferente.\n""")
text(text8, 0.03)
text9 = ("""Uno de tus compañeros de escuela no entiende la tarea
y te pide ayuda. Tu...\n""")
text(text9, 0.03)
text10 = ("""A: Lo ayudarias y resolverias todas las dudas que el tenga.
B: Lo ignorarias, no es tu problema.\n""")
text(text10, 0.03)

respuesta = str(input())
print("Puntos de conexion:", contador(respuesta), "\n")

if puntos_de_conexion > 0:
    text11 = ("Veo que estas entendiendo de que va esto.¡Muy bien!\n")
    text(text11, 0.03)
elif puntos_de_conexion < 0:
    text12 = ("""Deberias plantearte en tomar cursos
sobre relaciones interpersonales amig%s.""" % (y))
    text(text12, 0.03)

text13 = ("""\nComo viste, en la vida tus decisiones importan,
si eres bueno tus puntos de conexion subiran
y cosas buenas pasaran...
De lo contrario, viviras consecuencias catastroficas.
No digas que no te lo adverti.\n""")
text(text13, 0.03)
text14 = ("¿No hay dudas? Perfecto. Que la diversion comience.\n")
text(text14, 0.03)

"""
========Dia 1========
"""
print("====Dia 1====")
text15 = ("""Es hoy, el primer dia en la Universidad X.
¿Que llevaras contigo?\n""")
text(text15, 0.03)
text16 = ("""(Recuerda que para asegurar un mejor funcionamiento
debes copiar y pegar la respuesta o copiarla sin errores :D)\n""")
text(text16, 0.03)
print("Objetos: computadora gamer o marcadores posca.")

respuesta_boost = str(input())
agregar_inventario_boost(respuesta_boost)
print(inventario)

text17 = ("""\nExcelente decision, como podras ver arriba
esta tu inventario, podras verlo cuando recojas objetos.\n""")
text(text17, 0.03)
text18 = ("""Ya estas en la Universidad X, una persona bajita se acerca
a ti y te mira con ojos timidos.
No puedes evitar sentir ternura.\n""")
text(text18, 0.03)
text19 = ("""Eli: Hola me llamo Eli, ¿sabes donde está el salon 6103?
Soy nueva aqui y no tengo ni idea de donde es mi clase.\n""")
text(text19, 0.03)
text20 = ("""Es la personita mas adorable que has visto.
Llena de pecas y el cabello esponjado y ondulado.
Claro que vas ayudarla, ¿no?\n""")
text(text20, 0.03)
text21 = ("""A: Por supuesto que si, no la culpo por no entender
la rara enumeracion de los salones.
B: No, no tengo tiempo que perder voy tarde a clases.\n""")
text(text21, 0.03)

contador_eli()
print("Puntos de conexion con Eli:", puntos_de_conexion_eli, "\n")

if eleccion_eli == 2.0:
    text22 = ("""Le explicas a Eli que el primer numero indica el numero
del edificio, el segundo numero el piso y
los dos ultimos el numero de salon.\n""")
    text(text22, 0.03)
    text23 = ("""Eli: ¡Muchas, muchas, muuuuuuuchaaas graciaaas!
No tenia ni idea de que eras alguien tan amable <3.\n""")
    text(text23, 0.03)
elif eleccion_eli == -1.0:
    text24 = ("""Te rehusas a explicarle a Eli y la ignoras friamente
mientras te alejas con pasos largos para llegar a tiempo.\n""")
    text(text24, 0.03)
    text25 = ("""Por suerte aun no es tarde para reconsiderar tus
acciones, aunque Eli no olvidara este momento.\n""")
    text(text25, 0.03)

text26 = ("""\nTU-RU-RU-RUUUUU, has encontrado 'audifonos de gatito'
en tu camino a clase. ¿Quieres agregarlos a tu inventario?\n""")
text(text26, 0.03)

respuesta_sn_item = str(input("\nSi o No: "))
print(agregar_inventario_item(respuesta_sn_item), "\n")

text27 = ("""\nContinuas con tu dia tranquilamente.
Las clases y actividades son mas faciles de lo que esperabas.\n""")
text(text27, 0.03)
text28 = ("""Te diriges a tu clase de matemáticas y en cuanto entras,
en el pizarron ves escrito: '¡Examen sorpresa!.'
No puedes creerlo, apenas es tu primera clase.\n""")
text(text28, 0.03)
text29 = ("""Volteas a ver al resto de la clase para ver sus reacciones,
cuando entre todas las caras, ves a la chica pecosa de la mañana.
Eli se ve tranquila, en este momento desearias ser como ella.\n""")
text(text29, 0.03)
text30 = ("""Te sientas junto a ella, y te voltea a ver con una mirada
que no sabes descifrar. El profesor comienza a pasar los examenes
y cuando ves el tuyo se te hiela la sangre. ¿Que haras?\n""")
text(text30, 0.03)
text31 = ("""A: Aceptar que no sabes nada e intentar
resolverlo por tu cuenta.
B: Sacar tu telefono y hacer trampa para no quedar en ridiculo.\n""")
text(text31, 0.03)

contador_eli()
print("Puntos de conexion con Eli:", puntos_de_conexion_eli, "\n")

if eleccion_eli == 2.0:
    text32 = ("""Eli te ve teniendo dificultades
y te ofrece una sonrisa.
Despues de clases se te acerca.\n""")
    text(text32, 0.03)
    text33 = ("""Eli: Se que no nos conocemos, pero si gustas podria
enseñarte todo sobre los vectores para que no tengas dificultes
en futuros examenes. UWU\n""")
    text(text33, 0.03)
    text34 = ("""Le agradeces con todo tu corazón,
ah que harías sin ella.\n""")
    text(text34, 0.03)
elif eleccion_eli == -1.0:
    text35 = ("""Sacas tu telefono y comienzas a copiar, sonries.
Sin embargo, antes de que te des cuenta Eli lleva tiempo observandote,
para cuando te das cuenta ya es tarde.\n""")
    text(text35, 0.03)
    text36 = ("""Eli desprecia los actos de corrupcion y las injusticias.
Asi que no es sorpresa que te mire llena de furia.
Por suerte para ti ella no le dira nada al profesor.>:( \n""")
    text(text36, 0.03)

text37 = ("""\nTU-RU-RU-RUUUUU, has encontrado 'tarjeta STOM'
tirada en el suelo. ¿Quieres agregarla a tu inventario?\n""")
text(text37, 0.03)

respuesta_sn_item = str(input("\nSi o No: "))
print(agregar_inventario_item(respuesta_sn_item), "\n")

text38 = ("""\nTras ese horrible examen caminas hacia la cafeteria.
Tienes que alimentarte para ser un ser humano optimo,
funcional y productivo y servir a la sociedad.\n""")
text(text38, 0.03)
text39 = ("""Miras con calma las opciones en el menu.
Nada se ve realmente bueno, pero necesitas comer.\n""")
text(text39, 0.03)
text40 = ("""El sonido de una voz llorando interrumpe tus
pensamientos sobre que comida es mejor.
Volteas a donde se origina la voz y vez a
Eli en el piso junto a otras personas.\n""")
text(text40, 0.03)
text41 = ("""Unos chicos mas altos la estan amenazando y le
estan gritando. Eli se ve indefensa y demasiado
timida como para hacer algo por su cuenta. Tu...\n""")
text(text41, 0.03)
text42 = ("""A: Corres hacia los tipos y te enfrentas en una
lucha para hacer justicia al matrato que recibio Eli.
B: Te da igual, no es tu problema. Es solo una chica
que ni siquiera conoces, no vale la pena salir lastimad%s.\n""" % (y))
text(text42, 0.03)

contador_eli()
print("Puntos de conexion con Eli:", puntos_de_conexion_eli, "\n")

if eleccion_eli == 2:
    text43 = ("""Te armas de coraje y luchas con valentia.
Terminas herid%s, pero Eli te mira
con ojos de asombro y agradecimiento.\n""" % (y))
    text(text43, 0.03)
    text44 = ("""Eli: No tenias que hacer eso...
Gracias, realmente necesitaba tu ayuda.\n""")
    text(text44, 0.03)
    text45 = ("""Por supuesto que la ibas a ayudar,
ninguna persona debe ser tratada asi y mucho menos Eli.\n""")
    text(text45, 0.03)
elif eleccion_eli == -1.0:
    text46 = ("""Ignoras a los matones y a Eli y te dispones a comer
la comida que elegiste. Felicidades, ahora eres un ser humano
alimentado, optimo, funcional y productivo para servir a
la sociedad, pero a que costo...\n""")
    text(text46, 0.03)
    text47 = ("""Comes en silencio por el resto de la hora
mientras escuchas los sollozos de Eli.\n""")
    text(text47, 0.03)

text48 = ("""\nTU-RU-RU-RUUUUU, un chico que no conoces te ha ofrecido
'figura de accion'. ¿Quieres agregarla a tu inventario?\n""")
text(text48, 0.03)

respuesta_sn_item = str(input("Si o No: "))
print(agregar_inventario_item(respuesta_sn_item), "\n")

text49 = ("""Sin duda fue un primer dia muy interesante.
Conociste alguien, tuviste tu primer examen,
el asunto de la cafetería... Es hora de regresar a casa.\n""")
text(text49, 0.03)
text50 = ("""Vas al estacionamiento de la Universidad X y
alguien te intercepta Eli.\n""")
text(text50, 0.03)
text51 = ("""Eli: Yo... necesito tu ayuda, veras,
mi auto no funciona, creo que se le acabo la bateria.\n""")
text(text51, 0.03)
text52 = ("""Tu sabes bastante de autos y tienes todo lo
necesario para ayudarla en tu cajuela. Es cuestion de que decidas
ayudarla o decirle que deje de molestarte.\n""")
text(text52, 0.03)
text53 = ("""A: Realmente no tienes mucho que hacer,
ni siquiera tienes tarea o algo asi,
no pierdes nada, asi que la ayudas.
B: La miras con molestia y le dices que
te deje de estar pidiendo favores.\n""")
text(text53, 0.03)

contador_eli()
print("Puntos de conexion con Eli:", puntos_de_conexion_eli, "\n")

if eleccion_eli == 2.0:
    text54 = ("""Eli: Wow en serio debes ser un angel o algo asi.
Escucha, realmente me costo mucho pedirte esto,
soy muy timida... pero necesito a alguien que me
de una mano de vez en cuando.\n""")
    text(text54, 0.03)
    text55 = ("""Eli: Gracias, realmente necesitaba tu ayuda.
La proxima vez no dudes en pedirme algo si lo necesitas.\n""")
    text(text55, 0.03)
    text56 = ("""Le das las gracias y le regalas una sonrisa.
Regresas a tu casa feliz por haber ayudado a alguien.\n""")
    text(text56, 0.03)
elif eleccion_eli == -1.0:
    text57 = ("""Eli: Eres una persona tan grosera...
esta bien, no te quitare mas tu tiempo.\n""")
    text(text57, 0.03)
    text58 = ("""Algo dentro de ti no se siente bien, pero como sea,
no es tu problema, ¿verdad? Regresas a tu casa en un
silencio incomodo pensando en lo que hiciste mal.\n""")
    text(text58, 0.03)

"""
========Día 2========
"""
print("====Dia 2====")
text59 = ("""Es el segundo dia, momento de conocer mas personas y
experimentar las clases que te tocan el dia de hoy.\n""")
text(text59, 0.03)
text60 = ("""Es martes, asi que la unica clase de hoy es tu optativa
de artes. Muy interesantes materias,
para un%s futur%s ingenier%s.\n""" % (y, y, y))
text(text60, 0.03)
text61 = ("""En tu camino a la Universidad X observas con
detenimiento la ciudad, tiene su propio encanto.
Lleno de ruido, gente y un hermoso sol que nace del horizonte.\n""")
text(text61, 0.03)
text62 = ("""Te estacionas en el lugar que se convertira en tu lugar sin
nombre. A lo lejos escuchas a los estudiantes reirse y
te llama la atencion algo inusual.\n""")
text(text62, 0.03)
text63 = ("""Una persona, disimuladamente pinta la pared de un edificio.
¡¿Que es esto?! V A N D A L I S M O O O O.
Te bajas de tu auto y azotas la puerta,
no hay tiempo que perder debes detenerlo.\n""")
text(text63, 0.03)
text64 = ("Tu: ¡¿QUE CREES QUE HACEEEEEES?!\n")
text(text64, 0.03)
text65 = ("La persona te voltea a ver con una sonrisa desafiante.\n")
text(text65, 0.03)
text66 = ("""Milo: Saludos bella persona, llegas justo a tiempo
para ver como culmino mi obra de arte.\n""")
text(text66, 0.03)
text67 = ("""Te acercas para arrebatarle la pintura, pero intercepta con
una mano suya tus manos. Estas atrapad%s sin posibilidades
de hacer nada al respecto.\n""" % (y))
text(text67, 0.03)
text68 = ("""Milo: Y... listo, mira. Tremendo trabajo y casi me detienes.
Ah, por cierto no me presente pero soy Milo, signo escorpio y me
encanta el arte. Ahora dime, ¿que opinas de esta pintura?\n""")
text(text68, 0.03)
text69 = ("""La figura de un gato con penetrantes ojos verdes
te sorprende. Te deja sin palabras, odias cualquier acto de vandalismo,
pero esto...\n""")
text(text69, 0.03)
text70 = ("""A: Le dices la verdad, que esta hermosa la pintura.
B: Le mientes, dices que es lo peor que has visto y
que el es un delincuente.\n""")
text(text70, 0.03)

contador_milo()
print("Puntos de conexion con Milo:", puntos_de_conexion_milo, "\n")

if eleccion_milo == 2.0:
    text71 = ("""Milo: Tienes buen ojo, aunque esto no es nada...
he hecho cosas mejores. Quizas algun dia te las enseñe,
bueno debo retirarme tengo clases a las que ir.\n""")
    text(text71, 0.03)
    text72 = ("""Te despides de milo, sigues impresionad%s
de su talento.\n""" % (y))
    text(text72, 0.03)
elif eleccion_milo == -1.0:
    text73 = ("""Milo: Oww bueno, entiendo que en el mundo del arte
cada quien tiene su opinion,
pero pudoste haber sido menos dur%s.\n""" % (y))
    text(text73, 0.03)
    text74 = ("""Milo se aleja de ti, triste. :(\n""")
    text(text74, 0.03)

text75 = ("""\nTU-RU-RU-RUUUUU, has encontrado junto a la pintura de
Milo 'pincel de Bob Gross'. ¿Quieres agregarlo a tu inventario?\n""")
text(text75, 0.03)

respuesta_sn_item = str(input("\nSi o No: "))
print(agregar_inventario_item(respuesta_sn_item), "\n")

text76 = ("""Vas a tu optativa de artes, mientras ries por dentro
pensando en la coincidencia que seria encontrarte a Milo.\n""")
text(text76, 0.03)
text77 = ("""Entras a tu salon y lo primero que atrapa tu
mirada es la cara de Milo. Tus cachetes se ponen rojos
y te sientas lejos de el.\n""")
text(text77, 0.03)
text78 = ("""Por alguna razon hay algo en su persona que te
hace sentir diminut%s. Entonces ves que se acerca a ti
con una mirada seria.\n""" % (y))
text(text78, 0.03)
text79 = ("""Milo: ¿Por que te sientas lejos de mi y me evitas?\n""")
text(text79, 0.03)
text80 = ("""Oh no mas vale pensar en alguna respuesta
lo antes posible, rapido.\n""")
text(text80, 0.03)
text81 = ("""A: Le explicas timidamente que te sientes intimidad%s
por su talento. o B: Le dices que no quieres estar con una
persona tan rara y desagradable como el.\n""" % (y))
text(text81, 0.03)

contador_milo()
print("Puntos de conexion con Milo:", puntos_de_conexion_milo, "\n")

if eleccion_milo == 2.0:
    text82 = ("""Milo: Oh vaya jajaja, me siento tan halagdado,
no se que decir. Muchas gracias.\n""")
    text(text82, 0.03)
    text83 = ("""Durante el resto de la clase ves como Milo no deja
de sonreir. Tu corazon se siente claiente y feliz tambien.\n""")
    text(text83, 0.03)
elif eleccion_milo == -1.0:
    text84 = ("""Observas como los labios de Milo forman una linea
delgada de seriedad y se aleja bruscamente de tu lugar.\n""")
    text(text84, 0.03)
    text85 = ("""Quizas deberias intentar ser mas amable, quien sabe.
Quizas podrias abrirte nuevas puertas.\n""")
    text(text85, 0.03)

text86 = ("""\nTU-RU-RU-RUUUUU, has encontrado olvidado en el salon
de arte 'tableta Wecom'. ¿Quieres agregarla a tu inventario?\n""")
text(text86, 0.03)

respuesta_sn_item = str(input("\nSi o No: "))
print(agregar_inventario_item(respuesta_sn_item), "\n")

text87 = ("""El dia de hoy decides sacar tu lado mas artistico
y vas a la Plaza Azul a tocar el piano.
No se te da muy bien, pero lo disfurtas bastante.\n""")
text(text87, 0.03)
text88 = ("""Cuando llegas observas que Milo esta tocando el piano.\n""")
text(text88, 0.03)
text89 = ("""En serio, ¿como es que te lo encuentras
a cada lugar que vas?\n""")
text(text89, 0.03)
text90 = ("""Te sientes un poco frustrad%s, porque querias tocar.\n""" % (y))
text(text90, 0.03)
text91 = ("""En este momento tienes dos opciones, esperar o
decirle que se quite, veamos que desicion tomas.\n""")
text(text91, 0.03)
text92 = ("""A: Esperas cerca del piano a que Milo acabe su turno.
B: Le dices se mueva del asiento, interrupiendolo.\n""")
text(text92, 0.03)

contador_milo()
print("Puntos de conexion con Milo:", puntos_de_conexion_milo, "\n")

if eleccion_milo == 2.0:
    text93 = ("""Te sientas tranquilamente, cerca del piano, mientras
escuchas como toca Milo. De pronto, sientes que te observan
y cuando subes la mirada, ves que Milo te esta viendo.\n""")
    text(text93, 0.03)
    text94 = ("""Milo: Hey, ven sientante a mi lado.\n""")
    text(text94, 0.03)
    text95 = ("""Pasas una tarde tranquila junto a Milo y
su musica. Es bastante relajante.\n""")
    text(text95, 0.03)
elif eleccion_milo == -1.0:
    text96 = ("""Le gritas agresivamente a Milo que se quite del piano
interrumpiendo la cancion que tocaba.\n""")
    text(text96, 0.03)
    text97 = ("""Milo no te dice nada, solo toma sus cosas y se va,
ya tuvo suficiente.\n""")
    text(text97, 0.03)

text98 = ("""\nTU-RU-RU-RUUUUU, alguien ha dejado 'CD inspirador'
sobre el piano. ¿Quieres agregarla a tu inventario?\n""")
text(text98, 0.03)

respuesta_sn_item = str(input("\nSi o No: "))
print(agregar_inventario_item(respuesta_sn_item), "\n")

text99 = ("""Tras el asunto del piano, te vas a tu clase extracurricular
de pintura En este punto ya no te sorprenderia ver a Milo por ahi.\n""")
text(text99, 0.03)
text100 = ("""Justo como lo esperaste ahi esta, sentado detras
de un lienzo muy concentrado.""")
text(text100, 0.03)
text101 = ("""El ejercico de hoy es pintar un personaje de anime.
Quizas deberias pintar a Jotaro o a Josuke de JoJo's.\n""")
text(text101, 0.03)
text102 = ("""El momento de la verdad llega y todos muestrn sus
pinturas. Por supuesto la mejor es la de Milo.\n""")
text(text102, 0.03)
text103 = ("""Sientes envidia, mucha adimrasión y tu espirituo
competitivo se pone alerta. A continuacion...\n""")
text(text103, 0.03)
text104 = ("""A: Comienzas a aplaudir felicitando a todos,
especialmente a Milo por sus magnificos trabajos.
B: Tomas con fuerza una brocha llena de pintura y rayoneas la
pintura de Milo antes de que pueda hacer algo.\n""")
text(text104, 0.03)

contador_milo()
print("Puntos de conexion con Milo:", puntos_de_conexion_milo, "\n")

if eleccion_milo == 2.0:
    text105 = ("""Todos comienzan a aplaudir contigo y el salon se llena
de diferentes conversaciones sobre la increible pintura de Milo.
Milo no te dice nada pero te regala una sonrisa complice.\n""")
    text(text105, 0.03)
    text106 = ("""Regresas a casa con las manos llenas de pintura,
    por suerte no sera tan dificil lavarlas.\n""")
    text(text106, 0.03)
    text113 = ("""Pasas una tarde tranquila junto a Milo y
su musica. Es bastante relajante.\n""")
    text(text113, 0.03)
elif eleccion_milo == -1.0:
    text107 = ("""En cuanto rayas el cuadro en un ataque frenetico de
celos, todo el salon se queda callado. No falta decir que
la maestra te saco del salon por no respetar a Milo.\n""")
    text(text107, 0.03)
    text108 = ("""Vas en tu auto, probablemente disfurtando tu venganza
contra Milo, cielos a veces puedes ser muy cruel.\n""")
    text(text108, 0.03)

"""
========Día 3 (Final)========
"""
text109 = ("""Ah el quinto día. Hoy veremos lo que los dioses han decidido
para ti según carga karmática y el boost secreto.\n""")
text(text109, 0.03)
text110 = ("Veamos...\n")
text(text110, 0.03)
text111 = ("Veamos...\n")
text(text111, 0.03)
text112 = ("Veamos...\n")
text(text112, 0.03)
print("Puntos de conexion + boost: ", boost())
destino = [puntos_de_conexion_milo, puntos_de_conexion_eli]
maxdestino = maximo(destino)
print(final(maxdestino))
print("Conseguiste", num_items(items_totales), "de 6 items!!!\n")
print(logro_completado())

exit()
