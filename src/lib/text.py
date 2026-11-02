def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Возвращает объект типа str, представляющий нормализованный текстовый эквивалент 
    исходной строки
    normalize("ПрИвЕт\nМИр\t") == "привет мир"
    """
    
    if casefold==True:      
        text=(text.casefold())
    else: text=text.lower()
    
    if yo2e==True:                 
        text=text.replace('ё', 'е').replace('Ё', 'Е')
    
    text=' '.join(text.split())
    
    return text

# print(normalize("ПрИвЕт\nМИр\t"))
# print(normalize("ёжик, Ёлка"))
# print(normalize("Hello\r\nWorld"))
# print(normalize("  двойные   пробелы  "))



##################################################################################################################################################3



import re

def tokenize(text: str) -> list[str]:
    '''Функция возвращает объект типа list[str],
    элементами которого являются текстовые токены, выделенные из исходной строки.
    tokenize("привет, мир!") == ["привет", "мир"]
    '''
    result=normalize(text)
    
    result=re.findall(r"\w+(?:-\w+)*",result)
    
    return result

# print(tokenize("привет мир"))
# print(tokenize("heLLo,world!!!"))
# print(tokenize("по-настоящему круто"))
# print(tokenize("2025 год"))
# print(tokenize("emoji 😀 не слово"))



#################################################################################3######################################



def count_freq(tokens: list[str]) -> dict[str, int]:
    """Подсчёт частоты встречаемости элементов.
    Возвращает объект типа dict[str, int]
    freq == {"a":3, "b":2, "c":1}
    """
    slovar={}
    
    for w in tokens:
        slovar[w]=slovar.get(w,0) + 1  #Если слово w уже в словаре,.get() возвращает его текущее количество. К нему прибавляется 1, обновляя счётчик.
        
    return slovar

# print(count_freq(["a","b","a","c","b","a"]))
# print(count_freq(["bb","aa","bb","aa","cc"]))




##########################################################################################33333



def top_n(freq: dict[str, int], n: int = 3) -> list[tuple[str, int]]:
    
    """Возвращает список топ-N по убыванию частоты; при равенстве — строго по алфавиту слова.
    top_n({"bb":2,"aa":2,"cc":1}, 2) == [("aa",2), ("bb",2)]"""
    
    result=sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))[:n]
    return result 

# print(top_n({"a":3,"b":2,"c":1},2))
# print(top_n({"bb":2,"aa":2,"cc":1},2))

from pathlib import Path
"""Открыть файл на чтение; вернуть содержимое как одну строку.
Чтобы выбрать кодировку, её нужно передать явно в метод read_text в виде строки"""

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p=Path(path)
    return p.read_text(encoding=encoding)


if __name__ == "__main__":
    if len(read_text('data/lab4/input.txt'))==0:
        print()
    try:
        print(read_text('data/lab4/input.txt'))
    except FileNotFoundError:
        print('файл не найден')
    except UnicodeDecodeError:
        print('неверная кодировка')