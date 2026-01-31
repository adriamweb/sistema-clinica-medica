# Configuração de Monitoramento - Sistema de Triagem

## 📊 Métricas Monitoradas

### Performance
- **tempo_ordenacao**: Tempo para ordenar fila de pacientes
- **tempo_espera**: Tempo que paciente aguarda na fila
- **tamanho_fila**: Número de pacientes na fila

### Operações
- **pacientes_adicionados**: Total de pacientes cadastrados
- **pacientes_atendidos**: Total de pacientes atendidos
- **erros_validacao**: Erros de entrada de dados

## 🚨 Thresholds de Alerta

| Métrica | Threshold | Ação |
|---------|-----------|------|
| tempo_ordenacao | > 1.0s | Alerta de performance |
| tamanho_fila | > 50 | Alerta de capacidade |
| tempo_espera | > 300s | Alerta de atendimento |
| erros_validacao | 5+ consecutivos | Alerta de qualidade |

## 📁 Arquivos de Log

- **triagem_sistema.log**: Operações normais
- **triagem_metricas.log**: Métricas de performance
- **triagem_erros.log**: Erros e alertas

## 🔍 Monitoramento Proativo

### Detecção de Anomalias
- Picos de tempo de ordenação
- Crescimento anormal da fila
- Erros de validação frequentes
- Degradação de performance

### Alertas Automáticos
- Console: Alertas imediatos
- Logs: Registro estruturado
- Métricas: Análise histórica

## 📈 Dashboard de Métricas

Execute `gerar_relatorio_sistema()` para ver:
- Contadores em tempo real
- Métricas de performance
- Histórico de operações
- Status de alertas