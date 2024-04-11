impair = []
pair = []

for i in range(0, 16):
    if i % 2 == 0:
        pair.append(i)
    else:
        impair.append(i)
        
print(impair)
print(pair)