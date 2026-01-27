# Análise de Conflito - Regras de Cancelamento de Consultas

## Problema Identificado

### Regras em Conflito:

**Regra A**: Médicos podem cancelar qualquer consulta a qualquer momento para atender emergências.

**Regra B**: O paciente deve ser notificado com 24h de antecedência sobre qualquer cancelamento, e o sistema não deve permitir cancelamentos fora deste prazo.

## Análise do Conflito

### ⚠️ **Inconsistência Lógica Identificada**

**SIM, existe um conflito direto** entre as duas regras:

- **Regra A** permite cancelamentos **a qualquer momento**
- **Regra B** **proíbe** cancelamentos com menos de 24h de antecedência

### Cenários Problemáticos:

1. **Emergência Médica**: Médico precisa cancelar consulta em 2 horas para atender emergência
2. **Doença Súbita**: Médico fica doente na manhã do dia da consulta
3. **Urgência Hospitalar**: Médico é chamado para cirurgia de emergência

## Solução Técnica Proposta

### 🔧 **Implementação de Tipos de Cancelamento**

```
CANCELAMENTO_PROGRAMADO (>24h antecedência)
├── Permite cancelamento normal
├── Notifica paciente automaticamente
└── Sem justificativa obrigatória

CANCELAMENTO_EMERGENCIAL (<24h antecedência)
├── Requer justificativa obrigatória
├── Notifica paciente imediatamente
├── Registra log de auditoria
└── Aciona protocolo de reagendamento prioritário
```

### 📋 **Regras de Negócio Revisadas**

#### **RN-CANC-01: Cancelamento Programado**
- Cancelamentos com **≥24h de antecedência**
- Notificação automática ao paciente
- Sem necessidade de justificativa
- Reagendamento opcional

#### **RN-CANC-02: Cancelamento Emergencial**
- Cancelamentos com **<24h de antecedência**
- **Apenas para situações emergenciais**
- Justificativa obrigatória (lista pré-definida)
- Notificação imediata ao paciente
- Reagendamento prioritário obrigatório

#### **RN-CANC-03: Justificativas Válidas para Emergência**
- Emergência médica do profissional
- Emergência familiar grave
- Chamada para atendimento de urgência/emergência
- Condições climáticas extremas
- Falha de equipamentos críticos

## Implementação Técnica

### 🏗️ **Estrutura de Dados**

```sql
-- Tabela de Cancelamentos
CREATE TABLE cancelamentos (
    id INT PRIMARY KEY,
    consulta_id INT,
    tipo_cancelamento ENUM('PROGRAMADO', 'EMERGENCIAL'),
    motivo_categoria VARCHAR(50),
    justificativa TEXT,
    cancelado_por INT, -- ID do usuário
    data_cancelamento TIMESTAMP,
    reagendamento_obrigatório BOOLEAN,
    status_notificacao ENUM('PENDENTE', 'ENVIADA', 'FALHOU')
);
```

### 🔄 **Fluxo de Cancelamento**

```
1. VERIFICAR ANTECEDÊNCIA
   ├── ≥24h → CANCELAMENTO_PROGRAMADO
   └── <24h → CANCELAMENTO_EMERGENCIAL

2. CANCELAMENTO_PROGRAMADO
   ├── Cancelar consulta
   ├── Notificar paciente
   └── Liberar horário

3. CANCELAMENTO_EMERGENCIAL
   ├── Validar justificativa
   ├── Registrar log de auditoria
   ├── Notificar paciente (SMS + Email + Ligação)
   ├── Acionar reagendamento prioritário
   └── Gerar relatório para gestão
```

### 📱 **Interface de Cancelamento**

```
TELA: Cancelar Consulta
├── [Consulta: João Silva - 15/01 14:00]
├── [Antecedência: 8 horas] ⚠️ EMERGENCIAL
├── 
├── Motivo da Emergência: [Dropdown obrigatório]
│   ├── Emergência médica pessoal
│   ├── Emergência familiar
│   ├── Chamada para urgência hospitalar
│   └── Outros (especificar)
├── 
├── Justificativa: [Texto obrigatório]
├── 
├── ☑️ Confirmo que é uma situação emergencial
├── ☑️ Autorizo reagendamento prioritário
├── 
└── [CANCELAR EMERGENCIAL] [VOLTAR]
```

## Benefícios da Solução

### ✅ **Vantagens**

1. **Flexibilidade**: Permite cancelamentos emergenciais quando necessário
2. **Controle**: Mantém rastreabilidade e justificativas
3. **Experiência do Paciente**: Notificação imediata + reagendamento prioritário
4. **Auditoria**: Logs completos para análise posterior
5. **Prevenção de Abuso**: Justificativas obrigatórias inibem uso inadequado

### 📊 **Métricas de Monitoramento**

- Taxa de cancelamentos emergenciais por médico
- Tempo médio de reagendamento
- Satisfação do paciente pós-cancelamento
- Distribuição de motivos de cancelamento

## Implementação por Fases

### **Fase 1**: Estrutura Básica
- Implementar tipos de cancelamento
- Criar interface de justificativas
- Configurar notificações diferenciadas

### **Fase 2**: Automação
- Reagendamento automático prioritário
- Integração com sistema de notificações
- Dashboard de monitoramento

### **Fase 3**: Inteligência
- Análise preditiva de cancelamentos
- Sugestões automáticas de reagendamento
- Alertas para padrões suspeitos

## Conclusão

A solução proposta **resolve o conflito** mantendo:
- **Flexibilidade operacional** para emergências
- **Proteção ao paciente** com notificações e reagendamentos
- **Controle administrativo** com auditoria e justificativas
- **Experiência de usuário** otimizada para ambos os cenários

Esta abordagem transforma um conflito de regras em uma **funcionalidade robusta** que atende às necessidades reais da clínica médica.