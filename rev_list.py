from os import name,system

def clear():
    if name=='nt':
        _ = system('cls')
    else:
        _ = system('clear')

while True:
    print('Press q For Quite The Programme . ')
    a=input('How Many Elements Do You Want To Enter In List : ').strip()
    if a=='q':
        break
    try:
        num=int(a)
    except Exception as e:
        print('Only Numbers Are Allowed In This Programme . ')
    else:
        print('Please Enter %d Numbers '%num)
        total=[]
        for i in range(num):
            total.append(input().strip())
        print(list(set(total)))

        # new_total=[]
        # for i in total:
        #     if i not in new_total:
        #         new_total.append(i)
        # print(new_total)

    input()
    clear()