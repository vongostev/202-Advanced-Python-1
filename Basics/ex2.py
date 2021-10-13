def read_file(file_name):
    with open(file_name, 'r') as f:
        for s in f:
            yield s


def split_log_string(s):
    try:
        # Разбиение строки по шаблону
        s = s.split(' - ')
        s += s.pop(1).split(' [', maxsplit=1)
        s += s.pop(2).split(']  ', maxsplit=1)
        s[2] = s[2].strip()
    except Exception:
        # Если любая из функций разбиения возвращает ошибку,
        # строка не удовлетворяет заданному шаблону, и её надо пропустить
        return []
    else:
        return s


def analyze_logs(file_name):
    output_dict = {}
    fun_count = 0
    modes_list = []
    radial_modes_list = []
    message = []
    for s in read_file(file_name):
        fun_count += int(s.find('fun:') != -1)
        s = split_log_string(s)
        if s != []:
            if s[1] not in output_dict:
                output_dict[s[1]] = {
                    'DEBUG': 0,
                    'INFO': 0,
                    'WARNING': 0,
                    'ERROR': 0}
            output_dict[s[1]][s[2]] += 1
            message = s[3].split()
            if message[0] == 'Found' and message[2] == 'modes':
                modes_list.append(message[1])
            if message[0] == 'Found' and message[2] == 'radial' and message[3] == 'mode(s)':
                radial_modes_list.append(message[1])
    return [output_dict, fun_count, modes_list, radial_modes_list]


if __name__ == '__main__':
    result = analyze_logs('log.txt')
    print(result[0])
    print(f'fun_count: {result[1]}')
    print(f'modes_list: {result[2]}')
    print(f'radial_modes_list: {result[3]}')
