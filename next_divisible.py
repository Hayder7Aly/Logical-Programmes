print('Press q for exit the programme .\n ')

def next_divisible(num):
    
    # number = num+1
    # while True:
    #     if number%5==0:
    #         return number
    #     number+=1

    # simple that you work ! NOTE  the quote of Haider Ali 


    remainder=num%5
    plus=5-remainder
    return num+plus
    
    



while True:
    a=input('Please Enter A Number For Get Next Divisible Number of 5 : ')
    if a=='q':
        break
    try:
        num=int(a)
    except Exception as e:
        print('\nOnly Integers Number are allowed in this programme .\n ')
    else:
        print(f'\nNext Divisible Number of 5 is {next_divisible(num)}\n')
