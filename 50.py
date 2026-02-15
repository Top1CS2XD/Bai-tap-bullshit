#50/Tìm và in lên màn hình tất cả các số nguyên trong phạm vi từ 10 đến 99 sao cho tích của 2 chữ số bằng 2 lần tổng của 2 chữ số đó.
for i in range(10,100):
    donvi=i%10
    chuc=i//10
    if chuc*donvi==2*(chuc+donvi):
        print(i)