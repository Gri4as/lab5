import db
import multiprocessing as mp
import time
import math

def begin(number : int):
    with mp.Pool(processes=2) as my_pool:
        proc = my_pool.starmap(atkin,iterable=[[number , 1],[number , 0]],)
        my_pool.close()


def atkin(number : int, x: int):
    if x == 1:
        path = 'one_thr.txt'
        status = 'Первый процесс окончен'
        i=1
    elif x == 0:
        path = "sec_thr.txt"
        status = 'Второй процесс окончен'
        i=2
    m_list = [False for _ in range(number+1)]
    t=time.time()
    t=int(t)
    for x in range(i, int(math.sqrt(number )) + 1, 2):
        for y in range(1, int(math.sqrt(number )) + 1):
            n = 4 * x ** 2 + y ** 2
            if n <= number  and (n % 12 == 1 or n % 12 == 5):
                m_list[n] = not m_list[n]
            n = 3 * x ** 2 + y ** 2
            if n <= number  and n % 12 == 7:
                m_list[n] = not m_list[n]
            n = 3 * x ** 2 - y ** 2
            if x > y and n <= number  and n % 12 == 11:
                m_list[n] = not m_list[n]
            if int(time.time())-t>3:
                print(x)
                t=time.time()
                t=int(t)
    db.write(m_list, path)
    print(status)