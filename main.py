print('Please Enter 10 Students Marks ')
total_marks  = int(input('Please Enter Total Marks Of Student : '))
info = {}
list1 = []
for i in range(1,5):
    name = input('Please Enter Student Name : ')
    obtain_marks = int(input('Please Enter Obtain Marks Of Student : '))
    per = ((obtain_marks/total_marks)*100).__round__(2)
    list1.append(per)
    info.update({per:name})

data1 = max(list1)
data11 = info[data1]
list1.remove(data1)
print(f"1 . {data11}\t\t{data1} ")

data2 = max(list1)
data22 = info[data2]
list1.remove(data2)
print(f"2 . {data22}\t\t{data2} ")




