#!/usr/bin/env python3
"""
Sistema de Logging e Métricas para Monitoramento Proativo
Detecta falhas de entrada de dados e monitora performance das operações.
"""

import logging
import json
import time
from datetime import datetime
from typing import Dict, Any, Optional
from dataclasses import dataclass, asdict
from functools import wraps


@dataclass
class Metrica:
    """Representa uma métrica do sistema."""
    nome: str
    valor: float
    timestamp: datetime
    categoria: str
    detalhes: Optional[Dict[str, Any]] = None


class MonitorTriagem:
    """Sistema de monitoramento para triagem de pacientes."""
    
    def __init__(self):
        self.metricas: Dict[str, list] = {}
        self.contadores = {
            'pacientes_adicionados': 0,
            'pacientes_atendidos': 0,
            'erros_validacao': 0,
            'operacoes_ordenacao': 0,
            'tempo_total_ordenacao': 0.0
        }
        self._configurar_logging()
    
    def _configurar_logging(self):
        """Configura sistema de logging estruturado."""
        # Logger para operações normais
        self.logger = logging.getLogger('triagem_sistema')
        self.logger.setLevel(logging.INFO)
        
        # Logger para métricas
        self.metrics_logger = logging.getLogger('triagem_metricas')
        self.metrics_logger.setLevel(logging.INFO)
        
        # Logger para erros críticos
        self.error_logger = logging.getLogger('triagem_erros')
        self.error_logger.setLevel(logging.ERROR)
        
        # Formatter estruturado
        formatter = logging.Formatter(
            '%(asctime)s | %(name)s | %(levelname)s | %(message)s'
        )
        
        # Handler para arquivo de logs
        file_handler = logging.FileHandler('triagem_sistema.log')
        file_handler.setFormatter(formatter)
        
        # Handler para métricas
        metrics_handler = logging.FileHandler('triagem_metricas.log')
        metrics_handler.setFormatter(formatter)
        
        # Handler para erros
        error_handler = logging.FileHandler('triagem_erros.log')
        error_handler.setFormatter(formatter)
        
        # Adicionar handlers
        self.logger.addHandler(file_handler)
        self.metrics_logger.addHandler(metrics_handler)
        self.error_logger.addHandler(error_handler)
    
    def log_operacao(self, operacao: str, detalhes: Dict[str, Any]):
        """Registra operação do sistema."""
        log_data = {
            'operacao': operacao,
            'timestamp': datetime.now().isoformat(),
            'detalhes': detalhes
        }
        self.logger.info(json.dumps(log_data))
    
    def log_erro_validacao(self, erro: str, dados_entrada: Dict[str, Any]):
        """Registra erro de validação de dados."""
        self.contadores['erros_validacao'] += 1
        
        erro_data = {
            'tipo_erro': 'validacao_entrada',
            'erro': erro,
            'dados_entrada': dados_entrada,
            'timestamp': datetime.now().isoformat(),
            'contador_total': self.contadores['erros_validacao']
        }
        
        self.error_logger.error(json.dumps(erro_data))
        
        # Alerta se muitos erros
        if self.contadores['erros_validacao'] % 5 == 0:
            self._alerta_erros_frequentes()
    
    def registrar_metrica(self, nome: str, valor: float, categoria: str, detalhes: Dict[str, Any] = None):
        """Registra métrica de performance."""
        metrica = Metrica(
            nome=nome,
            valor=valor,
            timestamp=datetime.now(),
            categoria=categoria,
            detalhes=detalhes
        )
        
        if nome not in self.metricas:
            self.metricas[nome] = []
        
        self.metricas[nome].append(metrica)
        
        # Log da métrica
        self.metrics_logger.info(json.dumps(asdict(metrica), default=str))
        
        # Verificar thresholds
        self._verificar_thresholds(nome, valor)
    
    def _verificar_thresholds(self, nome: str, valor: float):
        """Verifica se métricas excedem thresholds críticos."""
        thresholds = {
            'tempo_ordenacao': 1.0,  # 1 segundo
            'tamanho_fila': 50,      # 50 pacientes
            'tempo_atendimento': 300  # 5 minutos
        }
        
        if nome in thresholds and valor > thresholds[nome]:
            self._alerta_threshold(nome, valor, thresholds[nome])
    
    def _alerta_threshold(self, metrica: str, valor: float, threshold: float):
        """Gera alerta quando threshold é excedido."""
        alerta = {
            'tipo': 'threshold_excedido',
            'metrica': metrica,
            'valor_atual': valor,
            'threshold': threshold,
            'timestamp': datetime.now().isoformat()
        }
        
        self.error_logger.warning(json.dumps(alerta))
        print(f"⚠️  ALERTA: {metrica} = {valor} (threshold: {threshold})")
    
    def _alerta_erros_frequentes(self):
        """Alerta para erros de validação frequentes."""
        alerta = {
            'tipo': 'erros_frequentes',
            'total_erros': self.contadores['erros_validacao'],
            'timestamp': datetime.now().isoformat()
        }
        
        self.error_logger.warning(json.dumps(alerta))
        print(f"🚨 ALERTA: {self.contadores['erros_validacao']} erros de validação detectados!")
    
    def obter_relatorio_metricas(self) -> Dict[str, Any]:
        """Gera relatório de métricas."""
        relatorio = {
            'timestamp': datetime.now().isoformat(),
            'contadores': self.contadores.copy(),
            'metricas_recentes': {}
        }
        
        # Últimas 10 métricas de cada tipo
        for nome, metricas in self.metricas.items():
            relatorio['metricas_recentes'][nome] = [
                asdict(m) for m in metricas[-10:]
            ]
        
        return relatorio


