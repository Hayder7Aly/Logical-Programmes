for i in range(1,int(input('Please Enter A Number For Prime : '))+1):
    if i<2:
        print(f"{i} is not a prime number")
    else:
        for j in range(2,i):
            if i%j==0:
                print(f"{i} is not a prime number")
        else:
            print(f'{i} is a prime number')
input()

