# Plano de Testes - Sistema de Triagem de Pacientes

**Versão**: 1.0  
**Data**: 27/01/2024  
**Analista QA**: Analista de Qualidade Sênior  
**Sistema**: triagem.py - Gerenciamento de Fila de Pacientes

---

## 🎯 Estratégia de Testes (T1)

### **Foco Principal: TESTES FUNCIONAIS**

#### **Justificativa da Estratégia**

**Por que Funcionais?**
- ✅ **Sistema Crítico**: Triagem médica impacta diretamente na segurança do paciente
- ✅ **Lógica de Negócio Complexa**: Ordenação por urgência + timestamp requer validação rigorosa
- ✅ **Regras Específicas**: Validação de urgência (1-5) e idade (>0) são críticas
- ✅ **Cenários de Desempate**: Timestamp como critério secundário precisa ser testado

**Por que NÃO Performance (prioritário)?**
- ❌ **Volume Baixo**: Sistema para clínica pequena (~50 pacientes simultâneos)
- ❌ **Operações Simples**: Inserção e ordenação de listas pequenas
- ❌ **Sem Concorrência**: Sistema single-thread sem paralelismo

#### **Estratégia Híbrida Recomendada**
```
Prioridade 1: Testes Funcionais (80%)
├── Validação de regras de negócio
├── Cenários de ordenação
├── Tratamento de exceções
└── Fluxos de uso principais

Prioridade 2: Testes de Performance (20%)
├── Stress test com 100+ pacientes
├── Tempo de ordenação < 1s
└── Uso de memória controlado
```

---

## 📊 Níveis de Teste (T2)

### **1. 🔬 Testes Unitários**
**Escopo**: Funções e métodos isolados

#### **Componentes a Testar**
- **Classe Paciente**
  - Validação de urgência (1-5)
  - Validação de idade (≥0)
  - Geração automática de timestamp
  
- **Função ordenar_por_prioridade()**
  - Ordenação por urgência decrescente
  - Desempate por timestamp crescente
  - Lista vazia e com um elemento
  
- **Função obter_texto_urgencia()**
  - Mapeamento correto de níveis 1-5
  - Tratamento de valores inválidos

#### **Ferramentas**: pytest, unittest

### **2. 🔗 Testes de Integração**
**Escopo**: Interação entre componentes

#### **Cenários de Integração**
- **GerenciadorTriagem + Paciente**
  - Adicionar paciente com timestamp automático
  - Ordenação correta na fila
  - Remoção do paciente correto
  
- **Fluxo Completo**
  - Adicionar → Listar → Atender → Verificar fila

#### **Ferramentas**: pytest com fixtures

### **3. 🎭 Testes de Sistema**
**Escopo**: Sistema completo end-to-end

#### **Cenários de Sistema**
- **Fluxo Principal**
  - Múltiplos pacientes com urgências diferentes
  - Verificação da ordem final
  - Atendimento sequencial correto
  
- **Cenários de Exceção**
  - Fila vazia ao tentar atender
  - Dados inválidos de paciente

#### **Ferramentas**: pytest com cenários completos

### **4. ✅ Testes de Aceitação**
**Escopo**: Validação com usuário final

#### **Critérios de Aceitação**
- Paciente com urgência 5 sempre primeiro
- Desempate por ordem de chegada funciona
- Interface de listagem clara e informativa
- Tratamento adequado de erros

---

## 🚪 Critérios de Entrada e Saída (T3)

### **📥 Critérios de Entrada**

#### **Código Deve Ter**
- ✅ **Cobertura Mínima**: 80% do código coberto por testes
- ✅ **Documentação**: Docstrings em todas as funções públicas
- ✅ **Type Hints**: Tipagem completa implementada
- ✅ **Validações**: Tratamento de dados inválidos implementado
- ✅ **Estrutura Limpa**: Separação clara entre classes e funções

#### **Ambiente de Teste**
- ✅ **Python 3.7+** instalado
- ✅ **Dependências** instaladas (pytest, coverage)
- ✅ **Dados de Teste** preparados
- ✅ **Ambiente Isolado** configurado

#### **Pré-condições**
- ✅ **Code Review** aprovado
- ✅ **Lint Check** sem erros críticos
- ✅ **Smoke Test** básico executado

### **📤 Critérios de Saída**

#### **Qualidade Mínima**
- ✅ **Zero Bugs Críticos**: Nenhum erro que impeça funcionamento
- ✅ **Cobertura ≥ 90%**: Cobertura de testes aceitável
- ✅ **Todos Testes Passando**: 100% dos testes unitários e integração
- ✅ **Performance OK**: Ordenação < 1s para 100 pacientes

#### **Funcionalidades Validadas**
- ✅ **Ordenação Correta**: Urgência + timestamp funcionando
- ✅ **Validações**: Dados inválidos rejeitados adequadamente
- ✅ **Exceções**: Tratamento de erros implementado
- ✅ **Usabilidade**: Interface clara e informativa

#### **Documentação**
- ✅ **Relatório de Testes**: Resultados documentados
- ✅ **Bugs Conhecidos**: Issues não-críticos catalogados
- ✅ **Manual de Uso**: Instruções básicas disponíveis

---

## 📋 Casos de Teste Prioritários

### **🔥 Críticos (Deve Passar)**
1. **Ordenação por Urgência**
   - Paciente urgência 5 antes de urgência 1
   - Múltiplos níveis ordenados corretamente

2. **Desempate por Timestamp**
   - Mesma urgência: primeiro a chegar tem prioridade
   - Timestamps diferentes funcionam corretamente

3. **Validações de Entrada**
   - Urgência fora do range (0, 6) → ValueError
   - Idade negativa → ValueError

### **⚠️ Importantes (Deve Funcionar)**
4. **Fila Vazia**
   - atender_proximo() em fila vazia → IndexError
   - listar_fila() em fila vazia → "Fila vazia"

5. **Casos Extremos**
   - Um único paciente na fila
   - Todos pacientes com mesma urgência

### **📊 Desejáveis (Performance)**
6. **Stress Test**
   - 100 pacientes: ordenação < 1s
   - 1000 pacientes: sem crash de memória

---

## 🛠️ Ferramentas e Ambiente

### **Framework de Testes**
```bash
# Instalação
pip install pytest pytest-cov

# Execução
pytest --cov=triagem --cov-report=html
```

### **Estrutura de Arquivos**
```
Teste de Software (TES)/
├── test_paciente.py          # Testes unitários Paciente
├── test_gerenciador.py       # Testes unitários GerenciadorTriagem  
├── test_ordenacao.py         # Testes função ordenar_por_prioridade
├── test_integracao.py        # Testes de integração
├── test_sistema.py           # Testes end-to-end
├── conftest.py               # Fixtures compartilhadas
└── relatorio_testes.md       # Relatório de execução
```

### **Métricas de Qualidade**
- **Cobertura**: ≥ 90%
- **Tempo Execução**: < 30s todos os testes
- **Taxa de Sucesso**: 100% testes críticos
- **Bugs por KLOC**: < 1 bug crítico por 1000 linhas

---

**Plano aprovado por**: Analista de Qualidade Sênior  
**Data de aprovação**: 27/01/2024  
**Próxima revisão**: Após implementação dos testes