from pprint import pprint


def custom_write(file_name, strings):
    file_name = 'text.txt'
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        pos_ = file.tell()
        strings_positions[(strings.index(string) + 1, pos_)] = string
        file.write(string + '\n')
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
