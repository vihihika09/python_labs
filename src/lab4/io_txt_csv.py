from pathlib import Path
"""Открыть файл на чтение; вернуть содержимое как одну строку.
Чтобы выбрать кодировку, её нужно передать в метод read_text в виде строки"""

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p=Path(path)
    return p.read_text(encoding=encoding)


if __name__ == "__main__":
    try:
        print(read_text('data/lab4/input.txt'))
    except FileNotFoundError:
        print('файл не найден')
    except UnicodeDecodeError:
        print('неверная кодировка')


def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    
    best=len(rows[0])
    for i in rows:
        if len(i)!=best:
            raise ValueError ('строки разной длины')
    