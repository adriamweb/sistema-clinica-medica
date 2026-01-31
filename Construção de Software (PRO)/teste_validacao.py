#!/usr/bin/env python3
"""
Teste isolado para identificar o problema de validação
"""

from monitor_sistema import validar_entrada_paciente

# Testar pacientes válidos
print("🧪 Testando pacientes válidos:")
print(f"Maria Silva, 45, 3: {validar_entrada_paciente('Maria Silva', 45, 3)}")
print(f"João Santos, 30, 5: {validar_entrada_paciente('João Santos', 30, 5)}")
print(f"Carlos Lima, 40, 3: {validar_entrada_paciente('Carlos Lima', 40, 3)}")

print("\n🧪 Testando paciente inválido:")
print(f"'', -5, 10: {validar_entrada_paciente('', -5, 10)}")