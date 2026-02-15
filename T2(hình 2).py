n=int(input())
for i in range(n):
    for j in range(2*n):
        if (
            (j == 0 and i <= n//2) or
            (j == 2*n-1 and i >= n//2) or
            (i == n//2) or
            (j == i + n)
        ):
            print("*", end="")
        else:
            print(" ", end="")
    print()