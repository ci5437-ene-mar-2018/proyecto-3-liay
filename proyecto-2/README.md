# Objetivo

El objetivo del proyecto es aprender sobre el modelo de &aacute;rboles de juego
y algoritmos b&aacute;sicos de soluci&oacute;n. Trabajaremos con una versi&oacute;n
reducida del juego de Othello.

# Material entregado

Se entrega una representaci&oacute;n *incompleta* de la variant 6x6 de Othello (el juego
completo tiene un tablero 8x8), y un programa principal para evaluar los algoritmos
implementados. Tambi&eacute;n se incluye un art&iacute;culo en cuyo ap&eacute;ndice
se describe la versi&oacute;n 6x6 de Othello y una variaci&oacute;n principal del
mismo.

# Actividad 1

Completar y verificar la representaci&oacute;n dada del juego

# Actividad 2

Implementar los siguientes algoritmos para &aacute;rboles de juego:
* Negamax sin poda alpha-beta
* Negamax con poda alpha-beta
* Scout
* Negascout = negamax con poda alpha-beta + scout

# Actividad 3

Para asegurarnos que la implementaci&oacute;n de los algoritmos es
correcta, evaluamos los mismos a lo largo de la *variaci&oacute;n principal*.
El valor del juego es -4 y por lo tanto, todo nodo sobre la variaci&oacute;n
principal debe evaluar a dicho valor.

Para cada algoritmo, la evaluaci&oacute;n se hace comenzando sobre el 
tablero terminal en la variaci&oacute;n principal, y subimos a lo
largo de la misma. Cada vez que subimos, volvemos a ejecutar el algoritmo
de soluci&oacute;n a partir del nodo actual hasta que termine o hasta
que el l&iacute;mite de tiempo expire.

El mejor algoritmo es aquel que puede llegar m&aacute;s lejos (arriba)
sobre la variaci&oacute;n principal.

# Entregables

Se debe entregar, en el repositorio, todo el c&oacute;digo implementado,
los resultados experimentales, y un peque&ntilde;o informe, preferiblemente
en formato .md, que describa lo que hicieron y sus conclusiones.

