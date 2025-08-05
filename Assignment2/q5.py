def sortstr(file):
    sorted_file = sorted(file, key = len)    
    return sorted_file
file = ["hello", "Its", "me", "by", "Adele"]
print(sortstr(file))

def extsort(file):
    sorted_file = sorted(file, key = lambda x: x.split('.')[-1])
    return sorted_file
file = ["hello.txt", "Its.py", "me.java", "by.cpp", "Adele.py"]
print(extsort(file))