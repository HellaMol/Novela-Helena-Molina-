"""ISe importa la libreria de tiempo para usar la función de sleep"""
from time import sleep 

""" Se importar la libreria de sys, donde se usara la función de flush"""
import sys 

"""
========Contador tutorial========
"""

"""Funcion para hacer aparecer el texto a cierta velocidad obtenido de https://es.stackoverflow.com/questions/25901/como-imprimir-una-cadena-de-texto-con-pausas-entre-cada-letra-impresa-en-python"""
def text(texto,speed):
    """
    (uso de biblioteca, uso de funciones)
    recibe: string de texto,velocidad de texto
    imprime cada letra segun la velocidad
    devuelve: texto impreso según la velocidad
    """
    for c in texto: 
        print(c,end='') 
        sys.stdout.flush() 
        sleep(speed) 

"""
========Contador tutorial========
"""
puntos_de_conexion = 0
def contador(respuesta):
    global puntos_de_conexion
    while respuesta != "A" and respuesta != "B":
        print("Escribe una respuesta disponible A o B:")
        respuesta = str(input())
    if(respuesta == "A"):
        eleccion = 2
        puntos_de_conexion = puntos_de_conexion + eleccion
        return float(puntos_de_conexion)
    elif(respuesta == "B"):
        eleccion = -1
        puntos_de_conexion = puntos_de_conexion + eleccion
        return float(puntos_de_conexion)

"""
========Contador Milo========
"""
puntos_de_conexion_milo = 0
def contador_milo(respuesta_milo):
    global puntos_de_conexion_milo
    while respuesta_milo != "A" and respuesta_milo != "B":
        print("Escribe una respuesta disponible A o B:")
        respuesta_milo = str(input())
    if(respuesta_milo == "A"):
        eleccion_milo = 2
        puntos_de_conexion_milo = puntos_de_conexion_milo + eleccion_milo
        return float(puntos_de_conexion_milo)
    elif(respuesta == "B"):
        eleccion_milo = -1
        puntos_de_conexion_milo = puntos_de_conexion_milo + eleccion_milo
        return float(puntos_de_conexion_milo)

"""
========Contador Eli========
"""
puntos_de_conexion_eli = 0
def contador_eli(respuesta_eli):
    global puntos_de_conexion_eli
    while respuesta_eli != "A" and respuesta_eli != "B":
        print("Escribe una respuesta disponible A o B:")
        respuesta_eli = str(input())
    if(respuesta_eli == "A"):
        eleccion_eli = 2
        puntos_de_conexion_eli = puntos_de_conexion_eli + eleccion_eli
        return float(puntos_de_conexion_eli)
    elif(respuesta_eli == "B"):
        eleccion_eli = -1
        puntos_de_conexion_eli = puntos_de_conexion_eli + eleccion_eli
        return float(puntos_de_conexion_eli)

    
"""
========Inventario========
"""
Cosas_de_gamer = []
Cosas_de_artista = []
Cosas_de_nerd = []
Cosas_de_deportista = []
Inventario = [[Cosas_de_gamer],[Cosas_de_artista],[Cosas_de_nerd],[Cosas_de_deportista]]

def agregar_inventario_boost(respuesta_boost):
    while respuesta_boost != "marcadores posca" and respuesta_boost != "computadora gamer":
        print("Objetos disponibles: computadora gamer o marcadores posca")
        respuesta_boost = str(input())
    if (respuesta_boost == "marcadores posca" or respuesta_boost == "computadora gamer"):
        Inventario.append(respuesta_boost)
        return Inventario
    
