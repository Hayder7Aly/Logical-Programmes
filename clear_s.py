# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
  
# print out some text 
print('hello geeks\n') 
  
# sleep for 2 seconds after printing output 
# sleep(2) 
  
# now call function we defined above 
input()
clear() 
input()

















# another way to 



# filter_none
# edit
# play_arrow

# brightness_4
# # import call method from subprocess module 
# from subprocess import call 
  
# # import sleep to show output for some time period 
# from time import sleep 
  
# # define clear function 
# def clear(): 
#     # check and make call for specific operating system 
#     _ = call('clear' if os.name =='posix' else 'cls') 
  
# print('hello geeks\n'*10) 
  
# # sleep for 2 seconds after printing output 
# sleep(2) 
  
# # now call function we defined above 
# clear() 