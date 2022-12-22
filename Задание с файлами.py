def numb1():
    with open("Numb1", "w") as n1:
        for i in range(1,11):
            n1.write(f"{i} ")
def numb2():
    with open("Numb2", "w") as n2:
        for i in range(2,11):
            for j in range(i):
                n2.write(f"{i-1} ")
            n2.write("\n")
def numb3():
    with open("Numb3", "w") as n3:
        for i in range(256, 301):
            n3.write(f"Число {i} установить в адрес {id(i)}\n")
def numb4():
    with open("Numb3", "r") as n4:
        for strk in n4:
            s=strk.split()
            print(f"|{s[1].center(5)}|{s[5].center(15)}|")
def numb5():
    with open("log.txt", "r") as n5:
        d={}
        start={"DEBUG": 0, "INFO": 0, "WARNING": 0, "ERROR": 0}
        k=0
        modes=[]
        for strk in n5:
           if " - " in strk:
               s=strk[strk.find(" - ")+3: strk.find("[")]
               d.setdefault(s, start)
               l=strk[strk.find("[")+1:strk.find("]")]
               if "DEBUG" in l:
                   d[s]["DEBUG"]=d[s]["DEBUG"]+1
               elif "INFO" in l:
                   d[s]["INFO"]=d[s]["INFO"]+1
               elif "WARNING" in l:
                   d[s]["WARNING"]=d[s]["WARNING"]+1
               elif "ERROR" in l:
                   d[s]["ERROR"]=d[s]["ERROR"]+1
               if "fun:" in strk:
                   k+=1
               if "modes" in strk:
                   modes.append(strk[strk.find("ound ")+5: strk.find(" modes")])
    print(d)
    print(f"fun: {k}")
    print(modes)
numb1()
numb2()
numb3()
numb4()
numb5()