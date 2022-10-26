a = []
for i in range(101):
    if i == 0:
        a.append(0)
    else:
        a.append(a[i - 1] + 1)


b = [i for i in a if i % 3 == 0] # нуль залишив спеціально, так як нуль кратний всім числам

print(b)