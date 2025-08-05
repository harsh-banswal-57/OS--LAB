a = [1,2,1,3,4,2,6,6,8,4]

def duplicate(a):
    seen = set()
    dupl = set()
    
    for i in a :
        if i in seen:
            dupl.add(i)
        else: seen.add(i)
    return seen , dupl

seen , dupl = duplicate(a);
print("List :", a, len(a));
print("Unique :", seen);
print("Duplicate :", dupl);
