import math
import atkin
import main


def read() -> list:
    with open('one_thr.txt', 'r', encoding='utf-8') as f1:
        first_read = f1.read()
        list_1 = first_read.split("\n")
    with open('sec_thr.txt', 'r', encoding='utf-8') as f2:
        first_read = f2.read()
        list_2 = first_read.split("\n")
    lens = len(list_1)
    list_12 = [False] * lens
    for i in range(0, lens):
        if list_1[i] == "False":
            a = False
        else:
            a = True
        if list_2[i] == "False":
            b = False
        else:
            b = True
        list_12[i] = (a + b) % 2
    list_3 = [False] * len(list_12)
    for id, x in enumerate(list_12):
        if x == 1:
            if id % 5 == 0:
                pass
            else:
                list_3[id] = id
    for x in range(5, int(math.sqrt(len(list_12)))):
        if list_3[x]:
            for y in range(x ** 2, main.number + 1, x ** 2):
                list_3[y] = False
    return list_3


def write(lst, pth):
    with open(pth, 'w+', encoding='utf-8') as fle:
        for i in range(len(lst)):
            if lst[i]:
                fle.write(str(i))
                fle.write('\n')
