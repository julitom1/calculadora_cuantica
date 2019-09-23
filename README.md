# libreria cuantica

Es una libreria para python capaz de calcular ciertos posibles comportamientos de los sistemas cuanticos. Esta libreria se importa con el nombre de calculadora_cuantica que se apoya a traves de la libreria de imaginar y calculadora_matrices.
El uso de esta libreria es mediante matrices, vectores, enteros, matrices imaginarias(los numeros imaginarios se representan mediante tuplas donde el primer numero representa la parte real y el segundo numero representa la parte imaginaria)
A continuacion se encuentra las operaciones que maneja:

Para utilizar la calculadora cuantica, se importa con: **import calculadora_cuantica**.

Para invocar la calculadora cuantica es cuestion de llamarla como calculadora_cuantica.funcion(el nombre de la funcion que desea usar) a continuacion se muestra el nombre de las funciones

**funciones de la calduladora cuantica:**

  **Sistemas determinadas clasicos: booleano(matriz,vector,n)**
  
  Calcula el estado actual de los nodos(elementos que contiene) despues de n clicks. Recibe una matriz booleana que el uno indica que el nodo se conecta con ese nodo, una lista que es el estado inicial de cada nodo y un entero que indica el numero de clicks que se van aplicar. Retorna el estado actual de la lista.
      
  **Sistemas probabilistico:   booleanoFraccion(matriz,vector,n)**
  
  Recibe una matriz con numeros probabilisticos para ir de un nodo a otro, un vector con las probabilidades actuales y un n que representa el numero de clicks. Retorna un vector con el sistema probabilistico de cada nodo.
  
  **Renijas :booleano(matriz,vector,n)**
    Muestra las probabilidades de llrgar a un nodo en 2 tiempos comenzando desde 0, Recibe 2 parametros n que representa el numero de renijas y m que indica los objetivos cuando pasa la renija, Devuelve la matriz en el segundo tiempo y el vector con informacion de cada nodo.
  
  **Sistema probabilisitico imaginario:  booleanoFraccionimaginarios(matrizValidar,vector,numero)**
  
  Recibe na matriz llena de tuplas, donde el primer numero de la tupla representa la parte real y el segundo numero la parte imaginaria, el vector que contiene la probabilidades en numeros imaginarios y el numero que representa el numero de clicks que se le va hacer a la matriz.

  
  
 
  # Autores
  
  *Yarit Yajanny Villalobos Jimenez
