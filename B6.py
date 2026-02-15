#Tìm và in lên màn hình tất cả các số nguyên trong phạm vi từ 10 đến 99 sao cho tích của 2 chữ số bằng 2 lần tổng của 2 chữ số đó.
for i in range(10,100):
    chuso1=i//10
    chuso2=i%10
    if chuso1*chuso2==2*(chuso1+chuso2):
        print(i,end=' ') 