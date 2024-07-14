calls = 0   # Создать переменную calls = 0 вне функций
def count_calls():     # Создать функцию count_calls и изменять в ней значение переменной calls
    global calls
    calls += 1
    return calls


def string_info(string):       # Создать функцию string_info с параметром string
    count_calls()
    str_ = len(string), string.lower(), string.upper()
    return string

def is_contains(string, list_to_search):    # Создать функцию is_contains с двумя параметрами string и list_to_search
    count_calls()
    s = string.lower()
    lst_ = [item.lower() for item in list_to_search]
    return s in lst_


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)



