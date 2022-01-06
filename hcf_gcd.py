try:
    num=int(input("PLEASE ENTER 1st THE NUMBER : "))
    num2=int(input("PLEASE ENTER 2ND THE NUMBER : "))
except Exception as e:
    print('ONLY NUMBERS ARE ALLOWED IN THIS PROGRAMME ! ')
else:
    for i in range(num,0,-1):
        if num%i==0 and num2%i==0:
            print(f"HCF OF {num} AND {num2} = {i}")
            break

    # part II NOTE
    # for i in range(1,min(num,num2)+1):
    #     if num%i==0 and num2%i==0:
    #         hcf = i
    # print(f"HCF OF {num} AND {num2} = {hcf}")
        
input()