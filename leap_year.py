'''
AUTHOR : HAIDER ALI JUTT
DATE  : JANUARY 18 2021
PURPOSE : PROBLEM SOLVING 
'''


print('If you want to exit the programme then press q .\n')
while True:
    a=input('Please Enter a year for check whether a year is leap or not ? ')
    if a=='q':
        print('Thanks for using leap year programme')
        break
    else:
        try:
            year=int(a)
        except Exception as e:
            print('Only Numbers are allowed in this programme .\n')
        else:
            result=f'{year} is Leap Year'if year%400==0 else f'{year} is a Leap Year' if year%4==0 and year%100!=0 else f'{year} is Non Leap Year'

            print(result)

            # short hand if else statement    <-------- NOTE 
            # if year%400==0:print(f"{year} is a leap year")
            # elif year%4==0 and year%100!=0:print(f"{year} is not a leap year")
            # else:print(f'{year} is not a leap year') 

 