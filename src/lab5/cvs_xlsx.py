from openpyxl import Workbook
import csv
from pathlib import Path

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Библиотека openpyxl.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    csv_file=Path(csv_path)
    xlsx_file=Path(xlsx_path)
    
    if not csv_file.exists():
            raise FileNotFoundError("CSV Файл не найден")
    if csv_file.suffix.lower() != ".csv":
                raise ValueError("Входной файл должен быть CSV")
    if xlsx_file.suffix.lower() != ".xlsx":
                    raise ValueError("Файл должен быть XLSX")
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1" 
        
    with csv_file.open('r', newline='', encoding='utf-8') as f:
        for row in csv.reader(f):
            ws.append(row) 
        
    for col in ws.columns:
        max_len = 0
        for cell in col:
            if cell.value: #Проверка на пустоту
                val_len = len(str(cell.value))
                if val_len > max_len:
                    max_len = val_len
        col_letter = col[0].column_letter
        ws.column_dimensions[col_letter].width = max(max_len, 7)
            
    wb.save(xlsx_file)
    
if __name__=='__main__':
    # csv_to_xlsx('data/lab5/samples/cities3.csv','data/lab5/out/cities.xlsx')    
    csv_to_xlsx('data/lab5/samples/my_example_bakery.csv','data/lab5/out/bakery_csv_to_.xlsx')