file = open("testfile", "r")
count = 0
hcount = 0
for line in file:
    if line.startswith('h'):
        hcount += 1

    else:
        print(" no letter with h")
print(hcount)