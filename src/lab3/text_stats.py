from src.lib.text import normalize, tokenize, count_freq, top_n
''' Скрипт читает одну строку текста из stdin, применяет функции 
    normalize, tokenize, count_freq, top_n к вводимому тексту.
    Выводит:
    Всего слов: n
    Уникальных слов: k
    Топ-5: — по убыванию частоты; при равенстве — строго по алфавиту слова.
'''

text=input()

norm_text=normalize(text)
token_text=tokenize(norm_text)
cnt_unik_words=count_freq(token_text)
top=top_n(cnt_unik_words)

print(f'Всего слов: {len(token_text)}')
print(f'Уникальных слов: {len(cnt_unik_words)}')
print('Топ-5:')
for kzh in top:
    print(f'{kzh[0]}: {kzh[1]}')

