def sortdic(t): 
    #  key = lambda item : item[1])
    new_dic = dict(sorted(t.items()))
    return new_dic 


t = {3: "r", 2: "a", 4:"s", 5 : "h", 1:"h", 6:"k"};
new_dic = sortdic(t)
print(new_dic)