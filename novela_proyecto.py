print("Elige tu nombre:")

n=str(input())

while True:
    print("Escribe tu pronombre:ella,él o elle")
    pronombre_jugador=input()
    if pronombre_jugador == "ella":
        y="a"
        z="la"
        f="a"
        break
    elif pronombre_jugador == "él":
        y="o"
        z="el"
        v="e"
        f=""
        break
    elif pronombre_jugador == "elle":
        y="x"
        f="x"
        break
    else:
        print("Pronombres disponibles por el momento: él, ella, elle (lamento las molestias >_< )")
    continue

print("Hola %s ¿list%s para la aventura?\n"%(n,y))
print("Comencemos por lo básico. Tú eres %s, un%s estudiante de nuevo ingreso en la Universidad X. No conoces a nadie… aún."%(n,f))
print("Pero no te preocupes, esta es tu historia, tendrás el poder de elegir y fortalecer los vínculos que hagas.\n")
print("Mira, practiquemos un poco la toma decisiones.")
print("Supongamos que tu mejor amigo está triste,¿Qué harías para hacerlo sentirse mejor?\n")
print("A: Darle un abrazo para reconfortarlo o B: Burlarte de sus sentimientos")

respuesta=input()

if respuesta == "A":
     elecciones= +2
elif respuesta == "B":
     elecciones= -1
puntos_de_conexion = 0 + elecciones

print("Puntos de conexión:\n",puntos_de_conexion)
if puntos_de_conexion == -1:
    print("Oh no, eso no es lo que hace un%s buen%s amig%s. Tendrás que ser penalizado."%(f,y,y))

print("Cómo viste, en la vida tus decisiones importan, si eres bueno tus puntos de conexión subirán y cosas buenas pasarán...\n""De lo contrario, vivirás consecuencias catastróficas. No digas que no te lo advertí.\n")
print("¿No hay dudas? Perfecto. Que la diversión comience.\n")

print("Es hoy, el primer día en la Universidad X.¿Qué llevarás contigo?")
print("Objetos: computadora gamer o tu saga favorita de libros.")

item=input()
exit()
