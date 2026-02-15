x = float(input("Nhập x: "))
n = int(input("Nhập n: "))
S = 0
gt = 1
for i in range(1, n + 1):
    gt = gt * i
    S = S + (x ** i) / gt
print("Giá trị S(x, n) =", S)