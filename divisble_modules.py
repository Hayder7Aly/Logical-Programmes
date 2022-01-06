print('Press q for quite the programme \n\n')
while True:
    a=input('Enter a number for check wether a number is divisible by 5 : ')
    if a=='q':
        break
    try:
        num=int(a)
    except Exception as e:
        print('\nOnly numbers are allowed in this programme .\n ')
    else:
        if num%5==0:
            # print(f"{num} Is Divisible By 5\n")
            print("%d Is Divisible By 5"%num)
        else:
            print(f"{num} Is Not Divisible By 5\n")