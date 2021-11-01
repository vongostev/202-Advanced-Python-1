#Task2
def read_file(fname):
    with open(fname, 'r') as f:
        for st in f: yield st

def split_str(st):
    try:
        st = st.split(' - ')
        st += st.pop(1).split(' [', maxsplit=1)
        st += st.pop(2).split(']  ', maxsplit=1)
        st[2] = st[2].strip()
    except Exception:
        return []
    else:
        return st

def analyze(fname):
    m_list = []
    radm_list = []
     
    fun_count = 0
    
    DIWE = {}
    m = []
    
    for st in read_file(fname):
        fun_count += int(st.find('fun:') != -1)
        st = split_str(st)
        if st != []:
            if st[1] not in DIWE:
                DIWE[st[1]] = {'DEBUG': 0,'INFO': 0,'WARNING': 0,'ERROR': 0}
            DIWE[st[1]][st[2]] += 1
            m = st[3].split()
            
            if m[0] == 'Found' and m[2] == 'modes':
                m_list.append(m[1])
                
            if m[0] == 'Found' and m[2] == 'radial' and m[3] == 'mode(s)':
                radm_list.append(m[1])
                
    return [DIWE, fun_count, m_list, radm_list]

if __name__ == '__main__':
    result = analyze('log.txt')
    print(result[0])
    print(f'fun_count: {result[1]}')
    print(f'm_list: {result[2]}')
    print(f'radm_list: {result[3]}')
