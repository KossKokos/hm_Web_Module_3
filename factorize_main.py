from multiprocessing import Pool, cpu_count, current_process
from time import time


def output_result(result: list):
    print('Finished')
    for lst in result:
        for ls in lst:
            print(ls)


def factorize(*numbers):
    name = current_process().name
    print(f'{name} started...')
    result = []
    for num in numbers:
        lst_numbers = [n for n in range(1, num + 1) if num % n == 0]
        result.append(lst_numbers)
    return result


if __name__ == '__main__':
    with Pool(cpu_count()) as p:
        timer = time()
        p.map_async(
            factorize, 
            (128, 255, 99999, 10651060, 12103004,),
            callback=output_result
        )
        p.close()
        p.join()
    print(f'Time: {round(time() - timer, 4)}')