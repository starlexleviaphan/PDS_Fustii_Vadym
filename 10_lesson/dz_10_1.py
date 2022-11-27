
def month(num):
    a = ["January", "February", "March", "April", "May", "June", "July", "August",
         "September", "October", "November", "December"]
    try:
        name = a[num - 1]
        return name
    except IndexError as ex:
        print("enter valid month number, {0}".format(ex))
    except TypeError as ex:
        print("enter number, not letter or smt, {0}".format((ex)))
    except Exception as ex:
        print("You did something wrong :)")

print(month())