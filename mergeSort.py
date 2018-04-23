
def mergeSort(lists):
	if len(lists) <= 1:
		return lists
	middle = int(len(lists)/2)
	left = mergeSort(lists[:middle])
	right = mergeSort(lists[middle:])
	return merge(left,right)

def merge(a,b):
	#p<=q<r
	#merge alist[p,q] and alist[q+1,r] in a sorted order
	alist1 = a.copy()
	alist2 = b.copy()
	#print('alist1:',alist1)
	#print('alist2:',alist2)
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



def digui_selectionSort(alist):
	n = len(alist)
	if n == 1:
		return alist
	else:
		templist = digui_selectionSort(alist[:n-1])
		templist = insert(templist,alist[n-1])
		return templist

def insert(alist,inval):
	for i in range(len(alist)):
		if alist[i]>inval:
			inval,alist[i] = alist[i],inval
	alist.append(inval)
	return alist

if __name__ == '__main__':
	a = [1,2,3,4,6,5]
	print(mergeSort(a))
	print(digui_selectionSort(a))
