print('Enter q for quite the calculations ... \n')
prices=[]
product=[]
while True:
    num=input('Please Enter The Price Of Product : ')
    product_name=input('Please Enter the Product Name : ')
    print()
    if num=='q' or product_name=='q':
        break
    try:
        number=int(num)
    except Exception as e:
        print('Only numbers are allowed in Price please check it ..')
    else:
        prices.append(number)
        product.append(product_name)


result=list(zip(prices,product))


i=1
for price,product in result:
    print(f"{i} . {product}  Price {price} Rs")
    i+=1

print(f'\nSum Of All Product Is : {sum(prices)} Rs.')


input()
