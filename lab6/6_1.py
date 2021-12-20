import threading
import time


def process(barrier):
    th_name = threading.current_thread().name
    print(f'{th_name} в ожидании барьера с {barrier.n_waiting} другими')
    number_in_front_of_barrier = barrier.wait()
    print(f'{th_name} прохождение барьера {number_in_front_of_barrier}')


NUM_THREADS = 12

barrier = threading.Barrier(3)

threads = []
for i in range(NUM_THREADS):
    th = threading.Thread(name=f'Process_{i}',
                          target=process,
                          args=(barrier,),
                          )
    threads.append(th)
    print(f'Запуск {th.name}')
    th.start()
    time.sleep(0.6)

for thread in threads:
    thread.join()
