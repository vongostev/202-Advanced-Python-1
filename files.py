if __name__ == '__main__':

    with open('str.txt', 'w', encoding = 'utf-8') as f:
        for i in range(1, 11):
            print(i, end = " ", file = f)
    
    with open('col.txt', 'w', encoding = 'utf-8') as f:
        for i in range(1, 11):
            print(i, file = f)

    with open('xy.txt', 'w', encoding = 'utf-8') as f:
        for X in range(256, 301):
            print('Number', X, 'set to adress', id(X), file = f)

    with open('xy.txt', encoding = 'utf-8') as f:
        for line in f.readlines():
            line_list = line.split()
            print("|", line_list[1].center(5), "|", line_list[5].center(15), "|")

    with open('log.txt', encoding = 'utf-8') as f:
        DEBUG_counter = 0
        INFO_counter = 0
        WARNING_counter = 0
        ERROR_counter = 0
        content_dictionary = {}
        fun_counter = 0
        for line in f:
            module = line[line.find(' - ') + 3:line.find(' [')]
            if '-' in line:
                if 'DEBUG' in line:
                    DEBUG_counter += 1
                if 'INFO' in line:
                    INFO_counter += 1
                if 'WARNING' in line:
                    WARNING_counter += 1
                if 'ERROR' in line:
                    ERROR_counter += 1
                if module in content_dictionary:
                    DEBUG_counter += content_dictionary[module]['DEBUG']
                    INFO_counter += content_dictionary[module]['INFO']
                    WARNING_counter += content_dictionary[module]['WARNING']
                    ERROR_counter += content_dictionary[module]['ERROR']
                type_amount = {'DEBUG': DEBUG_counter,'INFO': INFO_counter, 'WARNING': WARNING_counter, 'ERROR': ERROR_counter}
                content_dictionary.update({module: type_amount})
                DEBUG_counter = 0
                INFO_counter = 0
                WARNING_counter = 0
                ERROR_counter = 0
                if 'fun:' in line:
                    fun_counter += 1
                
                
print('the amount of "fun:" is ', fun_counter)
print(content_dictionary)


