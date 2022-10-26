def letter(a):
    stat = {}
    a = a.lower()
    for i in a:
        if i not in stat:
            stat.update({i: 1})
        else:
            stat[i] = stat.get(i) + 1
    sorted_dict = sorted(stat.items(), key=lambda x: x[1], reverse=True)

    return sorted_dict[0][0]

print(letter("Adasdaassssssspokjdfgdfgdfgfffffffffgljk"))


