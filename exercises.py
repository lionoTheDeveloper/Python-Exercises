print('hello')
txt = 'my name is ståle'
print(txt.encode(encoding='ascii',errors='backslashreplace'))
print(txt.encode(encoding='ascii',errors='ignore'))
print(txt.encode(encoding='ascii',errors='namereplace'))
print(txt.encode(encoding='ascii',errors='replace'))
print(txt.encode(encoding='ascii',errors='xmlcharrefreplace'))