def monitorar_performance(categoria: str = "geral"):
    """Decorator para monitorar performance de funções."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            inicio = time.time()
            
            try:
                resultado = func(*args, **kwargs)
                
                # Registrar sucesso
                tempo_execucao = time.time() - inicio
                monitor.registrar_metrica(
                    nome=f"tempo_{func.__name__}",
                    valor=tempo_execucao,
                    categoria=categoria,
                    detalhes={'funcao': func.__name__, 'sucesso': True}
                )
                
                monitor.log_operacao(
                    operacao=func.__name__,
                    detalhes={'tempo_execucao': tempo_execucao, 'sucesso': True}
                )
                
                return resultado
                
            except Exception as e:
                # Registrar erro
                tempo_execucao = time.time() - inicio
                monitor.log_erro_validacao(
                    erro=str(e),
                    dados_entrada={'funcao': func.__name__, 'args': str(args)[:100]}
                )
                
                monitor.registrar_metrica(
                    nome=f"erro_{func.__name__}",
                    valor=1,
                    categoria="erros",
                    detalhes={'funcao': func.__name__, 'erro': str(e)}
                )
                
                raise
        
        return wrapper
    return decorator


# Instância global do monitor
monitor = MonitorTriagem()


def validar_entrada_paciente(nome: str, idade: int, urgencia: int) -> bool:
    """Valida dados de entrada do paciente com logging."""
    erros = []
    
    # Validar nome
    if not nome or not nome.strip():
        erros.append("Nome não pode ser vazio")
    elif len(nome.strip()) < 2:
        erros.append("Nome deve ter pelo menos 2 caracteres")
    
    # Validar idade
    if not isinstance(idade, int):
        erros.append("Idade deve ser um número inteiro")
    elif idade < 0:
        erros.append("Idade não pode ser negativa")
    elif idade > 150:
        erros.append("Idade não pode ser maior que 150 anos")
    
    # Validar urgência
    if not isinstance(urgencia, int):
        erros.append("Urgência deve ser um número inteiro")
    elif not 1 <= urgencia <= 5:
        erros.append("Urgência deve estar entre 1 e 5")
    
    # Registrar erros se houver
    if erros:
        monitor.log_erro_validacao(
            erro="; ".join(erros),
            dados_entrada={'nome': nome, 'idade': idade, 'urgencia': urgencia}
        )
        return False
    
    return True


def gerar_relatorio_sistema():
    """Gera relatório completo do sistema."""
    relatorio = monitor.obter_relatorio_metricas()
    
    print("\n" + "="*60)
    print("📊 RELATÓRIO DE MONITORAMENTO DO SISTEMA")
    print("="*60)
    
    print(f"🕐 Timestamp: {relatorio['timestamp']}")
    print(f"👥 Pacientes adicionados: {relatorio['contadores']['pacientes_adicionados']}")
    print(f"🏥 Pacientes atendidos: {relatorio['contadores']['pacientes_atendidos']}")
    print(f"❌ Erros de validação: {relatorio['contadores']['erros_validacao']}")
    print(f"🔄 Operações de ordenação: {relatorio['contadores']['operacoes_ordenacao']}")
    
    if relatorio['contadores']['operacoes_ordenacao'] > 0:
        tempo_medio = relatorio['contadores']['tempo_total_ordenacao'] / relatorio['contadores']['operacoes_ordenacao']
        print(f"⏱️  Tempo médio de ordenação: {tempo_medio:.3f}s")
    
    print("="*60)
    
    return relatorio


if __name__ == "__main__":
    # Demonstração do sistema de monitoramento
    print("🔍 Sistema de Monitoramento Inicializado")
    
    # Simular algumas operações
    validar_entrada_paciente("João Silva", 30, 3)
    validar_entrada_paciente("", -5, 10)  # Erro intencional
    
    gerar_relatorio_sistema()