from collections import defaultdict

if __name__ == '__main__':

    parsedic = {}
    modelist = []
    fun = 0

    try:
        with open('log.txt', 'r') as file:
            try:
                for line in file:
                    if len(line) > 38:
                        if line[37] == '[':
                            parsedic.setdefault(line[26:36].rstrip(), defaultdict(lambda: 0))
                            parsedic[line[26:36].rstrip()][line[38:45].rstrip()] += 1
                        if (line[48:53] == 'Found') and (line[54:].split()[1] == 'modes'):
                            modelist.append(line[54:].split()[0])
                    fun += line.count('fun:')
                print('Fun: {}'.format(fun))
            except UnicodeError as ex0:
                print(ex0)
            except Exception as ex:
                print(ex)
            finally:
                file.close()
            for k in parsedic:
                parsedic[k] = dict(parsedic[k])
            print(parsedic)
            print(modelist)
    except (FileNotFoundError, PermissionError) as e:
        print(e)
