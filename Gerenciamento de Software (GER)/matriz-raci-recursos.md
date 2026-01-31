# Matriz RACI e Alocação de Recursos - Módulo de Histórico

**Data**: 31/01/2026  
**Gerente de Projeto**: Adriam  
**Versão**: 1.0

---

## 👥 Definição da Equipe

### **Papéis e Responsabilidades**

| Papel | Nome/Perfil | Dedicação | Custo/Hora |
|-------|-------------|-----------|------------|
| **Product Owner (PO)** | Dr. Silva (Médico) | 20% (8h/semana) | R$ 200 |
| **Scrum Master (SM)** | Adriam | 25% (10h/semana) | R$ 150 |
| **Backend Developer (BE)** | Dev Backend | 100% (40h/semana) | R$ 100 |
| **Frontend Developer (FE)** | Dev Frontend | 100% (40h/semana) | R$ 100 |
| **QA Engineer (QA)** | Analista QA | 50% (20h/semana) | R$ 80 |
| **DevOps (DO)** | Especialista DevOps | 10% (4h/semana) | R$ 120 |

---

## 📋 Matriz RACI

### **Legenda**
- **R** = Responsible (Responsável pela execução)
- **A** = Accountable (Prestação de contas/aprovação)
- **C** = Consulted (Consultado)
- **I** = Informed (Informado)

| Atividade | PO | SM | BE | FE | QA | DO |
|-----------|----|----|----|----|----|----|
| **SPRINT 1 - FUNDAÇÃO** |
| Definir requisitos funcionais | **R** | C | C | C | C | I |
| Modelagem de dados | C | I | **R** | I | C | C |
| Criar API REST básica | C | I | **R** | I | C | I |
| Testes unitários backend | I | C | C | I | **R** | I |
| Validação médica | **A** | C | I | I | I | I |
| **SPRINT 2 - INTERFACE** |
| Design de interface | **A** | C | I | **R** | C | I |
| Implementar componentes | C | I | I | **R** | C | I |
| Integração frontend-backend | C | C | C | **R** | C | I |
| Testes de interface | C | C | I | C | **R** | I |
| Validação UX médica | **A** | C | I | C | C | I |
| **SPRINT 3 - REFINAMENTO** |
| Otimização performance | C | C | **R** | C | C | **A** |
| Relatórios e exportação | **A** | C | C | **R** | C | I |
| Monitoramento integrado | I | C | C | I | C | **R** |
| Testes de integração | C | C | C | C | **R** | C |
| Documentação técnica | C | **A** | C | C | C | C |
| **GESTÃO DO PROJETO** |
| Sprint Planning | C | **A** | **R** | **R** | **R** | C |
| Daily Standups | C | **A** | **R** | **R** | **R** | C |
| Sprint Review | **A** | **R** | **R** | **R** | **R** | C |
| Sprint Retrospective | C | **A** | **R** | **R** | **R** | C |
| Comunicação stakeholders | **A** | **R** | I | I | I | I |

---

## ⏰ Alocação de Recursos Humanos (84h)

### **Distribuição por Sprint**

#### **Sprint 1 - Fundação (22h)**
| Papel | Horas | Atividades Principais |
|-------|-------|----------------------|
| **Backend Dev** | 16h | Modelagem dados (8h) + API CRUD (8h) |
| **QA Engineer** | 6h | Testes unitários + validação |
| **Product Owner** | 4h | Definição requisitos + validação |
| **Scrum Master** | 2h | Facilitação + gestão |
| **Total Sprint 1** | **28h** | |

#### **Sprint 2 - Interface (30h)**
| Papel | Horas | Atividades Principais |
|-------|-------|----------------------|
| **Frontend Dev** | 24h | Interface (12h) + Filtros (8h) + Integração (4h) |
| **QA Engineer** | 6h | Testes de interface |
| **Product Owner** | 6h | Validação UX + feedback |
| **Backend Dev** | 2h | Ajustes API |
| **Scrum Master** | 2h | Facilitação + gestão |
| **Total Sprint 2** | **40h** | |

#### **Sprint 3 - Refinamento (32h)**
| Papel | Horas | Atividades Principais |
|-------|-------|----------------------|
| **Backend Dev** | 8h | Performance + otimização |
| **Frontend Dev** | 10h | Relatórios + exportação |
| **QA Engineer** | 8h | Testes integração + performance |
| **DevOps** | 4h | Monitoramento + deploy |
| **Product Owner** | 4h | Validação final + aceite |
| **Scrum Master** | 2h | Facilitação + documentação |
| **Total Sprint 3** | **36h** | |

### **📊 Resumo de Alocação Total**

| Papel | Total Horas | % do Projeto | Custo Total |
|-------|-------------|--------------|-------------|
| **Backend Developer** | 26h | 31% | R$ 2.600 |
| **Frontend Developer** | 34h | 40% | R$ 3.400 |
| **QA Engineer** | 20h | 24% | R$ 1.600 |
| **Product Owner** | 14h | 17% | R$ 2.800 |
| **DevOps** | 4h | 5% | R$ 480 |
| **Scrum Master** | 6h | 7% | R$ 900 |
| **TOTAL** | **104h** | **124%*** | **R$ 11.780** |

*\*Overlap de papéis e atividades de gestão*

---

## 📞 Plano de Comunicação

### **🎯 Stakeholders Identificados**

| Stakeholder | Interesse | Influência | Estratégia |
|-------------|-----------|------------|------------|
| **Dr. Silva (PO)** | Alto | Alto | Envolvimento direto |
| **Médicos da Clínica** | Alto | Médio | Demonstrações + feedback |
| **Recepcionistas** | Médio | Baixo | Treinamento + suporte |
| **Diretor Clínica** | Alto | Alto | Relatórios executivos |
| **Equipe TI** | Alto | Médio | Comunicação técnica |

