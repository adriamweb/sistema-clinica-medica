#!/usr/bin/env python3
"""
Testes que falham intencionalmente para demonstrar tratamento de erros.
Usado para verificar como o sistema reporta falhas nos testes.
"""

import sys
import os

# Adicionar o diretório correto ao path
caminho_triagem = os.path.join(os.path.dirname(__file__), '..', 'Construção de Software (PRO)')
sys.path.insert(0, os.path.abspath(caminho_triagem))

from triagem import Paciente, GerenciadorTriagem, ordenar_por_prioridade


def test_falha_proposital_ordenacao():
    """Teste que falha propositalmente - ordenação incorreta."""
    paciente1 = Paciente("João", 30, 1)  # urgência baixa
    paciente2 = Paciente("Maria", 40, 5)  # urgência crítica
    
    resultado = ordenar_por_prioridade([paciente1, paciente2])
    
    # ERRO INTENCIONAL: esperando ordem errada
    assert resultado[0].nome == "João", "❌ FALHA INTENCIONAL: João deveria vir primeiro (mas não deveria!)"
    print("✅ test_falha_proposital_ordenacao passou")


def test_falha_proposital_validacao():
    """Teste que falha propositalmente - validação incorreta."""
    try:
        # Tentando criar paciente com urgência inválida
        paciente = Paciente("Pedro", 25, 10)  # urgência 10 é inválida
        
        # ERRO INTENCIONAL: não deveria chegar aqui
        assert False, "❌ FALHA INTENCIONAL: Deveria ter dado ValueError mas não deu!"
        
    except ValueError:
        # ERRO INTENCIONAL: invertendo a lógica
        assert False, "❌ FALHA INTENCIONAL: ValueError foi lançado (como esperado), mas teste falha mesmo assim!"
    
    print("✅ test_falha_proposital_validacao passou")


def test_falha_proposital_fila_vazia():
    """Teste que falha propositalmente - comportamento de fila vazia."""
    gerenciador = GerenciadorTriagem()
    
    # ERRO INTENCIONAL: esperando que fila vazia tenha pacientes
    assert len(gerenciador.fila) == 5, "❌ FALHA INTENCIONAL: Fila vazia deveria ter 5 pacientes!"
    print("✅ test_falha_proposital_fila_vazia passou")


def executar_testes():
    """Executa todos os testes de falhas intencionais."""
    print("💥 Executando testes de falhas intencionais...")
    print("⚠️  ATENÇÃO: Estes testes DEVEM falhar para demonstrar tratamento de erros!")
    
    test_falha_proposital_ordenacao()
    test_falha_proposital_validacao() 
    test_falha_proposital_fila_vazia()
    
    print("\n✅ Todos os testes de falhas passaram!")


if __name__ == "__main__":
    executar_testes()