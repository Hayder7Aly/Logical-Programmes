'''
check armstrong number num = 124
1**3+2**3+4**3 = 1+8+64 = 73
'''

try:
    num=int(input(f"PLEASE ENTER THE NUMBER FOR CHECK IT ARMSTRONG NUMBER : "))
except Exception as e:
    print(f"ONLY NUMBERS ARE ALLOWED IN THIS PROGRAMME ")
else:
    exponent=len(str(num))
    armstrong=0
    for i in str(num):
        armstrong+=int(i)**exponent
    if armstrong==num:
        print(f"THIS IS ARMSTRONG NUMBER : {num} ")
    else:
        print(f"THIS IS NOT ARMSTRONG NUMBER : {num} ")
input()

        

