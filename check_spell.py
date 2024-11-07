'''Напишите простую программу check_spell.py
Которая отправляет на проверку строку Колакал малако и получает исправленный вариант обратно.
Пришлите код и скриншот.'''

from pyaspeller import YandexSpeller

#speller = YandexSpeller()
#print(speller.spelled('в суббботу утромъ'))

def check(words):
    speller = YandexSpeller()
    result = speller.spelled(' '.join(words))
    return result.split(' ')

if __name__ == "__main__":
    words_to_check = ['Колакал', 'пелъмены']
    result = check(words_to_check)

    print(result)