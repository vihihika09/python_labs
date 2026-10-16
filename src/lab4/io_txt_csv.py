# from pathlib import Path
# """Открыть файл на чтение; вернуть содержимое как одну строку.
# Чтобы выбрать кодировку, её нужно передать в метод read_text в виде строки"""

# def read_text(path: str | Path, encoding: str = "utf-8") -> str:
#     p=Path(path)
#     return p.read_text(encoding=encoding)


# if __name__ == "__main__":
#     try:
#         print(read_text('data/lab4/input.txt'))
#     except FileNotFoundError:
#         print('файл не найден')
#     except UnicodeDecodeError:
#         print('неверная кодировка')
        
###############################################################################

import csv
from pathlib import Path

"""Создать/перезаписать CSV с разделителем ,.
Если передан header, записать его первой строкой.
Rows должны быть одинаковой длины, иначе ValueError"""

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    if not rows: return
    
    best=len(rows[0])
    for i in rows:
        if len(i)!=best:
            raise ValueError ('строки разной длины')
        
    file=Path('data/lab4/report.csv')  
    
    with open(file,'w',encoding='utf-8',newline='') as f:
        writer=csv.writer(f,delimiter=',')
        
        if header is not None:
            writer.writerow(header)
            
        writer.writerows(rows)
        
# write_csv([("word","count"),("test",3)], "data/check.csv",('Первый',"заголовок"))
write_csv('',"data/check.csv",('a','b'))