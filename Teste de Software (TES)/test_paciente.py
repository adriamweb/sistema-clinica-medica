#!/usr/bin/env python3
"""
Testes unitários para a classe Paciente do sistema de triagem.
Testes usando apenas bibliotecas padrão do Python.
"""

from datetime import datetime
import sys
import os

# Adicionar o diretório do módulo triagem ao path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Construção de Software (PRO)')))

import triagem


def test_criacao_paciente_valido():
    """Testa criação de paciente com dados válidos."""
    paciente = triagem.Paciente("João Silva", 45, 3)
    
    assert paciente.nome == "João Silva"
    assert paciente.idade == 45
    assert paciente.urgencia == 3
    assert isinstance(paciente.timestamp, datetime)
    print("✅ test_criacao_paciente_valido passou")


def test_timestamp_automatico():
    """Testa se timestamp é gerado automaticamente."""
    antes = datetime.now()
    paciente = triagem.Paciente("Maria", 30, 2)
    depois = datetime.now()
    
    assert antes <= paciente.timestamp <= depois
    print("✅ test_timestamp_automatico passou")


def test_urgencia_valida():
    """Testa urgências válidas (1-5)."""
    p1 = triagem.Paciente("Ana", 25, 1)
    p5 = triagem.Paciente("Carlos", 60, 5)
    
    assert p1.urgencia == 1
    assert p5.urgencia == 5
    print("✅ test_urgencia_valida passou")


def test_urgencia_invalida():
    """Testa que urgências inválidas geram erro."""
    try:
        triagem.Paciente("Pedro", 40, 0)
        assert False, "Deveria ter dado erro"
    except ValueError as e:
        assert "Urgência deve estar entre 1 e 5" in str(e)
    
    try:
        triagem.Paciente("Lucia", 35, 6)
        assert False, "Deveria ter dado erro"
    except ValueError as e:
        assert "Urgência deve estar entre 1 e 5" in str(e)
    
    print("✅ test_urgencia_invalida passou")


def test_idade_valida():
    """Testa idades válidas."""
    bebe = triagem.Paciente("Bebê", 0, 4)
    idoso = triagem.Paciente("Centenário", 120, 2)
    
    assert bebe.idade == 0
    assert idoso.idade == 120
    print("✅ test_idade_valida passou")


def test_idade_invalida():
    """Testa que idade negativa gera erro."""
    try:
        triagem.Paciente("Inválido", -1, 3)
        assert False, "Deveria ter dado erro"
    except ValueError as e:
        assert "Idade deve ser positiva" in str(e)
    
    print("✅ test_idade_invalida passou")


def executar_testes():
    """Executa todos os testes da classe Paciente."""
    print("🧪 Executando testes da classe Paciente...")
    
    test_criacao_paciente_valido()
    test_timestamp_automatico()
    test_urgencia_valida()
    test_urgencia_invalida()
    test_idade_valida()
    test_idade_invalida()
    
    print("\n✅ Todos os testes da classe Paciente passaram!")


if __name__ == "__main__":
    executar_testes()