### **📅 Cronograma de Comunicação**

#### **Comunicação Regular**

| Evento | Frequência | Participantes | Duração | Objetivo |
|--------|------------|---------------|---------|----------|
| **Daily Standup** | Diário | Equipe dev | 15min | Sincronização técnica |
| **Sprint Review** | A cada 2 semanas | PO + Médicos + Equipe | 1h | Demonstração + feedback |
| **Sprint Retrospective** | A cada 2 semanas | Equipe dev | 30min | Melhoria contínua |
| **Status Report** | Semanal | Diretor + PO | 15min | Acompanhamento executivo |

#### **Comunicação por Sprint**

### **Sprint 1 - Fundação**
```
Semana 1:
├── Kick-off Meeting (2h)
│   ├── Participantes: Todos stakeholders
│   ├── Objetivo: Alinhamento inicial
│   └── Entregáveis: Roadmap + expectativas
├── Sprint Planning (1h)
│   ├── Participantes: Equipe dev + PO
│   └── Objetivo: Definir backlog Sprint 1
└── Daily Standups (15min × 5 dias)

Semana 2:
├── Mid-Sprint Check (30min)
│   ├── Participantes: PO + SM + Tech Lead
│   └── Objetivo: Ajustes de curso
├── Sprint Review (1h)
│   ├── Participantes: Médicos + Equipe
│   ├── Demo: API funcionando
│   └── Feedback: Validação técnica
└── Sprint Retrospective (30min)
```

### **Sprint 2 - Interface**
```
Semana 3:
├── Sprint Planning (1h)
├── Design Review (1h)
│   ├── Participantes: Médicos + UX + Dev
│   └── Objetivo: Validar interface
└── Daily Standups (15min × 5 dias)

Semana 4:
├── User Testing Session (2h)
│   ├── Participantes: 3 médicos + 2 recepcionistas
│   ├── Objetivo: Testar usabilidade
│   └── Método: Observação + questionário
├── Sprint Review (1h)
│   ├── Demo: Interface funcionando
│   └── Feedback: UX + funcionalidades
└── Sprint Retrospective (30min)
```

### **Sprint 3 - Refinamento**
```
Semana 5:
├── Sprint Planning (1h)
├── Performance Review (30min)
│   ├── Participantes: DevOps + Backend
│   └── Objetivo: Validar métricas
└── Daily Standups (15min × 5 dias)

Semana 6:
├── Final Demo (1.5h)
│   ├── Participantes: Todos stakeholders
│   ├── Demo: Sistema completo
│   └── Aceite: Validação final
├── Go-Live Planning (1h)
│   ├── Treinamento: Cronograma
│   ├── Suporte: Plano de suporte
│   └── Rollout: Estratégia de implantação
└── Project Closure (30min)
```

### **📊 Canais de Comunicação**

| Canal | Uso | Frequência | Responsável |
|-------|-----|------------|-------------|
| **WhatsApp Grupo** | Comunicação rápida | Conforme necessário | SM |
| **Email Semanal** | Status reports | Semanal | SM |
| **Slack/Teams** | Comunicação técnica | Diário | Equipe Dev |
| **Jira/Trello** | Acompanhamento tasks | Tempo real | Todos |
| **Google Meet** | Reuniões remotas | Conforme agenda | SM |

### **📋 Templates de Comunicação**

#### **Status Report Semanal**
```
ASSUNTO: [Histórico Pacientes] Status Semana X

🎯 PROGRESSO:
- Sprint atual: X/3
- Horas executadas: X/84h
- Funcionalidades entregues: X

📊 MÉTRICAS:
- Velocity: X story points
- Bugs encontrados: X
- Testes passando: X%

🚨 RISCOS/BLOQUEIOS:
- [Listar se houver]

📅 PRÓXIMOS PASSOS:
- [Atividades da próxima semana]

👥 FEEDBACK NECESSÁRIO:
- [Decisões pendentes dos médicos]
```

#### **Convite Sprint Review**
```
ASSUNTO: [CONVITE] Demo Sprint X - Módulo Histórico

📅 Data: [Data]
🕐 Horário: [Horário]
📍 Local: [Presencial/Online]

🎯 AGENDA:
- Demo das funcionalidades (30min)
- Feedback e validação (20min)
- Próximos passos (10min)

💻 SERÁ DEMONSTRADO:
- [Lista de funcionalidades]

👥 SUA PARTICIPAÇÃO É IMPORTANTE:
Seu feedback é essencial para garantir que o sistema atenda às necessidades médicas.
```

### **🎯 KPIs de Comunicação**

| Métrica | Meta | Medição |
|---------|------|---------|
| **Participação Sprint Reviews** | 100% médicos | Presença/reunião |
| **Tempo resposta feedback** | < 24h | Tempo médio |
| **Satisfação comunicação** | > 4.0/5.0 | Survey mensal |
| **Clareza requisitos** | < 10% retrabalho | % mudanças |

---

## 🚀 Próximos Passos

### **Semana 1 - Setup**
- [ ] Confirmar disponibilidade da equipe
- [ ] Agendar kick-off meeting
- [ ] Criar canais de comunicação
- [ ] Preparar ambiente de desenvolvimento

### **Semana 2 - Início Sprint 1**
- [ ] Sprint Planning detalhado
- [ ] Definir Definition of Done
- [ ] Iniciar desenvolvimento
- [ ] Estabelecer rotina de comunicação

**Aprovação necessária**: Diretor da Clínica + Dr. Silva (PO)  
**Data limite aprovação**: 07/02/2026