def agregar_inventario_item(respuesta_sn_item):
    while respuesta_sn_item != "Si" and respuesta_sn_item != "No":
        print("Escribe una respuesta disponible Si o No:")
        respuesta_sn_item = str(input())
    if (respuesta_sn_item == "Si"):
        respuesta_item = str(input("Escribe el nombre del objeto: "))
        while respuesta_item != "audifonos de gatito" and respuesta_item != "tarjeta STOM" and respuesta_item != "figura de accion" and respuesta_item != "pincel de Bob Gross" and respuesta_item != "tableta Wecom" and respuesta_item != "CD inspirador":
            print("Objeto inexistente o no disponible, por favor escribe correctamente el nombre del objeto:")
            respuesta_item = str(input("Escribe el nombre del objeto: "))
        if (respuesta_item == "audifonos de gatito" or respuesta_item == "tarjeta STOM" or respuesta_item == "figura de accion"):
            if (respuesta_item not in Inventario):
                Cosas_de_gamer.append(respuesta_item) and items_totales.append(respuesta_item)
                print ("Se agrego al inventario")
                return Inventario
            else:
                print("Ese objeto ya lo tienes -_-")
        elif (respuesta_item == "pincel de Bob Gross" or respuesta_item == "tableta Wecom" or respuesta_item == "CD inspirador"):
            if (respuesta_item not in Inventario):
                Cosas_de_artista.append(respuesta_item) and items_totales.append(respuesta_item)
                print ("Se agrego al inventario")
                return Inventario
            else:
                print("Ese objeto ya lo tienes -_-")
    elif (respuesta_sn_item == "No"):
        return "De acuerdo"
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
    if num_items(items_totales) == 6:
        print("¡Felicidades, conseguiste todos los objetos del juego!")
    else:
        print("Bien jugado.")
"""
========Boost========
"""

def boost():
    if "marcadores posca" in Inventario:
        return (puntos_de_conexion_milo + 2.25)
    elif "computadora gamer" in Inventario:
        return (puntos_de_conexion_eli + 2.25)


"""
========Finales========
"""


def maximo(destino):
    max = destino[0]
    for i in destino:
        if i > max:
            max = i
    return max



def final(max):
    if max >= 5 and max == puntos_de_conexion_milo:
        return ("""El ultimo dia no te encuentras a nadie de las personas que mas destacaron en tu semana. Sin embargo, cuando te diriges una voz te llama y te detienes.
                Milo: Hey, espera, se que no me has dicho tu nombre y que no nos conocemos bien. Es solo que, quiero conocerte mas. ¿Crees... que podriamos ser amigos y hablar sobre arte?""")
    elif max >= 5 and max == puntos_de_conexion_eli:
        return ("""El ultimo dia no te encuentras a nadie de las personas que mas destacaron en tu semana. Sin embargo, cuando te diriges una voz te llama y te detienes.
                Eli: Umm hola, solo queria agradecerte por ser tan amable conmigo, me gustaria saber si podriamos pasar mas tiempo junt%ss y quizas jugar videojuegos o algo asi.%(y)""")


"""
========Elilge tu nombre========
"""

print("Elige tu nombre:")

n = str(input())

print("Escribe tu pronombre: ella, el o elle")
pronombre_jugador=input()
while pronombre_jugador != "ella" and pronombre_jugador != "el" and pronombre_jugador != "elle":
    print("Pronombres disponibles por el momento: el, ella, elle (lamento las molestias >_< ). Escribe una opcion disponible:")
    pronombre_jugador=input()
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

print("Hola %s ¿list%s para la aventura?\n"%(n,y))
print("Comencemos por lo básico. Tu eres %s, un%s estudiante de nuevo ingreso en la Universidad X. No conoces a nadie… aun."%(n,f))
print("Pero no te preocupes, esta es tu historia, tendras el poder de elegir y fortalecer los vinculos que hagas.\n")
print("Mira, practiquemos un poco la toma decisiones.")
print("Supongamos que tu mejor amigo esta triste,¿Que harias para hacerlo sentirse mejor?\n")
print("A: Darle un abrazo para reconfortarlo. o B: Burlarte de sus sentimientos.")

respuesta = str(input())
print("Puntos de conexion:",contador(respuesta),"\n")

if puntos_de_conexion == -1:
    print("Oh no, eso no es lo que hace un%s buen%s amig%s. Tendras que ser penalizad%s.\n"%(f,y,y,y))

print("El numero de arriba son los puntos de conexion que vas teniendo a lo largo de la historia con los personajes y dependiendo de tus acciones estos bajaran o subiran. De acuerdo, intentemoslo de nuevo. Ahora la situacion será diferente.")
print("Uno de tus compañeros de escuela no entiende la tarea y te pide ayuda. Tu...\n")
print("A: Lo ayudarias y resolverias todas las dudas que el tenga. o B: Lo ignorarias, no es tu problema.")

respuesta = str(input())
print("Puntos de conexion:",contador(respuesta),"\n")

