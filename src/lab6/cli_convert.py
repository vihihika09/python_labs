import argparse
from src.lab5.json_csv import json_to_csv, csv_to_json
from src.lab5.cvs_xlsx import csv_to_xlsx
import json
import csv


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv", help="Преобразует JSON-файл в CSV")
    p1.add_argument("--in", dest="input", required=True, help='Входной файл') 
    # dest="input" нужно, т.к. "in" — это запрещенное ключевое слово в Python. 
    # В терминале пишем --in, а в коде читаем как args.input
    p1.add_argument("--out", dest="output", required=True,help='Файл вывода')

    p2 = sub.add_parser("csv2json", help="Преобразует csv-файл в json-файл")
    p2.add_argument("--in", dest="input", required=True, help='Входной файл')
    p2.add_argument("--out", dest="output", required=True,help='Файл вывода')

    p3 = sub.add_parser("csv2xlsx", help="Преобразует CSV-файл в xlsx-файл")
    p3.add_argument("--in", dest="input", required=True, help='Входной файл')
    p3.add_argument("--out", dest="output", required=True,help='Файл вывода')

    args = parser.parse_args()
    try:
        if args.cmd=='json2csv':
            json_to_csv(args.input,args.output)
        elif args.cmd=='csv2json':
            csv_to_json(args.input,args.output) 
        elif args.cmd=='csv2xlsx':
                csv_to_xlsx(args.input,args.output)  
    
    except FileNotFoundError as e:
        parser.error(str(e))
    except ValueError as e:
        parser.error(str(e))

if __name__=='__main__':
    main()
# python -m src.lab6.cli_convert json2csv --in data/lab5/samples/people1.json --out data/lab6/output/json2csv.csv
# python -m src.lab6.cli_convert csv2json --in data/lab5/samples/cities3.csv --out data/lab6/output/csv2json.json
# python -m src.lab6.cli_convert csv2xlsx --in data/lab5/samples/my_example_bakery.csv --out data/lab6/output/csv2xlsx.xlsx
