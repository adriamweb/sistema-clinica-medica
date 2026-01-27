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
    participant R as 👤 Recepcionista
    participant UI as 🖥️ Interface
    participant S as ⚙️ Sistema
    participant DB as 🗄️ Banco de Dados
    participant N as 📧 Notificação
    
    Note over R,N: Fluxo: Realizar Agendamento de Consulta
    
    %% 1. Buscar Paciente
    R->>+UI: Digita nome/CPF do paciente
    UI->>+S: buscarPaciente(termo)
    S->>+DB: SELECT pacientes
    DB-->>-S: Lista de pacientes
    S-->>-UI: Retorna pacientes encontrados
    UI-->>-R: Exibe lista de pacientes
    
    R->>UI: Seleciona paciente
    UI->>UI: Armazena dados do paciente
    
    %% 2. Selecionar Médico
    R->>+UI: Seleciona especialidade
    UI->>+S: listarMedicos(especialidade)
    S->>+DB: SELECT medicos
    DB-->>-S: Lista de médicos
    S-->>-UI: Retorna médicos disponíveis
    UI-->>-R: Exibe lista de médicos
    
    R->>UI: Seleciona médico
    UI->>UI: Armazena dados do médico
    
    %% 3. Selecionar Data
    R->>+UI: Seleciona data
    UI->>+S: verificarDisponibilidade(medicoId, data)
    S->>+DB: SELECT consultas existentes
    DB-->>-S: Consultas existentes
    S->>S: Calcula horários disponíveis
    S-->>-UI: Retorna grade de horários
    UI-->>-R: Exibe horários disponíveis
    
    %% 4. Selecionar Horário
    R->>+UI: Seleciona horário
    UI->>UI: Valida seleção
    UI-->>-R: Exibe resumo da consulta
    
    %% 5. Confirmar Agendamento
    R->>+UI: Clica Confirmar Agendamento
    UI->>+S: confirmarAgendamento(dadosConsulta)
    
    %% Validações
    S->>S: Validar regras de negócio
    S->>+DB: Verificar disponibilidade final
    DB-->>-S: Horário ainda disponível
    
    alt Horário disponível
        S->>+DB: INSERT consulta
        DB-->>-S: Consulta criada
        S->>S: Gerar protocolo único
        S->>+N: enviarNotificacao(pacienteId)
        N->>N: Enviar SMS/Email
        N-->>-S: Notificação enviada
        S->>+DB: INSERT log
        DB-->>-S: Log registrado
        S-->>-UI: Agendamento confirmado
        UI-->>R: Exibe modal de sucesso
    else Horário indisponível
        S-->>-UI: Erro: Horário não disponível
        UI-->>R: Exibe mensagem de erro
        UI->>UI: Atualiza grade de horários
    end
    
    %% 6. Finalização
    R->>UI: Fecha modal de confirmação
    UI->>UI: Limpa formulário
    
    Note over R,N: Consulta agendada com sucesso!
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