# Diagramas UML - Módulo Agendamento de Consultas (Corrigido)

## 1. Diagrama de Caso de Uso

```mermaid
graph TB
    %% Atores
    R[👤 Recepcionista]
    M[👨⚕️ Médico]
    P[👥 Paciente]
    
    %% Sistema
    subgraph Sistema["🏥 Sistema de Agendamento"]
        UC1[Buscar Paciente]
        UC2[Cadastrar Paciente]
        UC3[Agendar Consulta]
        UC4[Verificar Disponibilidade]
        UC5[Cancelar Consulta]
        UC6[Reagendar Consulta]
        UC7[Consultar Agenda]
        UC8[Confirmar Presença]
        UC9[Gerar Relatórios]
        UC10[Notificar Paciente]
    end
    
    %% Relacionamentos Recepcionista
    R --> UC1
    R --> UC2
    R --> UC3
    R --> UC4
    R --> UC5
    R --> UC6
    R --> UC7
    R --> UC8
    R --> UC9
    
    %% Relacionamentos Médico
    M --> UC4
    M --> UC5
    M --> UC7
    M --> UC8
    
    %% Relacionamentos Paciente (indiretos)
    P -.-> UC10
    
    %% Relacionamentos entre casos de uso
    UC3 -.-> UC1
    UC3 -.-> UC4
    UC3 -.-> UC10
    UC2 -.-> UC3
    UC6 -.-> UC5
    UC6 -.-> UC3
    
    %% Estilos
    classDef ator fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef sistema fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef casoUso fill:#e8f5e8,stroke:#2e7d32,stroke-width:1px
    
    class R,M,P ator
    class Sistema sistema
    class UC1,UC2,UC3,UC4,UC5,UC6,UC7,UC8,UC9,UC10 casoUso
```

## 2. Diagrama de Sequência - Realizar Agendamento

```mermaid
sequenceDiagram
    participant R as Recepcionista
    participant UI as Interface
    participant S as Sistema
    participant DB as Banco
    participant N as Notificacao
    
    R->>UI: Digita nome do paciente
    UI->>S: buscarPaciente(termo)
    S->>DB: SELECT pacientes
    DB-->>S: Lista de pacientes
    S-->>UI: Retorna pacientes
    UI-->>R: Exibe lista
    
    R->>UI: Seleciona paciente
    R->>UI: Seleciona especialidade
    UI->>S: listarMedicos(especialidade)
    S->>DB: SELECT medicos
    DB-->>S: Lista de medicos
    S-->>UI: Retorna medicos
    UI-->>R: Exibe medicos
    
    R->>UI: Seleciona medico
    R->>UI: Seleciona data
    UI->>S: verificarDisponibilidade(medicoId, data)
    S->>DB: SELECT consultas
    DB-->>S: Consultas existentes
    S-->>UI: Grade de horarios
    UI-->>R: Exibe horarios
    
    R->>UI: Seleciona horario
    UI-->>R: Exibe resumo
    R->>UI: Confirma agendamento
    UI->>S: confirmarAgendamento(dados)
    
    alt Horario disponivel
        S->>DB: INSERT consulta
        DB-->>S: Consulta criada
        S->>N: enviarNotificacao(paciente)
        N-->>S: Notificacao enviada
        S->>DB: INSERT log
        DB-->>S: Log registrado
        S-->>UI: Agendamento confirmado
        UI-->>R: Modal de sucesso
    else Horario indisponivel
        S-->>UI: Erro horario
        UI-->>R: Mensagem de erro
    end
```

## 3. Diagrama de Atividades - Processo de Agendamento

