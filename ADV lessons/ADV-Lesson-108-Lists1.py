


cities = ['New York', 'Moscow', 'new dehli', 'Simferopol', 'Toronto']

print(cities)
print(len(cities))

print(cities[0])
print(cities[-1])
print(cities[2].title())
print(cities[2].upper())

cities[2] = 'Tula'
print(cities)


cities.append('Kursk')
cities.append('Yalta')
print(cities)

cities.insert(2, 'Feodosya')
print(cities)

del cities[-1]
print(cities)

cities.remove('Tula')
print(cities)

deleted_city = cities.pop()
print('Delited city is ' + deleted_city)
print(cities)
print('-------------------------------------------------')


cities.sort()
print(cities)

cities.sort(reverse = True)
print(cities)

cities.reverse()
print(cities)
