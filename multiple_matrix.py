mat1 = []
print("PLEASE ENTER 1ST MATRIX .")
for i in range(1,5):
    mat1.append(int(input(f"Enter {i} Element Number : ")))

mat2 = []
print("PLEASE ENTER 2ND MATRIX .")

for i in range(1,5):
    mat2.append(int(input(f"Enter {i} Element Number : ")))

mul_matrix = []

mul_matrix.append(mat1[0]*mat2[0]+mat1[1]*mat2[2])
mul_matrix.append(mat1[0]*mat2[1]+mat1[1]*mat2[3])
mul_matrix.append(mat1[2]*mat2[0]+mat1[3]*mat2[2])
mul_matrix.append(mat1[2]*mat2[1]+mat1[3]*mat2[3])

for i in mul_matrix:
    if i<=2:
        print(i,end='  ')
    else:
        print()
        print(i,end='  ')

# '''
# [1 2 ] [3 5]
# [3 4 ] [5 6]
# '''
    


