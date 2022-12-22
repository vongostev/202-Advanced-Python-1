f = open('basics 2_2_1.txt', 'w')
for i in range(1, 11):
    f.write(str(i)+' ')
f.close()

f = open('basics 2_2_2.txt', 'w')
for i in range(1, 11):
    f.write(str(i)+'\n')
f.close()

f = open('basics 2_2_3.txt', 'w')
for X in range (256, 300):
    f.write("Number {} set to address {}".format(X, id(X))+'\n')
f.close()

f = open('basics 2_2_3.txt', 'r')
l = list()
for line in f:
    l = line.split()
    print('|'+l[1].center(5)+'|'+l[5].center(15)+'|')
f.close()

