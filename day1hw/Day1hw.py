def counterstr(str_a):
    upper_num = 0 #statistic upper letters
    lower_num = 0 #statistic lower letters
    not_num = 0 #not for needs, just for else

    for i in str_a:
        if i.isupper():
            upper_num += 1
        elif i.islower():
            lower_num += 1
        else:
            not_num += 1

    print("Task 3")
    print("Uppercase are: %d" %upper_num)
    print("Lowercase are: %d" %lower_num)

str_a = "Hello World"
counterstr(str_a)

encode_txt = "encode.txt" # url of morsecode file

def GetFile(path): # read morsecode dictionary file and return
    dic = dict()
    txt = ""
    with open(path, "r") as fp:
        txt = fp.read()
        lis_data = list(set(txt.split("\n")))
        if "" in lis_data:
            lis_data.remove("")
        for datas in lis_data:
            key, data = datas.split(" ")
            dic[key] = data
    return dic

def MorseEncode(target):
    dic = GetFile(encode_txt) # get the dictionary of Morsecode
    result = ""
    for i in target:
        if i in dic.keys():
            result += " " + dic[i]
        else:
            result += " "
    return result

print("Task 1")
print (MorseEncode(str_a))

def unique_letters(str_a):
    letter_num = 0
    no_num = 0
    str_a1 = str_a.upper() #lower letters to upper
    for i in str_a1:
        if i.isalpha(): #if it is letter in this place
            letter_num += 1
            if i.islower():
                i.upper()
            else: no_num +=1
        else: i.replace('"','') #if it is symbol, remove " at first
    str_b1 = str_a1.replace(' ','') #then remove blank
    list1 = list(str_b1)
    return list1,letter_num

str_b = 'Hello World'
print("Task 2")
print(unique_letters(str_b))
