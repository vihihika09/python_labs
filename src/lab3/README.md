# ЛР3 — Тексты и частоты слов (словарь/множество)
## Задание A — src/lib/text.py
## Normalize
``` python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    if casefold==True:
        text=(text.casefold())
    else: text=text.lower()
    
    if yo2e==True: 
        text=text.replace('ё', 'е').replace('Ё', 'Е')
    
    text=' '.join(text.split())
    
    return text
```
### Тест-кейсы:
```python
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))
```
![](../../images/lab03/normalize_out.png)

Добавить докстринг в 1 функцию
