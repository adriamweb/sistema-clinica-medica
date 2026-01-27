# Requisitos do Sistema de Gestão de Clínica Médica

## Requisitos Funcionais (RF)

| ID | Requisito | Descrição | Prioridade |
|----|-----------|-----------|------------|
| RF01 | Cadastro de Pacientes | O sistema deve permitir cadastrar pacientes com dados pessoais (nome, CPF, RG, telefone, email, endereço, data de nascimento) | Alta |
| RF02 | Cadastro de Médicos | O sistema deve permitir cadastrar médicos com dados profissionais (nome, CRM, especialidade, telefone, email) | Alta |
| RF03 | Agendamento de Consultas | O sistema deve permitir agendar consultas especificando paciente, médico, data e horário | Alta |
| RF04 | Verificação de Conflitos | O sistema deve verificar conflitos de horário antes de confirmar agendamentos | Alta |
| RF05 | Cancelamento de Consultas | O sistema deve permitir cancelar consultas agendadas | Média |
| RF06 | Reagendamento de Consultas | O sistema deve permitir reagendar consultas existentes | Média |
| RF07 | Consulta de Agenda | O sistema deve exibir a agenda de consultas por médico e por data | Alta |
| RF08 | Prontuário Eletrônico | O sistema deve permitir criar e manter prontuários médicos dos pacientes | Alta |
| RF09 | Histórico do Paciente | O sistema deve exibir o histórico completo de consultas e tratamentos do paciente | Alta |
| RF10 | Busca de Pacientes | O sistema deve permitir buscar pacientes por nome, CPF ou ID | Média |
| RF11 | Busca de Médicos | O sistema deve permitir buscar médicos por nome, CRM ou especialidade | Média |
| RF12 | Registro de Consulta | O sistema deve permitir registrar informações da consulta (sintomas, diagnóstico, prescrição) | Alta |
| RF13 | Controle de Status | O sistema deve controlar o status das consultas (agendada, realizada, cancelada, faltou) | Média |
| RF14 | Notificações | O sistema deve enviar lembretes de consultas para pacientes | Baixa |
| RF15 | Relatórios Básicos | O sistema deve gerar relatórios de consultas por período e médico | Baixa |

## Requisitos Não Funcionais (RNF)

| ID | Requisito | Descrição | Categoria |
|----|-----------|-----------|-----------|
| RNF01 | Performance | O sistema deve responder às consultas em no máximo 2 segundos | Performance |
| RNF02 | Disponibilidade | O sistema deve estar disponível 99% do tempo durante horário comercial | Confiabilidade |
| RNF03 | Segurança de Dados | O sistema deve criptografar dados sensíveis dos pacientes | Segurança |
| RNF04 | Controle de Acesso | O sistema deve implementar autenticação e autorização por perfis de usuário | Segurança |
| RNF05 | Backup | O sistema deve realizar backup automático dos dados diariamente | Confiabilidade |
| RNF06 | Conformidade LGPD | O sistema deve estar em conformidade com a Lei Geral de Proteção de Dados | Legal |
| RNF07 | Interface Intuitiva | O sistema deve ter interface amigável e de fácil uso | Usabilidade |
| RNF08 | Compatibilidade | O sistema deve funcionar nos principais navegadores web | Portabilidade |
| RNF09 | Escalabilidade | O sistema deve suportar até 1000 pacientes e 50 médicos simultaneamente | Escalabilidade |
| RNF10 | Auditoria | O sistema deve registrar logs de todas as operações críticas | Segurança |
| RNF11 | Recuperação | O sistema deve permitir recuperação de dados em caso de falha | Confiabilidade |
| RNF12 | Manutenibilidade | O código deve seguir padrões de desenvolvimento para facilitar manutenção | Manutenibilidade |

## Regras de Negócio

| ID | Regra | Descrição |
|----|-------|-----------|
| RN01 | Horário de Funcionamento | Consultas só podem ser agendadas entre 7h e 18h, de segunda a sexta |
| RN02 | Intervalo Mínimo | Deve haver intervalo mínimo de 30 minutos entre consultas do mesmo médico |
| RN03 | Antecedência Mínima | Consultas devem ser agendadas com pelo menos 1 hora de antecedência |
| RN04 | Cancelamento | Consultas podem ser canceladas até 2 horas antes do horário agendado |
| RN05 | Dados Obrigatórios | CPF e telefone são obrigatórios para cadastro de pacientes |
| RN06 | CRM Único | Cada médico deve ter um CRM único no sistema |
| RN07 | Prontuário Obrigatório | Consultas realizadas devem ter prontuário preenchido |