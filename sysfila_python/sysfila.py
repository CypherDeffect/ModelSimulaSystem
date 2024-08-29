import numpy as np
import pandas as pd

def modelar_sistema_filas(qtd_clientes, intervalo_chegada, duracao_atendimento):
    # Inicializa listas para armazenar dados
    tempos_chegada = []
    tempos_inicio_atendimento = []
    tempos_fim_atendimento = []
    tempos_espera = []
    
    tempo_atual = 0
    fila = []
    
    # Simulação
    for cliente in range(qtd_clientes):
        chegada = tempo_atual + np.random.exponential(intervalo_chegada)
        tempo_atual = chegada
        
        # Adiciona cliente na fila
        fila.append(chegada)
        
        if len(fila) == 1:  # Se a fila está vazia, o atendimento começa imediatamente
            inicio_atendimento = chegada
        else:
            inicio_atendimento = max(chegada, fila[0])
        
        duracao = np.random.exponential(duracao_atendimento)
        fim_atendimento = inicio_atendimento + duracao
        
        # Armazena os tempos
        tempos_chegada.append(chegada)
        tempos_inicio_atendimento.append(inicio_atendimento)
        tempos_fim_atendimento.append(fim_atendimento)
        tempos_espera.append(inicio_atendimento - chegada)
        
        # Remove cliente da fila
        fila.pop(0)
    
    # Calcula estatísticas
    intervalo_medio_chegada = np.mean(np.diff(tempos_chegada)) if len(tempos_chegada) > 1 else 0
    duracao_media_atendimento = np.mean(np.array(tempos_fim_atendimento) - np.array(tempos_inicio_atendimento))
    tamanho_medio_fila = np.mean([len([x for x in tempos_chegada if x <= t and x >= t - intervalo_chegada]) for t in tempos_fim_atendimento])
    tempo_medio_espera = np.mean(tempos_espera)
    
    # Gera a tabela de funcionamento do sistema
    tabela_funcionamento = pd.DataFrame({
        'Cliente': range(1, qtd_clientes + 1),
        'Tempo de Chegada': tempos_chegada,
        'Início de Atendimento': tempos_inicio_atendimento,
        'Fim de Atendimento': tempos_fim_atendimento,
        'Tempo de Espera': tempos_espera
    })
    
    # Exibe os resultados
    print("Intervalo Médio entre Chegadas: {:.2f}".format(intervalo_medio_chegada))
    print("Duração Média do Atendimento: {:.2f}".format(duracao_media_atendimento))
    print("Tamanho Médio da Fila: {:.2f}".format(tamanho_medio_fila))
    print("Tempo Médio de Espera na Fila: {:.2f}".format(tempo_medio_espera))
    
    print("\nTabela de Funcionamento do Sistema:")
    print(tabela_funcionamento)
    
    return intervalo_medio_chegada, duracao_media_atendimento, tamanho_medio_fila, tempo_medio_espera, tabela_funcionamento

# Exemplo de uso
qtd_clientes = int(input("Quantidade de clientes: "))
intervalo_chegada = float(input("Intervalo médio entre chegadas (em unidades de tempo): "))
duracao_atendimento = float(input("Duração média do atendimento (em unidades de tempo): "))

modelar_sistema_filas(qtd_clientes, intervalo_chegada, duracao_atendimento)
