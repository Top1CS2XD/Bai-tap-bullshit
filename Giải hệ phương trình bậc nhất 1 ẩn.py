a=float(input('Nhập a: '))
b=float(input('Nhập b: '))
c=float(input('Nhập c: '))
m=float(input('Nhập m: '))
c=float(input('Nhập c: '))
d=float(input('Nhập d: '))
n=float(input('Nhập n: '))
dd=a*d-b*c
dx=m*d-b*n
dy=a*n-m*c
if dd==0:
    if dx==0 and dy==0:
        print('Hệ phương trình có vô số nghiệm')
    else:
        print('Hệ phương trình vô nghiệm')
else:
    x=dx/dd
    y=dy/dd
    print(f'x={x}, y={y}')