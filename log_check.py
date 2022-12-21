import re


def log_read():
    with open('log.txt', 'r') as f:
        d = {}
        fun = 0
        modes = []
        for line in f:
            # проверка на соответствие шаблону data
            # 2021-06-30 18:39:45,180 
            # yyyy-mm-dd hh:mm:ss,ttt
            if (line[:4] == "2021" and
                line[4] == "-" and
                (line[5:7] >= "01" and line[5:7] <= "12") and
                line[7] == "-" and
                (line[8:10] >= "01" and line[8:10] <= "31") and
                line[10] == " " and
                (line[11:13] >= "00" and line[10:13] <= "23") and
                line[13] == ":" and
                (line[14:16] >= "00" and line[14:16] <= "59") and
                line[16] == ":" and
                (line[17:19] >= "00" and line[17:19] <= "59") and
                line[19] == "," and
                (line[20:23] >= "000" and line[20:23] <= "999")):

                    # module
                    if line[23:26] == " - ":
                        s = line[26:line.find("[") - 1]
                        d.setdefault(s, {})
                        d[s].setdefault("DEBUG", 0)
                        d[s].setdefault("INFO", 0)
                        d[s].setdefault("WARNING", 0)
                        d[s].setdefault("ERROR", 0)

                    # type
                    type_m = line[line.find("[")+1:line.find("]")].strip()
                    d[s][type_m] += 1

            # fun:
            if line.find("fun:") != -1:
                fun += 1

            # modes
            pattern = 'Found [0-9]+ modes'
            result = re.search(pattern, line)
            if result:
                modes.append(result.group()[6:-6])

    print(d, '\n')
    print("Подстрока 'fun:' встречается в логе", fun, "раз(а).", '\n')
    print(modes)


if __name__ == '__main__':
#    print('Dear LGTM, please, analyse me')
    log_read()
