def checkDigit(para_checker):
    cnum=0
    posi=0
    notFlag = 0
    size = len(para_checker)
    if not para_checker[size-1:].isdigit(): return False
    for n in para_checker:
        notFlag +=1
        if notFlag==size: break
        value = 0
        if (n.isalpha()):
            value = ord(n)-55
        elif (n.isdigit()):
            value = int(n)
        elif (n == '<'):
            value = 0
        else:
            return False
        if(posi%3 == 0):
            cnum += value*7
        elif(posi%3 == 1):
            cnum += value*3
        elif(posi%3 == 2):
            cnum += value
        posi+=1
    if (int(para_checker[size-1:]) != cnum%10): return False
    else: return True

def checkAlpha(checker):
    if checker=="D<<": return True
    for c in checker:
        if c == " ": continue
        if not c.isalpha(): return False
    return True

def passCode(data):
    #to check type of passport
    if (data[:1] != "P"):
        print("There is another type")
        return "Picture error"

    Ptype = data[1:2]

    #to check country
    country = data[2:5]
    if not checkAlpha(country): return "Picture is error!"
    print("Country is "+country)

    #to keep name 
    name = ""
    i=5
    while True:
        temp = data[i:i+1]
        i+=1
        if (temp == '\n'): break
        if (temp == "<"):
            temp += data[i:i+1]
            i+=1
            if (temp == "<\n" or temp == "<<"):
                break
        name += temp
    name += '\0'
    print("Name is "+name.replace("<", " "))

    #to keep surname
    sur = ""
    while True: 
        temp = data[i:i+1]
        i+=1
        if (i>44 or temp == '\n'): break
        if (temp == "<"):
            temp += data[i:i+1]
            i+=1
            if (temp == "<\n" or temp == "<<"):
                break
        sur += temp
    sur += '\0'
    print("Surname is "+sur.replace("<", " "))

    #to skip line
    if not (data[i-1:i] == '\n'):
        while True:
            ch = data[i:i+1]
            i+=1
            if (ch == '\n'or i>44): break

    #to line 2 keep passport's number
    Pnum = data[i:i+10]
    i+=10
    if not checkDigit(Pnum): return "Picture is error!"
    print("Passport's number is "+Pnum[:len(Pnum)-1])

    #to keep nationality
    nat = data[i:i+3]
    i+=3
    if not checkAlpha(nat): return "Picture is error!"
    print("Nationality is "+nat)

    #to keep dateOfBirth
    birth = data[i:i+7]
    i+=7
    if not checkDigit(birth): return "Picture is error!"
    print("Date of birth is "+birth[:len(birth)-1])

    #to keep sex
    sex = data[i:i+1]
    i+=1
    if not checkAlpha(sex): return "Picture is error!"
    print("Sex is "+sex)
    
    #to keep expiration
    exp = data[i:i+7]
    i+=7
    if not checkDigit(exp): return "Picture is error!"
    print("Expiration is "+exp[:len(exp)-1])

    #to keep Personal number
    per = data[i:i+15]
    i+=15
    if not checkDigit(per): return "Picture is error!"
    print("Persoanl number is "+per.replace("<","")[:len(per)-1])

    #to check digit for positions
    last = Pnum+birth+exp+per
    last += data[i:i+1]
    i+=1
    if not checkDigit(last): return "Picture is error!"
    print("No Problem")
    return "Done"
