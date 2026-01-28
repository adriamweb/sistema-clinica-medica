#!/usr/bin/env python3
"""
Algoritmo de Dijkstra - Caminho Mais Curto em Grafo Ponderado
Implementação clean code com separação de responsabilidades.
"""

import heapq
from typing import Dict, List, Tuple, Optional, Set
from dataclasses import dataclass


@dataclass
class Aresta:
    """Representa uma aresta do grafo com destino e peso."""
    destino: str
    peso: float


class Grafo:
    """Estrutura de dados para representar um grafo ponderado."""
    
    def __init__(self) -> None:
        """Inicializa um grafo vazio."""
        self._adjacencias: Dict[str, List[Aresta]] = {}
    
    def adicionar_vertice(self, vertice: str) -> None:
        """
        Adiciona um vértice ao grafo.
        
        Args:
            vertice: Nome do vértice a ser adicionado
        """
        if vertice not in self._adjacencias:
            self._adjacencias[vertice] = []
    
    def adicionar_aresta(self, origem: str, destino: str, peso: float) -> None:
        """
        Adiciona uma aresta direcionada ao grafo.
        
        Args:
            origem: Vértice de origem
            destino: Vértice de destino
            peso: Peso da aresta (deve ser não-negativo)
        """
        if peso < 0:
            raise ValueError("Dijkstra não funciona com pesos negativos")
        
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        self._adjacencias[origem].append(Aresta(destino, peso))
    
    def obter_vizinhos(self, vertice: str) -> List[Aresta]:
        """
        Retorna os vizinhos de um vértice.
        
        Args:
            vertice: Vértice para obter vizinhos
            
        Returns:
            Lista de arestas conectadas ao vértice
        """
        return self._adjacencias.get(vertice, [])
    
    def obter_vertices(self) -> Set[str]:
        """
        Retorna todos os vértices do grafo.
        
        Returns:
            Conjunto com todos os vértices
        """
        return set(self._adjacencias.keys())


class Dijkstra:
    """Implementação do algoritmo de Dijkstra."""
    
    @staticmethod
    def encontrar_caminho_mais_curto(
        grafo: Grafo, 
        origem: str, 
        destino: str
    ) -> Tuple[Optional[float], Optional[List[str]]]:
        """
        Encontra o caminho mais curto entre dois vértices usando Dijkstra.
        
        Args:
            grafo: Grafo ponderado onde buscar o caminho
            origem: Vértice de origem
            destino: Vértice de destino
            
        Returns:
            Tupla contendo:
            - Distância mínima (None se não houver caminho)
            - Lista com o caminho (None se não houver caminho)
            
        Raises:
            ValueError: Se origem ou destino não existirem no grafo
        """
        vertices = grafo.obter_vertices()
        
        if origem not in vertices:
            raise ValueError(f"Vértice de origem '{origem}' não existe no grafo")
        if destino not in vertices:
            raise ValueError(f"Vértice de destino '{destino}' não existe no grafo")
        
        # Inicialização
        distancias: Dict[str, float] = {v: float('inf') for v in vertices}
        predecessores: Dict[str, Optional[str]] = {v: None for v in vertices}
        visitados: Set[str] = set()
        
        distancias[origem] = 0
        fila_prioridade: List[Tuple[float, str]] = [(0, origem)]
        
        while fila_prioridade:
            distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)
            
            if vertice_atual in visitados:
                continue
                
            visitados.add(vertice_atual)
            
            # Se chegamos ao destino, podemos parar
            if vertice_atual == destino:
                break
            
            # Relaxamento das arestas
            for aresta in grafo.obter_vizinhos(vertice_atual):
                if aresta.destino not in visitados:
                    nova_distancia = distancia_atual + aresta.peso
                    
                    if nova_distancia < distancias[aresta.destino]:
                        distancias[aresta.destino] = nova_distancia
                        predecessores[aresta.destino] = vertice_atual
                        heapq.heappush(fila_prioridade, (nova_distancia, aresta.destino))
        
        # Reconstruir caminho
        if distancias[destino] == float('inf'):
            return None, None
        
        caminho = Dijkstra._reconstruir_caminho(predecessores, origem, destino)
        return distancias[destino], caminho
    
    @staticmethod
    def _reconstruir_caminho(
        predecessores: Dict[str, Optional[str]], 
        origem: str, 
        destino: str
    ) -> List[str]:
        """
        Reconstrói o caminho a partir dos predecessores.
        
        Args:
            predecessores: Dicionário de predecessores
            origem: Vértice de origem
            destino: Vértice de destino
            
        Returns:
            Lista ordenada com o caminho da origem ao destino
        """
        caminho = []
        atual = destino
        
        while atual is not None:
            caminho.append(atual)
            atual = predecessores[atual]
        
        caminho.reverse()
        return caminho


def main() -> None:
    """Demonstração do algoritmo de Dijkstra."""
    # Criar grafo de exemplo
    grafo = Grafo()
    
    # Adicionar arestas (origem, destino, peso)
    arestas = [
        ("A", "B", 4),
        ("A", "C", 2),
        ("B", "C", 1),
        ("B", "D", 5),
        ("C", "D", 8),
        ("C", "E", 10),
        ("D", "E", 2)
    ]
    
    for origem, destino, peso in arestas:
        grafo.adicionar_aresta(origem, destino, peso)
    
    print("🗺️  Algoritmo de Dijkstra - Caminho Mais Curto")
    print("=" * 50)
    print("Grafo de exemplo:")
    print("A → B (4), A → C (2)")
    print("B → C (1), B → D (5)")
    print("C → D (8), C → E (10)")
    print("D → E (2)")
    print("=" * 50)
    
    # Encontrar caminhos
    casos_teste = [("A", "E"), ("A", "D"), ("B", "E"), ("A", "F")]
    
    for origem, destino in casos_teste:
        try:
            distancia, caminho = Dijkstra.encontrar_caminho_mais_curto(grafo, origem, destino)
            
            if distancia is not None and caminho is not None:
                print(f"Caminho de {origem} para {destino}:")
                print(f"  Distância: {distancia}")
                print(f"  Caminho: {' → '.join(caminho)}")
            else:
                print(f"Não há caminho de {origem} para {destino}")
        except ValueError as e:
            print(f"Erro: {e}")
        print()


if __name__ == "__main__":
    main()