#!/usr/bin/env python3
"""
Sistema de Triagem de Pacientes - Clínica Médica
Gerencia fila de espera com priorização por urgência e ordem de chegada.
"""

from typing import List
from dataclasses import dataclass, field
from datetime import datetime
import time

# Importar sistema de monitoramento
from monitor_sistema import monitor, monitorar_performance, validar_entrada_paciente, gerar_relatorio_sistema


@dataclass
class Paciente:
    """Representa um paciente na fila de triagem."""
    nome: str
    idade: int
    urgencia: int  # 1 (baixa) a 5 (crítica)
    timestamp: datetime = field(default_factory=datetime.now)
    
    def __post_init__(self) -> None:
        """Valida os dados do paciente após inicialização."""
        # Validação com logging integrado
        if not validar_entrada_paciente(self.nome, self.idade, self.urgencia):
            if not 1 <= self.urgencia <= 5:
                raise ValueError("Urgência deve estar entre 1 e 5")
            if self.idade < 0:
                raise ValueError("Idade deve ser positiva")
        
        # Log de criação bem-sucedida
        monitor.log_operacao(
            operacao="criar_paciente",
            detalhes={
                'nome': self.nome,
                'idade': self.idade,
                'urgencia': self.urgencia,
                'timestamp': self.timestamp.isoformat()
            }
        )


class GerenciadorTriagem:
    """Gerencia a fila de triagem de pacientes."""
    
    def __init__(self) -> None:
        """Inicializa o gerenciador com fila vazia."""
        self.fila: List[Paciente] = []
        monitor.log_operacao("inicializar_gerenciador", {'fila_inicial': 0})
    
    @monitorar_performance("triagem")
    def adicionar_paciente(self, paciente: Paciente) -> None:
        """
        Adiciona paciente à fila de triagem.
        
        Args:
            paciente: Paciente a ser adicionado
        """
        self.fila.append(paciente)
        monitor.contadores['pacientes_adicionados'] += 1
        
        # Registrar métrica de tamanho da fila
        monitor.registrar_metrica(
            nome="tamanho_fila",
            valor=len(self.fila),
            categoria="capacidade",
            detalhes={'operacao': 'adicionar_paciente'}
        )
        
        monitor.log_operacao(
            operacao="adicionar_paciente",
            detalhes={
                'paciente': paciente.nome,
                'urgencia': paciente.urgencia,
                'tamanho_fila': len(self.fila)
            }
        )
    
    @monitorar_performance("triagem")
    def obter_fila_ordenada(self) -> List[Paciente]:
        """
        Retorna fila ordenada por prioridade de urgência e ordem de chegada.
        
        Returns:
            Lista de pacientes ordenada por urgência (maior primeiro),
            depois por timestamp (quem chegou primeiro)
        """
        inicio = time.time()
        resultado = ordenar_por_prioridade(self.fila)
        tempo_ordenacao = time.time() - inicio
        
        # Registrar métricas de performance
        monitor.contadores['operacoes_ordenacao'] += 1
        monitor.contadores['tempo_total_ordenacao'] += tempo_ordenacao
        
        monitor.registrar_metrica(
            nome="tempo_ordenacao",
            valor=tempo_ordenacao,
            categoria="performance",
            detalhes={'tamanho_fila': len(self.fila)}
        )
        
        return resultado
    
    @monitorar_performance("triagem")
    def atender_proximo(self) -> Paciente:
        """
        Remove e retorna o próximo paciente da fila ordenada.
        
        Returns:
            Próximo paciente a ser atendido
            
        Raises:
            IndexError: Se a fila estiver vazia
        """
        if not self.fila:
            monitor.log_erro_validacao(
                erro="Tentativa de atender paciente com fila vazia",
                dados_entrada={'tamanho_fila': 0}
            )
            raise IndexError("Fila vazia")
        
        fila_ordenada = self.obter_fila_ordenada()
        proximo = fila_ordenada[0]
        self.fila.remove(proximo)
        
        monitor.contadores['pacientes_atendidos'] += 1
        
        # Calcular tempo de espera
        tempo_espera = (datetime.now() - proximo.timestamp).total_seconds()
        
        monitor.registrar_metrica(
            nome="tempo_espera",
            valor=tempo_espera,
            categoria="atendimento",
            detalhes={
                'paciente': proximo.nome,
                'urgencia': proximo.urgencia
            }
        )
        
        monitor.log_operacao(
            operacao="atender_paciente",
            detalhes={
                'paciente': proximo.nome,
                'urgencia': proximo.urgencia,
                'tempo_espera_segundos': tempo_espera,
                'fila_restante': len(self.fila)
            }
        )
        
        return proximo
    
    def listar_fila(self) -> None:
        """Exibe a fila atual ordenada por prioridade."""
        if not self.fila:
            print("Fila vazia")
            return
        
        fila_ordenada = self.obter_fila_ordenada()
        print("=== FILA DE TRIAGEM ===")
        for i, paciente in enumerate(fila_ordenada, 1):
            urgencia_texto = obter_texto_urgencia(paciente.urgencia)
            chegada = paciente.timestamp.strftime("%H:%M:%S")
            print(f"{i}. {paciente.nome} ({paciente.idade} anos) - {urgencia_texto} - Chegada: {chegada}")


