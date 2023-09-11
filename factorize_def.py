from time import time

def factorize(*numbers):
    result = []
    for num in numbers:
        lst_numbers = [n for n in range(1, num+1) if num % n == 0]
        result.append(lst_numbers)
    return result

if __name__ == '__main__':
    timer = time()
    print('Hello')
    a, b, c, d, e = factorize(128, 255, 99999, 10651060, 12103004)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    assert e == [1, 2, 4, 1697, 1783, 3394, 3566, 6788, 7132, 3025751, 6051502, 12103004]
    print(f'{a}\n{b}\n{c}\n{d}\n{e}')
    print(f'Time: {round(time() - timer, 4)}')