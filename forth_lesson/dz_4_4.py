def summ(a):
    sum = 0
    a = str(a)
    for i in a:
        sum += int(i)
    return sum
print(summ(654))