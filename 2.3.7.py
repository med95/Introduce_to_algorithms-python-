
'''
描述一个运行时间为Θ（nlgn）的算法，
给定n个整数的集合S和另一个整数x，
该算法能确定S中是否存在两个其和刚好为x的元素
'''
def judge(alist,x):
    '''
    0.归并排序 O(nlogn)
    1.判断重复元素 -> 重复元素*2等于要求的数 -> True
    2.删除重复元素避免干扰 暂时觉得没有这一步也🆗
    3.创建辅助列表s = {x-i|i belongs alist}
    4.s 和 alist 有重复元素 且 重复元素*2 ！= x -> True
    '''
    alist = mergeSort(alist)
    multi_elems = multiSearch(alist)
    for i in multi_elems:
        if 2*i == x:
            return True
        # else:
        #     alist = deleteElem(alist,i)
    s = []
    for i in alist:
        s.append(x-i)
    for i in s:
        if iterativeBinarySearch(alist,i,0,len(alist)-1) and 2*i != x:
            return True
    return False
#---------------------------------------------
# 辅助函数
# mergeSort merge 归并排序
# iterativeBinarySearch 二分查找
# multiSearch 查找重复元素，返回重复元素列表
# deleteElem 按值删除列表中的指定元素
#---------------------------------------------
def mergeSort(lists):
    if len(lists) <= 1:
        return lists
    middle = int(len(lists)/2)
    left = mergeSort(lists[:middle])
    right = mergeSort(lists[middle:])
    return merge(left,right)

def merge(a,b):
    alist1 = a.copy()
    alist2 = b.copy()
    i = 0
    j = 0
    alist = []
    while i<len(alist1) and j<len(alist2):
        if alist1[i]<alist2[j]:
            alist.append(alist1[i])
            i += 1
        else:
            alist.append(alist2[j])
            j += 1
    if i==len(alist1):
        for k in alist2[j:]:
            alist.append(k)
    else:
        for k in alist1[i:]:
            alist.append(k)
    return alist

def iterativeBinarySearch(alist,val,low,high):
    while low <= high:
        mid = int((low+high)/2)
        if val == alist[mid]:
            return mid
        elif val>alist[mid]:
            low = mid+1
        else:
            high = mid-1
    return False

def multiSearch(alist):
    #sorted list
    #返回重复元素
    n = len(alist)
    multi_elem = []
    
    for i in range(n):
        if iterativeBinarySearch(alist[i+1:],alist[i],0,len(alist[i+1:])-1) or str(iterativeBinarySearch(
            alist[i+1:],alist[i],0,len(alist[i+1:])-1))=='0':
            multi_elem.append(alist[i])
    return multi_elem

def deleteElem(alist,val):
    while iterativeBinarySearch(alist,val,0,len(alist)-1) or str(
        iterativeBinarySearch(alist,val,0,len(alist)-1))=='0':
        pos = iterativeBinarySearch(alist,val,0,len(alist)-1)
        alist = alist[:pos]+alist[pos+1:]
    return alist

#--------------------------------------------------

if __name__ == '__main__':    
    S1 = [1,4,6,5]
    S2 = [1,4,4,6,5]
    S3 = [4,3,2,1]
    x = 8
    print(judge(S1,x))
    print(judge(S2,x))
    print(judge(S3,x))
