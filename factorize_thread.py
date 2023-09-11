from threading import Thread, Event, current_thread
from time import time


def master(event: Event):
    event.set()

def factorize(number, event: Event):
    name = current_thread().name
    print(f'{name} started...')
    if event.is_set():
        result = []
        # for num in numbers:
        lst_numbers = [n for n in range(1, number+1) if number % n == 0]
        result.append(lst_numbers)

        print(result)

if __name__ == '__main__':
    nums = (128, 255, 99999, 10651060, 12103004)
    event = Event()
    timer = time()
    threads = []
    for i in nums:
        mstr = Thread(target=master, name=f'Master', args=(event, ))
        th = Thread(target=factorize, name=f'Thread - {i}', args=(i, event))
        th.start()
        threads.append(th)
        mstr.start()
    [th.join() for th in threads]
    
    print(f'Time: {round(time() - timer, 4)}')
    print('End of program')