t1=(1,2,3,1,2,3,1,21,56,'haider','ali','haider')
total=[]
for e in t1:
    if e not in total:
        total.append(e)
        print(f"{e} With Times {t1.count(e)}")