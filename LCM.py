try:
    num=int(input("PLEASE ENTER THE 1ST NUMBER : "))
    num2=int(input("PLEASE ENTER THE 2ND NUMBER : "))
except Exception as e:
    print('ONLY NUMBERS ARE ALLOWED IN THIS PROGRAMME !')
else:
    # tab1=[]
    # tab2=[]
    # i=1
    # while True:
    #     tab1.append(num*i)
    #     tab2.append(num2*i)
    #     if i in tab1 and i in tab2:
    #         print(f"LCM OF THESE TWO NUMBER = {i}")
    #         break
    #     i+=1

    maxNum=max(num,num2)
    while True:
        if maxNum%num == 0 and maxNum%num2 == 0:
            print(f"LCM OF THESE TWO NUMBERS IS = {maxNum}")
            break
        maxNum+=max(num,num2)

input()