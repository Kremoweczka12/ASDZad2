
def countoccurence(word):
    res = []
    word = sorted(word)
    word = list(word)
    for i in word:
        if i not in res:
            res.append(i)
    dict = []
    lista1 = []
    lista2 = []
    for l in res:
        n=0
        for letter in word:
            if letter==l:
                n+=1
        lista1.append(l)
        lista2.append(n)
    dict.append(lista1)
    dict.append(lista2)
    return dict

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def heapify(i,list):
    l=left(i)
    r=right(i)
    if l<len(list[0]) and list[1][l] > list[1][i]:
        largest = l
    else:
        largest = i
    if r < len(list[0]) and list[1][r] > list[1][largest]:
        largest = r
    if largest != i:
        list[0][i], list[0][largest] = list[0][largest], list[0][i]
        list[1][i], list[1][largest] = list[1][largest], list[1][i]
        heapify(largest, list)

def buildheap(list):
    i = len(list[0])//2
    while i >= 0:
        heapify(i, list)
        i-=1


def findMIN(list):
    key = list[0][0]
    value = list[1][0]
    i=0
    indeks = 0
    for element in list[1]:
        if element <= value:
            key=list[0][i]
            value=element
            indeks=i
        i+=1
    del list[0][indeks]
    del list[1][indeks]
    buildheap(list)
    return key, value

def instert(list, key, value):
    list[0].append(key)
    list[1].append(value)
    buildheap(list)

def compress(sentence):
    dict = countoccurence(sentence)
    lista2 = {}
    while len(dict[0])!=1:
        key1, value1 = findMIN(dict)
        key2, value2 = findMIN(dict)
        if value1<value2:
            name = key1+key2
            lista2[key1] = value1
            lista2[key2] = value2
            lista2[name] = value1 + value2
        else:
            name = key2+key1
            lista2[key2] = value2
            lista2[key1] = value1
            lista2[name] = value1 + value2
        instert(dict, name, value1+value2)
    return createdictionary(list(lista2.keys()))


def compress2(dict):
    lista2 = {}
    while len(dict[0])!=1:
        key1, value1 = findMIN(dict)
        key2, value2 = findMIN(dict)
        if value1<value2:
            name = key1+key2
            lista2[key1] = value1
            lista2[key2] = value2
            lista2[name] = value1 + value2
        else:
            name = key2+key1
            lista2[key2] = value2
            lista2[key1] = value1
            lista2[name] = value1 + value2
        instert(dict, name, value1+value2)
    return createdictionary(list(lista2.keys()))


def encodeletter(letter, listka1):
    l=letter
    code = ""
    for key in listka1:
        if key != letter:
            if key.startswith(letter):
                letter = key
                code+="0"
            elif key.endswith(letter):
                letter = key
                code+="1"
    return code[::-1]

def createdictionary(listka1):
    dict = {}
    for letter in listka1:
        if len(letter)==1:
            dict[letter] = encodeletter(letter,listka1)
    return dict

from pathlib import Path

def codeall(path):
    txt = Path(path).read_text(encoding="utf-8")
    length = len(txt)
    #txt = txt + txt[-1]*(len(txt) % 8)
    dict = compress(txt)
    txt = list(txt)
    for elem in txt:
        txt[txt.index(elem)] = dict[elem]
    arr=''
    for c in txt:
        arr+=c
    i=9
    while i < len(arr):
        arr = arr[0:i]+" "+arr[i:]
        i+=9
    arr=arr.split(" ")
    ascii_string = ''
    f = open("coded" + path, "w+", encoding="utf-8")
    f.write(str(dict)+"\n")
    f.write(str(length) + "\n")
    for elem in arr:
        a = int(elem, 2)
        ascii_character = chr(a)
        f.write(ascii_character)
        ascii_string += ascii_character
    f.close()


#codeall("sample.txt")
print(compress("go go gophers"))



