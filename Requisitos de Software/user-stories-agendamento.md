# User Stories - Agendamento de Consultas

## RF03: Agendamento de Consultas
**Requisito Original**: O sistema deve permitir agendar consultas especificando paciente, médico, data e horário

---

## US001 - Agendar Nova Consulta

**Como** recepcionista da clínica,  
**Eu quero** agendar uma nova consulta selecionando paciente, médico, data e horário,  
**Para que** eu possa organizar a agenda médica e garantir atendimento aos pacientes.

### Critérios de Aceite:

1. **Seleção de Paciente**
   - O sistema deve permitir buscar e selecionar um paciente cadastrado
   - Deve exibir nome completo e CPF do paciente selecionado
   - Caso o paciente não esteja cadastrado, deve permitir redirecionamento para cadastro

2. **Seleção de Médico e Horário**
   - O sistema deve listar apenas médicos disponíveis na data selecionada
   - Deve exibir horários livres do médico em intervalos de 30 minutos
   - Deve respeitar o horário de funcionamento (7h às 18h, segunda a sexta)

3. **Validação e Confirmação**
   - O sistema deve validar se o horário ainda está disponível antes de confirmar
   - Deve exibir resumo da consulta (paciente, médico, data/hora) para confirmação
   - Após confirmação, deve gerar número de protocolo único para a consulta

---

## US002 - Verificar Disponibilidade de Horários

**Como** recepcionista da clínica,  
**Eu quero** visualizar a disponibilidade de horários por médico e data,  
**Para que** eu possa oferecer as melhores opções de agendamento aos pacientes.

### Critérios de Aceite:

1. **Visualização de Agenda**
   - O sistema deve exibir agenda semanal ou diária do médico selecionado
   - Deve mostrar horários ocupados, livres e bloqueados de forma visual
   - Deve permitir navegação entre diferentes datas e médicos

2. **Filtros e Busca**
   - O sistema deve permitir filtrar por especialidade médica
   - Deve permitir busca por nome do médico
   - Deve exibir próximos horários disponíveis automaticamente

3. **Informações Detalhadas**
   - Ao clicar em horário ocupado, deve mostrar apenas "Ocupado" (sem dados do paciente)
   - Deve exibir tempo estimado de consulta (padrão 30 minutos)
   - Deve indicar se há lista de espera para cancelamentos

---

## US003 - Validar Conflitos de Agendamento

**Como** sistema de agendamento,  
**Eu quero** verificar automaticamente conflitos de horário,  
**Para que** não ocorram duplos agendamentos ou sobreposições de consultas.

### Critérios de Aceite:

1. **Validação de Conflitos**
   - O sistema deve impedir agendamento no mesmo horário para o mesmo médico
   - Deve verificar se o paciente já possui consulta agendada no mesmo dia
   - Deve validar se o horário respeita o intervalo mínimo de 30 minutos entre consultas

2. **Regras de Negócio**
   - O sistema deve impedir agendamentos com menos de 1 hora de antecedência
   - Deve bloquear agendamentos fora do horário de funcionamento
   - Deve verificar se o médico não está em férias ou licença na data solicitada

3. **Tratamento de Erros**
   - Deve exibir mensagem clara quando houver conflito de horário
   - Deve sugerir horários alternativos próximos ao solicitado
   - Deve permitir inclusão em lista de espera caso não haja horários disponíveis

---

## Definição de Pronto (Definition of Done)

Para que uma User Story seja considerada concluída, deve atender:

- [ ] Todos os critérios de aceite implementados
- [ ] Testes unitários criados e passando
- [ ] Interface responsiva e acessível
- [ ] Validações de segurança implementadas
- [ ] Logs de auditoria registrados
- [ ] Documentação técnica atualizada
- [ ] Aprovação do Product Owner

---

## Notas Técnicas

- **Prioridade**: Alta
- **Estimativa**: 13 Story Points
- **Sprint**: 1
- **Dependências**: Cadastro de Pacientes (RF01) e Cadastro de Médicos (RF02)