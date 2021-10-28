# A saddle point is an element of the matrix such that it is
# the minimum element in its row and maximum in its column

def saddle(row,col,flag,l):
    for i in range(row):            #O(n)
        max = 0                   #|
        min = l[i][0]             #|-->O(1)
        index = 0                 #|

        #first we find the minimum element in the jth row
        for j in range(col):        #O(n)
            if (min > l[i][j]):     #O(c1)
                min = l[i][j]
                #after we find the minimum element in the row,
                #we store its column value in the index variable
                index = j

        #now we find the maximum element in the above stored column
        for k in range(row):        #O(n)
            if (l[k][index] > max): #O(c2)
                max = l[k][index]

        #To satisfy condition of saddle point,
        #We compare that the max and min elements are same
        if max==min:                #O(c3)
            print("The saddle point is present at ", min)
            flag = 1
    if flag==0:                     #O(1)
        print("There is no saddle point present in the given matrix")

'''
Total Time Complexity :

=O(n*(O(n)*c1 + O(n)*c2+c3+O(1))  ....(c1,c2,c3 are constants(same number of iterations)))
=O(n*(2*O(n)))                    ....(neglecting negligible iterations)
=O(n**2)
'''

if __name__=="__main__":
 '''row = int(input("Enter the number of rows : "))
    col = int(input("Enter the number of column : "))
    l = [(list(map(int, input().split()))) for i in range(col)] = [[1,2,3],
                                                                    [4,5,6],
                                                                    [7,8,9]]
    flag = 0

    from timeit import timeit
    print(timeit(lambda: saddle(row,col,flag,l), number=10000)) #0.29033070000000016'''
