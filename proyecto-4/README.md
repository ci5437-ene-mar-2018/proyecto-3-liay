#### Proyecto 4

##### Inteligencia Artificial I 

##### Solucionador del rompecabezas Tents con MiniZinc

###### Autores:
* Lautaro Villalón 12-10427
* Yarima Luciani 13-10770


#### Implementación 

* Se realizaron dos módulos: tentSolver.mzn y solveTents.py.

* El módulo tentSolver.mzn, escrito en MiniZinc, contiene el modelado del juego, la llamada al solucionador de MiniZinc y las restricciones del juego, las cuales son:

  * Pistas: Para cada pista, de una columna o fila, debe haber esa cantidad exacta de Carpas en su respectiva columna o fila.
  * Relación con Árboles: Para cada Árbol, debe haber una carpa perpendicular y adyacente a él.
  * Carpas sobre Árboles: No debe haber una Carpa sobre un Árbol.
  * Carpas sin Vecinos: Para cada Carpa, no deben haber más Carpas en sus alrededores. 

* El módulo solveTents.py posee el programa principal, el cual toma un archivo .dzn correspondiente a un caso de prueba del juego, llama al comando minizinc sobre el archivo, guarda el resultado en el directorio results y lo muestra en pantalla.

#### Uso

python3 solveTents.py archivo_dzn [-h, --help]

##### Requerimientos: 

* Python 3.x
* MiniZinc (el comando minizinc debe ser global)


#### Conclusiones 

* MiniZinc permite la especificación de un problema de satisfacibilidad a mayor nivel que MiniSat, permitiendo el uso de variables, arreglos y otras estructuras para modelar el problema; siendo así, flexible y potente.

* Todos los casos de prueba, hasta ahora, son satisfacibles y funciona la solución.


##### Nota: 

* MiniZinc no se incluye en el repositorio debido a que es muy pesado. 

* El tablero resultante es una matriz con los siguientes números: 1=Carpa, 2=Árbol, 0=Vacío.
