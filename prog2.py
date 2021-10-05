import datetime as DT
import re

def solving():
    
    with open('log.txt') as file:
        my_lines = list(file)
    
    line = []
    modules = []
    DIWE_counter = []
    fun_counter = 0
    DIWE = ['[DEBUG', '[INFO', '[WARNING]', '[ERROR']
    modes_l = []
    for i in range(len(my_lines)):
        line.append(my_lines[i].split())
        if re.search(r'Found \d{1,10} modes', my_lines[i]):
            modes_l.append(
                re.search(r'Found \d{1,10} modes', my_lines[i])[0].split()[1])
        # skipping useless lines:
        try:
            DT.datetime.strptime(str(line[i][0]), '%Y-%m-%d').date()
        
            #
            # updating modules
            if not(str(line[i][3]) in modules):
                modules.append(str(line[i][3]))
                DIWE_counter.append(['DEBUG', 0, 'INFO', 0, 'WARNING', 0, 'ERROR', 0])
            #
            # sorting DIWE
            for j in range(len(modules)):
                if str(line[i][3]) != modules[j]:
                    continue
                for k in range(4):
                    if str(line[i][4]) == DIWE[k]:
                        DIWE_counter[j][2*k+1] += 1
            #
            if 'fun:' in my_lines[i]:
                fun_counter += 1
        except ValueError:
            continue
    dictionary_list = []
    for i in range(len(modules)):
        dictionary_list.append({modules[i]: {
            'DEBUG': DIWE_counter[i][1], 
            'INFO': DIWE_counter[i][3],
            'WARNING': DIWE_counter[i][5],
            'ERROR': DIWE_counter[i][7]
            }})
    dictionary = {}
    for i in range(len(modules)):
        dictionary = {**dictionary, **dictionary_list[i]}
    
    return (dictionary,fun_counter,modes_l)
if __name__ == '__main__':
    a=solving()
    print('словарь:', a[0])
    print('\nЧисло fun-ов:', a[1])
    print('\nСписок **Found x modes**:', a[2])
