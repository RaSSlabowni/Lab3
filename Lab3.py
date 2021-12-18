alfavitRU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' #Русский алфавит
alfavitEU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #Английский алфавит 
yazik = input('Введите язык алфавита RU/EU: ') #Выбор алфавита
soobshenie = input('Введите сообщение для шивровки: ').upper() #Ввод сообщения для шифрования
shag = int(input('Введите шаг шифровки: ')) #Ввод шага
shifr = '' #Строка для вывода шифра
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
        if i in alfavitEU:
            shifr += alfavitEU[(a + shag)%26]
        else:
            shifr += i
print (shifr) #Вывод зашифрованного сообщение
print ('Если хотите расшифровать сообщение нажмите 1') 
vibor = int(input()) #Дешифровка
if vibor == 1:
    print (soobshenie)
