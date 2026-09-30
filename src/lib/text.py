def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    if casefold==True:      #делаю нижний регистр
        text=(text.casefold())
    else: text=text.lower()
    
    if yo2e==True:                  # если надо меняю ё на е
        text=text.replace('ё', 'е').replace('Ё', 'Е')
    
    text=' '.join(text.split())    # строки записываются в список через запятую и соединяются джоином в строку черзе пробел 
    
    return text
    

print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))