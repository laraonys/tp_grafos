from itertools import permutations, product
from collections import deque

def es_palindromo(s: str) -> bool:
    """
    Determina si una cadena es un palíndromo. Una cadena es palíndromo si se lee
    igual de izquierda a derecha y de derecha a izquierda.
    """
    return s[::-1] == s
   

class GrafoDirigido:
    def __init__(self) -> None:
        self.vertices: list = []
        self.vecinos: dict = {}
      
    def agregar_vertice(self, vertice: str) -> None:

        if len(self.vertices) == 0:
            self.vertices.append(vertice)
            self.vecinos[vertice] = []

        elif len(self.vertices[0]) == len(vertice):
            self.vertices.append(vertice)
            self.vecinos[vertice] = []
        
        else:
            return "La palabra no tiene el largo correspondiente"
            
            
    def agregar_arista(self, origen: str, destino: str) -> None:

        if origen in self.vertices and destino in self.vertices:
            self.vecinos[origen].append(destino)
        

    def __eq__(self, other: "GrafoDirigido") -> bool:
        """ compara dos grafos dirigidos (sin tener en cuenta el orden de los conjuntos de vertices y aristas)"""
        
        return (sorted(self.vertices) == sorted(other.vertices) and sorted(self.vecinos.items()) == sorted(other.vecinos.items()))
    
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
    # Completar 
    ...

def distancia_a_palindromo(grafo: GrafoDirigido, start: str) -> int:
    """ utiliza un algoritmo BFS para encontrar la minima distancia desde start
    a un palindromo en el grafo de reemplazos"""
    # Completar 
    ...


# Ejemplo Básico:
grafo = generar_G_r(4, ["o", "n", "c", "e"])
print(grafo.vecinos)
print(distancia_a_palindromo(grafo, "once")) # Deberia devolver 2.