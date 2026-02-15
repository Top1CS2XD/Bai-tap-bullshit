a=int(input('Nhập a: '))
b=int(input('Nhập b: '))
'''def ucln(a,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a'''
if b==0:
    print(a)
else:
    while b!=0:
        r=a%b
        a=b
        b=r
    print(a)