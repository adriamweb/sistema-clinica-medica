#!/usr/bin/env python3
"""
Testes unitários para a função obter_texto_urgencia.
Testes usando apenas bibliotecas padrão do Python.
"""

import sys
import os

# Adicionar o diretório do módulo triagem ao path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Construção de Software (PRO)')))

import triagem


def test_urgencias_validas():
    """Testa mapeamento de urgências válidas (1-5)."""
    assert triagem.obter_texto_urgencia(1) == "🟢 Baixa"
    assert triagem.obter_texto_urgencia(2) == "🟡 Moderada"
    assert triagem.obter_texto_urgencia(3) == "🟠 Alta"
    assert triagem.obter_texto_urgencia(4) == "🔴 Muito Alta"
    assert triagem.obter_texto_urgencia(5) == "🚨 Crítica"
    print("✅ test_urgencias_validas passou")


def test_urgencias_invalidas():
    """Testa mapeamento de urgências inválidas."""
    assert triagem.obter_texto_urgencia(0) == "❓ Desconhecida"
    assert triagem.obter_texto_urgencia(6) == "❓ Desconhecida"
    assert triagem.obter_texto_urgencia(-1) == "❓ Desconhecida"
    assert triagem.obter_texto_urgencia(100) == "❓ Desconhecida"
    print("✅ test_urgencias_invalidas passou")


def executar_testes():
    """Executa todos os testes de texto de urgência."""
    print("📝 Executando testes de texto de urgência...")
    
    test_urgencias_validas()
    test_urgencias_invalidas()
    
    print("\n✅ Todos os testes de texto de urgência passaram!")


if __name__ == "__main__":
    executar_testes()