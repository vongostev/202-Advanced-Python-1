#Задание номер 1

with open('test1.txt', 'w+', encoding='utf-8') as f:
    for x in (str(y) for y in range(1, 11)): f.write(x + ' ') 

#Задание номер 2

with open('test2.txt', 'w+', encoding='utf-8') as f:
    for x in (str(y) for y in range(1, 11)): f.write(x + '\n')                               


#Задание номер 3

with open('test3.txt', 'w+', encoding='utf-8') as f:
    for i in range(255, 301):
        f.write("Number " + str(i) + " set to address " + str(id(i)) + '\n')

#Задание номер 4

with open("test3.txt", "r", encoding='utf-8') as f:
    s = f.read()
    l = s.split()
    num = [line for line in l if line.isnumeric()]
    x = num[0::2]
    y = num[1::2]
    for i in range(len(x)):
        print(f"| {x[i].center(5)} | {y[i]:15} |")

#Задание номер 5

with open('log.txt', 'r', encoding='utf-8') as f:
    count_debug, count_info, count_warning, count_error, count_fun = 0, 0, 0, 0, 0
    line_dict = {}
    modes = []
    for line in f:
        module = line[line.find(' - ') + 3:line.find('[') - 1]
        if '-' in line:
            if 'DEBUG' in line:
                count_debug += 1
            if 'INFO' in line:
                count_info += 1
            if 'WARNING' in line:
                count_warning += 1
            if 'ERROR' in line:
                count_error += 1
            if 'fun: ' in line:
                count_fun += 1
            if 'modes' in line:
                modes.append(line[(line.find('ound ') + 5):(line.find(' modes'))])
            amount = {'DEBUG': count_debug, 'INFO': count_info, 'WARNING': count_warning, 'ERROR': count_error}
            line_dict.update({module : amount})


    print(line_dict)
    print(count_fun)
    print(modes)
