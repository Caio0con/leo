import multiprocessing
import time
print(multiprocessing.cpu_count()) # Mostra a quantidade de núcleos do processador

def meu_processo():
    print("Processo rodando")
    inicio =time.time()
    #time.sleep(10)
    print("Processo finalizado")
    fim = time.time()
    print(f"Tempo de execução: {fim - inicio:.4f} segundos") # Calcula o tempo de execução

if __name__ == '__main__':
    #inicio = time.time() # Pega o tempo atual

    processo = multiprocessing.Process(target=meu_processo) # Cria um processo
    processo2 = multiprocessing.Process(target=meu_processo) # Cria um processo
    processo3 = multiprocessing.Process(target=meu_processo) # Cria um processo
    processo.start() # Inicia o processo
    processo.join() # Espera o processo terminar
    processo2.start() # Inicia o processo
    processo2.join() # Espera o processo
    processo3.start() # Inicia o processo
    processo3.join() # Espera o processo

    # fim = time.time() # Pega o tempo atual
    # print(f"Tempo de execução: {fim - inicio:.4f} segundos") # Calcula o tempo de execução
    # print("processo principal finalizado")
