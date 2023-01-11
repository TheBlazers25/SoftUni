def aliquotSum(n):
    sm = 0
    for i in range(1, n):
        if (n % i == 0):
            sm = sm + i
    if sm == n:
         return "We have a perfect number!"
    else:
         return "It's not so perfect."


# Driver Code
n = int(input())
print(aliquotSum(n))