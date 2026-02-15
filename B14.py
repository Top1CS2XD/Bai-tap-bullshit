#Nhập vào số tự nhiên n có 2 chữ số, in ra màn hình tất cả các số lẻ nhỏ hơn căn bậc hai của n và có chữ số đứng trước nhỏ hơn chữ số phía sau
import math
n=int(input('Nhập n: '))
can_n = int(math.sqrt(n))
for i in range(10, can_n):
    chuc=i//10
    donvi=i%10
    if (i%2!=0) and (chuc<donvi):
        print(i)