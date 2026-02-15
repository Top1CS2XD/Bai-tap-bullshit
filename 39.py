n=int(input())
dem=0
tong=0
tbc=0
for i in range(1,n):
    for j in range(1,i+1):
        if i%j==0:
            dem+=1
    if dem==2:
        t=True