#Python String encode() Method
# txt = "My name is Ståle"
# x = txt.encode()
# print(x)
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
# The capitalize() method returns a string where the first character is upper case, and the rest is lower case.
# txt = 'python is FUN!'
# x = txt.capitalize()
# print(x)
# txt = "36 is my age."
# x = txt.capitalize()
# print (x)

# Python String casefold() Method
# Converts string into lower case
# txt = "Hello, And Welcome To My World!"
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
# # The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
# # Example of characters that are not alphanumeric: (space)!#%&? etc.
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

#Python String isprintable() Method
# txt = 'hello! are you #1?'
# x = txt.isprintable()
# print(x)
# Example of none printable character can be carriage return and line feed.
# txt = "Hello!\nAre you #1?"
# x = txt.isprintable()
# print(x)

#Python String isspace() Method
# txt = "   "
# x = txt.isspace()
# print(x)
# txt = "   s   "
# x = txt.isspace()
# print(x)

#Python String istitle() Method
#Check if each word start with an upper case letter
# txt = "Hello, And Welcome To My World!"
# x = txt.istitle()
# print(x)
# a = "HELLO, AND WELCOME TO MY WORLD"
# b = "Hello"
# c = "22 Names"
# d = "This Is %'!?"
# print(a.istitle())
# print(b.istitle())
# print(c.istitle())
# print(d.istitle())

# Python String isupper() Method
# txt = "THIS IS NOW!"
# x = txt.isupper()
# print(x)
# a = "Hello World!"
# b = "hello 123"
# c = "MY NAME IS PETER"
# print(a.isupper())
# print(b.isupper())
# print(c.isupper())

# Python String join() Method
# Join all items in a tuple into a string, using a hash character as separator:
# myTuple = ("John", "Peter", "Vicky")
# x = "#".join(myTuple)
# print(x)
# myDict = {"name": "John", "country": "Norway"}
# mySeparator = "TEST"
# x = mySeparator.join(myDict)
# print(x)

# Python String ljust() Method
# Return a 20 characters long, left justified version of the word "banana":
# txt = "banana"
# x = txt.ljust(20)
# print(x, "is my favorite fruit.")
# Note: In the result, there are actually 14 whitespaces to the right of the word banana.
# txt = "banana"
# x = txt.ljust(20, "O")
# print(x)

# Python String lower() Method
# txt = "Hello my FRIENDS"
# x = txt.lower()
# print(x)

# Python String lstrip() Method
# Remove spaces to the left of the string:
# txt = "     banana     "
# x = txt.lstrip()
# print("of all fruits", x, "is my favorite")
# Remove the leading characters:
# txt = ",,,,,ssaaww.....banana"
# x = txt.lstrip(",.asw")
# print(x)

# Python String maketrans() Method
# txt = "Hello Sam!"
# mytable = str.maketrans("S", "P")
# print(txt.translate(mytable))
# txt = "Hi Sam!"
# x = "mSa"
# y = "eJo"
# mytable = str.maketrans(x, y)
# print(txt.translate(mytable))
# The third parameter in the mapping table describes characters that you want to remove from the string:
# txt = "Good night Sam!"
# x = "mSa"
# y = "eJo"
# z = "odnght"
# mytable = str.maketrans(x, y, z)
# print(txt.translate(mytable))
# The maketrans() method itself returns a dictionary describing each replacement, in unicode:
# txt = "Good night Sam!"
# x = "mSa"
# y = "eJo"
# z = "odnght"
# print(str.maketrans(x, y, z))

# Python String partition() Method
# txt = "I could eat bananas all day"
# x = txt.partition("bananas")
# print(x)
# txt = "I could eat bananas all day"
# x = txt.partition("apples")
# print(x)

# Python String replace() Method
# txt = "I like bananas"
# x = txt.replace("bananas", "apples")
# print(x)
# txt = "one one was a race horse, two two was one too."
# x = txt.replace("one", "three")
# print(x)
# txt = "one one was a race horse, two two was one too."
# x = txt.replace("one", "three", 2)
# print(x)

# Python String rfind() Method
# txt = "Mi casa, su casa."
# x = txt.rfind("casa")
# print(x)
# txt = "Hello, welcome to my world."
# x = txt.rfind("e", 5, 10)
# print(x)
# If the value is not found, the rfind() method returns -1, but the rindex() method will raise an exception:
# txt = "Hello, welcome to my world."
# print(txt.rfind("q"))
# print(txt.rindex("q"))

