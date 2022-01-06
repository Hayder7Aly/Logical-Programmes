def PrimeProducer(num):
    primeLst=[]
    i=1
    while True:
        if len(primeLst) == num:
            return primeLst
        primeLst.append(NextPrime(i))
        i=NextPrime(i)
        
def NextPrime(num):
    while True:
        num+=1
        for i in range(2,num):
            if num%i==0:
                break
        else:
            return num


if __name__ == '__main__':
    try:
        num=int(input('How Many Prime Numbers Do You Want To Generate : '))
    except Exception as e:
        print('Only Numbers Are Allowed In This Programme . ')
    else:
        print(PrimeProducer(num)),input()
