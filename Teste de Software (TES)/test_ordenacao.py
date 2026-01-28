#!/usr/bin/env python3
"""
Testes unitários para a função ordenar_por_prioridade.
"""

import pytest
from datetime import datetime, timedelta
import sys
import os

# Adicionar o diretório pai ao path para importar o módulo
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Construção de Software (PRO)'))

from triagem import Paciente, ordenar_por_prioridade


class TestOrdenacaoPrioridade:
    """Testes para a função ordenar_por_prioridade."""
    
    def test_lista_vazia(self):
        """Testa ordenação de lista vazia."""
        resultado = ordenar_por_prioridade([])
        assert resultado == []
    
    def test_um_paciente(self):
        """Testa ordenação com um único paciente."""
        paciente = Paciente("João", 30, 3)
        resultado = ordenar_por_prioridade([paciente])
        assert len(resultado) == 1
        assert resultado[0] == paciente
    
    def test_ordenacao_por_urgencia(self):
        """Testa ordenação por urgência (maior primeiro)."""
        base_time = datetime.now()
        
        p1 = Paciente("Baixa", 30, 1)
        p1.timestamp = base_time
        
        p2 = Paciente("Alta", 40, 4)
        p2.timestamp = base_time
        
        p3 = Paciente("Crítica", 50, 5)
        p3.timestamp = base_time
        
        resultado = ordenar_por_prioridade([p1, p2, p3])
        
        assert resultado[0].nome == "Crítica"  # urgência 5
        assert resultado[1].nome == "Alta"     # urgência 4
        assert resultado[2].nome == "Baixa"    # urgência 1
    
    def test_desempate_por_timestamp(self):
        """Testa desempate por timestamp (primeiro a chegar)."""
        base_time = datetime.now()
        
        # Mesma urgência, timestamps diferentes
        p1 = Paciente("Primeiro", 30, 3)
        p1.timestamp = base_time
        
        p2 = Paciente("Segundo", 40, 3)
        p2.timestamp = base_time + timedelta(seconds=1)
        
        resultado = ordenar_por_prioridade([p2, p1])  # Ordem inversa na entrada
        
        assert resultado[0].nome == "Primeiro"  # chegou primeiro
        assert resultado[1].nome == "Segundo"   # chegou depois
    
    def test_ordenacao_complexa(self):
        """Testa ordenação com urgência e timestamp combinados."""
        base_time = datetime.now()
        
        # Cenário: urgência 3 (primeiro), urgência 5, urgência 3 (segundo)
        p1 = Paciente("Urgência3_Primeiro", 30, 3)
        p1.timestamp = base_time
        
        p2 = Paciente("Urgência5", 40, 5)
        p2.timestamp = base_time + timedelta(seconds=1)
        
        p3 = Paciente("Urgência3_Segundo", 50, 3)
        p3.timestamp = base_time + timedelta(seconds=2)
        
        resultado = ordenar_por_prioridade([p1, p2, p3])
        
        # Ordem esperada: urgência 5, depois urgência 3 por timestamp
        assert resultado[0].nome == "Urgência5"
        assert resultado[1].nome == "Urgência3_Primeiro"
        assert resultado[2].nome == "Urgência3_Segundo"
    
    def test_todos_mesma_urgencia(self):
        """Testa ordenação quando todos têm mesma urgência."""
        base_time = datetime.now()
        
        p1 = Paciente("Primeiro", 30, 2)
        p1.timestamp = base_time
        
        p2 = Paciente("Segundo", 40, 2)
        p2.timestamp = base_time + timedelta(seconds=1)
        
        p3 = Paciente("Terceiro", 50, 2)
        p3.timestamp = base_time + timedelta(seconds=2)
        
        resultado = ordenar_por_prioridade([p3, p1, p2])  # Ordem aleatória
        
        assert resultado[0].nome == "Primeiro"
        assert resultado[1].nome == "Segundo"
        assert resultado[2].nome == "Terceiro"