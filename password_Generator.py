import string
import random

s1 = string.ascii_uppercase
# print(s1)
s2 = string.ascii_lowercase
# print(s2)
s3 = string.digits
# print(s3)
s4 = string.punctuation
# print(s4)

passwordLength = int(input("Please Enter The Length Of Password : "))

pwdElements = []
pwdElements.extend(list(s1))
pwdElements.extend(list(s2))
pwdElements.extend(list(s3))
pwdElements.extend(list(s4))

# Part I NOTE

password = ''
for i in range(passwordLength):
    charcter = random.choice(pwdElements)
    password+=charcter
print(password)


# Part II  NOTE

random.shuffle(pwdElements) # shuffle means mix the elements in list ...

print(''.join(pwdElements[0:passwordLength]))

# Part III NOTE 

print(f"{''.join(random.sample(pwdElements,passwordLength))}")


input()


# import string

# new=[]
# s=string.whitespace
# new.append(s)
# print(new)

# new= 'PrefixSuffiex'.removeprefix('Prefix')
# new= 'PrefixSuffiex'.removesuffix('Suffiex')
# print(new)



