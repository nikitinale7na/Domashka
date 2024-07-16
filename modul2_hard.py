def select(numbers_):
    cod_ = []
    for i in range(1, numbers_ + 1):
        for j in range(i + 1, numbers_ + 1):
            sum_ = i + j
            if numbers_ % sum_ == 0:
                cod_.append(i)
                cod_.append(j)
    return cod_

numbers_ = int(input('Введите число в первую каменную вставку и полученный пароль введите во вторую вставку: '))
cod_ = select(numbers_)
print(*cod_, sep=' ')
