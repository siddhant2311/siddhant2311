# to accept 3 no from key board and find sum and avg
a, b, c = [float(i) for i in input('Enter three nos: ').split(",") ]

tot = a+b+c
avg = tot/3
print('Sum = ', tot)
print('Average = %.3f%', avg)