if puntos_de_conexion > 0 :
    print("Veo que estas entendiendo de que va esto.¡Muy bien!\n")
if puntos_de_conexion < 0:
    print("Deberias plantearte en tomar cursos sobre relaciones interpersonales amig%s."%(y))

print("Como viste, en la vida tus decisiones importan, si eres bueno tus puntos de conexion subiran y cosas buenas pasaran...\n""De lo contrario, viviras consecuencias catastroficas. No digas que no te lo adverti.\n")
print("¿No hay dudas? Perfecto. Que la diversion comience.\n")

"""
========Dia 1========
"""
print("====Dia 1====")
print("Es hoy, el primer dia en la Universidad X. ¿Que llevaras contigo?")
print("(Recuerda que para asegurar un mejor funcionamiento debes copiar y pegar la respuesta o copiarla sin errores :D)\n")
print("Objetos: computadora gamer o marcadores posca.")

respuesta_boost = str(input())
agregar_inventario_boost(respuesta_boost)
print(Inventario)

print("Excelente decision, como podras ver arriba esta tu inventario, podras acceder a el en ciertos puntos de la historia y usar los objetos que encuentres.\n")
print("Ya estas en la Universidad X, una persona bajita se acerca a ti y te mira con ojos timidos.\n""No puedes evitar sentir ternura")
print("Eli: Hola me llamo Eli, ¿sabes donde está el salon 6103? Soy nueva aqui y no tengo ni idea de donde es mi clase.")
print("Es la personita mas adorable que has visto. Llena de pecas y el cabello esponjado y ondulado. Claro que vas ayudarla, ¿no?\n")
print("A: Por supuesto que si, no la culpo por no entender la rara enumeracion de los salones. o B: No, no tengo tiempo que perder voy tarde a clases.")

respuesta_eli = str(input())
print("Puntos de conexion con Eli:",contador_eli(respuesta_eli),"\n")

if respuesta_eli == "A" :
    print("Le explicas a Eli que el primer numero indica el numero de edificio, el segundo numero el piso y los dos ultimos el numero de salon")
    print("Eli: ¡Muchas, muchas, muuuuuuuchaaas graciaaas! No tenia ni idea de que eras alguien tan amable <3.\n")
if respuesta_eli == "B" :
    print("Te rehusas a explicarle a Eli y la ignoras friamente mientras te alejas con pasos largos para llegar a tiempo.")
    print("Por suerte aun no es tarde para reconsiderar tus acciones, aunque Eli no olvidara este momento.\n")

print("TU-RU-RU-RUUUUU, has encontrado 'audifonos de gatito' en tu camino a clase. ¿Quieres agregarlos a tu inventario?")

respuesta_sn_item = str(input("Si o No: "))
print(agregar_inventario_item(respuesta_sn_item),"\n")

print("Continuas con tu dia tranquilamente. Las clases y actividades son mas faciles de lo que esperabas.")
print("Te diriges a tu clase de matemáticas y en cuanto entras en el pizarron ves escrito: '¡Examen sorpresa!. No puedes creerlo, apenas es tu primera clase.")
print("Volteas a ver al resto de la clase para ver sus reacciones, cuando entre todas las caras, ves a la chica pecosa de la mañana. Eli se ve tranquila, en este momento desearias ser como ella.")
print("Te sientas junto a ella, y te voltea a ver con una mirada que no sabes descifrar. El profesor comienza a pasar los examenes y cuando ves el tuyo se te hiela la sangre. ¿Que haras?\n")
print("A: Aceptar que no sabes nada e intentar resolverlo por tu cuenta. o B: Sacar tu telefono y hacer trampa para no quedar en ridiculo.")

respuesta_eli = str(input())
print("Puntos de conexion con Eli:",contador_eli(respuesta_eli),"\n")

if respuesta_eli == "A" :
    print("Eli te ve teniendo dificultades y te ofrece una sonrisa. Despues de clases se te acerca.")
    print("Eli: Se que no nos conocemos, pero si gustas podria enseñarte todo sobre los vectores para que no tengas dificultes en futuros examenes. UWU")
    print("Le agradeces con todo tu corazón, ah que harías sin ella.\n")
