

def is_unical(list):
    flag = True
    for i in range(len(list) - 1):
        for j in range(i+1, len( list)):
            if flag == False:
                break
            if list[i] == list[j]:
                flag = False
                break

    return flag

list = [1, 5, 7, 87, 98, 65, 15, 78, 6]
char = 125

try:
    if is_unical(char):
        print("Is unical")
    else: print("Isn`t unical")
except NameError as ex:
    print("Name is not defined, {}".format(ex))
except TypeError as ex:
    print("Type error, {}".format(ex))
except Exception as ex:
    print("Some error, {}".format(ex))