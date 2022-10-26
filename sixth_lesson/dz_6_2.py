def descend(n):
    if n != 0:
        print(n)
        descend(n - 1)
descend(100)