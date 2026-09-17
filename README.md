# Лаболаторная работа 1
## Задание 1
![Hello wolrd!](./images/lab01/ex01.png)

## Задание 2
![a=float(input('a:').replace(',','.'))
b=float(input('b:').replace(',','.'))
print(f'sum={a+b}; avg={((a+b)/2):.2f}')](./images/lab01/ex-02.png)

## Задание 3
![price=float(input('price:'))
discount=float(input('discount:'))
vat=float(input('vat:'))


base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print(f'База после скидки: {base:.2f} ₽')
print(f'НДС:               {vat_amount:.2f} ₽')
print(f'Итого к оплате:    {total:.2f} ₽')](./images/lab01/ex-03.png)

## Задание 4
![minute=int(input('Минуты:'))
ans=f'{minute//60}:{(minute%60)}'
if (ans[-1]=='0' and ans[-2]==':'):
    print(ans+'0')
else:
    print(ans)](./images/lab01/ex-4.png)

## Задание 5
![fio=input("ФИО:")
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
print(f'Длина (символов):{cnt+2}')](./images/lab01/ex-05.png)
