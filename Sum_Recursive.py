add = lambda n : n+add(n-1) if n>=1 else 0
# Working With sum Of All Natural Numbers With Recursive Method 
# suppose Input is 5

# 5+add(4)
# 5+4+add(3)
# 5+4+3+add(2)
# 5+4+3+add(1)
# 5+4+3+2+1

print(f"Sum Of n Natural Numbers Is : ",add(int(input('Please Enter The Number For Sum : ')))),input()