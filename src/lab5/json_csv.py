from pathlib import Path
import csv
import json

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    json_f=Path(json_path)
    csv_f=Path(csv_path)
    
    if not json_f.exists():
        raise FileNotFoundError("файл не найден")
    
    if not csv_f.exists():
            raise FileNotFoundError("файл не найден")
        
    if json_f.suffix.lower() != ".json":
        raise ValueError(f"Неверный формат входного файла")
    
    if csv_f.suffix.lower() != ".csv":
        raise ValueError(f"Неверный формат выходного файла")
    
    with json_f.open ("r",encoding='UTF-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("Пустой JSON / неподдерживаемая структура")
        
    if not isinstance(data, list) or len(data) == 0:
        raise ValueError('Файл JSON пустой / имеет неправильный формат')
    
    if not all(isinstance(i, dict) for i in data):
        raise ValueError("Все элементы списка JSON должны быть словарями")
    
    fieldnames = {}
    for element in data:
        for key in element.keys():
            fieldnames[key] = None

    with csv_f.open('w', newline="", encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(fieldnames.keys()))
        w.writeheader()
        w.writerows(data)


if __name__ == '__main__':
    json_to_csv('data/lab5/samples/people.json','data/lab5/out/people_from_json.csv')
    json_to_csv('data/lab5/samples/cities.json','data/lab5/out/cities.csv')