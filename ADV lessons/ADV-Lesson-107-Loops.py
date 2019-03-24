


for x in range(0, 3):
    print('*****')
    print('----------')


for x in range(0, 100 + 1, 2):
    print('Number x = ' + str(x))
    if x == 12:
        break
print('--------------EOF----------------')

x = 9
while True:
    print(x, end='')
    x -= 1
    if x == -1:
        print('\nПоехали!')
        break