import itertools
import time

def cirle_number(n):
    start_time = time.time()
    end_list = []
    list_simple_numbers = []
    for i in range(1, n+1):
        lsit_circle_nubmer = []
        i_round = round(i**0.5)

        for d in range(2, i_round+1):
            i = str(i)
            if i.count('0') > 0 or i.count('2') > 0 or i.count('4') > 0 or i.count('6') > 0 or i.count('8') > 0:
                break
            i = int(i)
            if i%d==0:
                lsit_circle_nubmer.append(i)

        if len(lsit_circle_nubmer) == 0:
            list_simple_numbers.append(i)

    for z in list_simple_numbers:
        list_for_number = []
        z = str(z)

        for j in z:
            list_for_number.append(int(j))

        a = list(set(itertools.permutations(list_for_number)))
        len_a = len(list_for_number)
        cnt_a = 0
        for i in a:
            b = ''

            for j in i:
                b += str(j)

            cnt = 0
            c = int(b)
            b = round(int(b) ** 0.5)

            for d in range(2, b+1):
                if c%d==0:
                    cnt += 1

            if cnt == 0:
                cnt_a += 1
                if cnt_a == len_a:
                    end_list.append(int(z))
    time_program = ((time.time() - start_time))
    return len(end_list)-1, time_program







if __name__ == "__main__":
    print(cirle_number(10000))
