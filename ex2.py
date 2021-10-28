from collections import defaultdict


with open('log.txt', "r") as file:
    #print(len('2021-06-30 18:39:45,181 -'))
    #print(len('2021-06-30 18:39:45,180 - Code.pyMMF [DEBUG  '))
    #print(len('2021-06-30 18:39:45,180 - Code.pyMMF ['))
    d = dict()
    fun_counter = 0
    
    
    for line in file:
        fun_counter += line.count('fun:')
        if len(line) > 37:
            if line[37] == '[':
                d.setdefault(line[26:37].strip(), defaultdict(lambda: 0))
                d[line[26:37].strip()][line[38:45].strip()] += 1
    
    for i in d:
        d[i] = dict(d[i])
    print(d)
    print('Количество подстрок "fun" = ' + str(fun_counter))
    file.close() 
    