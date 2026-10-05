def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Возвращает объект типа str, представляющий нормализованный текстовый эквивалент 
    исходной строки"""
    
    if casefold==True:      #делаю нижний регистр
        text=(text.casefold())
    else: text=text.lower()
    
    if yo2e==True:                  # если надо меняю ё на е
        text=text.replace('ё', 'е').replace('Ё', 'Е')
    
    text=' '.join(text.split())    # строки записываются в список через запятую и соединяются джоином в строку черзе пробел 
    
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
    '''
    result=normalize(text)
    
    result=re.findall(r"\w+(?:-\w+)*",result)
    
    return result

print(tokenize("привет мир"))
print(tokenize("heLLo,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
