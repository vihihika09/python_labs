from openpyxl import Workbook
import csv
from pathlib import Path

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
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
        for row in list(csv.reader(csv_file)):
            ws.append(row) 
        
    for col in ws.columns:
        
        max_len = max(len(str(cell.value or "")) for cell in col)
        col_letter = col[0].column_letter
        ws.column_dimensions[col_letter].width = max(max_len + 3, 8)
    wb.save(xlsx_file)