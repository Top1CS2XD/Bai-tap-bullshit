#Viết chương trình in ra màn hình dãy các chữ cái tiếng Anh từ “A” đến “Z” theo ba hàng ngang trên màn hình, hai hàng ngang đầu có 10 chữ cái, hàng thứ ba có 6 chữ cái.
for i in range(65,91):
    print(chr(i),end=' ')
    if (i-64)%10==0:
        print()