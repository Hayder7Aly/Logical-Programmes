a=input('Please Enter Your String : ').strip()
dup=''
for i in a:
    if i not in dup:
        dup+=i
print(dup)
input()