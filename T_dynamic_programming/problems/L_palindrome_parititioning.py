def method1(str):

    
    n = len(str)

    
    
    
    
    
    
    
    
    C = [[0 for i in range(n)] for i in range(n)]
    P = [[False for i in range(n)] for i in range(n)]

    
    j = 0
    k = 0
    L = 0

    
    
    for i in range(n):
        P[i][i] = True
        C[i][i] = 0

    
    
    
    
    
    
    for L in range(2, n + 1):

        
        
        for i in range(n - L + 1):
            j = i + L - 1  

            
            
            
            
            if L == 2:
                P[i][j] = str[i] == str[j]
            else:
                P[i][j] = (str[i] == str[j]) and P[i + 1][j - 1]

            
            
            if P[i][j] == True:
                C[i][j] = 0
            else:

                
                
                
                C[i][j] = 100000000
                for k in range(i, j):
                    C[i][j] = min(C[i][j], C[i][k] + C[k + 1][j] + 1)

    
    
    return C[0][n - 1]


if __name__ == "__main__":
    
    from timeit import timeit

    str = "ababbbabbababa"
    print(timeit(lambda: method1(str), number=10000))  
    
