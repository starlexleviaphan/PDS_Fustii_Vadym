def combine(*args):
    a = {}
    for i in args:
        a |= i
    return a, type(args)

print(combine({1: "winter", 2: "spring", 3: "summer", 4: "fall"}, {5: "Bob", 6: "Scarlett", 7: "Jessica", 8: "Elton"}, {9: "brown", 10: "yellow", 11: "red", 12: "key"}))