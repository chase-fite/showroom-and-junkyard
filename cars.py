showroom = {'Camaro'}

showroom.add('G35')
showroom.add('Supra')
showroom.add('GTR')

print(len(showroom))

showroom.add('Camaro')

print(showroom)

showroom.update({'Corvette', 'Mustang'})

print(showroom)

showroom.discard('Mustang')

print(showroom)

junkyard = {'Supra', '3000GT'}

print(showroom.intersection(junkyard))

showroom = showroom.union(junkyard)

print(showroom)

showroom.discard('Corvette')

print(showroom)