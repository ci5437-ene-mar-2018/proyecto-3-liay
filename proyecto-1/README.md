# Objetivo

El objetivo del proyecto es aprender sobre el modelo de espacio de estados y sobre
los diferentes algoritmos de b&uacute;squeda heur&iacute;stica. No s&oacute;lo se
evaluar&aacute; la correctitud de la implementaci&oacute;; es importante que los
algoritmos sean eficientes y puedan resolver los problemas propuestos en los
tiempos estipulados.

# Problemas

Consideramos los siguientes problemas:
* N-puzzles: 15-puzzle y 24-puzzle
* Cubo de Rubik: 3x3x3
* Top spin: 12-4, 14-4, y 17-4
* Torre de Hanoi con 4 astas: 12, 14, y 18 discos

# &Aacute;rboles de b&uacut;squeda

Estudiar los &aacute;rboles de b&uacute;queda y su factor de ramificaci&oacute;on sin
eliminaci&oacute;on de duplicados y con eliminaci&oacute;on parcial de duplicados.
Se deben crear tablas para cada problema donde se reporte el nu&uacute;mero de estados
a cada profundidad en el &aacute;rbol de b&uacute;squeda a partir del estado goal,
hasta las profundidad m&aacute;xima que se alcance en 15 minutos de ejecuci&oacute;n.

# Heur&iacute;sticas

Se deben implementar heur&iacute;sticas PDBs para cada problema. Para los n-puzzles
las PDBs deben ser aditivas. Para los otros problemas, se toma el m&aacute;ximo de
varias PDBs. Leer el paper "Additive Pattern Databases" de Felner et al. que se
incluye, y el paper sobre el Cubo de Rubik.

# Algoritmos informados

Estudiar la b&uacute;squeda de *soluciones &oacute;ptimas* con algoritmos informados.
Buscar soluciones para las instancias dadas en cada problema utilizando los algoritmos:
A* con eliminaci&oacute;n parcial de duplicados (DDD) e IDA*. Para las heur&iacute;sticas
en cada problema:
* N-puzzles: distancia Manhattan y diferentes additive PDBs
* Cubo de Rubik: max de corner PDB y 2 edge PDBs
* Top Spin: max de diferents PDBs
* Torre de Hanoi con 4 astas: max de diferentes PDBs

El tiempo m&aacute;ximo de ejecuci&oacute;n lo deciden ustedes seg&uacute;n los
recursos que tengan a su disposici&oacute;n. Para A*, no permitan que el programa
utilice memoria virtual (i.e. paginaci&oacute;n sobre disco) ya que corre extremadament
lento y no podr&aacute;n resolver el problema (y la m&aacute;quina se les "congelar&aacute;").

# Casos de prueba

Se entregan casos de prueba para los n-puzzles y para el Cubo de Rubik. Para los
problema restantes deben generar casos de prueba con el programa global/generator.cc
que se entrega en la distribuci&oacute;n de PSVN. Leer el programa para entenderlo
y poder ejecutarlo. Se deben generar casos de prueba f&aacute;ciles y dif&iacute;ciles.


