li = [1, 2, 3, 4, 5, 6, 7, 8]

def group(li, x):
    a = [li[i:i+x] for i in range(0, len(li), x)]
    return a



print(group(li, 3))