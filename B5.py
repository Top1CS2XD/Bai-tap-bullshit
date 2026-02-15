#Tìm số nguyên dương nhỏ nhất sao cho 1+2+3+...+n>1000:
n=0
tong=0
while tong<=1000:
    tong+=n
    n+=1
print(n)