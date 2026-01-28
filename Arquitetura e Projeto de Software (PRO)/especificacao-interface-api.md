# Especificação Técnica de Interface - API REST Agendamento

**Versão**: 1.0  
**Data**: 27/01/2024  
**Arquiteto**: Arquiteto de Software Sênior  
**Status**: Aprovado para Implementação

---

## 📋 Visão Geral

Esta especificação define as interfaces da API REST para o módulo de Agendamento e a comunicação inter-modular no sistema de clínica médica.

### **Base URL**
```
https://api.clinica-medica.com/v1
```

### **Autenticação**
```
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json
```

---

## 🔗 API REST - Módulo de Agendamento

### **1. 📅 Criar Agendamento**

#### **POST** `/appointments`

##### **Request Body**
```json
{
  "patientId": "uuid",
  "doctorId": "uuid", 
  "dateTime": "2024-02-15T14:30:00Z",
  "duration": 30,
  "notes": "Consulta de rotina",
  "priority": "normal"
}
```

##### **Response 201 - Created**
```json
{
  "success": true,
  "data": {
    "id": "apt_123456789",
    "protocol": "#AG2024001",
    "patientId": "uuid",
    "doctorId": "uuid",
    "dateTime": "2024-02-15T14:30:00Z",
    "duration": 30,
    "status": "scheduled",
    "notes": "Consulta de rotina",
    "priority": "normal",
    "createdAt": "2024-01-27T10:00:00Z",
    "updatedAt": "2024-01-27T10:00:00Z"
  },
  "message": "Agendamento criado com sucesso"
}
```

