from collections import defaultdict

with open('log.txt', 'r') as f:
    d = {}
    l = []
    count = 0
    for row in f:
        if len(row) > 38:
            if row[37] == '[':
                d.setdefault(row[26:36].rstrip(), defaultdict(lambda: 0))
                d[row[26:36].rstrip()][row[38:45].rstrip()] += 1
            if (row[48:53] == 'Found') and (row[54:].split()[1] == 'modes'):
                l.append(row[54:].split()[0])
        count += row.count('fun:')
    print('The number of "fun": {}'.format(count))
    for k in d:
        d[k] = dict(d[k])
    print(d)
    print(l)
