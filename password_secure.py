import random,string

symbols = list(string.punctuation)

len1 = input('Please Entter Your Password : ')

# random.shuffle(symbols)

newchr = ''.join(random.sample(symbols,len(len1)//2))
list1 = list(len1)

pasword = ''
for i in ''.join(random.sample(list1,len(len1)//2)):
    pasword+=i
    

print('Your secure password is : ',pasword+newchr)

SECURE = (('s','$'),('a','@'),('and','&'),('o','0'),('i','1'),('I','|'))
def securePassword(password):
    for first,second in SECURE:
        if first in password:
            password = password.replace(first,second)
    return password

password = input("Please Enter Your Password : ")
print(f"Your Secure Password Is : {securePassword(password)}")

input()