'''
问题描述：
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
解决方案：
1.行、列向量直接打印
2.矩阵(m!=1,n!=1)选择四个顶点，顺时针打印，然后将四个顶点内缩成为一次打印的四个顶点
  满足全部打印完毕的条件返回打印列表
辅助函数：
print_4points(matrix,point1,point2,point3,point4,print_list)
顺时针打印四个顶点
特别的：
    若point1 == point4，需要打印的范围为某一行的部分元素
    若point1 == point2，需要打印的范围为某一列的部分元素
'''
def clockwise_print_matrix(matrix):
    row = len(matrix)
    col = len(matrix[0])
    if row == 1:
        return matrix[0]
    if col == 1:
        return [matrix[i][0] for i in range(row)]
    #initial 4 points
    point1 = [1,1]
    point2 = [1,col]
    point3 = [row,col]
    point4 = [row,1]
    print_list = []
    for i in range(max(row,col)):
        # loop exit condition when row = col
        if point1 == point2 == point3 == point4:
            print_list.append(matrix[point1[0]-1][point1[1]-1])
            return print_list
        if point1[1]+1 == point2[1]:
            print_list = print_4points(matrix,point1,point2,point3,point4,print_list)
            return print_list
        # loop exit condition when row != cow
        # loop exit condition when row < col
        if point1[0] > point4[0]:
            return print_list
        # loop exit condition when row > col
        if point1[1] > point2[1]:
            return print_list
        # clockwise print point1->point2->point3->point4->point1 without overlap
        print_list = print_4points(matrix,point1,point2,point3,point4,print_list)
        # next point1
        point1[0] += 1
        point1[1] += 1
        # next point2
        point2[0] += 1
        point2[1] -= 1
        # next point3
        point3[0] -= 1
        point3[1] -= 1
        # next point4
        point4[0] -= 1
        point4[1] += 1

def print_4points(matrix,point1,point2,point3,point4,print_list):

    if point1 == point4:
        # remain a row
        # print point1 to point2
        for i in range(point1[1],point2[1]):
            print_list.append(matrix[point1[0]-1][i-1])
        # add point2
        print_list.append(matrix[point2[0]-1][point2[1]-1])

    elif point1 == point2:
        # remain a col
        # print point2 to point3
        for i in range(point2[0],point3[0]):
            print_list.append(matrix[i-1][point2[1]-1])
        # add point3
        print_list.append(matrix[point3[0]-1][point3[1]-1])

    else:        
        #print point1 to point2
        for i in range(point1[1],point2[1]):
            print_list.append(matrix[point1[0]-1][i-1])
        #print point2 to point3
        for i in range(point2[0],point3[0]):
            print_list.append(matrix[i-1][point2[1]-1])
        #print point3 to point4
        for i in range(point3[1],point4[1],-1):
            print_list.append(matrix[point3[0]-1][i-1])
        #print point4 to point1
        for i in range(point4[0],point1[0],-1):
            print_list.append(matrix[i-1][point4[1]-1])

    return print_list
if __name__ == '__main__':
    amatrix1 = [[1,2,3,4]]
    amatrix2 = [[1],[2],[3],[4]]
    amatrix3 = [[1,2,3,4,5],[6,7,8,9,10]]
    amatrix4 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
    amatrix5 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
    print(clockwise_print_matrix(amatrix1))
    print(clockwise_print_matrix(amatrix2))
    print(clockwise_print_matrix(amatrix3))
    print(clockwise_print_matrix(amatrix4))
    print(clockwise_print_matrix(amatrix5))
