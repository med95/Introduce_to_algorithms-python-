#an original edition from introduce to algorithms(v3) pseudocode
def insertionSort1(a):
    alist = a.copy()
    for j in range(0,len(alist)):
        key = alist[j]
        i = j - 1
        while i>=0 and alist[i]>key:
            alist[i+1]=alist[i]
            i = i - 1
            alist[i+1] = key
    return alist

#a more modern edition

def insertionSort2(a):
    alist = a.copy()
    for j in range(len(alist)):
        for i in range(j):
            if  alist[i]>alist[j]:
                alist[i],alist[j] = alist[j],alist[i]
    return alist

if __name__ == '__main__':    
    a = [5,2,4,6,1,3]
    print(insertionSort1(a))
    print(insertionSort2(a))