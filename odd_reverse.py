print('Press q For Quite The Programme .')
def rev_odd(num):
    print('All Odd Numbers are given below .')

    # for i in range(num*2,0,-1):
    #     if i%2!=0:
    #         print(i)

    # for i in range(1,num+1):
    #     print(num*2-2*i+1)

    for i in range(2*num-1,0,-2):
        print(i)


if __name__ == "__main__":
    while True:
        a=input('Please Enter A Number For Print Odd Number In Range : ')
        if a=='q':
            break
        try:
            num=int(a)
        except Exception as e:
            print("Only Numbers are allowed in this programme . ")
        else:
            rev_odd(num)
