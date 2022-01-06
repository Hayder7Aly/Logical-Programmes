print('Enter q for exit the programme . ')
while True:
    num=input('\nPlease Enter a Number : ')
    if num=='q':
        break
    try:
        num=int(num)
    except Exception as e:
        print('\nOnly Numbers are allowed in this programme')
    else:
        if num<=0:
            print('\nZero and negatives number are not possible')
            continue
        print(f"\nAll Natural Number From 1 to {num} in reverse order")
        # FOR LOOP NOTE

        # for i in range(num,0,-1):
        #     print(f"{i}",end=', ')

        # 2 NOTE ---> 
        i=1
        while i<=num:
            print(f"{num+1-i}")
            i+=1

        

        # NOTE  WHILE LOOP
        # i=num
        # while i>=1:
        #     print(i)
    
