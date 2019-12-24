class mrz:
    TD="3"

    def __init__(self,data):
        #to check type of passport
        if (data[:1] != "P"):
            raise ValueError("There is another type")

        #Ptype = data[1:2]

        #to check country
        self.country = data[2:5]
        if not checkAlpha(self.country): raise ValueError("Picture is error!")

        #to keep name 
        self.name = ""
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
            self.name += temp
        self.name = self.name.replace("<"," ")

        #to keep surname
        self.surname = ""
        while True: 
            temp = data[i:i+1]
            i+=1
            if (i>44 or temp == '\n'): break
            if (temp == "<"):
                temp += data[i:i+1]
                i+=1
                if (temp == "<\n" or temp == "<<"):
                    break
            self.surname += temp
        self.surname = self.surname.replace("<"," ")

        #to skip line
        if not (data[i-1:i] == '\n'):
            while True:
                ch = data[i:i+1]
                i+=1
                if (ch == '\n'or i>44): 
                    break

        #to line 2 keep passport's number
        self.passportNum = data[i:i+9]
        i+=10
        self.c_passportNum = data[i-1:i]
        if not checkDigit(self.passportNum, self.c_passportNum): raise ValueError("Picture is error!")

        #to keep nationality
        self.nationality = data[i:i+3]
        i+=3
        if not checkAlpha(self.nationality): raise ValueError("Picture is error!")

        #to keep dateOfBirth
        self.dateOfBirth = data[i:i+6]
        i+=7
        self.c_dateOfBirth = data[i-1:i]
        if not checkDigit(self.dateOfBirth, self.c_dateOfBirth): raise ValueError("Picture is error!")

        #to keep sex
        self.sex = data[i:i+1]
        i+=1
        if not checkAlpha(self.sex): raise ValueError("Picture is error!")
        
        #to keep expiration date of passport
        self.expiry = data[i:i+6]
        i+=7
        self.c_expiry = data[i-1:i]
        if not checkDigit(self.expiry, self.c_expiry): raise ValueError("Picture is error!")

        #to keep Personal number
        self.personalNum = data[i:i+14]
        i+=15
        self.c_personalNum = data[i-1:i]
        if not checkDigit(self.personalNum, self.c_personalNum): raise ValueError("Picture is error!")

        #to check digit for positions
        last = data[i-22:i]+data[i-30:i-23]+data[i-43:i-33]
        self.checksum = data[i:i+1]
        i+=1
        if not checkDigit(last, self.checksum): raise ValueError("Picture is error!")
        print("Done")
    
    def result(self):
        print("Type = "+self.TD)
        print("Name = "+self.name)
        print("Surname = "+self.surname)
        print("Passport number = "+self.passportNum.replace("<",""))
        print("Nationality = "+self.nationality)
        yy = self.dateOfBirth[:2]
        mm = self.dateOfBirth[2:4]
        dd = self.dateOfBirth[4:]
        print("Date of birth = "+yy+" "+mm+" "+dd)
        print("Sex = "+self.sex)
        yy = self.expiry[:2]
        mm = self.expiry[2:4]
        dd = self.expiry[4:]
        print("Expiration date = "+yy+" "+mm+" "+dd)
        print("Personal number = "+self.personalNum.replace("<",""))

def checkDigit(data,checker):
    cnum=0
    posi=0
    size = len(data)
    if not checker.isdigit(): return False
    for n in data:
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
    if (int(checker) == cnum%10): return True
    else:
        return False

def checkAlpha(checker):
    if checker=="D<<": return True
    for c in checker:
        if c == " ": continue
        if not c.isalpha(): return False
    return True

