class RepeatException(Exception):
    enter = False


key = []
string = "\0"

def fill (t):
    global string
    global key
    enter_text = True
    enter = False
    while(not enter):
        ls = len(string)
        lk = len(key)
        print('Введите ключ')
        key = input().split()
        enter = check()
    if (enter_text):
        match t:
            case "1": 
                print('Введите строку')
                string = input()
                enter_text = False
            case "2":
                stringm = []
                print('Введите строку')
                string = input()
                enter_text = False
                print('Введите Кол-во символов')
                item = int(input())
                for i in range (0, len(string), item):
                    stringm.append(string[i:i+item])
                return stringm
            case "3":
                stringm = []
                print('Введите строку')
                string = input()
                enter_text = False
                stringm = string.split()
                return stringm
                


def check ():
    k = [int(item) for item in key]
    for i in range (max(k) + 1):
        if (k.count(i) > 1 or k.count(i) < 1):
            print("Ключ не корректен")
            return False
    else:
        return True


def Encryption (s, k):
    if (len(s) % len(k) != 0):
        if (isinstance(s,str)):
            s = s + "\0"*(len(k) - (len(s) % len(k)))
        if (isinstance(s,list)):
            for i in range (len(k) - (len(s) % len(k))):
                s.append("\0")
    print(s)
    str_new = [0]*len(s)
    p = 0
    for i in range (len(s)):
        str_new[int(k[i%len(k)]) + (p)] = s[i]
        if ((i+1)%len(k) == 0):
            p += len(k)
    return str_new

def prt (str):
    print("".join(str))

def prt_word (str):
    print(" ".join(str))

print('Шифровать - 1')
print('Разшифровать - 2')
s = int(input())
match s:
    case 1:
        print('По буквам - 1')
        print('По группе букв - 2')
        print('По словам - 3')
        cs = input()
        match cs:
            case "1":
                fill(cs)
                str2 = Encryption(string, key)
                prt(str2)


            case "2":
                strr = fill(cs)
                str2 = Encryption(strr, key)
                prt(str2)
            case "3":
                strr = fill(cs)
                str2 = Encryption(strr, key)
                prt_word(str2)
    case 2:
        print('По буквам - 1')
        print('По группе букв - 2')
        print('По словам - 3')
        cs = input()
        match cs:
            case "1":
                print(1)

            case "2":
                print(1)

            case "3":
                print(1)

