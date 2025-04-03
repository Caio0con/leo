import multiprocessing
import threading  
import time # Importa a biblioteca de tempo
import os # Importa a biblioteca do sistema
import psutil # Importa a biblioteca de monitoramento de processos

def memoria_consumida():
    processo = psutil.Process(os.getpid()) # Pega o processo atual
    memoria = processo.memory_info().rss # Pega a memoria consumida
    return memoria


def tarefa(nome):
    print(f"Processo {nome} iniciado")
    time.sleep(10) # Dorme por 10 segundos
    print(f"Processo {nome} finalizado")

print ("iniciando demonstração com processos")
mem_inicio = memoria_consumida()
start_time = time.time() # Pega o tempo atual

processo1 = multiprocessing.Process(target=tarefa, args=("Processo 1",)) # Cria um processo
processo2 = multiprocessing.Process(target=tarefa, args=("Processo 2",)) # Cria outro processo
processo3 = multiprocessing.Process(target=tarefa, args=("Processo 3",)) # Cria outro processo

processo1.start() # Inicia o processo 1
processo2.start() # Inicia o processo 2
processo3.start() # Inicia o processo 3

processo1.join() # Espera o processo 1 terminar
processo2.join() # Espera o processo 2 terminar
processo3.join() # Espera o processo 3 terminar

tempo_execucao = time.time() - start_time # Calcula o tempo de execução
mem_fim = memoria_consumida()
print(f'Processos finalizado em {tempo_execucao:.2f} segundos')
print(f'Consumo de memoria com processos: {mem_fim - mem_inicio} kb')


#vantagens e desvantagens de processos:
# Vantagens: melhor isolamento, segurança e aproveitamento de multiplos nucleos da cpu
# Desvantagens: maior consumo de memoria e tempo de execução


#desmonstração com threads
print ("\niniciando demonstração com threads")
mem_inicio = memoria_consumida()
start_time = time.time() # Pega o tempo atual

thread1 = threading.Thread(target=tarefa, args=("Thread 1",)) # Cria uma thread
thread2 = threading.Thread(target=tarefa, args=("Thread 2",)) # Cria outra thread
thread3 = threading.Thread(target=tarefa, args=("Thread 3",)) # Cria outra thread

thread1.start() # Inicia a thread 1
thread2.start() # Inicia a thread 2
thread3.start() # Inicia a thread 3

thread1.join() # Espera a thread 1 terminar
thread2.join() # Espera a thread 2 terminar
thread3.join() # Espera a thread 3 terminar

tempo_execucao = time.time() - start_time # Calcula o tempo de execução
mem_fim = memoria_consumida()
print(f'Threads finalizado em {tempo_execucao:.2f} segundos')
print(f'Consumo de memoria com threads: {mem_fim - mem_inicio} kb')

#vantagens e desvantagens de threads:
# Vantagens: menor consumo de memoria e tempo de execução
# Desvantagens: menor isolamento, segurança e aproveitamento de multiplos nucleos da cpu



# Processos:
# - São executados em espaços de memória separados
# - Maior isolamento e segurança
# - Maior consumo de memória
# - Aproveitamento de múltiplos núcleos da CPU
# Threads:
# - São executados no mesmo espaço de memória
# - Menor isolamento e segurança
# - Menor consumo de memória
# - Menor aproveitamento de múltiplos núcleos da CPU
# - Mais eficientes para tarefas com muita I/O
# - Mais eficientes para tarefas que compartilham muitos dados