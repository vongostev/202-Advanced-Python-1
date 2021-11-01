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


def driller_file():
    fun_q = 0
    mode_q = 0
    r_mode_q = 0
    file_dic = {}
    for s in read_file('log.txt'):
        box = s.split(' - ')
        if len(box) != 2:
            continue
        box = box[1].split(' [')
        if len(box) != 2:
            continue
        type_message = box[1].split('] ')
        if len(type_message) < 2 or not type_message[0].strip() in [
                'DEBUG', 'INFO', 'WARNING', 'ERROR']:
            continue
        box = box[0]
        message = '] '.join(type_message[1:])
        type_message = type_message[0].strip()
        fun_q += 'fun:' in message
        mode_q += count_mode(message)
        r_mode_q += count_radial_mode(message)
        if box not in file_dic:
            file_dic[box] = {
                'DEBUG': 0,
                'INFO': 0,
                'WARNING': 0,
                'ERROR': 0}
        file_dic[box][type_message] += 1
    return (file_dic, fun_q, mode_q, r_mode_q)


if __name__ == '__main__':
    s = driller_file()
    print(s[0])
    print(f'fun_q: {s[1]}')
    print(f'mode_q: {s[2]}')
    print(f'r_mode_q: {s[3]}')
