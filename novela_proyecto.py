

"""
========Contador========
"""
puntos_de_conexion = 0
def contador(respuesta):
    if(respuesta == "A"):
        eleccion = 2
    elif(respuesta == "B"):
        eleccion = -1
    return float(puntos_de_conexion + eleccion)
    
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
print("Objetos: computadora gamer o tu saga favorita de libros.")

item = input()
exit()
#(Muchas gracias por la recomendación del parámetro, ya lo corregí, en la semana tec estaré haciendo más avances en el código)