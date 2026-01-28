#!/usr/bin/env python3
"""
Testes unitários para a função obter_texto_urgencia.
"""

import pytest
import sys
import os

# Adicionar o diretório pai ao path para importar o módulo
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Construção de Software (PRO)'))

from triagem import obter_texto_urgencia


class TestObterTextoUrgencia:
    """Testes para a função obter_texto_urgencia."""
    
    def test_urgencia_1_baixa(self):
        """Testa mapeamento de urgência 1."""
        resultado = obter_texto_urgencia(1)
        assert resultado == "🟢 Baixa"
    
    def test_urgencia_2_moderada(self):
        """Testa mapeamento de urgência 2."""
        resultado = obter_texto_urgencia(2)
        assert resultado == "🟡 Moderada"
    
    def test_urgencia_3_alta(self):
        """Testa mapeamento de urgência 3."""
        resultado = obter_texto_urgencia(3)
        assert resultado == "🟠 Alta"
    
    def test_urgencia_4_muito_alta(self):
        """Testa mapeamento de urgência 4."""
        resultado = obter_texto_urgencia(4)
        assert resultado == "🔴 Muito Alta"
    
    def test_urgencia_5_critica(self):
        """Testa mapeamento de urgência 5."""
        resultado = obter_texto_urgencia(5)
        assert resultado == "🚨 Crítica"
    
    def test_urgencia_0_desconhecida(self):
        """Testa mapeamento de urgência 0 (inválida)."""
        resultado = obter_texto_urgencia(0)
        assert resultado == "❓ Desconhecida"
    
    def test_urgencia_6_desconhecida(self):
        """Testa mapeamento de urgência 6 (inválida)."""
        resultado = obter_texto_urgencia(6)
        assert resultado == "❓ Desconhecida"
    
    def test_urgencia_negativa_desconhecida(self):
        """Testa mapeamento de urgência negativa."""
        resultado = obter_texto_urgencia(-1)
        assert resultado == "❓ Desconhecida"
    
    def test_urgencia_muito_alta_desconhecida(self):
        """Testa mapeamento de urgência muito alta."""
        resultado = obter_texto_urgencia(100)
        assert resultado == "❓ Desconhecida"