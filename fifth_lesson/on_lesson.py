def last_lines(path, n):
    with open(path, mode='r') as text:
        num = 0
        for i in text:
            num += 1

            print(text[-1])


last_lines("sample.txt", 2)
