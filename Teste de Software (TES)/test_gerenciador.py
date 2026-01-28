#!/usr/bin/env python3
"""
Testes unitários para a classe GerenciadorTriagem.
Testes usando apenas bibliotecas padrão do Python.
"""

from datetime import datetime, timedelta
import sys
import os
from io import StringIO

# Adicionar o diretório pai ao path para importar o módulo
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Construção de Software (PRO)'))

from triagem import Paciente, GerenciadorTriagem


def test_inicializacao():
    """Testa inicialização do gerenciador."""
    gerenciador = GerenciadorTriagem()
    assert gerenciador.fila == []
    print("✅ test_inicializacao passou")


def test_adicionar_paciente():
    """Testa adição de paciente à fila."""
    gerenciador = GerenciadorTriagem()
    paciente = Paciente("João", 30, 3)
    
    gerenciador.adicionar_paciente(paciente)
    
    assert len(gerenciador.fila) == 1
    assert gerenciador.fila[0] == paciente
    print("✅ test_adicionar_paciente passou")


def test_obter_fila_ordenada():
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
    print("✅ test_obter_fila_ordenada passou")


def test_atender_proximo_sucesso():
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
    print("✅ test_atender_proximo_sucesso passou")


def test_atender_proximo_fila_vazia():
    """Testa atendimento com fila vazia."""
    gerenciador = GerenciadorTriagem()
    
    try:
        gerenciador.atender_proximo()
        assert False, "Deveria ter dado erro"
    except IndexError as e:
        assert "Fila vazia" in str(e)
    
    print("✅ test_atender_proximo_fila_vazia passou")


def test_listar_fila_vazia():
    """Testa listagem de fila vazia."""
    gerenciador = GerenciadorTriagem()
    
    # Capturar saída do print
    import sys
    from io import StringIO
    
    old_stdout = sys.stdout
    sys.stdout = fake_out = StringIO()
    
    gerenciador.listar_fila()
    
    sys.stdout = old_stdout
    output = fake_out.getvalue()
    
    assert "Fila vazia" in output
    print("✅ test_listar_fila_vazia passou")


def test_fluxo_completo():
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
    print("✅ test_fluxo_completo passou")


def executar_testes():
    """Executa todos os testes do gerenciador."""
    print("🏥 Executando testes do GerenciadorTriagem...")
    
    test_inicializacao()
    test_adicionar_paciente()
    test_obter_fila_ordenada()
    test_atender_proximo_sucesso()
    test_atender_proximo_fila_vazia()
    test_listar_fila_vazia()
    test_fluxo_completo()
    
    print("\n✅ Todos os testes do GerenciadorTriagem passaram!")


if __name__ == "__main__":
    executar_testes()