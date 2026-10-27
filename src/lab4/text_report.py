def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    """Возвращает список отсортировнаных кортежей count ↓, слово ↑ (при равенстве)."""
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


from src.lab4.io_txt_csv import read_text, write_csv

ENcoDing='utf-8'

try:
    text=read_text('data/lab4/input.txt',encoding=ENcoDing)
except FileNotFoundError:
    print()
except UnicodeDecodeError:
    print('неверная кодировка')
    
from src.lib.text import normalize, tokenize, count_freq, top_n

tokens=tokenize(normalize(text))

cnt_unik_words=count_freq(tokens) # return словарь

top_5=top_n(cnt_unik_words,5) # return список
rows=sorted_word_counts(cnt_unik_words) # return список


if __name__=='__main__':
    write_csv(rows,'data/lab4/report.csv',('Word','Count'))

    print(f'Всего слов: {len(tokens)}')
    print(f'Уникальных слов: {len(cnt_unik_words)}')
    print('Топ-5:')
    for kzh in top_5:
        print(f'{kzh[0]}: {kzh[1]}')    




    
