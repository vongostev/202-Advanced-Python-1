import re
d = {}
my_form = r'\d{4}\-\d{2}\-\d{2} \d{2}:\d{2}:\d{2},\d{3} \- (\w*\.\w*) \[(\w*) *\]'
counter2 = 0
modes = []

with open('3sem2.txt', 'r') as f:
    # i=0
    for s in f:
        mode = re.findall(r'f|Found (\d+) modes', s)
        if len(mode) == 1 and mode[0] != '':
            modes.append((int(mode[0])))

        if re.match(r'.*fun:.*', s) != None:
            counter2 += 1

        my_list = re.findall(my_form, s)

        if len(my_list) == 1:
            key1, key2 = my_list[0][0], my_list[0][1]
            #print(key1, key2)
            try:

                d[key1][key2] += 1

            except KeyError:
                d[key1] = {'DEBUG': 0, 'INFO': 0, 'WARNING': 0, 'ERROR': 0}
                d[key1][key2] += 1
        
print(d, "\n'fun:' = ", counter2, '\nmodes = ',
      modes, '\nsum(modes) = ', sum(modes))
