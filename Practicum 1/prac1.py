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
    fun_count = 0
    mode_count = 0
    radial_mode_count = 0
    sol_dict = {}
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
        fun_count += 'fun:' in message
        mode_count += count_mode(message)
        radial_mode_count += count_radial_mode(message)
        if module not in sol_dict:
            sol_dict[module] = {
                'DEBUG': 0,
                'INFO': 0,
                'WARNING': 0,
                'ERROR': 0}
        sol_dict[module][type_message] += 1
    return (sol_dict, fun_count, mode_count, radial_mode_count)


if __name__ == '__main__':
    s = solve_problem()
    print(s[0])
    print(f'fun_count: {s[1]}')
    print(f'mode_count: {s[2]}')
    print(f'radial_mode_count: {s[3]}')
