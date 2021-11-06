from collections import defaultdict

with open("log.txt", "r") as file:
    len1 = len("2021-06-30 18:39:45,180 - Code.pyMMF [")
    len2 = len("2021-06-30 18:39:45,180 - ")
    len3 = len("2021-06-30 18:39:45,180 - Code.pyMMF")
    len4 = len("2021-06-30 18:39:45,180 - Code.pyMMF [DEBUG  ")
    d = {}
    for line in file:
        counter_fun = line.count("fun:")
        if len(line) > len1:
            if line[len1 - 1] == "[":
                d.setdefault(line[len2 : (len3 - 1)].strip(), defaultdict(lambda: 0))
                d[line[len2 : (len3 - 1)].strip()][line[len1:len4].strip()] += 1
    for i in d:
        d[i] = dict(d[i])
    print("Cтрока с заданной подстрокой fun: встречается {} раз".format(counter_fun))
    print(d)
