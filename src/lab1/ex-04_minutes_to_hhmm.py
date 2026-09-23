#задание 4

minute=int(input('Минуты:'))
ch=str(minute//60)
mi=str((minute%60))
if int(mi)<10:
    print(ch+':'+'0'+mi)
else:
    print(ch+':'+mi)
