#27/Cho 4 số tự nhiên a và b. Tìm ước chung lớn nhất của a và b
a=int(input())
b=int(input())
while b!=0:
    r=a%b
    a=b
    b=r
print(a)