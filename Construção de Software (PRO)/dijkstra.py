#!/usr/bin/env python3
"""
Algoritmo de Dijkstra - Solução do problema "Dijkstra?" do Codeforces
Implementação clean code com separação de responsabilidades.

Problema: https://codeforces.com/problemset/problem/20/C
Encontrar o caminho mais curto do vértice 1 ao vértice n em um grafo ponderado.
"""

import heapq
from typing import Dict, List, Tuple, Optional, Set
from dataclasses import dataclass
import sys


@dataclass
class Aresta:
    """Representa uma aresta do grafo com destino e peso."""
    destino: int
    peso: int


class Grafo:
    """Estrutura de dados para representar um grafo ponderado."""
    
    def __init__(self, n: int) -> None:
        """Inicializa um grafo com n vértices."""
        self._adjacencias: Dict[int, List[Aresta]] = {i: [] for i in range(1, n + 1)}
    
    def adicionar_aresta(self, origem: int, destino: int, peso: int) -> None:
        """
        Adiciona uma aresta bidirecional ao grafo.
        
        Args:
            origem: Vértice de origem
            destino: Vértice de destino
            peso: Peso da aresta
        """
        self._adjacencias[origem].append(Aresta(destino, peso))
        self._adjacencias[destino].append(Aresta(origem, peso))
    
    def obter_vizinhos(self, vertice: int) -> List[Aresta]:
        """
        Retorna os vizinhos de um vértice.
        
        Args:
            vertice: Vértice para obter vizinhos
            
        Returns:
            Lista de arestas conectadas ao vértice
        """
        return self._adjacencias.get(vertice, [])


class DijkstraSolver:
    """Solver para o problema Dijkstra? do Codeforces."""
    
    @staticmethod
    def encontrar_caminho_mais_curto(
        grafo: Grafo, 
        origem: int, 
        destino: int,
        n: int
    ) -> Tuple[Optional[int], Optional[List[int]]]:
        """
        Encontra o caminho mais curto entre dois vértices usando Dijkstra.
        
        Args:
            grafo: Grafo ponderado onde buscar o caminho
            origem: Vértice de origem
            destino: Vértice de destino
            n: Número total de vértices
            
        Returns:
            Tupla contendo:
            - Distância mínima (None se não houver caminho)
            - Lista com o caminho (None se não houver caminho)
        """
        # Inicialização
        distancias: List[int] = [float('inf')] * (n + 1)
        predecessores: List[Optional[int]] = [None] * (n + 1)
        visitados: Set[int] = set()
        
        distancias[origem] = 0
        fila_prioridade: List[Tuple[int, int]] = [(0, origem)]
        
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
        
        # Verificar se há caminho
        if distancias[destino] == float('inf'):
            return None, None
        
        # Reconstruir caminho
        caminho = DijkstraSolver._reconstruir_caminho(predecessores, origem, destino)
        return distancias[destino], caminho
    
    @staticmethod
    def _reconstruir_caminho(
        predecessores: List[Optional[int]], 
        origem: int, 
        destino: int
    ) -> List[int]:
        """
        Reconstrói o caminho a partir dos predecessores.
        
        Args:
            predecessores: Lista de predecessores
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


def resolver_codeforces() -> None:
    """
    Resolve o problema "Dijkstra?" do Codeforces.
    
    Input:
    - Primeira linha: n (vértices) e m (arestas)
    - Próximas m linhas: a, b, w (aresta de a para b com peso w)
    
    Output:
    - Se não há caminho: -1
    - Se há caminho: caminho do vértice 1 ao vértice n
    """
    # Leitura da entrada
    n, m = map(int, input().split())
    
    # Criar grafo
    grafo = Grafo(n)
    
    # Adicionar arestas
    for _ in range(m):
        a, b, w = map(int, input().split())
        grafo.adicionar_aresta(a, b, w)
    
    # Encontrar caminho mais curto do vértice 1 ao vértice n
    distancia, caminho = DijkstraSolver.encontrar_caminho_mais_curto(grafo, 1, n, n)
    
    # Saída
    if distancia is None or caminho is None:
        print(-1)
    else:
        print(' '.join(map(str, caminho)))


def demonstracao() -> None:
    """
    Demonstração do algoritmo com exemplo do Codeforces.
    
    Exemplo de entrada:
    5 6
    1 2 2
    2 5 5
    2 3 4
    1 4 1
    4 3 3
    3 5 1
    
    Saída esperada: 1 4 3 5
    """
    print("🏆 Solução do problema 'Dijkstra?' - Codeforces")
    print("=" * 55)
    print("Exemplo de entrada:")
    print("5 6")
    print("1 2 2")
    print("2 5 5")
    print("2 3 4")
    print("1 4 1")
    print("4 3 3")
    print("3 5 1")
    print("=" * 55)
    
    # Simular entrada do exemplo
    n, m = 5, 6
    grafo = Grafo(n)
    
    arestas = [
        (1, 2, 2),
        (2, 5, 5),
        (2, 3, 4),
        (1, 4, 1),
        (4, 3, 3),
        (3, 5, 1)
    ]
    
    for a, b, w in arestas:
        grafo.adicionar_aresta(a, b, w)
    
    # Resolver
    distancia, caminho = DijkstraSolver.encontrar_caminho_mais_curto(grafo, 1, n, n)
    
    print(f"Caminho mais curto de 1 para {n}:")
    if distancia is not None and caminho is not None:
        print(f"Distância: {distancia}")
        print(f"Caminho: {' → '.join(map(str, caminho))}")
        print(f"Saída Codeforces: {' '.join(map(str, caminho))}")
    else:
        print("Não há caminho disponível")
        print("Saída Codeforces: -1")
    
    print("=" * 55)
    print("\n📝 Documentação do Código:")
    print("- Classe Aresta: Representa aresta com destino e peso")
    print("- Classe Grafo: Estrutura do grafo com lista de adjacências")
    print("- Classe DijkstraSolver: Implementação do algoritmo")
    print("- Função resolver_codeforces(): Lê entrada e resolve problema")
    print("- Complexidade: O((V + E) log V)")
    print("- Usa heapq para fila de prioridade otimizada")


def main() -> None:
    """
    Função principal - escolhe entre demonstração ou resolver problema.
    """
    if len(sys.argv) > 1 and sys.argv[1] == "--codeforces":
        resolver_codeforces()
    else:
        demonstracao()


if __name__ == "__main__":
    main()