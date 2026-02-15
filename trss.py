for i in range(1,101):
    dem=0
    tong=0
    dv=i//10
    chuc=i%10
    for j in range(1,i+1):
        if i%j==0:
            dem+=1
        if dem==2:
            if (dv+chuc)%2:
                tong+=i
print(tong)