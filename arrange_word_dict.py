'''
AUTHOR : HAIDER ALI
DATE   : JANUARY 23 2021
PURPSE : PROBLEM SOLVING  IN DICTIONARY FOR ARRANGE THREE WORDS 
'''

# 1 SIMPLEST WAY TO SORT THE LIST ----->  NOTE

for x in sorted(input('Enter Three City Names : ').split(',')):print(x,end=', ') # without listcomprehension

# [x for x in sorted(input('Enter Three City Names : ').split(',')) if print(x,end=', ')]
input()


# print('Please Enter Three City Names : ')
# a,b,c=input(),input(),input()
# new.append(a),new.append(b),new.append(c)
# new.sort()
# for i in new:
#     print(i,end=' ')



# x=min(a,b,c)
# print(x,end=' ')
# if x==a:
#     print(min(b,c),max(b,c))
# elif x==b:
#     print(min(a,c),max(a,c))
# else:
#     print(min(a,b),max(b,a))


# if a<b<c:
#     print(a,b,c)
# elif a<c<b:
#     print(a,c,b)
# elif b<a<c:
#     print(b,a,c)
# elif b<c<a:
#     print(b,c,a)
# elif c<a<b:
#     print(c,a,b)
# else:
#     print(c,b,a)



 