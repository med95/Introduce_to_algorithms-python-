

'''
#问题描述
    著名的约瑟夫问题，一个一世纪著名历史学家弗拉维奥·约瑟夫斯的传奇故事。
    故事讲的是，他和他的 40 个战友被罗马军队包围在洞中。他们决定宁愿死，
    也不成为罗马人的奴隶。他们围成一个圈，其中一人被指定为第一个人，
    顺时针报数到第k人，就将他杀死。约瑟夫斯是一个成功的数学家，
    他立即想出了应该坐到哪才能成为最后一人。最后，他加入了罗马的一方，
    而不是杀了自己。你可以找到这个故事的不同版本，有些说是每次报数 3 个人，
    有人说允许最后一个人逃跑。无论如何，思想是一样的。
'''
def Joseph1(namelist, num=2):
    '''
    namelist 名字列表
    num      除去第num个人\
    使用Queue
    '''
    from queue import Queue
    if num == 1:#没有生存者
        print('Non survive')
        return
    simqueue = Queue()
    for name in namelist:
        simqueue.put(name)

    while simqueue.qsize() > 1:#直到只剩下最后一个人
        for i in range(num-1):#将前num-1个人循环左移到队列最后端
            simqueue.put(simqueue.get())

        simqueue.get() #除去第n个人，即将队列第一个吐出

    return simqueue.get()

def Joseph2(n):
    '''
    输入 n ： 多少个人 
    输出 幸存者编号    
    类似于Joseph1
    num = 2
    使用Queue
    解析解 J(n = 2**m+l) = 2*l+1 , l<2**m, 2**m<=n=<2**(m+1)
    即可用二进制循环左移一位可得答案    
    '''
    from queue import Queue
    q = Queue()
    bin_n = bin(n)

    for i in range(2,len(bin_n)):
        q.put(bin_n[i])

    q.put(q.get())
    joseph = ''

    for i in range(q.qsize()):
        joseph += str(q.get())

    return int(joseph,2)

def Joseph3(n):

    '''
    输入 n ： 多少个人 
    输出 幸存者编号
    类似于Joseph1
    num = 2
    使用List
    解析解 J(n = 2**m+l) = 2*l+1 , l<2**m, 2**m<=n=<2**(m+1)
    即可用二进制循环左移一位可得答案    
    '''

    bin_n = bin(n)
    q = list(bin_n[2:])
    q.append(q.pop(0))
    survival = ''

    for i in q:
        survival += i

    return int(survival,2)

if __name__ == '__main__':    
    print(Joseph1(["Bill","David","Susan","Jane","Kent","Brad"],2))
    print(Joseph2(5))
    print(Joseph3(5))
    print(Joseph2(10))
    print(Joseph3(10))