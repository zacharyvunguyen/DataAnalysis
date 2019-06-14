flintstones = ['fred','wilma','pebbles','dino']

newNames = []

for name in flintstones:
    newNames.append(name.upper())

print(newNames)

newNames = [name.upper() for name in flintstones if name=='dino'] #list comprehension

print(newNames)
