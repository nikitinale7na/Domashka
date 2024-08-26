def add_everything_up(arg1, arg2):
    try:
        result = round((arg1 + arg2), 3)
    except TypeError:
        result = str(arg1) + str(arg2)
        return result
    finally:
        return result




print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))