#!/usr/bin/env python3
"""
Sistema de Notificação de Consultas - Clínica Médica
Envia notificações de consulta via console usando apenas bibliotecas padrão do Python.
"""

import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional


class NotificadorConsulta:
    """Classe para envio de notificações de consulta via console."""
    
    def __init__(self) -> None:
        """Inicializa o notificador com dados de exemplo."""
        self.consultas: List[Dict] = [
            {
                "id": "AG2024001",
                "paciente": "Maria Silva Santos",
                "medico": "Dr. João Silva",
                "especialidade": "Cardiologia",
                "data": "2024-01-29",
                "horario": "09:00",
                "telefone": "(11) 99999-9999"
            },
            {
                "id": "AG2024002", 
                "paciente": "José Santos",
                "medico": "Dra. Ana Oliveira",
                "especialidade": "Ortopedia",
                "data": "2024-01-29",
                "horario": "14:30",
                "telefone": "(11) 88888-8888"
            }
        ]
    
    def enviar_lembrete(self, consulta_id: str) -> bool:
        """
        Envia lembrete de consulta via console.
        
        Args:
            consulta_id: ID da consulta para envio do lembrete
            
        Returns:
            True se enviado com sucesso, False caso contrário
        """
        consulta = self._buscar_consulta(consulta_id)
        if not consulta:
            print(f"❌ Consulta {consulta_id} não encontrada")
            return False
        
        data_consulta = datetime.strptime(f"{consulta['data']} {consulta['horario']}", "%Y-%m-%d %H:%M")
        agora = datetime.now()
        
        print("=" * 60)
        print("📱 LEMBRETE DE CONSULTA")
        print("=" * 60)
        print(f"Paciente: {consulta['paciente']}")
        print(f"Médico: {consulta['medico']}")
        print(f"Especialidade: {consulta['especialidade']}")
        print(f"Data: {data_consulta.strftime('%d/%m/%Y às %H:%M')}")
        print(f"Telefone: {consulta['telefone']}")
        print(f"Protocolo: {consulta['id']}")
        print(f"Enviado em: {agora.strftime('%d/%m/%Y às %H:%M:%S')}")
        print("=" * 60)
        
        return True
    
    def enviar_confirmacao(self, consulta_id: str) -> bool:
        """
        Envia confirmação de agendamento via console.
        
        Args:
            consulta_id: ID da consulta para confirmação
            
        Returns:
            True se enviado com sucesso, False caso contrário
        """
        consulta = self._buscar_consulta(consulta_id)
        if not consulta:
            print(f"❌ Consulta {consulta_id} não encontrada")
            return False
        
        data_consulta = datetime.strptime(f"{consulta['data']} {consulta['horario']}", "%Y-%m-%d %H:%M")
        
        print("=" * 60)
        print("✅ CONFIRMAÇÃO DE AGENDAMENTO")
        print("=" * 60)
        print(f"Olá {consulta['paciente']},")
        print(f"Sua consulta foi agendada com sucesso!")
        print(f"Médico: {consulta['medico']} - {consulta['especialidade']}")
        print(f"Data: {data_consulta.strftime('%d/%m/%Y às %H:%M')}")
        print(f"Protocolo: {consulta['id']}")
        print("Chegue 15 minutos antes do horário.")
        print("=" * 60)
        
        return True
    
    def listar_consultas_hoje(self) -> None:
        """Lista todas as consultas do dia atual."""
        hoje = datetime.now().strftime("%Y-%m-%d")
        consultas_hoje = [c for c in self.consultas if c['data'] == hoje]
        
        print("=" * 60)
        print(f"📅 CONSULTAS DE HOJE ({datetime.now().strftime('%d/%m/%Y')})")
        print("=" * 60)
        
        if not consultas_hoje:
            print("Nenhuma consulta agendada para hoje.")
        else:
            for consulta in consultas_hoje:
                print(f"{consulta['horario']} - {consulta['paciente']} ({consulta['medico']})")
        
        print("=" * 60)
    
    def _buscar_consulta(self, consulta_id: str) -> Optional[Dict]:
        """
        Busca consulta por ID.
        
        Args:
            consulta_id: ID da consulta
            
        Returns:
            Dados da consulta ou None se não encontrada
        """
        for consulta in self.consultas:
            if consulta['id'] == consulta_id:
                return consulta
        return None


def main() -> None:
    """Função principal para demonstração do notificador."""
    notificador = NotificadorConsulta()
    
    print("🏥 Sistema de Notificação - Clínica Médica")
    print("Demonstração de funcionalidades:\n")
    
    # Listar consultas do dia
    notificador.listar_consultas_hoje()
    print()
    
    # Enviar confirmação
    notificador.enviar_confirmacao("AG2024001")
    print()
    
    # Enviar lembrete
    notificador.enviar_lembrete("AG2024002")
    print()
    
    # Teste com ID inexistente
    notificador.enviar_lembrete("AG2024999")


if __name__ == "__main__":
    main()