from os import system,name

def clear():
    if name=='nt':
        _ = system('cls')
    else:
        _ = system('clear')

while True:
    print('Press q For Quite The Programme . ')
    a=input('Please Enter A Number for Table : ')
    if a=='q':
        break
    try:
        num=int(a)
    except Exception as e:
        print('Only Numbers are allowed in this programme : ')
    else:
        for i in range(1,11):
            print("%d * %d = %d"%(num,i,num*i))
        input()
        clear()