```mermaid
flowchart TD
    Start([🚀 Iniciar Agendamento]) --> SearchPatient[🔍 Buscar Paciente]
    
    SearchPatient --> PatientFound{Paciente Encontrado?}
    PatientFound -->|Não| CreatePatient[➕ Cadastrar Novo Paciente]
    PatientFound -->|Sim| SelectPatient[✅ Selecionar Paciente]
    CreatePatient --> SelectPatient
    
    SelectPatient --> FilterSpecialty[🏥 Filtrar Especialidade]
    FilterSpecialty --> SelectDoctor[👨⚕️ Selecionar Médico]
    
    SelectDoctor --> SelectDate[📅 Selecionar Data]
    SelectDate --> ValidateDate{Data Válida?}
    ValidateDate -->|Não| SelectDate
    ValidateDate -->|Sim| LoadSchedule[⏰ Carregar Grade de Horários]
    
    LoadSchedule --> SelectTime[🕐 Selecionar Horário]
    SelectTime --> ShowSummary[📋 Exibir Resumo]
    
    ShowSummary --> ConfirmBooking[✅ Confirmar Agendamento]
    ConfirmBooking --> ValidateAvailability{Horário Ainda Disponível?}
    
    ValidateAvailability -->|Não| ShowError[❌ Exibir Erro]
    ShowError --> LoadSchedule
    
    ValidateAvailability -->|Sim| CreateAppointment[💾 Criar Consulta]
    CreateAppointment --> GenerateProtocol[🔢 Gerar Protocolo]
    GenerateProtocol --> SendNotification[📧 Enviar Notificação]
    SendNotification --> LogActivity[📝 Registrar Log]
    LogActivity --> ShowSuccess[🎉 Exibir Sucesso]
    ShowSuccess --> End([✨ Fim])
    
    %% Estilos
    classDef startEnd fill:#4caf50,stroke:#2e7d32,stroke-width:2px,color:#fff
    classDef process fill:#2196f3,stroke:#1565c0,stroke-width:2px,color:#fff
    classDef decision fill:#ff9800,stroke:#ef6c00,stroke-width:2px,color:#fff
    classDef error fill:#f44336,stroke:#c62828,stroke-width:2px,color:#fff
    
    class Start,End startEnd
    class SearchPatient,CreatePatient,SelectPatient,FilterSpecialty,SelectDoctor,SelectDate,LoadSchedule,SelectTime,ShowSummary,ConfirmBooking,CreateAppointment,GenerateProtocol,SendNotification,LogActivity,ShowSuccess process
    class PatientFound,ValidateDate,ValidateAvailability decision
    class ShowError error
```

## 4. Diagrama de Estados - Consulta

```mermaid
stateDiagram-v2
    [*] --> Agendada : Criar agendamento
    
    Agendada --> Confirmada : Paciente confirma presença
    Agendada --> Cancelada : Cancelamento solicitado
    Agendada --> Reagendada : Reagendamento solicitado
    
    Confirmada --> EmAndamento : Médico inicia consulta
    Confirmada --> Faltou : Paciente não comparece
    Confirmada --> Cancelada : Cancelamento de última hora
    
    EmAndamento --> Realizada : Consulta finalizada
    EmAndamento --> Interrompida : Emergência/Interrupção
    
    Interrompida --> Reagendada : Reagendar consulta
    Interrompida --> Cancelada : Cancelar definitivamente
    
    Reagendada --> Agendada : Nova data/hora definida
    
    Realizada --> [*]
    Cancelada --> [*]
    Faltou --> [*]
    
    note right of Agendada
        Status inicial após
        confirmação do agendamento
    end note
    
    note right of Realizada
        Consulta concluída
        Prontuário preenchido
    end note
```

## 5. Notas de Implementação

### Casos de Uso Principais:
- **UC3 - Agendar Consulta**: Caso de uso central que orquestra todo o processo
- **UC4 - Verificar Disponibilidade**: Essencial para evitar conflitos
- **UC10 - Notificar Paciente**: Automatização importante para experiência do usuário

### Fluxo de Sequência:
1. **Busca de Paciente**: Validação e seleção
2. **Seleção de Médico**: Filtros por especialidade
3. **Escolha de Data/Hora**: Verificação de disponibilidade em tempo real
4. **Confirmação**: Validação final e persistência
5. **Notificação**: Comunicação automática com paciente

### Estados da Consulta:
- **Agendada**: Estado inicial após confirmação
- **Confirmada**: Paciente confirmou presença
- **Realizada**: Consulta concluída com sucesso
- **Cancelada**: Cancelamento por qualquer motivo
- **Faltou**: Paciente não compareceu

### Validações Críticas:
- Verificação de disponibilidade antes da confirmação
- Validação de regras de negócio (horário de funcionamento)
- Controle de concorrência para evitar duplo agendamento