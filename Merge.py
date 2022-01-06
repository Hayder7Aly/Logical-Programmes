# t1 = eval(input("PLEASE ENTER NUMBER WITH COMMA SEPERATED FOR 1ST TUPLE : "))
# t2 = eval(input("PLESE ENTER NUMBER WITH COMMA SEPERATED FOR 2ND TUPLE :"))
# t3 = tuple([eval(e) for e in input().split(',')])


# if t1 == t2:
#     print("They are same ")
# else:
#     print("These are not same ")


# for i in t1:
#     if i not in t2:
#         print("THEY ARE NOT SAME .")
#         break
# else:
#     print("THEY ARE SAME ...")



# t1 =(1,2,3,4,5,1,3,4)
# repeater=[]
# for i in t1:
#     if i not in repeater:
#         repeater.append(i)
#         print(f"{i} Repeats In {t1.count(i)} Times")



# lst = [1,2,3,4,5,6,1,2,3]
# print(lst)
# new = []
# for i in lst:
#     if i not in new:
#         new.append(i)
# print(new)


# lst = [1,4,2,55,7,8,9,33]
# lst.sort(reverse=True)
# print(lst)


# sq = lambda n : n**2+sq(n-1) if n>=1 else n
# print(sq(5))


# def even(n):
#     if n>=1:
#         print(n*2,end=', ')
#         even(n-1)
#     else:
#         print(n)

# def even(n):
#     if n>=1:
#         even(n-1)
#         print(n*2,end=', ')
#     else:
#         return 0
# even(5)




# def odd(n):
#     if n>1:
#         odd(n-1)
#         print(n*2-1,end=', ')
#     else:
#         print(n,end=', ')
# odd(5)