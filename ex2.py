# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 06:01:50 2021

@author: grego
"""


def is_date(inp_str):
    inp = inp_str.split('-')
    if len(inp) == 3:
        for element in inp:
            if element.isdigit() == False:
                return(False)
        return(True)
    else:
        return(False)


def is_type(inp_str):
    types = ('[DEBUG', "[INFO", '[WARNING', '[ERROR')
    if types.count(inp_str):
        return True
    else:
        return False


def test_structure(inp_list):  # date time - module [ type ] message
    if is_date(inp_list[0]) and inp_list[2] == '-'  and is_type(inp_list[4]) and inp_list[5] == ']':
        return True
    return False


def find_modes(line):
    first = line.find('Found') + len("Found") + 1 #if bad first = 5
    last = line.find('modes')-1                   #if bad last = -2
    if first != 5 and last !=-2:
        return line[first:last]


def analyze_file(file, fun):
    dic = {}
    num_of_fun = 0
    list_of_modes = []
    for line in file:
        buff = line.split()
        if find_modes(line): list_of_modes.append(find_modes(line))
        if test_structure(buff):
            divided = [*buff[0:4], '[', buff[4][1:], buff[5:]]
            if dic.get(divided[3], -1) == -1:
                dic[divided[3]] = {'DEBUG': 0,
                                   "INFO": 0, 'WARNING': 0, 'ERROR': 0}
            dic[divided[3]][divided[5]] = dic[divided[3]][divided[5]] + 1
        if line.rfind(fun) > -1:
            num_of_fun += line.rfind(fun) - line.find(fun) + 1
    return((dic, num_of_fun, list_of_modes))


if __name__ == '__main__':

    file = open("log.txt", "r")
    searched_phrase = 'fun:'
    dictionary = analyze_file(file, searched_phrase)
    print("Dictionary:", dictionary[0], '\n')
    print("How many phrases found?", dictionary[1], '\n')
    print("Number of found modes?", dictionary[2])
    file.close()
