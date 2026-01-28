#!/usr/bin/env python3
"""
Testes unitários para a classe Paciente do sistema de triagem.
"""

import pytest
from datetime import datetime
import sys
import os

# Adicionar o diretório pai ao path para importar o módulo
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Construção de Software (PRO)'))

from triagem import Paciente


class TestPaciente:
    """Testes para a classe Paciente."""
    
    def test_criacao_paciente_valido(self):
        """Testa criação de paciente com dados válidos."""
        paciente = Paciente("João Silva", 45, 3)
        
        assert paciente.nome == "João Silva"
        assert paciente.idade == 45
        assert paciente.urgencia == 3
        assert isinstance(paciente.timestamp, datetime)
    
    def test_timestamp_automatico(self):
        """Testa se timestamp é gerado automaticamente."""
        antes = datetime.now()
        paciente = Paciente("Maria", 30, 2)
        depois = datetime.now()
        
        assert antes <= paciente.timestamp <= depois
    
    def test_urgencia_minima_valida(self):
        """Testa urgência mínima válida (1)."""
        paciente = Paciente("Ana", 25, 1)
        assert paciente.urgencia == 1
    
    def test_urgencia_maxima_valida(self):
        """Testa urgência máxima válida (5)."""
        paciente = Paciente("Carlos", 60, 5)
        assert paciente.urgencia == 5
    
    def test_urgencia_zero_invalida(self):
        """Testa que urgência 0 é inválida."""
        with pytest.raises(ValueError, match="Urgência deve estar entre 1 e 5"):
            Paciente("Pedro", 40, 0)
    
    def test_urgencia_seis_invalida(self):
        """Testa que urgência 6 é inválida."""
        with pytest.raises(ValueError, match="Urgência deve estar entre 1 e 5"):
            Paciente("Lucia", 35, 6)
    
    def test_urgencia_negativa_invalida(self):
        """Testa que urgência negativa é inválida."""
        with pytest.raises(ValueError, match="Urgência deve estar entre 1 e 5"):
            Paciente("Roberto", 50, -1)
    
    def test_idade_zero_valida(self):
        """Testa que idade 0 é válida (recém-nascido)."""
        paciente = Paciente("Bebê", 0, 4)
        assert paciente.idade == 0
    
    def test_idade_negativa_invalida(self):
        """Testa que idade negativa é inválida."""
        with pytest.raises(ValueError, match="Idade deve ser positiva"):
            Paciente("Inválido", -1, 3)
    
    def test_idade_muito_alta_valida(self):
        """Testa que idade muito alta é válida."""
        paciente = Paciente("Centenário", 120, 2)
        assert paciente.idade == 120