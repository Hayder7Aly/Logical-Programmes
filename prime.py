num=int(input('Please Enter Your Number For Check Prime Or Not : '))


if num<2:
    print('Not A Prime Number ')
else:
    for i in range(2,num):
        if num%i==0:
            print('Not A Prime Number')
            break
    else:
        print('Prime Number')
input()