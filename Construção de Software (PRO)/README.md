# Algoritmo de Dijkstra - Caminho Mais Curto

Implementação clean code do algoritmo de Dijkstra para encontrar o caminho mais curto em grafos ponderados.

## 🎯 Funcionalidades

- ✅ Encontra o caminho mais curto entre dois vértices
- ✅ Suporte a grafos ponderados direcionados
- ✅ Validação de pesos não-negativos
- ✅ Estrutura de dados separada (Clean Code)
- ✅ Type Hints completos
- ✅ Documentação detalhada

## 🛠️ Requisitos

- Python 3.7 ou superior
- Bibliotecas padrão: `heapq`, `typing`, `dataclasses`

## 🚀 Como Executar

### Windows
```cmd
cd "Construção de Software (PRO)"
python dijkstra.py
```

### Linux/macOS
```bash
cd "Construção de Software (PRO)"
python3 dijkstra.py

# Ou tornar executável
chmod +x dijkstra.py
./dijkstra.py
```

## 📖 Exemplo de Uso

```python
from dijkstra import Grafo, Dijkstra

# Criar grafo
grafo = Grafo()
grafo.adicionar_aresta("A", "B", 4)
grafo.adicionar_aresta("A", "C", 2)
grafo.adicionar_aresta("B", "D", 5)

# Encontrar caminho mais curto
distancia, caminho = Dijkstra.encontrar_caminho_mais_curto(grafo, "A", "D")

print(f"Distância: {distancia}")  # 9
print(f"Caminho: {' → '.join(caminho)}")  # A → B → D
```

## 📊 Saída Esperada

```
🗺️  Algoritmo de Dijkstra - Caminho Mais Curto
==================================================
Grafo de exemplo:
A → B (4), A → C (2)
B → C (1), B → D (5)
C → D (8), C → E (10)
D → E (2)
==================================================
Caminho de A para E:
  Distância: 7.0
  Caminho: A → C → B → D → E

Caminho de A para D:
  Distância: 5.0
  Caminho: A → C → B → D

Caminho de B para E:
  Distância: 7.0
  Caminho: B → D → E

Erro: Vértice de destino 'F' não existe no grafo
```

## 🏗️ Arquitetura Clean Code

### Classes Principais

#### `Aresta`
```python
@dataclass
class Aresta:
    destino: str
    peso: float
```

#### `Grafo`
- `adicionar_vertice(vertice: str)` - Adiciona vértice
- `adicionar_aresta(origem: str, destino: str, peso: float)` - Adiciona aresta
- `obter_vizinhos(vertice: str)` - Retorna vizinhos
- `obter_vertices()` - Retorna todos os vértices

#### `Dijkstra`
- `encontrar_caminho_mais_curto(grafo, origem, destino)` - Algoritmo principal
- `_reconstruir_caminho(predecessores, origem, destino)` - Reconstrói caminho

## ⚡ Complexidade

- **Tempo**: O((V + E) log V) onde V = vértices, E = arestas
- **Espaço**: O(V) para armazenar distâncias e predecessores

## 🔍 Características

- **Separação de Responsabilidades**: Grafo e algoritmo em classes distintas
- **Type Safety**: Type hints em todos os métodos
- **Validação**: Verifica pesos não-negativos e vértices existentes
- **Eficiência**: Usa `heapq` para fila de prioridade otimizada
- **Documentação**: Docstrings detalhadas com parâmetros e retornos

## 📦 Estrutura de Arquivos

```
Construção de Software (PRO)/
├── dijkstra.py      # Implementação principal
├── requirements.txt # Dependências (vazio)
└── README.md       # Esta documentação
```