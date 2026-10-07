# Задание 3
def format_record(rec: tuple[str, str, float]) -> str:
    """Тип записи студента как кортеж
    ("Иванов Иван Иванович", "BIVT-25", 4.6) → "Иванов И.И., гр. BIVT-25, GPA 4.60"
    """
    
    if type(rec[0])!=str or type(rec[1])!=str or type(rec[2])!=float:
        raise TypeError('Неверный тип данных')
    if rec[0]=='' or rec[1]=='':
        raise ValueError('Некорректная запись')
    
    fio,group,gpa=rec
    
    try:
        f,i,o=fio.split()
        ans1=f'{f[0].upper()+f[1:]} {i[0].upper()}.{o[0].upper()}.'
    except: 
        f,i=fio.split()
        ans1=f'{f[0].upper()+f[1:]} {i[0].upper()}.'
    ans2=group.strip()
    if 0.0<=gpa<=5.0:
        ans3=float(str(gpa).strip())
    else:
        raise ValueError('Некорректная запись')
    
    return f'{ans1}, гр. {ans2}, GPA {ans3:.2f}'

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
