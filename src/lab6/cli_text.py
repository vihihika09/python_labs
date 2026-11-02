import argparse
from src.lib.text import read_text, normalize,tokenize,top_n,count_freq

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command") # в command записывается название команды (cat)

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help='Путь к входному файлу')
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help='Путь к входному файлу')
    stats_parser.add_argument("--top", type=int, default=5, help='Кол-во строк в топе')

    args = parser.parse_args()


    if args.command == "cat":
        try:
            rows=read_text(args.input).splitlines()
        except FileNotFoundError:
            parser.error('Отсутствие входного файла')
            
        if args.n:
            for num, row in enumerate(rows,start=1):
                print(f'{num}  {row}')
        else:
            for row in rows:
                print(row)
                
                
    elif args.command == "stats":
        try:
            rows=read_text(args.input)
        except FileNotFoundError:
            parser.error('Отсутствие входного файла')
        if args.top<=0: parser.error('Параметр "top" должен быть больше 0')
            
        norm_text=normalize(rows)
        token=tokenize(norm_text)
        cnt=count_freq(token)
        topN=top_n(cnt,n=args.top)
        
        print(f'Всего слов: {len(token)}')
        print(f'Уникальных слов: {len(cnt)}')
        print(f'Топ:{args.top}')
        for kzh in topN:
            print(f'{kzh[0]}: {kzh[1]}')
    
if __name__=='__main__':
    main()
            