import time

def processo_p1():
    print("Processo 1 rodando!")
    time.sleep(1)

def processo_p2():
    print("Processo 2 rodando!")
    time.sleep(1)

def processo_p3():
    print("Processo 3 rodando!")
    time.sleep(1)

def processo_p4():
    print("Processo 4 rodando!")
    time.sleep(1)

def fifo(processos):
    for _,_,_,_, func in sorted(processos, key=lambda x: x[0]):
        func()

def sjf(processos):
    for _,_,_,_, func in sorted(processos, key=lambda x: x[1]):
        func()

def prioridade(processos):
    for _,_,_,_, func in sorted(processos, key=lambda x: x[2]):
        func()

def usagem_cpu(processos):
    for _,_,_,_, func in sorted(processos, key=lambda x: x[3]):
        func()

if __name__ == "__main__":
    processos = [
        (0, 5, 1, 3, processo_p1), # (tempo de chegada, tempo de execução, prioridade, uso de CPU, função)
        (0, 3, 4, 4, processo_p2),
        (0, 1, 3, 7, processo_p3),
        (0, 1, 2, 8, processo_p4)
    ]

    
print("Execução FIFO")
fifo(processos)
print("Execução SJF")
sjf(processos)
print("Execução Prioridade")
prioridade(processos)
print("Execução Uso de CPU")
usagem_cpu(processos)

#caio henrique ocon 1958689
