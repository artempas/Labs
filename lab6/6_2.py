import math
import multiprocessing
import random
from multiprocessing import Process, shared_memory
from datetime import datetime
import colorama




def calculate_part(P: list, Q: list, R: list, i_from: int, i_to: int, N: int):
    print(f"Process {multiprocessing.current_process().name} started")

    for i in range(i_from, i_to):
        for j in range(N):
            R[i*N+j]=math.sqrt(Q[i] ** 2 + P[j] ** 2)


    print(f"Process {multiprocessing.current_process().name} ended")


if __name__ == '__main__':

    print("Filling P,Q,R")
    N = 5000
    P: list[int] = [random.randint(0, 10 * N) for _ in range(N)]
    Q: list[int] = [random.randint(0, 10 * N) for _ in range(N)]
    R = []
    print("Filled")

    start = datetime.now()

    for i in range(N):
        for j in range(N):
            R.append(math.sqrt(Q[i] ** 2 + P[j] ** 2))

    print(f"Without multiprocessing {datetime.now() - start}")
    single_R = R.copy()

    R = shared_memory.ShareableList([None]*(N**2))

    tasks: list[Process] = []
    start = datetime.now()
    process = Process(target=calculate_part, args=(P, Q, R, 0, N // 4, N))
    process.start()
    tasks.append(process)
    process = Process(target=calculate_part, args=(P, Q, R, N // 4, N // 2, N))
    process.start()
    tasks.append(process)
    process = Process(target=calculate_part, args=(P, Q, R, N // 2, (3 * N) // 4, N))
    process.start()
    tasks.append(process)
    process = Process(target=calculate_part, args=(P, Q, R, (3 * N) // 4, N, N))
    process.start()
    tasks.append(process)

    for process in tasks:
        process.join()
    print(f"{colorama.Fore.GREEN}Multiprocessed {datetime.now() - start}{colorama.Fore.RESET}   ")


    for i in range(N):
        for j in range(N):
            if single_R[i*N+j] != R[i*N+j]:
                print(f"{colorama.Fore.RED}{round(R[i*N+j])}{colorama.Fore.RESET}", end=' ')
            else:
                print(round(R[i*N+j]), end=' ')
        print()
