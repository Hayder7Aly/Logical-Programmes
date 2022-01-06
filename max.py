# With Out Function Max ... For Locate the maximum number in user input !
num=0
for  i in range(1,int(input("How Many Number Do You Want Enter For Locate The Maximium Number : "))+1):
    usern=int(input("Enter A number : "))
    if usern>=num:
        num=usern
print(num),input()
