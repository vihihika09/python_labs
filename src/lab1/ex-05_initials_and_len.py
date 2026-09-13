#задание 5

fio=input("ФИО:")
init=''
cnt=0
fl=0
for i in fio:
    if i!=' ' and fl==0:
        init+=i
        fl=1
    if i!=' ' and fl==1:
        cnt+=1
    if i==' ':
        fl=0

print(f'Инициалы: {init}.')
print(f'Длина (символов):{cnt+2}')
