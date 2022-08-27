# Proyecto: Novela interactiva

Este proyecto consiste en crear una novela interactiva dónde tú cómo jugador tengas el poder de tomar distintas decisiones a lo largo del juego. En esta aventura el jugador conocerá distintos personajes con los que podrá entablar una amistad o una relación romántica y podrá desbloquear distintos finales dependiendo de las opciones que haya elegido. Por cada personaje habrán 3 finales: uno bueno, uno neutral y uno malo. Además, entre los diálogos e interacciones habrá un final secreto que sólo se rebelará sí se presentan las condiciones adecuadas.

# La razón detrás del proyecto :D

Durante la pandemia yo, cómo muchas otras personas, sufrí de aislamiento y tuve varios problemas emocionales debido a la falta de interacción humana. Sin embargo, durante esta época descubrí el mundo de los videojuegos y esto me ayudó a mantener mi estabilidad emocional. En este proyecto mi intención es crear una fuente de entretenimiento que ayude a las personas a sobrellevar momentos de soledad o de tristeza y que en forma indirecta deje alguna enseñanza.

# Algoritmo

### Nombre del jugador

imprimir(Elige tu nombre)
si nombre_jugador=Usuario1
n=nombre_jugador

### Pronombres del jugador

imprimir(Escribe tu pronombre)
si pronombre_jugador=ella
  y=pronombre_jugador

si pronombre_jugador=él
  y=pronombre_jugador

si pronombre_jugador=elle
  y=pronombre_jugador

si pronombre_jugador no es ninguna de las anteriores
  imprimir(Pronombres disponibles por el momento: él, ella, elle (lamento las molestias >_< ))
  
### terminación de adjetivos 
 
 si pronombre_jugador=ella
  z=a

si pronombre_jugador=él
  z=o

si pronombre_jugador=elle
  z=x
  
### Diálogos
imprimir(Diálogo 1)
imprimir(Respuesta A)
imprimir(Respuesta B)
imprimir(Respuesta C)

  si jugador elige=Respuesta A
    imprimir(Reacción a A)
    sumar +2 a puntos_de_conexión
    
  si jugador elige=Respuesta B
    imprimir(Reacción a B)
    sumar +1 a puntos_de_conexión

  si jugador elige=Respuesta C
    imprimir(Reacción a C)
    sumar +0 a puntos_de_conexión
 
### Puntos de conexión

  si al final del juego puntos_de_conexión < o = 10 es Final malo
  si al final del juego puntos_de_conexión = 11 o <22 es Final neutral
  si al final del juego puntos_de_conexión = 22 o < o = 30 Final bueno
  
(Este es el esqueleto de la novela)
