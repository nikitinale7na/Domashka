def test_function():

    def inner_function():
        global str_
        str_ = 'Я в области видимости функции test_function'
        print(str_)
    inner_function()


test_function()
