class NewExept(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a <= 0 or self.b <= 0:
            return "Input numbers {0} or {1} is not valid, you need to put right numbers".format(self.a, self.b)


def rectangle(a, b):

    if a <= 0 or b <= 0:
        raise NewExept(a, b)
    else: return a * b



a = rectangle(-1, 45)
print(a)