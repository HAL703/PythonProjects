Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def(x)
SyntaxError: invalid syntax
>>> def (x)
SyntaxError: invalid syntax
>>> def
SyntaxError: invalid syntax
>>> def vars
SyntaxError: invalid syntax
>>> def (difficult function)
SyntaxError: invalid syntax
>>> def difficultfunction(n)
SyntaxError: invalid syntax
>>> def difficultfunction(a):
	aa=3/2
	
	hard=(2/5)* a(n-1) - 1
	return hard

>>> difficultfunction(2)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    difficultfunction(2)
  File "<pyshell#9>", line 4, in difficultfunction
    hard=(2/5)* a(n-1) - 1
NameError: name 'n' is not defined
>>> def difficultfunction(a):
	if a == 1:
		return 1
	else:
		difficult=(2/5)*difficultfunction(a-1)
		return difficult

	
>>> print(difficultfunction(100))
4.0173451106474994e-40
>>> int def difficultfunction(a):
	if a == 1:
		return 1
	else:
		difficult=(2/5)*difficultfunction(a-1)
		return difficult
	
SyntaxError: invalid syntax
>>> def difficultfunction(a):
	if a == 1:
		return 1
	else:
		difficult=(2/5)*difficultfunction(a-1)
		return int(difficult)

	
>>> difficultfunction(100)
0
>>> difficultfunction(2)
0
>>> print(difficultfunction(2))
0
>>> def difficultfunction(a):
	if a == 1:
		return 1
	else:
		difficult=(2/5)*difficultfunction(a-1)
		return(difficult)

	
>>> difficultfunction(2)
0.4
>>> difficultfunction(3)
0.16000000000000003
>>> def difficultfunction(a):
	if a == 1:
		return 1
	else:
		difficult=(2/5)*difficultfunction(a-1) -1

				return(difficult)
			
SyntaxError: unexpected indent
>>> def difficultfunction(a):
	if a == 1:
		return 1
	else:
		difficult=(2/5)*difficultfunction(a-1) - 1
		return(difficult)

	
>>> difficultfunction(2)
-0.6
>>> difficultfunction(3)
-1.24
>>> def difficultfunction(a):
	if a == 2:
		return 2
	else:
		difficult=(2/5)*difficultfunction(a-1) - 1
		return(difficult)

	
>>> difficultfunction(2)
2
>>> def difficultfunction(a):
	if a == 1:
		return (3/2)
	else:
		difficult=(2/5)*difficultfunction(a-1) - 1
		return(difficult)

	
>>> difficultfunction(2)
-0.3999999999999999
>>> difficultfunction(100)
-1.6666666666666665
>>> difficultfunction(3)
-1.16
>>> difficultfunction(0)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    difficultfunction(0)
  File "<pyshell#33>", line 5, in difficultfunction
    difficult=(2/5)*difficultfunction(a-1) - 1
  File "<pyshell#33>", line 5, in difficultfunction
    difficult=(2/5)*difficultfunction(a-1) - 1
  File "<pyshell#33>", line 5, in difficultfunction
    difficult=(2/5)*difficultfunction(a-1) - 1
  [Previous line repeated 1021 more times]
  File "<pyshell#33>", line 2, in difficultfunction
    if a == 1:
RecursionError: maximum recursion depth exceeded in comparison
>>> difficultfunction(101)
-1.6666666666666665
>>> difficultfunction(105)
-1.6666666666666665
>>> difficultfunction(120)
-1.6666666666666665
>>> 