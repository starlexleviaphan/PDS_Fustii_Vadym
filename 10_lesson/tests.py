

# def divider(a, b):
#     try:
#         c = a / b
#         print(c)
#     except ZeroDivisionError as ex:
#         print(0)
#         print("you can`t divide to zero")
#
# divider(12, 0)

# def list(a, b):
#     try:
#         return a[b]
#     except IndexError as ex:
#         print("there is no such index in list {0}".format(ex))
#         return -1
# a = list([0, 12, 15 ,14 ,48 ,68 ,"sdsdf", [1, 54, 84 ,87, 65]], 5)
# print(a)

class NewExept(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a <= 0 or self.b <= 0:
            return "Input numbers {0} or {1} is not valid".format(self.a, self.b)


def rectangle(a, b):

    if a <= 0 or b <= 0:
        raise NewExept(a, b)
    else: return a * b



a = rectangle(-1, 45)
print(a)