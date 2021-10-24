def read_file(filename):
    with open(filename, 'r') as f:
        for s in f:
            yield s


def driller_file():
    fun_q = 0
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
        if box not in file_dic:
            file_dic[box] = {
                'DEBUG': 0,
                'INFO': 0,
                'WARNING': 0,
                'ERROR': 0}
        file_dic[box][type_message] += 1
    return (file_dic, fun_q)


if __name__ == '__main__':
    s = driller_file()
    print(s[0])
    print(f'fun_q: {s[1]}')
