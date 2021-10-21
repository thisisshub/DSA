# A saddle point is an element of the matrix such that it is
# the minimum element in its row and maximum in its column
row=int(input("Enter the number of rows : "))
col=int(input("Enter the number of column : "))
l=[(list(map(int,input().split()))) for i in range(col)]
flag=0

for i in range(row):
    max = 0
    min = l[i][0]
    index = 0
    for j in range(col):
        if (min > l[i][j]):
            min = l[i][j]
            index = j
    for k in range(row):
        if (l[k][index] > max):
            max = l[k][index]

    if max==min:
        print("The saddle point is present at ", min)
        flag = 1
if flag==0:
    print("There is no saddle point present in the given matrix")


