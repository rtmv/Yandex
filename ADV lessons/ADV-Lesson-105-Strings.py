mystring = 'Bla bla bla'

name = 'vasya pupkin'
print(name)
print(name.title())

name = 'mr vASya pupkin'
print(name.title())
print(name.upper())
print(name.lower())

print('Privet stroka nomer 1\nPrivet stroka N2\n\nPrivet stroka N3\n\n')
print('Messages:\n\tMessage1\n\tMessage2\n\tMessage3\nEND')
print('Lower name: ' + name.lower())

a = '  . dadya vasya . ,      '
print(a)
print(a.rstrip())
print(a.lstrip())
print(a.strip())
a = '... dadya vasya   ....    '
a = a.strip('.')
a = a.strip(' ')
a = a.strip('.')
a = a.strip(' ')
print(a)