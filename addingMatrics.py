def matrix(m,n,mat):
    print(f'\n\n\t\tPLEASE ENTER THE {mat} MATRIX')
    o =  []
    for i in range(1,m+1):
        rows = []
        for j in range(n):
            rows.append(int(input(f'\n\n\t\tPLEASE ENTER {i} ROW MATRIX ENTRY : ')))
        o.append(rows)
    return o

            
rows = int(input('\n\n\t\tPLEASE ENTER THE NUMBER OF ROWS : '))
columns = int(input('\n\n\t\tPLEASE ENTER THE NUMBER OF COLUMNS : '))


A = matrix(rows,columns,"1st")


for row in A:
    print(row)

B = matrix(rows,columns,'2nd')
for row in B:
    print(row)


print(f'ADDITION OF MATRIX IS : \n')

for row in list(zip(A,B)):
    for







