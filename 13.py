n=int(input())
dem=0
for i in range(1,n+1):
    if n%i==0:
        dem+=1
if dem==2:
    print(f'{n} là số nguyên tố')
else:
    print(f'{n} không phải số nguyên tố')