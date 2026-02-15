x = int(input('Nhập x: '))
n = int(input('Nhập n: '))
S = 0
gt = 1      
mu = x     
for i in range(n + 1):
    if i > 0:
        mu*=x**2        
        gt=gt*(2*i)*(2*i+1)  
    S+=mu/gt
print(S)