print('Press q For Quite The Programme ')
# print("Haider ali jutt")




def con_bin(num):
    number=num
    total=''
    for i in range(1,number+1):
        if number==0:
            break
        total+=str(number%2)
        number=number//2
    return total[::-1]



while True:
    a=input('Please Enter A Number For Convert Binary System : ')
    if a=='q':
        break
    try:
        num=int(a)
    except Exception as e:
        print('Only Numbers are allowed in this programme  .  ')
    else:
        # 1 NOTE  use builtin function 
        # binary=bin(num)
        # binary=str(binary).replace('0b','')
        # print(binary)

        # 2 NOTE myfunction to convenrt number to binary
        print(con_bin(num))



