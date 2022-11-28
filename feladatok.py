from random import randint

# 31
print(randint(100, 999))

# 32
print(randint(0, 25))
print(randint(0, 250) / 10)

# 33
print(randint(15, 25))
print(randint(150, 250) / 10)

# 34
print(randint(0, 49) * 2)

# 35
print(randint(20, 40) * 5)

# 37
for n in range(6):
    print(randint(1, 6), end=' ')

print(end='\n')
print('ez\ntöbb\nsorba\nlesz\ntörve')
print('ezek\titt\tpedig\ttabulátorok')

# 39
a:int = randint(10, 50)
b:int = randint(10, 50)
pred:int = int(input(f'{a} + {b} = '))
if pred == a + b: print('így van!')
else: print(f'nope, a két szám összege: {a + b}')