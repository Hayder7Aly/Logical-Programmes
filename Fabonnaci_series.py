# def Recursive_approch(num):
#     if num==0:
#         return 0
#     elif num==1:
#         return 1
#     else:
#         return Recursive_approch(num-1) + Recursive_approch(num-2)

def Iterative_approch(num):
    if num==0:
        return 0
    else:
        preNum = 0
        currNum = 1
        for i in range(1,num):
            prepreNUM = preNum
            preNum = currNum
            currNum=preNum+prepreNUM
        
        return currNum 

if __name__ == "__main__":
    num = int(input('PLEASE ENTER A NUMBER FOR FABONACCI SERIES CONTENT : '))
    # print(f'The Index Of {num} the Number In fabonnaci series In Recurisve Method = ',Recursive_approch(num))
    print(f'The Index Of {num} the Number In fabonnaci series Iterative Method  = ',Iterative_approch(num))


# 0 1 1 2 3 5 NOTE :