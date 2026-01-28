#!/usr/bin/env python3
"""
Fixtures compartilhadas para os testes do sistema de triagem.
"""

import pytest
from datetime import datetime, timedelta
import sys
import os

# Adicionar o diretório pai ao path para importar o módulo
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Construção de Software (PRO)'))

from triagem import Paciente, GerenciadorTriagem


@pytest.fixture
def paciente_basico():
    """Fixture para um paciente básico."""
    return Paciente("João Silva", 45, 3)


@pytest.fixture
def paciente_critico():
    """Fixture para um paciente crítico."""
    return Paciente("Maria Santos", 60, 5)


@pytest.fixture
def paciente_baixa_urgencia():
    """Fixture para um paciente de baixa urgência."""
    return Paciente("Ana Costa", 25, 1)


@pytest.fixture
def gerenciador_vazio():
    """Fixture para um gerenciador de triagem vazio."""
    return GerenciadorTriagem()


@pytest.fixture
def gerenciador_com_pacientes():
    """Fixture para um gerenciador com pacientes pré-cadastrados."""
    gerenciador = GerenciadorTriagem()
    base_time = datetime.now()
    
    # Pacientes com timestamps controlados
    p1 = Paciente("Primeiro", 30, 2)
    p1.timestamp = base_time
    
    p2 = Paciente("Segundo", 40, 4)
    p2.timestamp = base_time + timedelta(seconds=1)
    
    p3 = Paciente("Terceiro", 50, 1)
    p3.timestamp = base_time + timedelta(seconds=2)
    
    gerenciador.adicionar_paciente(p1)
    gerenciador.adicionar_paciente(p2)
    gerenciador.adicionar_paciente(p3)
    
    return gerenciador


@pytest.fixture
def pacientes_mesmo_nivel():
    """Fixture para pacientes com mesmo nível de urgência."""
    base_time = datetime.now()
    
    p1 = Paciente("Primeiro_Chegada", 30, 3)
    p1.timestamp = base_time
    
    p2 = Paciente("Segunda_Chegada", 40, 3)
    p2.timestamp = base_time + timedelta(seconds=1)
    
    p3 = Paciente("Terceira_Chegada", 50, 3)
    p3.timestamp = base_time + timedelta(seconds=2)
    
    return [p1, p2, p3]