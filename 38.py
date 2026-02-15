dem=0
tong=0
for i in range(1,100):
    for i in range(1,100):
         for j in range(1,i):
            if i %j==0:
                dem==1
            if dem==2:
                if ((i//10)%10+(i%10)%2)==0:
                    print(i)         