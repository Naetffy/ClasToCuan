PROGRAMA SIMULACIÓN DE LO CLÁSICO A LO CUÁNTICO
Esta libreria esta desarrollado en python que permite la simulacion de experimentos clasicos y cuanticos.

Para empezar
Estas librerias desarrolladas para simulaciones de problemas que enrrollan la fisica cuantica, para su uso se debe tener en cuenta:

Prerequesitos:
1.Para el uso de la libreria es necesario tener instalado pyhton y configurado en la carpeta en la cual se quiere llamar a los experimentos.
2.Ser requiere tener instalado en la carpeta donde se va a usar el programa la libreria matplotlib.


Intalacion:
Para la instalacion de esta libreria se puede proceder de dos maneras.
    1.En la carpeta en la que se desea descargar la libreria hacer el uso de git y el comando git clone https://github.com/Naetffy/ClasToCuan.git de forma que se obtiene de manera directa la descarga completa de todos los archivos del repositorio dentro de una carpeta llamada VectSpace, dentro de la cual esta la libreria.
    2.En GitHub hacer la instalacion del repositorio descargandolo como un ZIP y extrayendo este en la carpeta en la cual se quiere hacer el uso de la libreria, esto nos creara una carpeta con el nombre "ClasToCuan-main", este lo cambiamos a "ClasToCuan".

Implemetacion:
Este repositorio se puede trabajar de dos formas, como archivo py o como libreria.

Para usar como un programa .py es de la siguiente forma:
Ejecutar el Experimento 1, 2 o 3.
El experimento 1 corresponde al experimento de las canicas, cuando lo ejecutes el programa procedera a pedirte el numero de vertices, cantidad de canicas en cada vertices y conecciones entre los vertices, posteriormente el progrma imprimira de manera automatica el grafo creado, y pedira al usuario en que click de tiempo quiere calcular el sistema, en este generara y imprimira el grafo en ese click de tiempo, posteriormente de maner automatica gnera el vector con el estado final del experimento del cual creara un grafico de barras.

El experimento 2 corresponde al experimento de las multiples rendijas, cuando lo ejecutes el programa procedera a pedirte el numero de rendijas, cantidad de objetivos y conecciones entre los vertices y las probabilidades de moverse en estas conecciones, posteriormente el progrma imprimira de manera automatica el grafo creado, y pedira al usuario en que click de tiempo quiere calcular el sistema, en este generara y imprimira el grafo en ese click de tiempo, posteriormente de maner automatica gnera el vector con el estado final del experimento del cual creara un grafico de barras.

El experimento 3 corresponde al experimento de las multiples rendijas cuanticas, cuando lo ejecutes el programa procedera a pedirte el numero de rendijas, cantidad de objetivos y conecciones entre los vertices y las probabilidades de moverse en estas conecciones representadas por numeros complejos, posteriormente el progrma imprimira de manera automatica el grafo creado con numero complejos y la matriz que representa el grafo en numeros reales para calcular la probabilidad, posteriormente de maner automatica genera el vector con el estado final del experimento del cual creara un grafico de barras.

Para usar como libreria en un proyecto es de la siguinte forma:
Para implementar la libreria en un proyecto se debe hacer el uso de la siguiente sintaxis from Cuantico import Cuantico, posteriormente se puede hacer el uso de cualquiera de las siguientes funciones:
    1.Cuantico.Marble(Lista,Matriz,Entero):Es una funcion que permite simular el experimento de las canicas.
    Parmetros: esta recibe como primer parametro el estado inicial de las canicas en forma de lista con elementos enteros, como segundo parametro recibe una lista de listas (Una matriz) que representa el grafo con las conexiones de los vertices, Como ultimo parametro recibe un entero que representa el tiempo en el cual quieres evaluar el estado final del sistema.
    Retorno: Esta funcion retorna una lista de enteros la cual representa el estado final del sitema despues de un determinado tiempo de click.

    Ejemplo: Cuantico.Marble([6,2,1,5,3,10],[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 0]],2)

    2.Cuantico.MultiR(Lista,Matriz):Es una funcion que permite simular el experimento de las multiples rendijas.
    Parmetros: Esta recibe como primer parametro el estado inicial del experimento de las multiples rendijas, como segundo parametro recibe una lista de listas (Una matriz) que como elementos tienen valores flotantes, que representa el grafo con las conexiones de los vertices.
    Retorno: Esta funcion retorna una lista de flotantes la cual representa el estado final del sitema despues de un determinado tiempo de click, este vector al sumar todos sus elementos debe dar 1, y este representa las probabilidades de la bala en caer en determinado objetivo.

    Ejemplo: Cuantico.MultR([[1], [0], [0], [0], [0], [0], [0], [0]],[[0, 0, 0, 0, 0, 0, 0, 0], [0.5, 0, 0, 0, 0, 0, 0, 0], [0.5, 0, 0, 0, 0, 0, 0, 0], [0, 0.33, 0.0, 1, 0, 0, 0, 0], [0, 0.33, 0.0, 0, 1, 0, 0, 0], [0, 0.33, 0.33, 0, 0, 1, 0, 0], [0, 0.0, 0.33, 0, 0, 0, 1, 0], [0, 0.0, 0.33, 0, 0, 0, 0, 1]])

    3.Cuantico.MultiRC(Lista,Matriz):Es una funcion que permite simular el experimento de las multiples rendijas cuanticas.
    Parmetros: Esta recibe como primer parametro el estado inicial del experimento de las multiples rendijas cuanticas, como segundo parametro recibe una lista de listas (Una matriz)que como elementos tienen valores complejos que se trabajan de la siguiente forma (Parte real,Parte imaginaria), que representa el grafo con las conexiones de los vertices.
    Retorno: Esta funcion retorna una lista de flotantes la cual representa el estado final del sitema despues de un determinado tiempo de click, este vector al sumar todos sus elementos debe dar 1, y se puede interpretar como las probabilidades de un foton en estar en esa posicion.
    
    Ejemplo: Cuantico.MultRC([1, 0, 0, 0, 0, 0, 0, 0],[[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0.7071, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),(0, 0)], [(0.7071, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), (-0.408, 0.408), (0.0, 0.0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), (-0.408, -0.408), (0.0, 0.0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), (0.408, -0.408), (-0.408, 0.408), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)], [(0, 0), (0.0, 0.0), (-0.408, -0.408), (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)], [(0, 0), (0.0, 0.0), (0.408, -0.408), (0, 0), (0, 0), (0, 0), (0, 0), (1, 0)]])

    4.Cuantico.grafics(Lista,Entero,Entero,Name):Es una funcion que permite graficar con un diagrama de barras las probabilidades de un vector de estados.
    Parametros:Como primer parametro permite una lista que representa un vector de estados, Segundo parametro es el numero de nodos o vertices que tenia el grafo representante del experimento que realizamos, como tercer parametro es el tiempo de cliks en el que se calculo el sitema, y por ultimo el nombre en el eje, por ejemplo, en el experimento de las canicas Name e igual a cantidad de canicas en un vertice, en el experimento de la multiple rendija es una probabilidad.
    retorna: un grafico de barra
    Ejemplo:grafics([0.0, 0.0, 0.0, 0.1664, 0.1664, 0.0, 0.1664, 0.1664],8,2,"Probabilidades")
Hecho con:
Math - Libreria que nos permite hacer operaciones matematicas como la raiz cuadrada.
matplotlib - Libreria que nos permite graficar informacion relevante del experimento.

Realizado por:
Mateo Sebastian Forero Fuentes
