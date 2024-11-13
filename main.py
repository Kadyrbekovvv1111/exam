som = int(input('Введите возраст: '))

if 0<= som <= 6:
    print('Бесплатно')
elif 6 <= som <= 12:
    print('100 СОМ')
elif 12 <= som <= 18:
    print('200 СОМ')
elif 18 <= som <= 60:
    print('500 СОМ')