def seasons(month):
    if 1 <= month <= 2 or month == 12:
        return "winter"
    elif 3 <= month <= 5:
        return "spring"
    elif 6 <= month <= 8:
        return "summer"
    elif 9 <= month <= 11:
        return "fall"
    else: return "wrong month number"

print(seasons(40))