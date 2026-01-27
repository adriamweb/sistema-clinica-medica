// Variáveis globais
let horarioSelecionado = null;
let dadosAgendamento = {};

// Inicialização
document.addEventListener('DOMContentLoaded', function() {
    configurarDataMinima();
    configurarEventos();
    simularBuscaPaciente();
});

// Configurar data mínima (hoje)
function configurarDataMinima() {
    const hoje = new Date();
    const dataFormatada = hoje.toISOString().split('T')[0];
    document.getElementById('data').min = dataFormatada;
}

// Configurar eventos
function configurarEventos() {
    // Eventos dos horários
    document.querySelectorAll('.horario-btn.disponivel').forEach(btn => {
        btn.addEventListener('click', function() {
            selecionarHorario(this);
        });
    });

    // Evento do formulário
    document.getElementById('agendamentoForm').addEventListener('submit', function(e) {
        e.preventDefault();
        confirmarAgendamento();
    });

    // Evento de busca de paciente
    document.getElementById('paciente').addEventListener('input', function() {
        if (this.value.length >= 3) {
            simularBuscaPaciente();
        }
    });
}

// Simular busca de paciente
function simularBuscaPaciente() {
    const input = document.getElementById('paciente');
    const pacienteInfo = document.getElementById('pacienteInfo');
    
    // Simular que encontrou um paciente após 3 caracteres
    if (input.value.length >= 3) {
        pacienteInfo.style.display = 'block';
        dadosAgendamento.paciente = {
            nome: 'Maria Silva Santos',
            cpf: '123.456.789-00'
        };
        validarFormulario();
    } else {
        pacienteInfo.style.display = 'none';
        dadosAgendamento.paciente = null;
        validarFormulario();
    }
}

// Filtrar médicos por especialidade
function filtrarMedicos() {
    const especialidade = document.getElementById('especialidade').value;
    const medico = document.getElementById('medico');
    const opcoes = medico.querySelectorAll('option');
    
    opcoes.forEach(opcao => {
        if (opcao.value === '') {
            opcao.style.display = 'block';
            return;
        }
        
        const especialidadeMedico = opcao.getAttribute('data-especialidade');
        if (especialidade === '' || especialidadeMedico === especialidade) {
            opcao.style.display = 'block';
        } else {
            opcao.style.display = 'none';
        }
    });
    
    // Reset seleção se médico atual não está na especialidade filtrada
    if (medico.value && especialidade) {
        const opcaoSelecionada = medico.querySelector(`option[value="${medico.value}"]`);
        if (opcaoSelecionada && opcaoSelecionada.getAttribute('data-especialidade') !== especialidade) {
            medico.value = '';
            atualizarDisponibilidade();
        }
    }
}

// Atualizar disponibilidade quando médico muda
function atualizarDisponibilidade() {
    const medico = document.getElementById('medico');
    dadosAgendamento.medico = medico.options[medico.selectedIndex]?.text || null;
    
    // Simular diferentes disponibilidades por médico
    if (medico.value) {
        simularDisponibilidadeMedico(medico.value);
    }
    
    validarFormulario();
}

// Simular disponibilidade do médico
function simularDisponibilidadeMedico(medicoId) {
    const horarios = document.querySelectorAll('.horario-btn');
    
    // Reset todos os horários
    horarios.forEach(btn => {
        if (!btn.disabled) {
            btn.className = 'horario-btn disponivel';
        }
    });
    
    // Simular horários ocupados baseado no médico
    const horariosOcupados = {
        '1': ['08:30', '10:30', '15:30'], // Dr. João
        '2': ['09:00', '11:00', '16:00'], // Dra. Maria
        '3': ['07:30', '14:00', '17:00'], // Dr. Pedro
        '4': ['08:00', '10:00', '15:00']  // Dra. Ana
    };
    
    const ocupados = horariosOcupados[medicoId] || [];
    ocupados.forEach(horario => {
        const btn = document.querySelector(`[data-horario="${horario}"]`);
        if (btn) {
            btn.className = 'horario-btn ocupado';
            btn.disabled = true;
        }
    });
}

