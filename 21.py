a=int(input())
b=int(input())
c=int(input())
if (a+b)>c and (a+c)>b and (b+c)>a:
    print('Có thể tạo thành tam giác')
else:
    print('Không thể tạo thành tam giác')