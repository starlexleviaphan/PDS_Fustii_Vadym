import os

def creator(dict, name):
    with open(name, mode='w') as f:
        for key, value in dict.items():
            f.write('{}: {}\n'.format(key, value))


name = 'test.txt'
dict = {1: "one",2: "two", 3: "three"}

creator(dict, name)