if respuesta_eli == "B" :
    print("Sacas tu telefono y comienzas a copiar, sonries. Sin embargo, antes de que te des cuenta Eli lleva tiempo observandote, para cuando te das cuenta ya es tarde.")
    print("Eli desprecia los actos de corrupcion y las injusticias. Asi que no es sorpresa que te mire llena de furia. Por suerte para ti ella no le dira nada al profesor.>:( \n")

print("TU-RU-RU-RUUUUU, has encontrado 'tarjeta STOM' tirada en el suelo. ¿Quieres agregarla a tu inventario?")

respuesta_sn_item = str(input("Si o No: "))
print(agregar_inventario_item(respuesta_sn_item),"\n")

print("Tras ese horrible examen caminas hacia la cafeteria. Tienes que alimentarte para ser un ser humano optimo, funcional y productivo y servir a la sociedad.")
print("Miras con calma las opciones en el menu. Nada se ve realmente bueno, pero necesitas comer.")
print("El sonido de una voz llorando interrumpe tus pensamientos sobre que comida es mejor. Volteas a donde se origina la voz y vez a Eli en el piso junto a otras personas")
print("Unos chicos mas altos la estan amenazando y le estan gritando. Eli se ve indefensa y demasiado timida como para hacer algo por su cuenta. Tu...\n")
print("A: Corres hacia los tipos y te enfrentas en una lucha para hacer justicia al matrato que recibio Eli. o B: Te da igual, no es tu problema. Es solo una chica que ni siquiera conoces, no vale la pena salir lastimad%s."%(y))

respuesta_eli = str(input())
print("Puntos de conexion con Eli:",contador_eli(respuesta_eli),"\n")

if respuesta_eli == "A" :
    print("Te armas de coraje y luchas con valentia. Terminas con herid%s, pero Eli te mira con ojos de asombro y agradecimiento."%(y))
    print("Eli: No tenias que hacer eso... Gracias, realmente necesitaba tu ayuda.")
    print("Por supuesto que la ibas a ayudar, ninguna persona debe ser tratada asi y mucho menos Eli.\n")
if respuesta_eli == "B" :
    print("Ignoras a los matones y a Eli y te dispones a comer la comida que elegiste. Felicidades, ahora eres un ser humano alimentado, optimo, funcional y productivo para servir a la sociedad, pero a que costo...")
    print("Comes en silencio por el resto de la hora mientras escuchas los sollozos de Eli.\n")

print("TU-RU-RU-RUUUUU, un chico que no conoces te ha ofrecido 'figura de accion'. ¿Quieres agregarla a tu inventario?")

respuesta_sn_item = str(input("Si o No: "))
print(agregar_inventario_item(respuesta_sn_item),"\n")

print("Sin duda fue un primer dia muy interesante. Conociste alguien, tuviste tu primer examen, el asunto de la cafetería... Es hora de regresar a casa.")
print("Vas al estacionamiento de la Universidad X y alguien te intercepta Eli.")
print("Eli: Yo... necesito tu ayuda, veras, mi auto no funciona, creo que se le acabo la bateria.")
print("Tu sabes bastante de autos y tienes tono lo necesaro para ayudarla en tu cajuela. Es cuestion de que decidas ayudarla o decirle que deje de molestarte.\n")
print("A: Realmente no tienes mucho que hacer, ni siquiera tienes tarea o algo asi, no pierdes nada, asi que la ayudas. o B: La miras con molestia y le dices que te deje de estar pidiendo favores.")

respuesta_eli = str(input())
print("Puntos de conexion con Eli:",contador_eli(respuesta_eli),"\n")

if respuesta_eli == "A" :
    print("Eli: Wow en serio debes ser un angel o algo asi. Escucha, realmente me costo mucho pedirte esto, soy muy timida... pero necesito a alguien que me de una mano de vez en cuando.")
    print("Eli: No tenias que hacer eso... Gracias, realmente necesitaba tu ayuda. La proxima vez no dudes en pedirme algo si lo necesitas.")
    print("Le das las gracias y le regalas una sonrisa. Regresas a tu casa feliz por haber ayudado a alguien.\n")
if respuesta_eli == "B" :
    print("Eli: Eres una persona tan grosera... esta bien, no te quitare mas tu tiempo.")
    print("Algo dentro de ti no se siente bien, pero como sea, no es tu problema, ¿verdad? Regresas a tu casa en un silencio incomodo pensando en lo que hiciste mal.\n")

