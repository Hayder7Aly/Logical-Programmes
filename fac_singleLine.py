# Working Of Given Factorial  with Recursive Method ..  NOTE


# 5 * fac(4)
# 5 * 4 * fac(3)
# 5 * 4 * 3 * fac(2)
# 5 * 4 * 3 * 2 * fac(1)
# 5 * 4 * 3 * 2 * 1

fac = lambda n : n*fac(n-1)  if n>1 else n
print(f"Factorail Of Given Number Is : {fac(int(input('Please Enter The Number For Locate The Factorial : ')))}")
