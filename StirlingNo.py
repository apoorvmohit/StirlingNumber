def countP(n, k):
     
    # Base cases
    if (n == 0 or k == 0 or k > n):
        return 0
    if (k == 1 or k == n):
        return 1
     
    # S(n+1, k) = k*S(n, k) + S(n, k-1)
    return (k * countP(n - 1, k) +
                countP(n - 1, k - 1))
 
# Driver Code
print(countP(4, 2))
