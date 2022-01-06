name=input('Enter Your Name :')
age= input('Enter Your Age  :')


# NOTE  -- THIS IS A BEST METHOD FOR STRING FORMATING
print(f"Hello word, {name} what new message {age} ")

# default arguments.
print('Hello {} , Your age is {}'.format(name,age))

# positional arguments.
print('Hello {0} , Your age is {1}'.format(name,age))

# keyword arguments
print('Hello {name},Your age is {age}'.format(name='Ali',age=20))

# mixed arguments
print('Hello Your name is {0}, Your salary is {1}'.format('Haider',100000))


# point = {'x':4,'y':-5}
# print('{x} {y}'.format_map(point))

# point = {'x':4,'y':-5, 'z': 0}
# print('{x} {y} {z}'.format_map(point))



# # default arguments
# print('Hello {}, your balance is {}.'.format('Adam', 230.2346))

# # positional arguments
# print('Hello {0}, your balance is {1}.'.format('Adam', 230.2346))

# # keyword arguments
# print('Hello {name}, your balance is {blc}.'.format(name='Adam', blc=230.2346))

# # mixed arguments
# print('Hello {0}, your balance is {blc}.'.format('Adam', blc=230.2346))


input()