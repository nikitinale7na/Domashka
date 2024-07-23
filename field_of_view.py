def test_function():
    # nonlocal inner_function
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()
# При попытке вызвать inner_function() возникает ошибка, тк. она определена внутри  test_function()
# и не видит ее как самостоятельную
# При попытке вызвать нелокальную inner_function ошибка: no binding for nonlocal 'inner_function' found
# inner_function()

from  field_of_view2 import str_
print(str_)
