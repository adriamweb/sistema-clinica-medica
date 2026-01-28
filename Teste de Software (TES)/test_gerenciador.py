#!/usr/bin/env python3
"""
Testes unitários para a classe GerenciadorTriagem.
"""

import pytest
from datetime import datetime, timedelta
import sys
import os
from io import StringIO
from unittest.mock import patch

# Adicionar o diretório pai ao path para importar o módulo
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Construção de Software (PRO)'))

from triagem import Paciente, GerenciadorTriagem


class TestGerenciadorTriagem:
    """Testes para a classe GerenciadorTriagem."""
    
    def test_inicializacao(self):
        """Testa inicialização do gerenciador."""
        gerenciador = GerenciadorTriagem()
        assert gerenciador.fila == []
    
    def test_adicionar_paciente(self):
        """Testa adição de paciente à fila."""
        gerenciador = GerenciadorTriagem()
        paciente = Paciente("João", 30, 3)
        
        gerenciador.adicionar_paciente(paciente)
        
        assert len(gerenciador.fila) == 1
        assert gerenciador.fila[0] == paciente
    
    def test_adicionar_multiplos_pacientes(self):
        """Testa adição de múltiplos pacientes."""
        gerenciador = GerenciadorTriagem()
        p1 = Paciente("João", 30, 3)
        p2 = Paciente("Maria", 25, 4)
        
        gerenciador.adicionar_paciente(p1)
        gerenciador.adicionar_paciente(p2)
        
        assert len(gerenciador.fila) == 2
        assert p1 in gerenciador.fila
        assert p2 in gerenciador.fila
    
    def test_obter_fila_ordenada(self):
        """Testa obtenção da fila ordenada."""
        gerenciador = GerenciadorTriagem()
        base_time = datetime.now()
        
        p1 = Paciente("Baixa", 30, 1)
        p1.timestamp = base_time
        
        p2 = Paciente("Alta", 40, 4)
        p2.timestamp = base_time
        
        gerenciador.adicionar_paciente(p1)
        gerenciador.adicionar_paciente(p2)
        
        fila_ordenada = gerenciador.obter_fila_ordenada()
        
        assert fila_ordenada[0].nome == "Alta"   # urgência 4
        assert fila_ordenada[1].nome == "Baixa"  # urgência 1
    
    def test_atender_proximo_sucesso(self):
        """Testa atendimento do próximo paciente com sucesso."""
        gerenciador = GerenciadorTriagem()
        base_time = datetime.now()
        
        p1 = Paciente("Normal", 30, 2)
        p1.timestamp = base_time
        
        p2 = Paciente("Crítico", 40, 5)
        p2.timestamp = base_time
        
        gerenciador.adicionar_paciente(p1)
        gerenciador.adicionar_paciente(p2)
        
        proximo = gerenciador.atender_proximo()
        
        assert proximo.nome == "Crítico"  # urgência 5 tem prioridade
        assert len(gerenciador.fila) == 1  # um paciente removido
        assert gerenciador.fila[0].nome == "Normal"  # sobrou o normal
    
    def test_atender_proximo_fila_vazia(self):
        """Testa atendimento com fila vazia."""
        gerenciador = GerenciadorTriagem()
        
        with pytest.raises(IndexError, match="Fila vazia"):
            gerenciador.atender_proximo()
    
    def test_listar_fila_vazia(self):
        """Testa listagem de fila vazia."""
        gerenciador = GerenciadorTriagem()
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            gerenciador.listar_fila()
            output = fake_out.getvalue()
        
        assert "Fila vazia" in output
    
    def test_listar_fila_com_pacientes(self):
        """Testa listagem de fila com pacientes."""
        gerenciador = GerenciadorTriagem()
        paciente = Paciente("João Silva", 45, 3)
        gerenciador.adicionar_paciente(paciente)
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            gerenciador.listar_fila()
            output = fake_out.getvalue()
        
        assert "=== FILA DE TRIAGEM ===" in output
        assert "João Silva" in output
        assert "45 anos" in output
        assert "🟠 Alta" in output
        assert "Chegada:" in output
    
    def test_fluxo_completo(self):
        """Testa fluxo completo: adicionar, listar, atender."""
        gerenciador = GerenciadorTriagem()
        base_time = datetime.now()
        
        # Adicionar pacientes
        p1 = Paciente("Maria", 30, 2)
        p1.timestamp = base_time
        
        p2 = Paciente("João", 40, 4)
        p2.timestamp = base_time + timedelta(seconds=1)
        
        gerenciador.adicionar_paciente(p1)
        gerenciador.adicionar_paciente(p2)
        
        # Verificar ordem inicial
        fila = gerenciador.obter_fila_ordenada()
        assert fila[0].nome == "João"  # urgência 4
        assert fila[1].nome == "Maria" # urgência 2
        
        # Atender primeiro
        primeiro = gerenciador.atender_proximo()
        assert primeiro.nome == "João"
        
        # Verificar que sobrou apenas Maria
        assert len(gerenciador.fila) == 1
        assert gerenciador.fila[0].nome == "Maria"