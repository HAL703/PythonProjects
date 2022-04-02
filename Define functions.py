Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=1
>>> b=-1
>>> c=-1
>>> negative= (b*b - 4*a*c) ** 0.5
>>> negative
2.23606797749979
>>> negative2= (-b - negative)/ 2a
SyntaxError: invalid syntax
>>> negative2= (-b - negative) / 2*a
>>> negative2
-0.6180339887498949
>>> a1=a2=a3=10
>>> a1
10
>>> a2
10
>>> a3
10
>>> tt, ty, tz = 10, 20, 30
>>> tt
10
>>> ty
20
>>> tz
30
>>> cels=77
>>> fahr=cels * 1.8 + 32
>>> fahr
170.6
>>> def convert(cels):
	fahr=cels*1.8 + 32
	return fahr
convert(25)
SyntaxError: invalid syntax
>>> convert(25)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    convert(25)
NameError: name 'convert' is not defined
>>> convert
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    convert
NameError: name 'convert' is not defined
>>> 
================================ RESTART: Shell ================================
>>> def convert(cels):
	fahr=cels*1.8 + 32
	return fahr

>>> 
>>> convert
<function convert at 0x000001F4CEDBAF70>
>>> convert(25)
77.0
>>> convert(100)
212.0
>>> convert(246.8)
476.24
>>> def inch_to_centimeters(x)
SyntaxError: invalid syntax
>>> def inch_to_centimeters(x):
	return x*2.54

>>> inch_to_centimeters(46)
116.84
>>> 
>>> 