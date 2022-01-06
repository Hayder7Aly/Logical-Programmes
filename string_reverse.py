string=input('Please Enter A String For Reverse : ')

# print(string[::-1])  --- 1

# print(string[len(string)-1::-1]) ---- 2



for i in range(len(string)-1,-1,-1):
    print(string[i],end='')

input()