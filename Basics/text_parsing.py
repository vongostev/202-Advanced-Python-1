d = {}
funs = 0
modes = []

with open("log.txt", "r") as file:
    for line in file:
        funs += line.count("fun:")

        if -1 < line.find("Found ") < line.find(" modes"):
            modes.append(line[line.find("Found ") + 6:line.find(" modes")])

        if -1 < line.find(' - ') < line.find(' [') < line.find('] '):
            module_start = line.find(' - ') + 3
            module_end = module_start + line[module_start:].find(' ')
            module = line[module_start : module_end]

            type_start = line.find(' [') + 2
            type_end = type_start + line[type_start:].find("]")
            type_ = line[type_start : type_end].replace(' ', '')

            if module in d:
                d[module][type_] += 1
            else:
                d[module] = {
                    'DEBUG': 0,
                    'INFO': 0,
                    'WARNING': 0,
                    'ERROR': 0
                }

print("Dict:", d)
print("Number of 'fun:':", funs)
print("List of modes count:", modes)
