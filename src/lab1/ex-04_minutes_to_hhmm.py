#задание 4

minute=int(input('Минуты:'))
ans=f'{minute//60}:{(minute%60)}'
if (ans[-1]=='0' and ans[-2]==':'):
    print(ans+'0')
else:
    print(ans)