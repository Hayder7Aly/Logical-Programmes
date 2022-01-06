def armstrong(n):
    while True:
        n+=1
        armstrong = next_armstrong(n)
        if armstrong == n:
            print(f"THIS IS NEXT ARMSTRONG NUMBER : {armstrong}")
            break

def next_armstrong(n):
    exponent = len(str(n))
    arm = 0
    for i in str(n):
        arm+=int(i)**exponent
    return arm

try:
    num = int(input("PLEASE ENTER THE NUMBER FOR FIND NEXT ARMSTRONG NUMBER : "))
except Exception as e:
    print('ONLY NUMBERS ARE ALLOWED IN THIS PROGRAMME ')
else:
    armstrong(num)
input()