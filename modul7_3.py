import io
from pprint import pprint

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}   # Переберите названия файлов и открывайте каждый из них, используя оператор with.
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()   # Избавьтесь от пунктуации
                    punctuation = [',', '.', '=', '!', '?', ';', ':']
                    for punct in punctuation:
                        line = line.replace(punct, '')
                    line = line.replace(' - ', ' ')
                    words.extend(line.split())
                    all_words[file_name] = words
        return all_words

    def find(self, word):
        dict_ = {}
        for i, j in self.get_all_words().items():
            if word.lower() in j:
                dict_[i] = j.index(word.lower()) + 1
        return dict_

    def count(self, word):
        dict2_ = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            dict2_[value] = words_count
        return dict2_


finder2 = WordsFinder('text.txt')
print(finder2.get_all_words)  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
