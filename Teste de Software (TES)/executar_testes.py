#!/usr/bin/env python3
"""
Executor principal de todos os testes do sistema de triagem.
Executa todos os testes usando apenas bibliotecas padrão do Python.
"""

import sys
import os

# Adicionar o diretório atual ao path
sys.path.append(os.path.dirname(__file__))

from test_paciente import executar_testes as testes_paciente
from test_ordenacao import executar_testes as testes_ordenacao
from test_gerenciador import executar_testes as testes_gerenciador
from test_texto_urgencia import executar_testes as testes_texto_urgencia


def executar_todos_testes():
    """Executa todos os testes do sistema de triagem."""
    print("🧪 EXECUTANDO TODOS OS TESTES DO SISTEMA DE TRIAGEM")
    print("=" * 60)
    
    try:
        # Executar cada módulo de teste
        testes_paciente()
        print()
        
        testes_ordenacao()
        print()
        
        testes_gerenciador()
        print()
        
        testes_texto_urgencia()
        print()
        
        print("🎉 TODOS OS TESTES PASSARAM COM SUCESSO!")
        print("=" * 60)
        print("✅ Sistema de triagem validado e pronto para uso")
        
    except Exception as e:
        print(f"❌ ERRO NOS TESTES: {e}")
        print("=" * 60)
        return False
    
    return True


if __name__ == "__main__":
    sucesso = executar_todos_testes()
    sys.exit(0 if sucesso else 1)