# Sistema de Triagem de Pacientes

Sistema simples para gerenciar fila de espera de pacientes com priorização por urgência.

## 🚀 Como Executar

### Windows
```cmd
cd "Construção de Software (PRO)"
python triagem.py
```

### Linux/macOS
```bash
cd "Construção de Software (PRO)"
python3 triagem.py
```

## 📋 Funcionalidades

- ✅ Cadastro de pacientes com nome, idade e urgência (1-5)
- ✅ Ordenação automática por urgência (maior primeiro)
- ✅ Atendimento do próximo paciente prioritário
- ✅ Visualização da fila ordenada

## 🏥 Níveis de Urgência

- **1** 🟢 Baixa
- **2** 🟡 Moderada  
- **3** 🟠 Alta
- **4** 🔴 Muito Alta
- **5** 🚨 Crítica

## 📖 Exemplo de Uso

```python
from triagem import Paciente, GerenciadorTriagem

# Criar gerenciador
triagem = GerenciadorTriagem()

# Adicionar paciente
paciente = Paciente("João Silva", 45, 3)
triagem.adicionar_paciente(paciente)

# Ver fila ordenada
triagem.listar_fila()

# Atender próximo
proximo = triagem.atender_proximo()
```

## 📊 Saída Esperada

```
🏥 Sistema de Triagem - Clínica Médica
========================================
Adicionando pacientes...
+ Maria Silva (urgência 2)
+ João Santos (urgência 4)
+ Ana Costa (urgência 1)
+ Pedro Lima (urgência 5)
+ Carla Souza (urgência 3)

=== FILA DE TRIAGEM ===
1. Pedro Lima (60 anos) - 🚨 Crítica
2. João Santos (78 anos) - 🔴 Muito Alta
3. Carla Souza (35 anos) - 🟠 Alta
4. Maria Silva (45 anos) - 🟡 Moderada
5. Ana Costa (25 anos) - 🟢 Baixa
```

## 🏗️ Estrutura do Código

- **Paciente**: Classe com nome, idade e urgência
- **GerenciadorTriagem**: Gerencia a fila de pacientes
- **ordenar_por_urgencia()**: Função pura de ordenação
- **obter_texto_urgencia()**: Converte número em texto descritivo