##### **Response 400 - Bad Request**
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Dados inválidos fornecidos",
    "details": [
      {
        "field": "dateTime",
        "message": "Data deve ser futura"
      }
    ]
  }
}
```

##### **Response 409 - Conflict**
```json
{
  "success": false,
  "error": {
    "code": "TIME_CONFLICT",
    "message": "Horário não disponível",
    "details": {
      "conflictingAppointment": "apt_987654321",
      "suggestedTimes": [
        "2024-02-15T15:00:00Z",
        "2024-02-15T15:30:00Z"
      ]
    }
  }
}
```

---

### **2. 📋 Listar Agendamentos**

#### **GET** `/appointments`

##### **Query Parameters**
```
?doctorId=uuid&date=2024-02-15&status=scheduled&page=1&limit=20
```

##### **Response 200 - OK**
```json
{
  "success": true,
  "data": {
    "appointments": [
      {
        "id": "apt_123456789",
        "protocol": "#AG2024001",
        "patient": {
          "id": "uuid",
          "name": "Maria Silva Santos",
          "phone": "(11) 99999-9999"
        },
        "doctor": {
          "id": "uuid", 
          "name": "Dr. João Silva",
          "specialty": "Cardiologia"
        },
        "dateTime": "2024-02-15T14:30:00Z",
        "duration": 30,
        "status": "scheduled",
        "priority": "normal"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 45,
      "totalPages": 3
    }
  }
}
```

---

### **3. 🔍 Buscar Agendamento por ID**

#### **GET** `/appointments/{id}`

##### **Response 200 - OK**
```json
{
  "success": true,
  "data": {
    "id": "apt_123456789",
    "protocol": "#AG2024001",
    "patient": {
      "id": "uuid",
      "name": "Maria Silva Santos",
      "cpf": "123.456.789-00",
      "phone": "(11) 99999-9999",
      "email": "maria@email.com"
    },
    "doctor": {
      "id": "uuid",
      "name": "Dr. João Silva", 
      "crm": "12345-SP",
      "specialty": "Cardiologia",
      "phone": "(11) 88888-8888"
    },
    "dateTime": "2024-02-15T14:30:00Z",
    "duration": 30,
    "status": "scheduled",
    "notes": "Consulta de rotina",
    "priority": "normal",
    "createdAt": "2024-01-27T10:00:00Z",
    "updatedAt": "2024-01-27T10:00:00Z"
  }
}
```

##### **Response 404 - Not Found**
```json
{
  "success": false,
  "error": {
    "code": "APPOINTMENT_NOT_FOUND",
    "message": "Agendamento não encontrado"
  }
}
```

---

### **4. ✏️ Atualizar Agendamento**

#### **PUT** `/appointments/{id}`

##### **Request Body**
```json
{
  "dateTime": "2024-02-15T15:00:00Z",
  "notes": "Consulta reagendada",
  "priority": "high"
}
```

##### **Response 200 - OK**
```json
{
  "success": true,
  "data": {
    "id": "apt_123456789",
    "protocol": "#AG2024001",
    "patientId": "uuid",
    "doctorId": "uuid",
    "dateTime": "2024-02-15T15:00:00Z",
    "duration": 30,
    "status": "scheduled",
    "notes": "Consulta reagendada",
    "priority": "high",
    "updatedAt": "2024-01-27T11:00:00Z"
  },
  "message": "Agendamento atualizado com sucesso"
}
```

---

### **5. ❌ Cancelar Agendamento**

#### **DELETE** `/appointments/{id}`

##### **Request Body**
```json
{
  "reason": "Paciente solicitou cancelamento",
  "cancelledBy": "receptionist"
}
```

##### **Response 200 - OK**
```json
{
  "success": true,
  "data": {
    "id": "apt_123456789",
    "status": "cancelled",
    "cancelledAt": "2024-01-27T12:00:00Z",
    "cancelReason": "Paciente solicitou cancelamento",
    "cancelledBy": "receptionist"
  },
  "message": "Agendamento cancelado com sucesso"
}
```

---

### **6. 🕐 Verificar Disponibilidade**

#### **GET** `/appointments/availability`

##### **Query Parameters**
```
?doctorId=uuid&date=2024-02-15&duration=30
```

##### **Response 200 - OK**
```json
{
  "success": true,
  "data": {
    "doctorId": "uuid",
    "date": "2024-02-15",
    "availableSlots": [
      {
        "startTime": "07:00:00",
        "endTime": "07:30:00",
        "available": true
      },
      {
        "startTime": "07:30:00", 
        "endTime": "08:00:00",
        "available": true
      },
      {
        "startTime": "08:00:00",
        "endTime": "08:30:00", 
        "available": false,
        "reason": "occupied"
      }
    ],
    "workingHours": {
      "start": "07:00:00",
      "end": "18:00:00"
    }
  }
}
```

---

### **7. 📊 Agenda do Médico**

#### **GET** `/appointments/doctor/{doctorId}/agenda`

##### **Query Parameters**
```
?date=2024-02-15&view=day
```

##### **Response 200 - OK**
```json
{
  "success": true,
  "data": {
    "doctorId": "uuid",
    "doctorName": "Dr. João Silva",
    "date": "2024-02-15",
    "appointments": [
      {
        "id": "apt_123456789",
        "patientName": "Maria Silva Santos",
        "startTime": "14:30:00",
        "endTime": "15:00:00",
        "status": "scheduled",
        "priority": "normal"
      }
    ],
    "summary": {
      "totalAppointments": 8,
      "scheduled": 6,
      "completed": 1,
      "cancelled": 1
    }
  }
}
```

---

## 🔄 Comunicação Inter-Modular

### **Arquitetura de Comunicação**

```
┌─────────────────────────────────────────────────────────┐
│                COMUNICAÇÃO INTER-MODULAR                │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─────────────────┐    ┌─────────────────────────────┐ │
│  │   Appointment   │    │        Patient Module       │ │
│  │     Module      │◄──►│                             │ │
│  └─────────────────┘    └─────────────────────────────┘ │
│           │                                             │
│           ▼                                             │
│  ┌─────────────────┐    ┌─────────────────────────────┐ │
│  │  Medical Staff  │    │      Notification           │ │
│  │     Module      │    │        Module               │ │
│  └─────────────────┘    └─────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

### **1. Appointment ↔ Patient Module**

#### **Padrão**: Direct Function Calls (Monolito Modular)

##### **Interface de Comunicação**
```typescript
// Patient Module Interface
interface IPatientService {
  findById(id: string): Promise<Patient | null>
  findByCPF(cpf: string): Promise<Patient | null>
  validatePatientExists(id: string): Promise<boolean>
  getPatientBasicInfo(id: string): Promise<PatientBasicInfo>
}

// Appointment Module Usage
class AppointmentService {
  constructor(
    private patientService: IPatientService,
    private doctorService: IDoctorService
  ) {}

  async createAppointment(data: CreateAppointmentDTO): Promise<Appointment> {
    // 1. Validar se paciente existe
    const patient = await this.patientService.findById(data.patientId)
    if (!patient) {
      throw new AppointmentError('PATIENT_NOT_FOUND', 'Paciente não encontrado')
    }

    // 2. Validar se médico existe
    const doctor = await this.doctorService.findById(data.doctorId)
    if (!doctor) {
      throw new AppointmentError('DOCTOR_NOT_FOUND', 'Médico não encontrado')
    }

    // 3. Criar agendamento
    return await this.appointmentRepository.create({
      ...data,
      patient,
      doctor
    })
  }
}
```

##### **Fluxo de Dados**
```
1. Appointment Controller recebe request
2. Appointment Service chama Patient Service
3. Patient Service consulta Patient Repository
4. Patient Repository retorna dados do paciente
5. Appointment Service valida e cria agendamento
6. Appointment Repository persiste no banco
```

---

### **2. Appointment ↔ Medical Staff Module**

#### **Interface de Comunicação**
```typescript
// Medical Staff Module Interface
interface IDoctorService {
  findById(id: string): Promise<Doctor | null>
  findBySpecialty(specialty: string): Promise<Doctor[]>
  checkAvailability(doctorId: string, dateTime: Date): Promise<boolean>
  getDoctorSchedule(doctorId: string, date: Date): Promise<Schedule>
  updateDoctorAvailability(doctorId: string, slots: TimeSlot[]): Promise<void>
}

// Appointment Module Usage
class AvailabilityService {
  constructor(private doctorService: IDoctorService) {}

  async getAvailableSlots(doctorId: string, date: Date): Promise<TimeSlot[]> {
    // 1. Obter agenda do médico
    const schedule = await this.doctorService.getDoctorSchedule(doctorId, date)
    
    // 2. Obter consultas já agendadas
    const existingAppointments = await this.appointmentRepository
      .findByDoctorAndDate(doctorId, date)
    
    // 3. Calcular slots disponíveis
    return this.calculateAvailableSlots(schedule, existingAppointments)
  }
}
```

---

### **3. Event-Driven Communication (Eventos Assíncronos)**

#### **Para Operações Não-Críticas**
```typescript
// Event Bus Implementation
interface IEventBus {
  publish(event: DomainEvent): Promise<void>
  subscribe(eventType: string, handler: EventHandler): void
}

// Domain Events
class AppointmentCreatedEvent implements DomainEvent {
  constructor(
    public readonly appointmentId: string,
    public readonly patientId: string,
    public readonly doctorId: string,
    public readonly dateTime: Date,
    public readonly occurredAt: Date = new Date()
  ) {}
}

// Event Handlers
class NotificationEventHandler {
  async handle(event: AppointmentCreatedEvent): Promise<void> {
    // Enviar notificação para paciente
    await this.notificationService.sendAppointmentConfirmation({
      patientId: event.patientId,
      appointmentId: event.appointmentId,
      dateTime: event.dateTime
    })
  }
}

// Usage in Appointment Service
class AppointmentService {
  async createAppointment(data: CreateAppointmentDTO): Promise<Appointment> {
    const appointment = await this.appointmentRepository.create(data)
    
    // Publicar evento assíncrono
    await this.eventBus.publish(
      new AppointmentCreatedEvent(
        appointment.id,
        appointment.patientId,
        appointment.doctorId,
        appointment.dateTime
      )
    )
    
    return appointment
  }
}
```

---

### **4. Padrões de Comunicação por Cenário**

| Cenário | Padrão | Justificativa |
|---------|--------|---------------|
| **Validação de Paciente** | Direct Call | Síncrono, crítico para validação |
| **Verificar Disponibilidade** | Direct Call | Síncrono, dados em tempo real |
| **Enviar Notificação** | Event-Driven | Assíncrono, não-crítico |
| **Auditoria** | Event-Driven | Assíncrono, logging |
| **Relatórios** | Direct Call | Síncrono, consulta de dados |

---

## 🔒 Segurança e Validação

### **Validação de Entrada**
```typescript
// DTO Validation
class CreateAppointmentDTO {
  @IsUUID()
  patientId: string

  @IsUUID() 
  doctorId: string

  @IsISO8601()
  @IsAfter(new Date())
  dateTime: string

  @IsInt()
  @Min(15)
  @Max(120)
  duration: number

  @IsOptional()
  @MaxLength(500)
  notes?: string
}
```

### **Autorização**
```typescript
// Role-Based Access Control
@Controller('/appointments')
@UseGuards(JwtAuthGuard, RoleGuard)
export class AppointmentController {
  
  @Post()
  @Roles('receptionist', 'doctor', 'admin')
  async create(@Body() dto: CreateAppointmentDTO) {
    return await this.appointmentService.create(dto)
  }

  @Get(':id')
  @Roles('receptionist', 'doctor', 'admin', 'patient')
  async findOne(@Param('id') id: string, @CurrentUser() user: User) {
    // Pacientes só podem ver seus próprios agendamentos
    if (user.role === 'patient') {
      return await this.appointmentService.findByIdAndPatient(id, user.patientId)
    }
    return await this.appointmentService.findById(id)
  }
}
```

---

## 📊 Monitoramento e Métricas

### **Health Checks**
```typescript
@Controller('/health')
export class HealthController {
  
  @Get('/appointments')
  async checkAppointmentModule(): Promise<HealthStatus> {
    const checks = await Promise.allSettled([
      this.appointmentRepository.healthCheck(),
      this.patientService.healthCheck(),
      this.doctorService.healthCheck()
    ])
    
    return {
      status: checks.every(c => c.status === 'fulfilled') ? 'healthy' : 'unhealthy',
      timestamp: new Date(),
      dependencies: this.mapHealthChecks(checks)
    }
  }
}
```

### **Métricas de Performance**
```typescript
// Metrics Collection
interface AppointmentMetrics {
  totalAppointments: number
  appointmentsPerDay: number
  averageResponseTime: number
  errorRate: number
  moduleHealthScore: number
}
```

---

## 🚀 Próximos Passos

### **Implementação**
1. **Setup Base** (Semana 1)
   - [ ] Configurar estrutura de módulos
   - [ ] Implementar interfaces base
   - [ ] Setup de validação e segurança

2. **Core Endpoints** (Semana 2)
   - [ ] Implementar CRUD de agendamentos
   - [ ] Integrar com módulos Patient e Doctor
   - [ ] Testes de integração

3. **Features Avançadas** (Semana 3)
   - [ ] Sistema de eventos
   - [ ] Verificação de disponibilidade
   - [ ] Métricas e monitoramento

### **Testes**
- [ ] Testes unitários para cada endpoint
- [ ] Testes de integração inter-modular
- [ ] Testes de carga para performance
- [ ] Testes de segurança

---

**Documento aprovado por**: Arquiteto de Software Sênior  
**Data de aprovação**: 27/01/2024  
**Próxima revisão**: Após implementação dos endpoints core