# def nextPrime(num):
#     while True:
#         num+=1
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             return num
# print(nextPrime(23))

def prime_number(n):
    if n<=0:
        return"Negative/Zero number is not defined .."
    elif n==1:
        return f"Next Prime Number is : 3"
    elif n>1:
        n+=1
        for i in range(2,n):
            if n%i==0:
                n+=1
        return f"Next Prime number is : {n}"


if __name__ == "__main__":
    while True:
        try:
            n=int(input('Enter a number for next prime number :'))
        except Exception as e:
            print('Only numbers are allowed in this Programme ')
            continue
        else:
            print(prime_number(n))
            break
input()