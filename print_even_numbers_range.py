print('Enter 0 For Close The Programme .\n')
while True:
    try:
        number=int(input("\nPlease Enter A Number For Collect Even Numbers : "))
    except Exception as e:
        print('\nOnly Numbers are allowed in this programme !')
    else:
        if number == 0 :
            break

        # 1ST        NOTE
        print(f'\nFirst {number} Number In Reverse Order .')
        for i in range(number*2,0,-2):
            print(f"{i}",end=', ')

        # 2ND        NOTE
        # for i in range(number*2,1,-1):
        #     if i%2==0:
        #         print(i)

        # 3rd        NOTE
        # for i in range(1,number*2+1):
        #     if i%2==0:
        #         print(i)

        # 4th     NOTE
        # for i in range(1,number+1):
        #     print(number*2+2-2*i)




