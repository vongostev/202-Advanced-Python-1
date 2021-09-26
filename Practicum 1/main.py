from collections import defaultdict

with open('log.txt', 'r') as f:
    fun_count = 0
    my_dict = {}
    for line in f:
        fun_count += line.count('fun:')
        if len(line) > 38:
            if line[37] == '[':
                my_dict.setdefault(line[26:36].rstrip(), defaultdict(lambda: 0))
                my_dict[line[26:36].rstrip()][line[38:45].rstrip()] += 1
    for key in my_dict:
        my_dict[key] = dict(my_dict[key])
    mod_count = len(my_dict)
    mod_list = 'Found ' + str(mod_count) + ' modes'
    print(my_dict)
    print(f'The number of "fun": {fun_count}')
    print(mod_list)
