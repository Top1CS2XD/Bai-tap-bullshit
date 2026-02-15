#Nhập 1 số nguyên dương, xuất ra số ngược lại
n=int(input('Nhập số n: '))
nguoc=0
while n>0:
    hang=n%10
    nguoc=nguoc*10+hang
    n=n//10
print(nguoc)