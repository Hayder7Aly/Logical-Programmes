print('Please Enter Comma Seperate Values In Two Tupples : ')
l1=tuple([eval(e) for e in input().split(',')])
l2=tuple([eval(e) for e in input().split(',')])
if l1==l2:
    print('Yes, This Is Same Tuple')
else:
    print("No,This Is Not Same Tuple")