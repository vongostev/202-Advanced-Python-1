{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "70ce4ae6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Task2\n",
    "def read_file(fname):\n",
    "    with open(fname, 'r') as f:\n",
    "        for st in f: yield st\n",
    "\n",
    "def split_str(st):\n",
    "    try:\n",
    "        st = st.split(' - ')\n",
    "        st += st.pop(1).split(' [', maxsplit=1)\n",
    "        st += st.pop(2).split(']  ', maxsplit=1)\n",
    "        st[2] = st[2].strip()\n",
    "    except Exception:\n",
    "        return []\n",
    "    else:\n",
    "        return st\n",
    "\n",
    "def analyze(fname):\n",
    "    m_list = []\n",
    "    radm_list = []\n",
    "     \n",
    "    fun_count = 0\n",
    "    \n",
    "    DIWE = {}\n",
    "    m = []\n",
    "    \n",
    "    for st in read_file(fname):\n",
    "        fun_count += int(s.find('fun:') != -1)\n",
    "        st = split_log_string(st)\n",
    "        if st != []:\n",
    "            if st[1] not in DIWE:\n",
    "                DIWE[st[1]] = {'DEBUG': 0,'INFO': 0,'WARNING': 0,'ERROR': 0}\n",
    "            DIwE[st[1]][st[2]] += 1\n",
    "            m = st[3].split()\n",
    "            \n",
    "            if m[0] == 'Found' and m[2] == 'modes':\n",
    "                m_list.append(m[1])\n",
    "                \n",
    "            if m[0] == 'Found' and m[2] == 'radial' and m[3] == 'mode(s)':\n",
    "                radm_list.append(m[1])\n",
    "                \n",
    "    return [DIWE, fun_count, m_list, radm_list]\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    result = analyze('f.txt')\n",
    "    print(result[0])\n",
    "    print(f'fun_count: {result[1]}')\n",
    "    print(f'm_list: {result[2]}')\n",
    "    print(f'radm_list: {result[3]}')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "70d2dfb9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e35236a3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