# Python String rindex() Method
# txt = "Mi casa, su casa."
# x = txt.rindex("casa")
# print(x)
# txt = "Hello, welcome to my world."
# x = txt.rindex("e", 5, 10)
# print(x)
# If the value is not found, the rfind() method returns -1, but the rindex() method will raise an exception:
# txt = "Hello, welcome to my world."
# print(txt.rfind("q"))
# print(txt.rindex("q"))

# Python String rjust() Method
# txt = "banana"
# x = txt.rjust(20)
# print(x, "is my favorite fruit.")
# txt = "banana"
# x = txt.rjust(20, "O")
# print(x)

# Python String rpartition() Method
# txt = "I could eat bananas all day, bananas are my favorite fruit"
# x = txt.rpartition("bananas")
# print(x)
# txt = "I could eat bananas all day, bananas are my favorite fruit"
# x = txt.rpartition("apples")
# print(x)

# Python String rsplit() Method
# txt = "apple, banana, cherry"
# x = txt.rsplit(", ")
# print(x)
# txt = "apple, banana, cherry"
# # setting the maxsplit parameter to 1, will return a list with 2 elements!
# x = txt.rsplit(", ", 1)
# print(x)

# Python String rstrip() Method
# txt = "     banana     "
# x = txt.rstrip()
# print("of all fruits", x, "is my favorite")
# txt = "banana,,,,,ssqqqww....."
# x = txt.rstrip(",.qsw")
# print(x)

# Python String split() Method
# Split a string into a list where each word is a list item:
# txt = "welcome to the jungle"
# x = txt.split()
# print(x)
# txt = "hello, my name is Peter, I am 26 years old"
# x = txt.split(", ")
# print(x)
# txt = "apple#banana#cherry#orange"
# x = txt.split("#")
# print(x)
# txt = "apple#banana#cherry#orange"
# # setting the maxsplit parameter to 1, will return a list with 2 elements!
# x = txt.split("#", 1)
# print(x)

# Python String splitlines() Method
# txt = "Thank you for the music\nWelcome to the jungle"
# x = txt.splitlines()
# print(x)
# Split the string, but keep the line breaks:
# txt = "Thank you for the music\nWelcome to the jungle"
# x = txt.splitlines(True)
# print(x)

# Python String startswith() Method
# txt = "Hello, welcome to my world."
# x = txt.startswith("Hello")
# print(x)
# txt = "Hello, welcome to my world."
# x = txt.startswith("wel", 7, 20)
# print(x)

# Python String strip() Method
# txt = "     banana     "
# x = txt.strip()
# print("of all fruits", x, "is my favorite")
# characters	Optional. A set of characters to remove as leading/trailing characters
# txt = ",,,,,rrttgg.....banana....rrr"
# x = txt.strip(",.grt")
# print(x)

# Python String swapcase() Method
# txt = "Hello My Name Is PETER"
# x = txt.swapcase()
# print(x)

# Python String title() Method
# txt = "Welcome to my world"
# x = txt.title()
# print(x)
# txt = "Welcome to my 2nd world"
# x = txt.title()
# print(x)
# txt = "hello b2b2b2 and 3g3g3g"
# x = txt.title()
# print(x)

# Python String translate() Method
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
# mydict = {83:  80}
# txt = "Hello Sam!"
# print(txt.translate(mydict))
# txt = "Hello Sam!"
# mytable = str.maketrans("S", "P")
# print(txt.translate(mytable))
# txt = "Hi Sam!"
# x = "mSa"
# y = "eJo"
# mytable = str.maketrans(x, y)
# print(txt.translate(mytable))
# txt = "Good night Sam!"
# x = "mSa"
# y = "eJo"
# z = "odnght"
# mytable = str.maketrans(x, y, z)
# print(txt.translate(mytable))
# txt = "Good night Sam!"
# mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
# print(txt.translate(mydict))

# Python String upper() Method
# txt = "Hello my friends"
# x = txt.upper()
# print(x)

# Python String zfill() Method
# txt = "50"
# x = txt.zfill(10)
# print(x)
# a = "hello"
# b = "welcome to the jungle"
# c = "10.000"
# print(a.zfill(10))
# print(b.zfill(10))
# print(c.zfill(10))