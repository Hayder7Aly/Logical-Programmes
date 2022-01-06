l=[x for x in input('Enter The Numbers in comma seperated : ').split(',')]
item=input('Enter A element for locate : ')
for i in range(len(l)):
    if l[i].lower() ==  item.lower():
        print(f"{item} In Index {i}")


