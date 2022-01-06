with open('currency_data.txt') as f:
    lines=f.readlines()


currencyDict={}
for line in lines:
    parsed=line.split(',')
    # print(parsed)
    currencyDict.update({parsed[0].strip():parsed[1].strip()})

# print(currencyDict)

try:
    amount=int(input('\tPlease Enter your Amount for convert the currency in Pakistan Rupees : '))
except Exception as e:
        print('\tOnly numbers are allowed in this Programme . ')
else:
    print('\tAvailable Options are Given below .')
    [print(f'\t{i}') for i in currencyDict.keys()]

    option=input('\tEnter the Option for convert the Currency : ').lower()
    # print(option)

    currencyDict1={}
    for country,rs in currencyDict.items():
        currencyDict1.update({country.lower() : rs})

        
    if option not in currencyDict1.keys():
        print('\tPlease check it your option invalid ..')
    else:
        print(f"\t{amount} INR is equal to {amount*int(currencyDict1[option])} {option}")
input()