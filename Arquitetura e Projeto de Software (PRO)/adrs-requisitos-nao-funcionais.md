# ADRs e Análise de Requisitos Não Funcionais

**Versão**: 1.0  
**Data**: 27/01/2024  
**Arquiteto**: Arquiteto de Software Sênior  
**Status**: Aprovado

---

## 📋 Índice

1. [Decisões Arquiteturais (ADRs)](#-decisões-arquiteturais-adrs)
2. [Análise de Requisitos Não Funcionais](#-análise-de-requisitos-não-funcionais)
3. [Matriz de Rastreabilidade](#-matriz-de-rastreabilidade)

---

## 🏗️ Decisões Arquiteturais (ADRs)

### **ADR-001: Escolha da Stack Tecnológica Frontend**

#### **Status**: ✅ Aceito  
#### **Data**: 27/01/2024  
#### **Decisores**: Arquiteto de Software, Tech Lead

#### **Contexto**
Sistema de clínica médica precisa de interface web responsiva e intuitiva para recepcionistas e médicos, com foco em usabilidade e manutenibilidade.

#### **Decisão**
**Frontend Stack Escolhida**: React 18+ + TypeScript + Material-UI

#### **Alternativas Consideradas**
| Opção | Prós | Contras | Pontuação |
|-------|------|---------|-----------|
| **React + TypeScript** | Ecossistema maduro, TypeScript safety, comunidade ativa | Curva de aprendizado | ⭐⭐⭐⭐⭐ |
| Vue.js + TypeScript | Sintaxe simples, performance | Ecossistema menor | ⭐⭐⭐⭐ |
| Angular | Framework completo, TypeScript nativo | Complexidade alta, overhead | ⭐⭐⭐ |
| Vanilla JS | Simplicidade, controle total | Desenvolvimento lento, sem tooling | ⭐⭐ |

#### **Justificativa**
- **Maturidade**: React tem 10+ anos de mercado
- **Produtividade**: Material-UI acelera desenvolvimento
- **Type Safety**: TypeScript reduz bugs em produção
- **Comunidade**: Vasta documentação e suporte
- **Talent Pool**: Facilidade para encontrar desenvolvedores

#### **Consequências**
- ✅ Desenvolvimento mais rápido com componentes prontos
- ✅ Menor probabilidade de bugs com TypeScript
- ✅ Interface consistente com Material Design
- ❌ Bundle size maior que vanilla JS
- ❌ Dependência de bibliotecas externas

---

### **ADR-002: Escolha da Stack Tecnológica Backend**

#### **Status**: ✅ Aceito  
#### **Data**: 27/01/2024  
#### **Decisores**: Arquiteto de Software, Tech Lead

#### **Contexto**
Backend deve processar 200 consultas/dia, suportar 15 usuários simultâneos, com foco em performance e simplicidade de manutenção.

#### **Decisão**
**Backend Stack Escolhida**: Node.js + Express.js + TypeScript + Prisma ORM

#### **Alternativas Consideradas**
| Opção | Performance | Produtividade | Manutenibilidade | Pontuação |
|-------|-------------|---------------|------------------|-----------|
| **Node.js + Express** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Python + FastAPI | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Java + Spring Boot | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| C# + .NET Core | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

#### **Justificativa**
- **Unificação de Stack**: JavaScript/TypeScript no frontend e backend
- **Performance Adequada**: Event-loop atende volume esperado
- **Prisma ORM**: Type-safe database access, migrations automáticas
- **Ecossistema NPM**: Vasta biblioteca de pacotes
- **Time-to-Market**: Desenvolvimento mais rápido

#### **Consequências**
- ✅ Equipe única para frontend e backend
- ✅ Compartilhamento de tipos entre camadas
- ✅ Desenvolvimento mais ágil
- ❌ Single-threaded pode ser limitante no futuro
- ❌ Dependência do ecossistema Node.js

---

### **ADR-003: Escolha do Banco de Dados**

#### **Status**: ✅ Aceito  
#### **Data**: 27/01/2024  
#### **Decisores**: Arquiteto de Software, DBA

#### **Contexto**
Sistema precisa armazenar dados relacionais (pacientes, médicos, consultas) com integridade ACID e suporte a transações complexas.

#### **Decisão**
**Database Stack Escolhida**: PostgreSQL 15+ + Redis (Cache)

#### **Alternativas Consideradas**
| Opção | ACID | Performance | Escalabilidade | Custo | Pontuação |
|-------|------|-------------|----------------|-------|-----------|
| **PostgreSQL** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| MySQL | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| SQL Server | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| MongoDB | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |

#### **Justificativa**
- **ACID Compliance**: Essencial para dados médicos críticos
- **JSON Support**: Flexibilidade para dados semi-estruturados
- **Advanced Features**: Full-text search, arrays, triggers
- **Open Source**: Sem custos de licenciamento
- **Prisma Integration**: Excelente suporte do ORM escolhido
- **Redis Cache**: Performance boost para consultas frequentes

#### **Consequências**
- ✅ Integridade de dados garantida
- ✅ Performance otimizada com cache
- ✅ Flexibilidade para evolução do schema
- ✅ Custo zero de licenciamento
- ❌ Complexidade adicional com Redis
- ❌ Necessidade de expertise em PostgreSQL

---

### **ADR-004: Estratégia de Segurança para Dados Sensíveis**

#### **Status**: ✅ Aceito  
#### **Data**: 27/01/2024  
#### **Decisores**: Arquiteto de Software, Security Officer

#### **Contexto**
Sistema processa dados pessoais sensíveis (CPF, dados médicos) e deve estar em conformidade com LGPD, garantindo proteção adequada.

#### **Decisão**
**Estratégia de Segurança**: Criptografia em Camadas + Controles de Acesso

#### **Componentes da Estratégia**

##### **1. Criptografia de Dados**
```
┌─────────────────────────────────────────────────────────┐
│                 CAMADAS DE CRIPTOGRAFIA                 │
├─────────────────────────────────────────────────────────┤
│ 🔐 HTTPS/TLS 1.3        │ Dados em Trânsito           │
│ 🔐 Disk Encryption      │ Dados em Repouso            │
│ 🔐 Application Level    │ Campos Sensíveis            │
│ 🔐 Database TDE         │ Tablespaces Críticos        │
└─────────────────────────────────────────────────────────┘
```

##### **2. Controles de Acesso**
- **Autenticação**: JWT + Refresh Tokens (30min/7dias)
- **Autorização**: RBAC (Role-Based Access Control)
- **Auditoria**: Log de todas operações sensíveis
- **Rate Limiting**: 100 req/min por usuário

##### **3. Proteção de Dados Pessoais**
```typescript
// Exemplo de implementação
class DataProtectionService {
  encryptPII(data: string): string {
    return AES.encrypt(data, process.env.PII_KEY).toString()
  }
  
  maskCPF(cpf: string): string {
    return cpf.replace(/(\d{3})\d{3}(\d{3})/, '$1.***.$2-**')
  }
  
  logDataAccess(userId: string, dataType: string, action: string): void {
    auditLogger.info({ userId, dataType, action, timestamp: new Date() })
  }
}
```

#### **Alternativas Consideradas**
| Estratégia | Segurança | Complexidade | Performance | Custo |
|------------|-----------|--------------|-------------|-------|
| **Criptografia em Camadas** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Apenas Disk Encryption | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Field-Level Encryption | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐ |
| HSM (Hardware Security) | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐ |

#### **Justificativa**
- **Conformidade LGPD**: Atende todos os requisitos legais
- **Defense in Depth**: Múltiplas camadas de proteção
- **Balance**: Segurança vs Performance vs Custo
- **Auditabilidade**: Rastreamento completo de acessos
- **Escalabilidade**: Suporta crescimento futuro

#### **Consequências**
- ✅ Conformidade total com LGPD
- ✅ Proteção robusta de dados sensíveis
- ✅ Auditoria completa para compliance
- ❌ Overhead de performance (5-10%)
- ❌ Complexidade adicional de implementação

---

## 📊 Análise de Requisitos Não Funcionais

### **RNF09: Escalabilidade - "Suportar até 1000 pacientes e 50 médicos simultaneamente"**

#### **Como a Arquitetura Garante**

##### **1. Estratégia de Escalabilidade Vertical**
```
┌─────────────────────────────────────────────────────────┐
│                ESCALABILIDADE VERTICAL                  │
├─────────────────────────────────────────────────────────┤
│ CPU: 4 → 8 → 16 cores                                  │
│ RAM: 8GB → 16GB → 32GB                                 │
│ Storage: HDD → SSD → NVMe                              │
│ Network: 1Gbps → 10Gbps                               │
└─────────────────────────────────────────────────────────┘
```

##### **2. Otimizações de Performance**
- **Database Indexing**: Índices em campos de busca frequente
- **Connection Pooling**: Pool de 20-50 conexões simultâneas
- **Redis Cache**: Cache de consultas frequentes (TTL 5min)
- **Query Optimization**: Queries otimizadas com EXPLAIN ANALYZE

##### **3. Monitoramento de Capacidade**
```typescript
// Métricas de escalabilidade
interface ScalabilityMetrics {
  concurrentUsers: number        // Target: 50 usuários
  activePatients: number         // Target: 1000 pacientes
  appointmentsPerDay: number     // Target: 200 consultas/dia
  responseTime: number           // Target: < 2 segundos
  cpuUsage: number              // Alert: > 80%
  memoryUsage: number           // Alert: > 85%
  dbConnections: number         // Alert: > 80% do pool
}
```

##### **4. Plano de Escalabilidade Horizontal (Futuro)**
```
Fase 1: Monolito Otimizado (0-1000 pacientes)
├── Single server + Redis cache
├── Database read replicas
└── CDN para assets estáticos

Fase 2: Load Balancing (1000-5000 pacientes)
├── 2-3 application servers
├── Load balancer (NGINX)
└── Database clustering

Fase 3: Microservices (5000+ pacientes)
├── Notification service extraction
├── Reporting service extraction
└── API Gateway distribuído
```

#### **Validação do Requisito**
- ✅ **1000 Pacientes**: PostgreSQL suporta milhões de registros
- ✅ **50 Médicos**: Estrutura modular permite crescimento
- ✅ **Simultaneidade**: Node.js event-loop + connection pooling
- ✅ **Performance**: < 2s com cache e otimizações

---

### **RNF06: Conformidade LGPD - "Sistema em conformidade com Lei Geral de Proteção de Dados"**

#### **Como a Arquitetura Garante**

##### **1. Princípios LGPD Implementados**

| Princípio LGPD | Implementação Arquitetural |
|----------------|----------------------------|
| **Finalidade** | Logs de propósito de coleta de dados |
| **Adequação** | Validação de necessidade de dados |
| **Necessidade** | Coleta mínima de dados pessoais |
| **Livre Acesso** | API para consulta de dados pessoais |
| **Qualidade** | Validação e sanitização de dados |
| **Transparência** | Logs de processamento acessíveis |
| **Segurança** | Criptografia em múltiplas camadas |
| **Prevenção** | Controles preventivos de acesso |
| **Não Discriminação** | Auditoria de decisões automatizadas |
| **Responsabilização** | Logs de auditoria completos |

##### **2. Direitos dos Titulares**
```typescript
// Implementação dos direitos LGPD
class LGPDComplianceService {
  // Art. 18, I - Confirmação da existência de tratamento
  async confirmDataProcessing(cpf: string): Promise<boolean> {
    return await this.auditRepository.hasDataProcessing(cpf)
  }
  
  // Art. 18, II - Acesso aos dados
  async getPersonalData(cpf: string): Promise<PersonalDataReport> {
    return await this.dataRepository.getPersonalDataReport(cpf)
  }
  
  // Art. 18, III - Correção de dados
  async correctPersonalData(cpf: string, corrections: DataCorrection[]): Promise<void> {
    await this.patientService.updatePersonalData(cpf, corrections)
    await this.auditService.logDataCorrection(cpf, corrections)
  }
  
  // Art. 18, VI - Eliminação dos dados
  async deletePersonalData(cpf: string, reason: string): Promise<void> {
    await this.dataRepository.anonymizePersonalData(cpf)
    await this.auditService.logDataDeletion(cpf, reason)
  }
}
```

##### **3. Controles Técnicos**
- **Pseudonimização**: IDs internos não relacionados a CPF
- **Anonimização**: Processo de remoção de dados identificáveis
- **Minimização**: Coleta apenas dados necessários
- **Retenção**: Política de retenção de 5 anos para dados médicos
- **Portabilidade**: Export de dados em formato estruturado

##### **4. Governança de Dados**
```
┌─────────────────────────────────────────────────────────┐
│                GOVERNANÇA LGPD                         │
├─────────────────────────────────────────────────────────┤
│ 📋 Data Protection Officer (DPO)                       │
│ 📊 Privacy Impact Assessment (PIA)                     │
│ 🔍 Data Processing Inventory                           │
│ 📝 Consent Management                                  │
│ 🚨 Incident Response Plan                              │
│ 📈 Regular Compliance Audits                          │
└─────────────────────────────────────────────────────────┘
```

#### **Validação do Requisito**
- ✅ **Direitos dos Titulares**: APIs implementadas para todos os direitos
- ✅ **Segurança**: Criptografia e controles de acesso
- ✅ **Auditoria**: Logs completos de processamento
- ✅ **Governança**: Processos e políticas definidas

---

### **RNF02: Disponibilidade - "99% do tempo durante horário comercial"**

#### **Como a Arquitetura Garante**

##### **1. Cálculo de Disponibilidade**
```
Horário Comercial: 12h/dia × 22 dias úteis = 264h/mês
99% Disponibilidade = 261.36h disponível
Downtime Permitido = 2.64h/mês = 158.4 minutos/mês
```

##### **2. Estratégias de Alta Disponibilidade**

###### **Nível de Aplicação**
- **Health Checks**: Endpoint `/health` com verificação de dependências
- **Graceful Shutdown**: Finalização adequada de conexões
- **Circuit Breaker**: Proteção contra falhas em cascata
- **Retry Logic**: Tentativas automáticas com backoff exponencial

```typescript
// Health Check Implementation
class HealthCheckService {
  async checkHealth(): Promise<HealthStatus> {
    const checks = await Promise.allSettled([
      this.checkDatabase(),
      this.checkRedis(),
      this.checkExternalAPIs()
    ])
    
    return {
      status: checks.every(c => c.status === 'fulfilled') ? 'healthy' : 'unhealthy',
      timestamp: new Date(),
      services: this.mapCheckResults(checks)
    }
  }
}
```

###### **Nível de Infraestrutura**
- **Database Replication**: Master-Slave com failover automático
- **Load Balancer**: NGINX com health checks
- **Backup Strategy**: Backup incremental a cada 6h
- **Monitoring**: Prometheus + Grafana com alertas

##### **3. Plano de Recuperação de Desastres**
```
┌─────────────────────────────────────────────────────────┐
│                DISASTER RECOVERY                        │
├─────────────────────────────────────────────────────────┤
│ RTO (Recovery Time Objective): 30 minutos              │
│ RPO (Recovery Point Objective): 1 hora                 │
│                                                         │
│ Cenário 1: Falha de Aplicação                         │
│ ├── Auto-restart com PM2/Docker                       │
│ └── Tempo de recuperação: 2-5 minutos                 │
│                                                         │
│ Cenário 2: Falha de Database                          │
│ ├── Failover para replica                             │
│ └── Tempo de recuperação: 10-15 minutos               │
│                                                         │
│ Cenário 3: Falha de Servidor                          │
│ ├── Restore em novo servidor                          │
│ └── Tempo de recuperação: 20-30 minutos               │
└─────────────────────────────────────────────────────────┘
```

##### **4. Monitoramento e Alertas**
```typescript
// SLA Monitoring
interface SLAMetrics {
  uptime: number              // Target: 99%
  responseTime: number        // Target: < 2s
  errorRate: number          // Target: < 1%
  throughput: number         // Requests per minute
}

// Alert Thresholds
const ALERT_THRESHOLDS = {
  responseTime: 3000,        // 3 segundos
  errorRate: 0.05,          // 5%
  cpuUsage: 0.80,           // 80%
  memoryUsage: 0.85,        // 85%
  diskUsage: 0.90           // 90%
}
```

#### **Validação do Requisito**
- ✅ **99% Uptime**: Estratégias de HA implementadas
- ✅ **Horário Comercial**: Monitoramento 7h-19h
- ✅ **Recovery**: RTO 30min, RPO 1h
- ✅ **Alertas**: Notificação proativa de problemas

---

## 🔄 Matriz de Rastreabilidade

### **Requisitos Não Funcionais vs Decisões Arquiteturais**

| RNF | Descrição | ADRs Relacionados | Componentes Arquiteturais |
|-----|-----------|-------------------|---------------------------|
| **RNF01** | Performance < 2s | ADR-002, ADR-003 | Redis Cache, PostgreSQL Indexes |
| **RNF02** | Disponibilidade 99% | ADR-002, ADR-003 | Health Checks, DB Replication |
| **RNF03** | Segurança de Dados | ADR-004 | Encryption Layers, Access Control |
| **RNF04** | Controle de Acesso | ADR-004 | JWT + RBAC, Audit Logs |
| **RNF05** | Backup Automático | ADR-003 | PostgreSQL Backup, Redis Persistence |
| **RNF06** | Conformidade LGPD | ADR-004 | Data Protection Service, Audit Module |
| **RNF07** | Interface Intuitiva | ADR-001 | React + Material-UI |
| **RNF08** | Compatibilidade Web | ADR-001 | Modern Web Standards |
| **RNF09** | Escalabilidade | ADR-002, ADR-003 | Modular Architecture, Caching |
| **RNF10** | Auditoria | ADR-004 | Audit Service, Structured Logging |
| **RNF11** | Recuperação | ADR-003 | Backup Strategy, DR Plan |
| **RNF12** | Manutenibilidade | ADR-001, ADR-002 | TypeScript, Modular Design |

---

## 📋 Próximos Passos

### **Implementação das ADRs**
1. **Setup de Desenvolvimento** (Semana 1)
   - [ ] Configurar stack Node.js + TypeScript
   - [ ] Setup PostgreSQL + Redis
   - [ ] Configurar React + Material-UI

2. **Implementação de Segurança** (Semana 2)
   - [ ] Implementar criptografia em camadas
   - [ ] Configurar JWT + RBAC
   - [ ] Setup de auditoria e logs

3. **Monitoramento e SLA** (Semana 3)
   - [ ] Implementar health checks
   - [ ] Configurar métricas de performance
   - [ ] Setup de alertas e monitoramento

### **Validação dos RNFs**
- [ ] Testes de carga para escalabilidade
- [ ] Auditoria de segurança LGPD
- [ ] Testes de disponibilidade e recovery

---

**Documento aprovado por**: Arquiteto de Software Sênior  
**Data de aprovação**: 27/01/2024  
**Próxima revisão**: Após implementação das ADRs