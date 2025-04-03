# Explique 4 algoritmos de escalonamento de processos e codifique 1 método para cada
# técnica.

def fcfs(processes):
        for process in processes:
            print(f"Executando processo {process}")

# Shortest Job Next (SJN): O algoritmo SJN seleciona o processo com o menor tempo de
# execução
# restante para ser executado em seguida. Para implementar esse algoritmo, basta ordenar a
# lista de processos por tempo de execução e executar o processo com o menor tempo
# restante. Aqui está um exemplo de implementação em Python:

def sjn(processes):
    processes.sort(key=lambda p: p.execution_time)
    for process in processes:
        print(f"Executando processo {process}")

# Round Robin (RR) permite que cada processo seja executado por um pequeno intervalo de tempo  antes de passar para o próximo processo. 

def rr(processes, quantum):
    queue = processes.copy()
    while queue:
        process = queue.pop(0)
        print(f"Executando processo {process}")
        process.execution_time -= quantum
        if process.execution_time > 0:
            queue.append(process)

# Priority Scheduling  algoritmo de escalonamento por prioridade atribui uma prioridade a cada processo e executa o processo com a maior prioridade em primeiro lugar.

def priority_scheduling(processes):
    processes.sort(key=lambda p: p.priority, reverse=True)
    for process in processes:
        print(f"Executando processo {process}")

# Esses são apenas exemplos simples de implementações dos algoritmos de escalonamento de
# processos em Python. Cada algoritmo pode ser adaptado e refinado de acordo com as
# necessidades específicas do sistema em questão.




