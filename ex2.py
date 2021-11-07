def read_file(filename):
  with open(filename, 'r') as f:
    for s in f:
      yield s


def split_string(str):
  try:
    str = str.split(' - ')
    str += str.pop(1).split(' [', 1)
    str += str.pop(2).split(']  ', 1)
    str[2] = str[2].strip()
  except Exception:
    return []
  else:
    return str


def solve_log(filename):
  solve_dict = {}
  fun_count = 0
  for str in read_file(filename):
    fun_count += int(str.find('fun:') != -1)
    str = split_string(str)
    if str != []:
      if str[1] not in solve_dict:
        solve_dict[str[1]] = {
          'DEBUG': 0,
          'INFO': 0,
          'WARNING': 0,
          'ERROR': 0}
      solve_dict[str[1]][str[2]] += 1
  return (solve_dict, fun_count)


if __name__ == '__main__':
  solution = solve_log('log.txt')
  print(solution[0])
  print(f'fun_count: {solution[1]}')