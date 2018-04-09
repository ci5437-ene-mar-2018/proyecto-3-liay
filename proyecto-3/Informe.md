#### Proyecto 3

##### Inteligencia Artificial I 

###### Autores:
* Lautaro Villalón 12-10427
* Yarima Luciani 13-10770


#### Implementación 

* Se realizaron tres módulos: generator.py, translator.py y solveNonogram.py.

* El módulo generator.py contiene todo el código relacionado con la codificación de un nonograma en teorías proposicionales, las cuales están en formato CNF y son aceptadas por el SAT solver usado (minisat). Contiene los siguientes procedimientos:
  * appendable: define si una regla puede ocurrir al mismo tiempo que una regla anterior
  * filterRules: filtra las reglas de dos bloques de manera que se mantenga el orden entre ambos, elimina reglas que son imposibles de llevar a cabo debido al orden y agrega reglas que mantienen al mismo. 
  * addNecessaryConditions: dadas las reglas de los bloques de una fila o columna, devuelve las reglas que definen la razón por la cual un píxel esta prendido. 
  * createRule: devuelve las reglas por bloque de una fila o columna. Utiliza los procedimientos filterRules y addNecessaryConditions. 
  * rulesFromBoard: recorre el tablero por filas y columnas, guardando todas las reglas por cada uno de los bloques. Utiliza el procedimiento createRule.
  * createBoard: crea un tablero con sus variables, representado como una lista de listas.
  * readHints: dado un file descriptor, devuelve una lista con todas las pistas. 
  * readFromFile: lee un archivo con extensión .non para obtener los datos de un nonograma. Utiliza los procedimientos readHints y createBoard. 
  * addUnicityRules: dada una lista de reglas por bloque, agrega las reglas de unicidad: sólo puede ocurrir una de las reglas por cada bloque. 
  * printToFile: guarda los resultados obtenidos en formato CNF en un archivo .sat, el cual va a ser leído por el minisat.  
  * encoder: dado el nombre de un archivo con extensión .non y otro con extensión .sat, lee el .non, codifica las reglas y las guarda en el archivo .sat. Utiliza los procedimientos readFromFile, rulesFromBoard, addUnicityRules y printToFile. 
  * satFilename: dado el nombre de un archivo con cualquier extensión, devuelve el nombre del mismo archivo pero ahora con extensión .sat en el directorio satFiles. 

 * El módulo translator.py decodifica la solución de un nonograma dada por el SAT solver minisat y guarda la representación del resultado en una imagen con formato .pbm. Contiene los siguientes procedimientos:
   * decoder: abre un archivo con la solución de un nonograma dada por el minisat y devuelve un arreglo con los píxeles que deben estar prendidos. 
   * createImage: dada una solución decodificada, las filas y las columnas del nonograma, guarda una imagen con formato .pbm que representa dicha solución. 
   * imageFileName: dado el nombre de un archivo con cualquier extensión, devuelve el nombre del mismo archivo pero ahora con extensión .pbm en el directorio images. 

* El módulo solveNonogram.py posee el programa principal, el cual toma un archivo .non correspondiente a un caso de prueba, lo codifica utilizando generator.py y dependiendo de las opciones dadas, llama al comando minisat sobre el archivo resultante del generador y guarda el resultado y sus estadísticas, en los directorios results y statistics respectivamente o utiliza translator.py para generar la imagen resultante. 


#### Uso

python3 solveNonogram.py archivo_non [-i, --image] [-m, --minisat] [-h, --help]

#### Requerimientos: 

* Python 3.x
* minisat 2.2 (el comando minisat debe ser global)


#### Conclusiones 

* El codificador generator.py funciona y es eficiente para todos los casos de prueba dados. 

* El SAT solver minisat resuelve casi todos los casos de prueba proporcionados en un corto tiempo (menos de 5 segundos en su mayoría), a excepción de los siguientes: knotty, meow, faase y webpbn-22336.  

* La codificación de las imágenes es la esperada. La mayoría se puede apreciar claramente. 


##### Nota: 

* Las reglas están definidas como claves en un diccionario que representa el bloque.

* Los archivos .sat no se incluyen en el repositorio debido a que son muy pesados. 

* Para generar la imagen correspondiente al resultado de un nonograma sin utilizar la opción -m, es necesario haber utilizado dicha opción anteriormente sobre el mismo archivo para obtener el resultado.

* No se pudieron incluir los resultados y las estadísticas de los casos de prueba knotty, meow, faase y webpbn-22336, debido a los largos tiempo de corrida del minisat (todavía no han terminado). 