from itertools import permutations, product
from collections import deque

def es_palindromo(s: str) -> bool:
    """
    Determina si una cadena es un palíndromo. Una cadena es palíndromo si se lee
    igual de izquierda a derecha y de derecha a izquierda.
    """
    return s[::-1] == s
   

class GrafoDirigido:
    # Inicializo el Grafo vacío
    def __init__(self) -> None:
        self.vertices: list = []
        self.vecinos: dict = {}
      
    def agregar_vertice(self, vertice: str) -> None:

        # Verifica que el largo del string a ingresar y agrego el vértice

        if len(self.vertices) == 0:
            self.vertices.append(vertice)
            self.vecinos[vertice] = []

        elif len(self.vertices[0]) == len(vertice):
            self.vertices.append(vertice)
            self.vecinos[vertice] = []
        
        else:
            return "La palabra no tiene el largo correspondiente"
            
            
    def agregar_arista(self, origen: str, destino: str) -> None:

        # Agrego la arista dirigida entre los vértices definidos

        if origen in self.vertices and destino in self.vertices and origen != destino:
            self.vecinos[origen].append(destino)
        

    def __eq__(self, other: "GrafoDirigido") -> bool:
        """ compara dos grafos dirigidos (sin tener en cuenta el orden de los conjuntos de vertices y aristas)"""

        # Tomo las listas de vecinos ordenadas y las comparo.
        # Luego ordeno los diccionarios transformados en listas y comparo.
        return (sorted(self.vertices) == sorted(other.vertices) and
                 sorted((llave, sorted(valor)) for llave, valor in self.vecinos.items()) == 
                 sorted((llave, sorted(valor)) for llave, valor in other.vecinos.items()))


def generar_G_r(n: int, alfabeto: list[str]) -> GrafoDirigido | None:
    """
    Genera el grafo de reemplazos para todas las cadenas posibles de longitud `n`
    construidas a partir de un conjunto de caracteres (alfabeto) dado.

    En el grafo de reemplazos, los nodos representan todas las combinaciones
    posibles de caracteres de longitud `n` generadas a partir del alfabeto.
    Dos nodos `s` y `s'` están conectados mediante una arista dirigida de `s` a `s'`
    si `s'` puede obtenerse de `s` mediante una operación de reemplazo que cambia
    todas las ocurrencias de un carácter `char1` por otro carácter `char2`.

    Args:
        n (int): La longitud de las cadenas que forman los nodos del grafo.
        alfabeto (list[str]): Lista de caracteres usados para generar todas las
                                combinaciones posibles de longitud `n`.

    Returns:
        GrafoDirigido | None: El grafo de reemplazos generado. Retorna `None` si
                                `n` es 0 o si el alfabeto está vacío, ya que no
                                pueden generarse cadenas en estos casos.

    """

    # Inicializo un grafo vacío
    grafo_dirigido = GrafoDirigido()


    # Con Product creo todas las combinaciones posibles de vertices y los agrego al grafo.
    for v in ["".join(combination) for combination in list(product(alfabeto, repeat = n))]:
        grafo_dirigido.agregar_vertice(v)


    # Hago una lista de tuplas que contengan las posibles combinaciones de los reemplazos para crear las aristas.
    for vertice in grafo_dirigido.vertices:
        for replace in list(permutations(alfabeto, r = 2)):
            grafo_dirigido.agregar_arista(vertice, vertice.replace(replace[0], replace[1]))

    return grafo_dirigido



def distancia_a_palindromo(grafo: GrafoDirigido, start: str) -> int:
    """ 
    Utiliza un algoritmo BFS para encontrar la minima distancia 
    desde start a un palindromo en el grafo de reemplazos.
    
    """

    # Verifico que el vértice que pasa como start esté en el grafo.     
    if start in grafo.vertices:
        
        # Me fijo si es un palíndromo.
        if es_palindromo(start):
            return 0 

        # Visitado almacena todos los vértices por los que ya pasó.
        visitado = set()

        # queue almacena (vértice, profundidad).
        queue = deque([(start, 0)])  

        while queue:

            # Desempaqueto los valores del primer elemento de la cola.
            vertice, distancia = queue.popleft()

            # Verifico si es palíndromo.
            if es_palindromo(vertice):
                return distancia

            # Si el vertice no fue visitado lo agrego a los visitados.
            if vertice not in visitado:
                visitado.add(vertice)
                
                # Agrego a la cola los vecinos para recorrerlos si no lo visité antes.
                for vecino in grafo.vecinos[vertice]:
                    if vecino not in visitado:
                        queue.append((vecino, distancia + 1))

        # Si no se encuentra un palíndromo devuelve distancia -1.
        return -1
    
    else:
        return "El nodo no está en el Grafo"



# Ejemplo Básico:
grafo = generar_G_r(4, ["o", "n", "c", "e"])
print(grafo.vecinos)
print(distancia_a_palindromo(grafo, "once")) # Deberia devolver 2.
