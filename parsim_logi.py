import pyparsing as pp

"""with open('1.txt', 'w') as f:
    for i in range(1, 11):
        f.write(f"{i} ")
        
with open('2.txt', 'w') as f:
    for i in range(1, 11):
        f.write(f"{i}\n")
        
with open('3.txt', 'w') as f:
    for i in range(256, 301):
        f.write(f"Number {i} set to address {id(i)}\n")
        
with open('3.txt', 'r') as f:
    for line in f:
        x = int(line[7:10])
        y = int(line[26:])
        print(f"|{x:^5}|{y:^15}|") """
        
with open('log.txt', 'r') as f:
    d = {}
    fun_count = 0
    for line in f:
        try:
            if 'fun:' in line:
                fun_count +=1
            date = pp.Word(pp.nums + '-')
            module = pp.Word(pp.alphanums + '.')
            mess_type =  pp.Word(pp.alphas)
            message = line[48:]
            message = message[:-1:]
            parsim = (date + pp.Suppress(pp.Word(pp.nums + ':' + ',')) + pp.Suppress('-') 
                      + module + pp.Suppress('[') + mess_type 
                      + pp.Suppress(']') + message)
            plist = parsim.parseString(line).asList()
            #print(plist)
            if not plist[1] in d:
                d[plist[1]] = {}
            if not plist[2] in d[plist[1]]:
                d[plist[1]][plist[2]] = 0
            d[plist[1]][plist[2]] += 1   
        except:
            continue
    print(d)
    print(fun_count)
        
        
        