num=int(input('How many Name Do You Want To Enter In This Programme . '))
names=[]
print("Please Enter",num,"Name Of Your Friends : ")
for i in range(num):
    names.append(input())
print(list(set(names)))
input()


# null=[]
# for i in names:
#     if i not in null:
#         null.append(i)
# print(null)


    