# Sistema de Notificação - Clínica Médica

Sistema simples para envio de notificações de consulta via console usando apenas bibliotecas padrão do Python.

## 📋 Funcionalidades

- ✅ Envio de confirmação de agendamento
- 📱 Envio de lembretes de consulta
- 📅 Listagem de consultas do dia
- 🔍 Busca de consultas por ID

## 🛠️ Requisitos

- Python 3.7 ou superior
- Nenhuma dependência externa (usa apenas bibliotecas padrão)

## 🚀 Como Executar

### Windows

```cmd
# Navegar até a pasta do projeto
cd "Construção de Software (PRO)"

# Executar o script
python notificador.py
```

### Linux/macOS

```bash
# Navegar até a pasta do projeto
cd "Construção de Software (PRO)"

# Executar o script
python3 notificador.py

# Ou tornar executável e rodar diretamente
chmod +x notificador.py
./notificador.py
```

## 📖 Exemplo de Uso

```python
from notificador import NotificadorConsulta

# Criar instância do notificador
notificador = NotificadorConsulta()

# Enviar confirmação
notificador.enviar_confirmacao("AG2024001")

# Enviar lembrete
notificador.enviar_lembrete("AG2024002")

# Listar consultas do dia
notificador.listar_consultas_hoje()
```

## 📝 Saída Esperada

```
🏥 Sistema de Notificação - Clínica Médica
============================================================
📅 CONSULTAS DE HOJE (29/01/2024)
============================================================
09:00 - Maria Silva Santos (Dr. João Silva)
14:30 - José Santos (Dra. Ana Oliveira)
============================================================

============================================================
✅ CONFIRMAÇÃO DE AGENDAMENTO
============================================================
Olá Maria Silva Santos,
Sua consulta foi agendada com sucesso!
Médico: Dr. João Silva - Cardiologia
Data: 29/01/2024 às 09:00
Protocolo: AG2024001
Chegue 15 minutos antes do horário.
============================================================
```

## 🏗️ Estrutura do Código

- **NotificadorConsulta**: Classe principal com Type Hints
- **enviar_confirmacao()**: Envia confirmação de agendamento
- **enviar_lembrete()**: Envia lembrete de consulta
- **listar_consultas_hoje()**: Lista consultas do dia atual
- **_buscar_consulta()**: Método privado para busca por ID

## 📦 Arquivos

- `notificador.py` - Script principal
- `requirements.txt` - Dependências (vazio - usa apenas stdlib)
- `README.md` - Este arquivo de documentação