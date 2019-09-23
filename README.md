# libreria cuantica

Es una libreria para python capaz de calcular ciertos posibles comportamientos de los sistemas cuanticos. Esta libreria se importa con el nombre de calculadora_cuantica que se apoya a traves de la libreria de imaginar y calculadora_matrices.
El uso de esta libreria es mediante matrices, vectores, enteros, matrices imaginarias(los numeros imaginarios se representan mediante tuplas donde el primer numero representa la parte real y el segundo numero representa la parte imaginaria)
A continuacion se encuentra las operaciones que maneja:

Para utilizar la calculadora cuantica, se importa con: **import calculadora_cuantica**.

Para invocar la calculadora cuantica es cuestion de llamarla como calculadora_cuantica.funcion(el nombre de la funcion que desea usar) a continuacion se muestra el nombre de las funciones

**funciones de la calduladora cuantica:**

  **Sistemas determinadas clasicos: booleano(matriz,vector,n)**
  
  Calcula el estado actual de los nodos(elementos que contiene) despues de n clicks. Recibe una matriz booleana que el uno indica que el nodo se conecta con ese nodo, una lista que es el estado inicial de cada nodo y un entero que indica el numero de clicks que se van aplicar. Retorna el estado actual de la lista.
      
  **Inversa de vectores complejos:   inversa_vectores(lista1)**
  
  Recibe una lista y retorna una lista que contiene la inversa de la lista enviada.
  
  **Multiplicación escalar de vectores complejos:producto_escalar(tupla1,lista1)**
  
  Recibe una tupla de longitud 2 y una lista retorna una lista que contiene la multiplicacion de la tupla con cada componente de la lista.
  
  **Adición de matrices complejos: adicion_matrices(matriz1,matriz2):**
  
  Recibe dos matrices y retorna una matriz que contiene la suma de elemento por elemento de las dos matrices enviadas.
  
  **Inversa de matrices complejos:  inversa(matriz1)** 
  
  Recibe una matriz y devuelve una matriz que contiene la inversa de la matriz.
  
  **Multiplicación escalar de matrices complejas: multiplicacion_escalar_matrices(tupla1,matriz1)**
  
  Recibe una tupla y una matriz y retorna una matriz que contiene la multiplicacion de la tupla con cada componente.
  
  **Matriz transpuesta: transpuesta(matriz1)**
  
  Recibe una matriz y retorna la matriz que contiene la transpuesta de la matriz enviada
  
  **Matriz conjugada:           conjugada(matriz1)** 
  
  Recibe una matriz y retorna una matriz que contiene el signo contrario en la parte imaginaria
  
  **Matriz adjunta:                 adjunta(matriz1)**   
  
  Recibe una matriz y retorna una matrizque contiene la adjunta de la matriz enviada
  
  **Norma de matrices: norma(matriz)**
  
  Recibe una matriz y retorna un float que representa la norma de la matriz.
  
  **Distancia entrematrices: distancia_matrices(matriz1,matriz2)**
  
  Recibe 2 matrices del mismo tamaño y retorna un numero flotante que representa la distancia entre las dos matrices.
  
  **Revisar si es unitaria: matriz_unitaria(matriz1)**
  
  Recibe una matriz y retorna y retorna un booleano diciendo si es una matriz unitaria o no.
  
  **Revisar si es Hermitian:matriz_hermitiana(matriz)**
  
  Recibe una matriz y retorna y retorna un booleano diciendo si es una matriz hermitiana o no.
  
  **Producto tensor: producto_tensor(matriz1,matriz2)**
  
  Recibe 2 matrices y retorna una matriz con el producto tensor de las dos matrices enviadas.
  
 
  # Autores
  
  *Yarit Yajanny Villalobos Jimenez
