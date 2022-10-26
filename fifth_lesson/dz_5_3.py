def compile(name):
    with open(name, mode='r') as file:
        a = {}
        for i in file:
            i.replace(':', "")
            i = i.split()
            a.update({i[0]: i[1]})
    return a
name = "test.txt"
print(compile(name))

