from collections import defaultdict

with open('log.txt', 'r') as f:
    fun_count = 0
    my_dict = {}
    mod_list = []
    for line in f:
        fun_count += line.count('fun:')
        if len(line) > 38:
            if line[37] == '[':
                my_dict.setdefault(line[26:36].rstrip(), defaultdict(lambda: 0))
                my_dict[line[26:36].rstrip()][line[38:45].rstrip()] += 1
            if line[48:53] == 'Found':
                if line[54:].split()[1] == 'modes':
                    mod_list.append(line[54:].split()[0])
    for key in my_dict:
        my_dict[key] = dict(my_dict[key])
    print(my_dict)
    print(f'The number of "fun": {fun_count}')
    print(mod_list)
