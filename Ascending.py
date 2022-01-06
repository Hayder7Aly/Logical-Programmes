user = int(input("Please Enter How Many Number Do You Want to Enter : "))
print(f"Please Enter {user} Number : ")
ascending = []
for i in range(1,user+1):
    ascending.append(int(input()))
asc = input("Enter 1 for Ascending 0 for Descending : ")
if asc == '1':
    ascending.sort()
    print(ascending)
elif asc=='0':
    ascending.sort(reverse=True)
    print(ascending)
input()