l = lambda n : n*l(n-1) if n>1 else n

def TrailingFactorial(number):
    # fac = l(number)
    # print(fac)

    count = 0
    i = 5
    while (number//i !=0):
        count += (number//i)
        i *=5
    return count


    # while (fac%10==0):
    #     count+=1
    #     fac//=10
    # return count

a=int(input('Please Enter the number : '))
print(TrailingFactorial(a))

input()