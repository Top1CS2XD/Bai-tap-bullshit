#25/Cho 2 số tự nhiên m và n. Hãy tính trung bình cộng các số chẵn trong phạm vi từ m đến n
m=int(input())
n=int(input())
tong=0
dem=0
for i in range(m,n+1):
    if i%2==0:
        tong+=i
        dem+=1
if dem!=0:
    print(tong/dem)
