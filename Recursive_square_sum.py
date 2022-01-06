sq=lambda n : n**2+sq(n-1) if n>=1 else 0


# Working Of Recursive Method Of SQuare Of N Natural Numbers Is  NOTE
# 5**2 + sq(4)
# 5**2 + 4**2 + sq(3)
# 5**2 + 4**2 + 3**2 + sq(2)
# 5**2 + 4**2 + 3**2 + 2**2 + sq(1)
# 5**2 + 4**2 + 3**2 + 2**2 + 1**2

# 25 + 16 + 9 + 4 + 1 = 25 NOTE ANS .

# def sq(n):
#     if n<=0:
#         return 0
#     else:
#         return n**2+sq(n-1)


print("Sum Of n Natural Numbers Square Is : ",sq(int(input('Please Enter The number For Sum Of Square s : ')))),input()