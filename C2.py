#C2. một lớp có số lượng bạn nam và bạn nữ được nhập từ bàn phím, các bạn tiến hành lập nhóm gồm các bạn nam và các bạn nữ , hãy sắp xếp xem có thể xếp được bao nhiêu nhóm (số bạn nam và nữ ở các nhóm là giống nhau)
def gcd(n,m):
    while m!=0:
        uoc=n%m
        n=m
        m=uoc
    return n
n=int(input('Nhập số nam: '))
m=int(input('Nhập số nữ: '))
nhom=gcd(n, m)
sonam=n//nhom
sonu=m//nhom
print(nhom)