"""
========Día 2========
"""
print("====Dia 2====")
print("Es el segundo dia, momento de conocer mas personas y experimentar las clases que te tocan el dia de hoy.")
print("Es martes, asi que la unica clase de hoy es tu optativa de artes. Muy interesantes materias, para un%s futur%s ingenier%s"%(y,y,y))
print("En tu camino a la Universidad X observas con detenimiento la ciudad, tiene su propio encanto. Lleno de ruido, gente y un hermoso sol que nace del horizonte.\n")

print("Te estacionas en el lugar que se convertira en tu lugar sin nombre. A lo lejos escuchas a los estudiantes reirse y te llama la atencion algo inusual.")
print("Una persona, disimuladamente pinta la pared de un edificio. ¡¿Que es esto?! B A N D A L I S M O O O O . Te bajas de tu auto y azotas la puerta, no hay tiempo que perder debes detenerlo.")
print("Tu: ¡¿QUE CREES QUE HACEEEEEES?!")
print("La persona te voltea a ver con una sonrisa desafiante.")
print("Milo: Saludos bella persona, llegas justo a tiempo para ver como culmino mi obra de arte.")
print("Te acercas para arrebatarle la pintura, pero intercepta con una mano suya tus manos. Estas atrapad%s sin posibilidades de hacer nada al respecto."%(y))
print("Milo: Y... listo, mira. Tremendo trabajo y casi me detienes. Ah, por cierto no me presente pero soy Milo, signo escorpio y me encanta el arte. Ahora dime, ¿que opinas de esta pintura?")
print("La figura de un gato con penetrantes ojos verdes te sorprende. Te deja sin palabras, odias cualquier acto de bandalismo, pero esto...\n")
print("A: Le dices la verdad, que esta hermosa la pintura. o B: Le mientes, dices que es lo peor que has visto y que el es un delincuente.")

respuesta_milo = str(input())
print("Puntos de conexion con Milo:",contador_milo(respuesta_milo),"\n")

if respuesta_milo == "A" :
    print(" Milo: Tienes buen ojo, aunque esto no es nada... he hecho cosas mejores. Quizas algun dia te las enseñe, bueno debo retirarme tengo clases a las que ir.")
    print("Te despides de milo, siuges impresionad%s de su talento.\n"%(y))
if respuesta_milo == "B" :
    print("Milo: Oww bueno, entiendo que en el mundo del arte cada quien tiene su opinion, pero pudoste haber sido menos dur%s."%(y))
    print("Milo se aleja de ti, triste. :(\n")
    
print("TU-RU-RU-RUUUUU, has encontrado junto a la pintura de Milo 'pincel de Bob Gross'. ¿Quieres agregarlo a tu inventario?")

respuesta_sn_item = str(input("Si o No: "))
print(agregar_inventario_item(respuesta_sn_item),"\n")

print("Vas a tu optativa de artes, mientras ries por dentro pensando en la coincidencia que seria encontrarte a Milo.")
print("Entras a tu salon y lo primero que atrapa tu mirada es la cara de Milo. Tus cachetes se ponen rojos y te sientas lejos de el.")
print("Por alguna razon hay algo en su persona que te hace sentir diminut%s. Entonces ves que se acerca a ti con una mirada seria."%(y))
print("Milo: ¿Por que te sientas lejos de mi y me evitas?")
print("Oh no mas vale pensar en alguna respuesta lo antes posible, rapido.")
print("A: Le explicas timidamente que te sientes intimidad%s por su talento. o B: Le dices que no quieres estar con una persona tan rara y desagradable como el."%(y))

respuesta_milo = str(input())
print("Puntos de conexion con Milo:",contador_milo(respuesta_milo),"\n")

if respuesta_milo == "A" :
    print("Milo: Oh vaya jajaja, me siento tan halagdado, no se que decir. Muchas gracias.")
    print("Durante el resto de la clase ves como Milo no deja de sonreir. Tu corazon se siente claiente y feliz tambien.\n")
if respuesta_milo == "B" :
    print("Observas como los labios de Milo forman una linea delgada de seriedad y se aleja bruscamente de tu lugar.")
    print("Quizas deberias intentar ser mas amable, quien sabe. Quizas podrias abrirte nuevas puertas.\n")
    