// Atualizar horários quando data muda
function atualizarHorarios() {
    const data = document.getElementById('data').value;
    dadosAgendamento.data = data;
    
    // Limpar seleção de horário
    if (horarioSelecionado) {
        horarioSelecionado.classList.remove('selecionado');
        horarioSelecionado.classList.add('disponivel');
        horarioSelecionado = null;
        dadosAgendamento.horario = null;
    }
    
    // Simular indisponibilidade em finais de semana
    if (data) {
        const dataObj = new Date(data + 'T00:00:00');
        const diaSemana = dataObj.getDay();
        
        if (diaSemana === 0 || diaSemana === 6) { // Domingo ou Sábado
            alert('A clínica não funciona aos finais de semana. Por favor, selecione uma data entre segunda e sexta-feira.');
            document.getElementById('data').value = '';
            dadosAgendamento.data = null;
            return;
        }
    }
    
    validarFormulario();
}

// Selecionar horário
function selecionarHorario(botao) {
    // Remover seleção anterior
    if (horarioSelecionado) {
        horarioSelecionado.classList.remove('selecionado');
        horarioSelecionado.classList.add('disponivel');
    }
    
    // Selecionar novo horário
    horarioSelecionado = botao;
    botao.classList.remove('disponivel');
    botao.classList.add('selecionado');
    
    dadosAgendamento.horario = botao.getAttribute('data-horario');
    
    validarFormulario();
    atualizarResumo();
}

// Validar formulário
function validarFormulario() {
    const btnConfirmar = document.getElementById('btnConfirmar');
    const temPaciente = dadosAgendamento.paciente;
    const temMedico = dadosAgendamento.medico;
    const temData = dadosAgendamento.data;
    const temHorario = dadosAgendamento.horario;
    
    if (temPaciente && temMedico && temData && temHorario) {
        btnConfirmar.disabled = false;
        atualizarResumo();
    } else {
        btnConfirmar.disabled = true;
        document.getElementById('resumoSection').style.display = 'none';
    }
}

// Atualizar resumo
function atualizarResumo() {
    const resumoSection = document.getElementById('resumoSection');
    
    if (dadosAgendamento.paciente && dadosAgendamento.medico && 
        dadosAgendamento.data && dadosAgendamento.horario) {
        
        document.getElementById('resumoPaciente').textContent = dadosAgendamento.paciente.nome;
        document.getElementById('resumoMedico').textContent = dadosAgendamento.medico;
        document.getElementById('resumoData').textContent = formatarData(dadosAgendamento.data);
        document.getElementById('resumoHorario').textContent = dadosAgendamento.horario;
        
        resumoSection.style.display = 'block';
    }
}

// Formatar data para exibição
function formatarData(data) {
    const dataObj = new Date(data + 'T00:00:00');
    return dataObj.toLocaleDateString('pt-BR', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}

// Confirmar agendamento
function confirmarAgendamento() {
    // Simular validação final
    if (!validarDisponibilidade()) {
        alert('Desculpe, este horário não está mais disponível. Por favor, selecione outro horário.');
        return;
    }
    
    // Gerar protocolo
    const protocolo = gerarProtocolo();
    document.getElementById('protocoloNumero').textContent = protocolo;
    
    // Mostrar modal de confirmação
    document.getElementById('modalConfirmacao').style.display = 'flex';
    
    // Simular envio de notificação
    console.log('Agendamento confirmado:', {
        protocolo: protocolo,
        paciente: dadosAgendamento.paciente,
        medico: dadosAgendamento.medico,
        data: dadosAgendamento.data,
        horario: dadosAgendamento.horario
    });
}

// Validar disponibilidade (simulação)
function validarDisponibilidade() {
    // Simular 95% de sucesso
    return Math.random() > 0.05;
}

// Gerar protocolo único
function gerarProtocolo() {
    const ano = new Date().getFullYear();
    const numero = Math.floor(Math.random() * 9999) + 1;
    return `#AG${ano}${numero.toString().padStart(4, '0')}`;
}

// Limpar formulário
function limparFormulario() {
    // Reset campos
    document.getElementById('agendamentoForm').reset();
    document.getElementById('pacienteInfo').style.display = 'none';
    document.getElementById('resumoSection').style.display = 'none';
    
    // Reset horário selecionado
    if (horarioSelecionado) {
        horarioSelecionado.classList.remove('selecionado');
        horarioSelecionado.classList.add('disponivel');
        horarioSelecionado = null;
    }
    
    // Reset dados
    dadosAgendamento = {};
    
    // Reset validação
    document.getElementById('btnConfirmar').disabled = true;
    
    // Reconfigurar data mínima
    configurarDataMinima();
}

// Fechar modal
function fecharModal() {
    document.getElementById('modalConfirmacao').style.display = 'none';
    limparFormulario();
}

// Fechar modal clicando fora
document.addEventListener('click', function(e) {
    const modal = document.getElementById('modalConfirmacao');
    if (e.target === modal) {
        fecharModal();
    }
});