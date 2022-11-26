#1
f = open('file1.txt', 'w')
for i in range(1, 11):
    str1 = str(i)
    f.write(str1 + ' ')
f.close()

#2
f = open('file2.txt', 'w')
for i in range(1, 11):
    str2 = str(i)
    f.write(str2 + '\n')
f.close()

#3
f = open('file3.txt', 'w')
for i in range(256, 301):
    stri = str(i)
    strid = str(id(i))
    str3 ="Number " + stri + " set to address " + strid
    f.write(str3 + '\n')
f.close()

#4
f = open("file3.txt", "r")
X0 = 'X'
Y0 = 'Y'
X0.center(5, ' ')
Y0.center(13, ' ')
print(f'| {X0} |      {Y0}      |')
for line in f:
    X_start = line.find('Number') + 7
    X_end = line.find('set') - 1
    X = int(line[X_start:X_end])

    Y_start = line.find('address') + 8
    Y_end = len(line) - 1
    Y = int(line[Y_start:Y_end])
    X = str(X)
    Y = str(Y)
    X.center(5, ' ')
    Y.center(15, ' ')

    print(f'|{X}|{Y}|')
f.close()
    
