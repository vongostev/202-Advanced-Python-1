import datetime as DT
import re
import requests

url = 'https://raw.githubusercontent.com/vongostev/202-Advanced-Python-1/main/Practicum%201/log.txt'
response = requests.get(url)
my_lines = list(response.text.splitlines())

# print(response.text)
# with open('F:/GitHub/prog-1/202-Advanced-Python-1/Practicum 1/log.txt') as file:
#     my_lines = list(file)

useless_lines_counter = 0
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
        date = DT.datetime.strptime(str(line[i][0]), '%Y-%m-%d').date()
    except:
        continue
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
dictionary_list = []
for i in range(len(modules)):
    dictionary_list.append({modules[i]: {'DEBUG': DIWE_counter[i][1], 'INFO': DIWE_counter[i][3],
                                         'WARNING': DIWE_counter[i][5], 'ERROR': DIWE_counter[i][7]}})
dictionary = {}

for i in range(len(modules)):
    dictionary = {**dictionary, **dictionary_list[i]}
print('Странный словарь:', dictionary)
print('\nЧисло fun-ов:', fun_counter)
print('\nСписок **Found x modes**:', modes_l)
