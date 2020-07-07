import atkin
import timeit
import db
from sys import argv

if __name__ == '__main__':
    try:
        if int(argv[1]) <= 0:
            raise Exception('not valid number')
        number  = int(argv[1])
        a = timeit.default_timer()
        atkin.begin(number)
        time_list = db.read()
        while len(time_list)>number :
            time_list.pop()
        res=list()
        for index,elem in enumerate(time_list):
            if elem is not False:
                res.append(elem)
        res.sort()
        with open("result.txt", "w", encoding='utf-8') as file:
            file.write("2\n3\n5\n")
            for p in res:
                string = ""+str(p)+"\n"
                file.write(string)
        print('Время работы:', timeit.default_timer()-a)
    except BaseException:
        print('Заканчивание работы...')
    except Exception:
        print('Фальшивый ввод!')
    except FileNotFoundError:
        pass