# l = lambda n : n*l(n-1) if n>1 else n

# def factorial(num):
#     list1= []
#     for i in range(1,num+1):
#         list1.append(l(i))
#     return list1

# a = int(input('Please Enter The Number For Factorial Trailing ?'))
# print(factorial(a))



# l = lambda n: n*l(n-1) if n>1 else n

# def factorial(num):
#     for i in range(1,num+1):
#         print(l(i))    
# a = int(input('Please Enter The Number For Factorial Trailing ?'))
# factorial(a)


# generator
l = lambda n: n*l(n-1) if n>1 else n

def factorial(num):
    ex = 1
    while True:
        if num>=ex:
            yield l(ex)
        else:
            break
        ex+=1

a = int(input('Please Enter The Number For Factorial Trailing ?'))

for i in factorial(a):
    print(i)
