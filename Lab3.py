alfavitRU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alfavitEU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
yazik = input('Введите язык алфавита RU/EU: ')
soobshenie = input('Введите сообщение для шивровки: ').upper()
shag = int(input('Введите шаг шифровки: '))
shifr = ''
if yazik == 'RU':
    for i in soobshenie:
        a = alfavitRU.find(i)   
        if i in alfavitRU:
           shifr += alfavitRU[(a + shag)%33]
        else:
            shifr += i
elif yazik == 'EU':
    for i in soobshenie:
        a = alfavitEU.find(i)   
        if i in alfavitRU:
            shifr += alfavitEU[(a + shag)%26]
        else:
            shifr += i
print (shifr)
print ('Если хотите расшифровать сообщение нажмите 1')
vibor = int(input())
if vibor == 1:
    print (soobshenie)
