import threading
from time import time

import requests

websites = (
    'https://apple.com',
    'https://google.com',
    'https://ok.ru',
    'https://cazino-vavada.name',
    'https://1xbet-kazino.net.ru',
    'https://joycasino2021.co',
    'https://worldoftanks.ru',
    'http://гончарнаямастерская.рф',
    'https://n.feimsk.city',
    'https://arzamas.academy',
    'https://krasnoeibeloe.ru',
)


def req_web(websites: iter):
    for site in websites:
        print(requests.get(site))


start = time()
req_web(websites)
print(f"Single thread {time() - start}")
start = time()
threads = []
for site in websites:
    thread = threading.Thread(target=req_web, args=([site],))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
print(f"10 threads {time() - start}")

