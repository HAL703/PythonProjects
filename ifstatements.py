Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> age = int(input('Enter your age, please: '))
Enter your age, please: 3
>>> >>> age = int(input('Enter your age, please: '))

SyntaxError: invalid syntax
>>> name_str = input('Enter your name: ')
Enter your name: cookie
>>> age = int(input('Enter your age: '))
name_str = input('Enter your name: ')
print('Happy birthday, ', name_str, '.', sep'')
print('You are', age, 'years old.')
if age>12 and age<20:
	print('You are a teenager!')
else:
	print('You/'re not a teenager!')
	      
Enter your age: 13
>>> age = int(input('Enter your age: '))
name_str = input('Enter your name: ')
print('Happy birthday, ', name_str, '.', sep='')
print('You are', age, 'years old.')
if age>12 and age<20:
	print('You are a teenager!')
else:
	print('You/'re not a teenager!')
	      
Enter your age: 13
>>> def birthday():
	age = int(input('Enter your age: '))
	name_str = input('Enter your name: ')
	print('Happy birthday, ', name_str, '.', sep'')
	print('You are', age, 'years old.')
	if age>12 and age<20:
		print('You are a teenager!')
	else:
		print('You/'re NOT a teenager!')
		      
SyntaxError: invalid syntax
>>> def birthday():
	age = int(input('Enter your age: '))
	name_str = input('Enter your name: ')
	print('Happy birthday, ', name_str, '.', sep='')
	print('You are', age, 'years old.')
	if age>12 and age<20:
		print('You are a teenager!')
	else:
		print('You/'re NOT a teenager!')
		      
SyntaxError: invalid syntax
>>> def birthday():
	age = int(input('Enter your age: '))
	name_str = input('Enter your name: ')
	print('Happy birthday, ', name_str, '.', sep='')
	print('You are', age, 'years old.')
	if age>12 and age<20:
		print('You are a teenager!')
	else:
		print('You are NOT a teenager!')

		
>>> birthday(4)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    birthday(4)
TypeError: birthday() takes 0 positional arguments but 1 was given
>>> birthday()
Enter your age: 12
Enter your name: andrew
Happy birthday, andrew.
You are 12 years old.
You are NOT a teenager!
>>> 