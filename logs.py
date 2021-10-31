if __name__ == '__main__':
    file = open("log.txt", "r")
    my_dictionary = dict()
    fun_counter = 0
    while True:
        line = file.readline()
        fun_counter += line.count('fun:')
        if not line:
            break
        if (len(line) > 37):
            if (line[37] == '['):
                modul = line[26:37].strip()
                type_message = line[38:45].strip()
                my_dictionary.setdefault(modul, {"DEBUG" : 0, "INFO": 0, "WARNING": 0, "ERROR": 0})
                my_dictionary[modul][type_message] += 1
    file.close()
    print(my_dictionary)
    print(fun_counter)


#{'DEBUG' : 0, 'INFO': 0, 'WARNING': 0, 'ERROR': 0}
#a = dict(zip(Standard_model[0], Standard_model[1]))
#print(Type_message[1][1][0])
#Standard_model = [0, [['DEBUG', 0], ['INFO', 0], ['WARNING', 0], ['ERROR', 0]]]