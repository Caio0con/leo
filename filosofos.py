import threading
import time
import random

NUM_FILOSOFOS = 5
TEMPO_EXECUCAO = 30  # segundos

# Cada garfo é um Lock
garfos = [threading.Lock() for _ in range(NUM_FILOSOFOS)]

# Semáforo para permitir no máximo 4 filósofos a tentar comer ao mesmo tempo
# Isso previne deadlock (permite no máximo N-1 filósofos comendo)
semaforo = threading.Semaphore(NUM_FILOSOFOS - 1)

def filosofar(filosofo_id):
    esquerda = filosofo_id
    direita = (filosofo_id + 1) % NUM_FILOSOFOS

    while True:
        print(f"Filósofo {filosofo_id} está pensando.")
        time.sleep(random.uniform(1, 3))  # pensa por um tempo aleatório

        print(f"Filósofo {filosofo_id} está com fome.")

        # Tenta entrar na "sala de jantar"
        semaforo.acquire()

        # Pega os dois garfos
        with garfos[esquerda]:
            with garfos[direita]:
                print(f"Filósofo {filosofo_id} está comendo.")
                time.sleep(random.uniform(1, 2))  # come por um tempo aleatório

        print(f"Filósofo {filosofo_id} terminou de comer.")
        semaforo.release()

def main():
    threads = []
    for i in range(NUM_FILOSOFOS):
        t = threading.Thread(target=filosofar, args=(i,), daemon=True)
        t.start()
        threads.append(t)

    try:
        time.sleep(TEMPO_EXECUCAO)  # Executa por tempo determinado
    except KeyboardInterrupt:
        print("\nInterrompido pelo usuário.")

    print("Encerrando simulação...")

if __name__ == "__main__":
    main()
