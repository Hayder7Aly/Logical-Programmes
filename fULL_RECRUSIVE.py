# s = lambda n : n+s(n-1) if n>1 else n
# print(s(int(input(f"PLEASE ENTER THE NUMBER FOR TOTAL SUM OF NATURAL NUMBERS : ")))),input()



# sq = lambda n : n**2+sq(n-1) if n>1 else n
# print(sq(int(input(f"PLEASE ENTER THE NUMBER FOR SUM OF SQUARE NATURAL NUMBERS : ")))),input()

# 5**2+4**2+3**2+2**2+1**1 = 25 + 16 + 9 + 4 + 1 = 55  NOTE if input = 5:


# def evenReverse(n):
#     if n>=1:
#         print(2*n , end= ', ')
#         evenReverse(n-1)

# print(evenReverse(int(input("PLEASE ENTER THE NUMBER FOR HOW MANY EVEN NUMBER PRINT : "))))

# def oddreverse(n):
#     if n>=1:
#         print(2*n-1,end=', ')
#         oddreverse(n-1)
# print(oddreverse(int(input("PLEASE ENTER THE NUMBER FOR HOW MANY ODD NUMBER PRINT : "))))


# def natural(n):
#     if n>=1:
#         print(n,end=', ')
#         natural(n-1)

# def natural(n):
#     if n>=1:
#         natural(n-1)
#         print(n,end=',')

# print(natural(int(input('PLEASE ENTER THE NUMBER FOR PRINT ALL BEHIND NATURAL NUMBERS : '))))


# def evennatural(n):
#     if n>=1:
#         evennatural(n-1)
#         print(n*2,end=', ')
# print(evennatural(5))


# l=lambda n : n*l(n-1) if n>1 else n

# print(l(int(input('PLEASE ENTER THE NUMBER FOR FACTORIAL : '))))
# input()


# def even(n):
#     if n>=1:
#         even(n-1)
#         print(n*2,end=', ')

# print(even(int(input("enter a number : "))))


# def odd(n):
#     if n>=1:
#         odd(n-1)
#         print(n*2-1)
# print(odd(int(input('Enter a number : '))))