print("TU-RU-RU-RUUUUU, has encontrado olvidado en el salon de arte 'tableta Wecom'. ¿Quieres agregarla a tu inventario?")

respuesta_sn_item = str(input("Si o No: "))
print(agregar_inventario_item(respuesta_sn_item),"\n")

print("El dia de hoy decides sacar tu lado mas artistico y vas a la Plaza Azul a tocar el piano. No se te da muy bien, pero lo disfurtas bastante.")
print("Cuando llegas observas que Milo esta tocando el piano.")
print("En serio, ¿como es que te lo encuentras a cada lugar que vas?")
print("Te sientes un poco frustrad%s, porque querias tocar."%(y))
print("En este momento tienes dos opciones, esperar o decirle que se quite, veamos que desicion tomas.\n")
print("A: Esperas cerca del piano a que Milo acabe su turno. o B: Le dices se mueva del asiento, interrupiendolo.")

respuesta_milo = str(input())
print("Puntos de conexion con Milo:",contador_milo(respuesta_milo),"\n")

if respuesta_milo == "A" :
    print("Te sientas tranquilamente, cerca del piano, mientras escuchas como toca Milo. De pronto, sientes que te observan y cuando subes la mirada, ves que Milo te esta viendo.")
    print("Milo: Hey, ven sientante a mi lado.\n")
    print("Pasas una tarde tranquila junto a Milo y su musica. Es bastante relajante.\n")
if respuesta_milo == "B" :
    print("Le gritas agresivamente a Milo que se quite del piano interrumpiendo la cancion que tocaba.")
    print("Milo no te dice nada, solo toma sus cosas y se va, ya tuvo suficiente.\n")
    
print("TU-RU-RU-RUUUUU, alguien ha dejado 'CD inspirador' sobre el piano. ¿Quieres agregarla a tu inventario?")

respuesta_sn_item = str(input("Si o No: "))
print(agregar_inventario_item(respuesta_sn_item),"\n")

print("Tras el asunto del piano, te vas a tu clase extracurricular de pintura En este punto ya no te sorprenderia ver a Milo por ahi.")
print("Justo como lo esperaste ahi esta, sentado detras de un lienzo muy concentrado.")
print("El ejercico de hoy es pintar un personaje de anime. Quizas deberias pintar a Jotaro o a Josuke de JoJo's.")
print("El momento de la verdad llega y todos muestrn sus pinturas. Por supuesto la mejor es la de Milo")
print("Sientes envidia, mucha adimrasión y tu espirituo competitivo se pone alerta. A continuacion...\n")
print("A: Comienzas a aplaudir felicitando a todos, especialmente a Milo por sus magnificos trabajos. o B: Tomas con fuerza una brocha llena de pintura y rayoneas la pintura de Milo antes de que pueda hacer algo.")

respuesta_milo = str(input())
print("Puntos de conexion con Milo:",contador_milo(respuesta_milo),"\n")

if respuesta_milo == "A" :
    print("Todos comienzan a aplaudir contigo y el salon se llena de diferentes conversaciones sobre la increible pintura de Milo. Milo no te dice nada pero te regala una sonrisa complice.")
    print("Regresas a casa con las manos llenas de pintura, por suerte no sera tan dificil lavarlas.\n")
    print("Pasas una tarde tranquila junto a Milo y su musica. Es bastante relajante.\n")
if respuesta_milo == "B" :
    print("En cuanto rayas el cuadro en un ataque frenetico de celos, todo el salon se queda callado. No falta decir que la maestra te saco del salon por no respetar a Milo.")
    print("Vas en tu auto, probablemente disfurtando tu venganza contra Milo, cielos a veces puedes ser muy cruel.\n")

"""
========Día 3 (Final)========
"""
print("Ah el quitno día. Hoy veremos lo que los dioses han decidido para ti según carga karmática y el boost secreto.")
print("Veamos...")
print("Veamos...")
print("Veamos...")
destino = [puntos_de_conexion_milo,puntos_de_conexion_eli]
maxdestino = maximo(destino)
print(boost())
print(final(maxdestino))

print(num_items(items_totales))
print(logro_completado())

exit()