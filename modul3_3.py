# 1.Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):   #Создайте функцию print_params со значениями по умолчанию
    print(a,b,c)                              # Функция должна выводить эти параметр
    # #Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.

print_params(3)
print_params(5, 'Ogogogo')
print_params(5,'Ogogogo', False)
print_params()
# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(b=25)  # работает
# print_params(с=[1,2,3]) не работает Ошибка "функция print_params() получила неожиданный аргумент ключевого слова 'c'"


# 2. Распаковка параметров:
values_list = [3, 'Слово', True]  #Создайте список  с тремя элементами разных типов
values_dict = {'a': 3, 'b': 'Слово', 'c': True}  # создайте словарь с тремя ключами, соответствующими параметрам функции print_params
print_params(*values_list)
print_params(**values_dict)

values_list_3 = [54.32, 'Строка']



# 3.Распаковка + отдельные параметры:

values_list_2 = [7, 'Конь'] # Создайте список values_list_2 с двумя элементами разных типов
print_params(*values_list_2, 42)  # Проверьте, работает ли print_params(*values_list_2, 42) список распоковался на b, c
print_params(*values_list_3, 42)

