with open('price.txt','r') as rf:
    lines=rf.readlines()
    economy={}
    for line in lines:
        line1=line.split(',')
        economy.update({line1[0]:line1[1]})
    a=int(input('How Many Items Do You Want To Buy : '))
    print(f'Please Enter {a} Product Names : ')
    list1=[]
    price=[]
    for i in range(a):
        pro=input()
        list1.append(pro)
        price.append(economy[pro])
    print('\t\t\t\tProduct\t\t\t\tPrice')
    for i in zip(list1,price):
        print(f"\t\t\t\t{i[0]}\t\t\t\t{i[1]}")
    print(f"Your Bill Is : {sum(list(map(int,price)))}")
input()
    
