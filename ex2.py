# -*- coding: utf-8 -*-
"""
@author: OGL (Egor Liakhov)
"""

def read_file(filename):
    with open(filename, 'r') as f:
        for s in f:
            yield s


def count_mode(s):
    s = s.split('Found ')
    if len(s) < 2:
        return 0
    s = s[1].split('modes')
    if len(s) < 2:
        return 0
    try:
        return int(s[0])
    except(ValueError):
        return 0


def count_radial_mode(s):
    s = s.split('Found ')
    if len(s) < 2:
        return 0
    s = s[1].split('radial mode(s)')
    if len(s) < 2:
        return 0
    try:
        return int(s[0])
    except(ValueError):
        return 0


def solve_problem():
    fun_c = 0
    mode_c = 0
    rad_mode_c = 0
    dictionary = {}
    for s in read_file('log.txt'):
        module = s.split(' - ')
        if len(module) != 2:
            continue
        module = module[1].split(' [')
        if len(module) != 2:
            continue
        type_message = module[1].split('] ')
        if len(type_message) < 2 or not type_message[0].strip() in [
                'DEBUG', 'INFO', 'WARNING', 'ERROR']:
            continue
        module = module[0]
        message = '] '.join(type_message[1:])
        type_message = type_message[0].strip()
        fun_c += 'fun:' in message
        mode_c += count_mode(message)
        rad_mode_c += count_radial_mode(message)
        if module not in dictionary:
            dictionary[module] = {
                'DEBUG': 0,
                'INFO': 0,
                'WARNING': 0,
                'ERROR': 0}
        dictionary[module][type_message] += 1
    return (dictionary, fun_c, mode_c, rad_mode_c)


if __name__ == '__main__':
    s = solve_problem()
    print(s[0])
    print(f'fun_c: {s[1]}')
    print(f'mode_c: {s[2]}')
    print(f'rad_mode_c: {s[3]}')