@monitorar_performance("ordenacao")
def ordenar_por_prioridade(pacientes: List[Paciente]) -> List[Paciente]:
    """
    Ordena pacientes por urgência (maior primeiro) e timestamp (primeiro a chegar).
    
    Args:
        pacientes: Lista de pacientes para ordenar
        
    Returns:
        Lista ordenada por urgência decrescente, depois por timestamp crescente
    """
    return sorted(pacientes, key=lambda p: (-p.urgencia, p.timestamp))


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
    """Demonstra o funcionamento do sistema com teste de desempate por timestamp."""
    print("🏥 Sistema de Triagem - Clínica Médica (com monitoramento)")
    print("=" * 50)
    
    # Criar gerenciador
    triagem = GerenciadorTriagem()
    
    # Simular chegadas em horários diferentes
    import time
    
    print("Simulando chegadas de pacientes...")
    
    # Pacientes com mesma urgência para testar desempate
    pacientes_exemplo = [
        Paciente("Maria Silva", 45, 3),  # Chega primeiro
        Paciente("João Santos", 30, 5),  # Urgência crítica
    ]
    
    for paciente in pacientes_exemplo:
        triagem.adicionar_paciente(paciente)
        print(f"+ {paciente.nome} (urgência {paciente.urgencia}) - {paciente.timestamp.strftime('%H:%M:%S')}")
        time.sleep(0.1)  # Pequeno delay para timestamps diferentes
    
    # Adicionar outro paciente com mesma urgência que Maria
    time.sleep(0.1)
    paciente_tardio = Paciente("Carlos Lima", 40, 3)  # Mesma urgência, mas chega depois
    triagem.adicionar_paciente(paciente_tardio)
    print(f"+ {paciente_tardio.nome} (urgência {paciente_tardio.urgencia}) - {paciente_tardio.timestamp.strftime('%H:%M:%S')}")
    
    # Simular erro de validação
    try:
        paciente_invalido = Paciente("", -5, 10)
    except ValueError as e:
        print(f"\n⚠️  Erro capturado: {e}")
    
    print("\n")
    triagem.listar_fila()
    
    print("\n📝 Teste de desempate:")
    print("Maria e Carlos têm urgência 3, mas Maria chegou primeiro")
    print("João tem urgência 5 (crítica) e deve ser atendido primeiro")
    
    print("\nAtendendo próximo paciente...")
    proximo = triagem.atender_proximo()
    print(f"Atendendo: {proximo.nome} - {obter_texto_urgencia(proximo.urgencia)}")
    
    print("\nFila após atendimento:")
    triagem.listar_fila()
    
    # Gerar relatório de monitoramento
    gerar_relatorio_sistema()


def main() -> None:
    """Função principal."""
    demonstracao()


if __name__ == "__main__":
    main()