import random

# ha ezt beállítod, akkor nem a rendszeridőből, hanem a seed-ből állítha elő a számokat (ha ua. a seed, mindig ugyan azt az eredményt kapod)
# random.seed(1234)

# randint: zárt - zárt intervallumon belöül előállít egy véletlen számot
for x in range(8):
    print(random.randint(10, 100), end=' ')
print(end='\n')

# zárt-nyílt intervallumon belül előállít egy 0 és 1 közötti lebegőpontos számot
print(random.random())

# start és end között, zárt-nyílt intervallumon belül veszi a számokat 'step'-esével, és ebből a számsorozatból kiválaszt egy véletlen számot
# randrange(start, end, step)

for x in range(8):
    print(random.randrange(2, 10, 2), end=' ')