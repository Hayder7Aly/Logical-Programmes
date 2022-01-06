print('Please Enter One Tuples In Comma Seperated .')
t1=[i for i in input().strip().split(',')]
print('Please Enter Two Tuples In Comma Seperated .')
t2=[i for i in input().strip().split(',')]
tup1,tup2=list(map(int,t1)),list(map(int,t2))
tup1.sort(),tup2.sort()
print(f"{tup1}\n{tup2}")
