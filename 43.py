##43/ Hãy tính tổng và in ra các số nguyên tố nhỏ hơn 100 và có tổng các chữ số của nó là số chẵn
dem=0
for i in range(2,100):
    for m in range(2,i):
        if i%m==0:
            dem+=1
    if dem==0:
        tong=0
    if dem==2:
        tong+=i
print(tong)