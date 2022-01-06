print('\n\n\t\t\t\t\tMark Sheet Of Five Subjects\n\n')

def mark_sheet(mark_list):
    minimum_marks=min(mark_list)
    max_marks=max(mark_list)
    if minimum_marks<33:
        print(f"\n\tYou are Failed In Sub Subjects")
    elif max_marks>100:
        print(f'\n\tYou Have Invalid Input In Subject Total Marks Is 100 Given Marks In Subject Is {max_marks}')
    else:
        print("\n\tCongratulation ! You Have Passed The Examination .\n")
        print(f"\t\tTotal Marks\t\tObtain Marks\t\tPercentage\t\tDivision")
        percentage=(sum(mark_list)/5).__round__(4)
        if percentage>=60:
            division='1st'
        elif percentage>=50:
            division='2nd'
        else:
            division='3rd'

        print(f"\t\t500\t\t\t{sum(mark_list)}\t\t\t{(sum(mark_list)/5).__round__(2)}\t\t\t{division}")
        


      
if __name__ == "__main__":

    mark_list=[]
    books=['Marks In English : ','Marks In Urdu : ','Marks In Math : ','Marks In Islamiyat :', 'Marks In Science : ']
    try:
        for i in books:
            a=int(input(f'\n\t{i}'))
            mark_list.append(a)
        
    except Exception as e:
        print('Only Numbers are Allowed In This Programme . ')
    else:
        mark_sheet(mark_list)
input()
