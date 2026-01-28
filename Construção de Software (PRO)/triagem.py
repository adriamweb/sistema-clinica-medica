#!/usr/bin/env python3
"""
Sistema de Triagem de Pacientes - Clínica Médica
Gerencia fila de espera com priorização por urgência.
"""

from typing import List
from dataclasses import dataclass


@dataclass
class Paciente:
    """Representa um paciente na fila de triagem."""
    nome: str
    idade: int
    urgencia: int  # 1 (baixa) a 5 (crítica)
    
    def __post_init__(self) -> None:
        """Valida os dados do paciente após inicialização."""
        if not 1 <= self.urgencia <= 5:
            raise ValueError("Urgência deve estar entre 1 e 5")
        if self.idade < 0:
            raise ValueError("Idade deve ser positiva")


class GerenciadorTriagem:
    """Gerencia a fila de triagem de pacientes."""
    
    def __init__(self) -> None:
        """Inicializa o gerenciador com fila vazia."""
        self.fila: List[Paciente] = []
    
    def adicionar_paciente(self, paciente: Paciente) -> None:
        """
        Adiciona paciente à fila de triagem.
        
        Args:
            paciente: Paciente a ser adicionado
        """
        self.fila.append(paciente)
    
    def obter_fila_ordenada(self) -> List[Paciente]:
        """
        Retorna fila ordenada por prioridade de urgência.
        
        Returns:
            Lista de pacientes ordenada por urgência (maior primeiro)
        """
        return ordenar_por_urgencia(self.fila)
    
    def atender_proximo(self) -> Paciente:
        """
        Remove e retorna o próximo paciente da fila ordenada.
        
        Returns:
            Próximo paciente a ser atendido
            
        Raises:
            IndexError: Se a fila estiver vazia
        """
        if not self.fila:
            raise IndexError("Fila vazia")
        
        fila_ordenada = self.obter_fila_ordenada()
        proximo = fila_ordenada[0]
        self.fila.remove(proximo)
        return proximo
    
    def listar_fila(self) -> None:
        """Exibe a fila atual ordenada por urgência."""
        if not self.fila:
            print("Fila vazia")
            return
        
        fila_ordenada = self.obter_fila_ordenada()
        print("=== FILA DE TRIAGEM ===")
        for i, paciente in enumerate(fila_ordenada, 1):
            urgencia_texto = obter_texto_urgencia(paciente.urgencia)
            print(f"{i}. {paciente.nome} ({paciente.idade} anos) - {urgencia_texto}")


def ordenar_por_urgencia(pacientes: List[Paciente]) -> List[Paciente]:
    """
    Ordena lista de pacientes por urgência (maior primeiro).
    
    Args:
        pacientes: Lista de pacientes para ordenar
        
    Returns:
        Lista ordenada por urgência decrescente, depois por idade crescente
    """
    return sorted(pacientes, key=lambda p: (-p.urgencia, p.idade))


def obter_texto_urgencia(nivel: int) -> str:
    """
    Converte nível numérico de urgência em texto descritivo.
    
    Args:
        nivel: Nível de urgência (1-5)
        
    Returns:
        Descrição textual da urgência
    """
    textos = {
        1: "🟢 Baixa",
        2: "🟡 Moderada", 
        3: "🟠 Alta",
        4: "🔴 Muito Alta",
        5: "🚨 Crítica"
    }
    return textos.get(nivel, "❓ Desconhecida")


def demonstracao() -> None:
    """Demonstra o funcionamento do sistema de triagem."""
    print("🏥 Sistema de Triagem - Clínica Médica")
    print("=" * 40)
    
    # Criar gerenciador
    triagem = GerenciadorTriagem()
    
    # Adicionar pacientes de exemplo
    pacientes_exemplo = [
        Paciente("Maria Silva", 45, 2),
        Paciente("João Santos", 78, 4),
        Paciente("Ana Costa", 25, 1),
        Paciente("Pedro Lima", 60, 5),
        Paciente("Carla Souza", 35, 3)
    ]
    
    print("Adicionando pacientes...")
    for paciente in pacientes_exemplo:
        triagem.adicionar_paciente(paciente)
        print(f"+ {paciente.nome} (urgência {paciente.urgencia})")
    
    print("\n")
    triagem.listar_fila()
    
    print("\nAtendendo próximo paciente...")
    proximo = triagem.atender_proximo()
    print(f"Atendendo: {proximo.nome} - {obter_texto_urgencia(proximo.urgencia)}")
    
    print("\nFila após atendimento:")
    triagem.listar_fila()


def main() -> None:
    """Função principal."""
    demonstracao()


if __name__ == "__main__":
    main()