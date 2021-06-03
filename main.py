import forma_file
from random import randint
import os
import random

"""
1) 0 - 710 (ID); 0 - 63(индекс) АТД, основные понятия
2) 781 - 836  (ID); 134 - 189 (индекс) статические структуры
3) 711 - 780  (ID); 64 - 133 (индекс) деревья
"""


def get_index(data, id):
    for i in range(len(data)):
        if data[i].id == id:
            return i


def stat(quest, x, lst):
    file = open("result.txt", "a")
    file.write("_" * 180 + "\n" + quest + "\nНеверный ответ: " + str(x) + "\n")
    for i in range(len(lst)):
        file.write(str(i + 1) + ") " + lst[i] + "\n")
    file.write("\n\n")
    file.close()


def hide_q(data, number):
    list_q = []
    random.shuffle(data[number].q)
    for q in data[number].q:
        list_q.append(q.replace("=", "").replace("~", ""))
    return list_q


def check_valid(data, number):
    for i in range(0, len(data[number].q), 1):
        if data[number].q[i].count("="):
            return i


def print_quest(lst):
    for i in range(len(lst)):
        print(i + 1, ") " + lst[i])


def event(data, res, invalid, lst_number):
    os.system("cls")
    nubmer_quest = randint(134, 189)
    while lst_number.count(nubmer_quest) != 0:
        nubmer_quest = randint(134, 189)
    lst_number.append(nubmer_quest)
    quest = "Прошлый ответ: {} \nID = {}\nВопрос: {}\nНеверных ответов: {}\n".format(res, data[nubmer_quest].id,
                                                                                     data[nubmer_quest].title[0],
                                                                                     invalid)

    print(quest)
    lst = hide_q(data, nubmer_quest)
    print_quest(lst)
    x = int(input("\nВыберете ответ: "))
    valid = check_valid(data, nubmer_quest)
    if valid == x - 1:
        print("Верно")
        res = "верный"
    else:
        stat(quest, x, lst)
        invalid += 1
        res = "неверный! \nВерный ответ: {}".format(data[nubmer_quest].q[valid])
    event(data, res, invalid, lst_number)


def main():
    lst_number = []
    data = forma_file.get_base()
    event(data, None, 0, lst_number)


if __name__ == '__main__':
    main()
