
def insertionSort(a):
    alist = a.copy()
    for j in range(0,len(alist)):
        key = alist[j]
        i = j - 1
        while i>=0 and alist[i]>key:
            alist[i+1]=alist[i]
            i = i - 1
            alist[i+1] = key
    return alist

def search(alist,val):
    pos = []
    length = len(alist)
    for i in range(length):
        if alist[i] == val:
            pos.append(i)
    return pos


def midsearch(alist,val):
    #assume alist is an ordered list(1<...<n)
    n = len(alist)
    if n==1:
        if alist[0] == val:
            return True
        else:
            return False
    mid = int(n/2)
    print('mid:',mid)
    if val>=alist[mid]:
        print('big')
        return midsearch(alist[mid:],val)
    else:
        print('small')
        return midsearch(alist[:mid],val)

print(midsearch(insertionSort(a),5))
if __name__ == '__main__':
    a = [5,2,4,6,1,3]
print(insertionSort(a))
print(search(a,5))