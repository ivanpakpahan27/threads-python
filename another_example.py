from time import sleep, perf_counter
from threading import Thread

start_time = perf_counter()
def looping():
    for i in range(10):
        print(i)
        sleep(1)
def looping2():
    for i in range(10):
        print(i)
        sleep(1)
a = Thread(target=looping, )
a.start()
b = Thread(target=looping2, )
b.start()
a.join()
b.join()
end_time = perf_counter()
print(f'It took {end_time- start_time: 0.5f}')
