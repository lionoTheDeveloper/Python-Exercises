#Python String encode() Method
# txt = 'my name is ståle'
# print(txt.encode(encoding='ascii',errors='backslashreplace'))
# print(txt.encode(encoding='ascii',errors='ignore'))
# print(txt.encode(encoding='ascii',errors='namereplace'))
# print(txt.encode(encoding='ascii',errors='replace'))
# print(txt.encode(encoding='ascii',errors='xmlcharrefreplace'))

# Python String count() Method
# txt = 'i love apples, apple are my favorite fruit'
# x = txt.count('apple')
# print(x)
# x = txt.count('apple',10,24)
# print(x)

# Python String capitalize() Method
# txt = 'hello, and welcome to my world'
# x = txt.capitalize()
# print(x)
# txt = 'python is FUN!'
# x = txt.capitalize()
# print(x)

# Python String casefold() Method
# Converts string into lower case
# txt = 'hello, and welcome to my world'
# x = txt.casefold()
# print(x)

# Python String center() Method
# txt = 'banana'
# x = txt.center(20)
# print(x)
# x = txt.center(20,'O')
# print(x)

# Python String endswith() Method
# txt = "hello, welcome to my world."
# x = txt.endswith('.')
# print(x)
# x = txt.endswith('welcome',0,14)
# print(x)

# Python String expandtabs() Method
# txt = 'H\te\tl\tl\to'
# print(txt)
# print(txt.expandtabs())
# print(txt.expandtabs(2))
# print(txt.expandtabs(4))

# Python String find() Method
# txt = "Hello, welcome to my world."
# x = txt.find('welcome')
# print(x)
# x = txt.find('jello')
# print(x)
# x = txt.find("to",0,17)
# print(x)
# x = txt.find('to')
# print(x)
# x = txt.index('to')
# print(x)
# x = txt.find('jello')
# print(x) 
# x = txt.index('jello')
# print(x)

# Python String format() Method
# txt = 'for only {price:.2f} dollars!'
# print(txt.format(price = 49))

# txt1 = "my name is {fname}, i'm {age}".format(fname="john",age = 36)
# txt2 = "my name is {0}, i'm {1}".format("john",36)
# txt3 = "my name is {}, I'm {}".format('john',36)
# print(txt1,txt2,txt3)

# txt = 'we have {:<8} chickens.'
# print(txt.format(49))
# txt = 'we have {:>8} chickens.'
# print(txt.format(49))
# txt = 'we have {:^8} chickens.'
# print(txt.format(49))
# txt = 'the temperature is {:=8} degrees celsius.'
# print(txt.format(-5))
# txt = 'the temperature is between {:+} and {:+} degrees celsius.'
# print(txt.format(-3,7))
# txt = 'the temperature is between {:-} and {:-} degrees celsius'
# print(txt.format(-3,7))
# txt = 'the temperature is between {:} and {:} degrees celsius'
# print(txt.format(-3,7))
# txt = 'The universe is {:,} years old.'
# print(txt.format(13800000000))
# txt = 'The universe is {:_} years old.'
# print(txt.format(13800000000))
# txt = 'The binary version of {0} is {0:b}'
# print(txt.format(5))
# txt = 'The unicode version of {0} is {:c}'
# print(txt.format('a'))
# txt ='we have {0:d} chickens.'
# print(txt.format(0b101))
# txt = 'we have {:e} chickens.'
# print(txt.format(50000))
# txt = 'we have {:E} chickens.'
# print(txt.format(50000))
# txt = 'The price is {:.2f} dollars.'
# print(txt.format(45))
# txt = 'The price is {:f} dollars.'
# print(txt.format(45))
# x = float('inf')
# txt = 'The price is {:F} dollars.'
# print(txt.format(x))
# txt = 'The price is {:f} dollars.'
# print(txt.format(x))
# x = float('nan')
# txt = 'The price is {:F} dollars.'
# print(txt.format(x))
# txt = 'The price is {:f} dollars.'
# print(txt.format(x))
# # :g		General format
# # :G		General format (using a upper case E for scientific notations)
# txt =  'the octal version of {0} is {0:o}'
# print(txt.format(10))
# txt = 'the hexadecimal version of {0} is {0:x}'
# print(txt.format(255))
# txt = 'the hexadecimal version of {0} is {0:X}'
# print(txt.format(255))
# # :n		Number format
# txt = 'you scored {:%}'
# print(txt.format(0.25))
# txt = 'you scored {:.0%}'
# print(txt.format(0.25))
# :n		Number format

# format_map()	Formats specified values in a string
# person = {'name':'Alice','age':25,'occupation':'engineer'}
# txt = 'my name is {name}, i am {age} years old, and I work as an {occupation}.'
# print(txt.format_map(person))

# Python String index() Method
# txt = 'Hello, welcome to my world.'
# x = txt.index('welcome')
# print(x)
# x = txt.index('e',5,10)
# print(x)
# print(txt.find('q'))
# print(txt.index('q')) # throws error

# Python String isalnum() Method
# txt = 'company12'
# x = txt.isalnum()
# print(x)
# txt = 'company 12'
# x = txt.isalnum()
# print(x)

# Python String isalnum() Method
# txt = 'companyX'
# x = txt.isalpha()
# print(x)
# txt = 'company10'
# x = txt.isalpha()
# print(x)

# Python String isascii() Method
# txt = 'company123'
# x = txt.isascii()
# print(x)
#ASCII reference https://www.w3schools.com/charsets/ref_html_ascii.asp

# txt = '1234'
# x = txt.isdecimal()
# print(x)
# a = '\u0030' #unicode for 0
# b = '\u0047' #unicode for G
# print(a.isdecimal())
# print(b.isdecimal())

# Python String isdigit() Method
# txt = '50800'
# x = txt.isdigit()
# print(x)
# a = "\u0030" #unicode for 0
# b = "\u00B2" #unicode for ²
# print(a.isdigit())
# print(b.isdigit())

# Python String isidentifier() Method
#A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
# txt = 'demo'
# x = txt.isidentifier()
# print(x)
# a = 'myfolder'
# b = 'demo002'
# c = '2bring'
# d = 'my demo'
# print(a.isidentifier())
# print(b.isidentifier())
# print(c.isidentifier())
# print(d.isidentifier())

# Python String islower() Method
# txt = 'hello world!'
# x = txt.islower()
# print(x)
# a = 'Hello world!'
# b = 'hello 123'
# c = 'mynameisPeter'
# print(a.islower())
# print(b.islower())
# print(c.islower())

# Python String isnumeric() Method
# txt = '566643'
# x = txt.isnumeric()
# print(x)
# a = "\u0030" #unicode for 0
# b = "\u00B2" #unicode for &sup2;
# c = "10km2"
# d = "-1"
# e = "1.5"
# print(a.isnumeric())
# print(b.isnumeric())
# print(c.isnumeric())
# print(d.isnumeric())
# print(e.isnumeric())