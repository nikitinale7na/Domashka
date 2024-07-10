my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    if my_list[index] < 0:
        index += 1
        continue   # continue а не break чтобы идти дальше до конца списка и собрать все положительные
    if my_list[index] > 0:
        print(my_list[index])
    index += 1
    # 2var
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    if my_list[index] < 0:
        break   # если break то заккончится, когда встретит первое отрицательное - на 99
    if my_list[index] > 0:
        print(my_list[index])
    index += 1




