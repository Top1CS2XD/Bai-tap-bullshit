#26/Hãy tìm số tự nhiên k nhỏ nhất sao cho 2k≥m. Với m là số tự nhiên nhập từ bàn phím
m=int(input())
k=0
while 2**k<m:
    k+=1
print(k)