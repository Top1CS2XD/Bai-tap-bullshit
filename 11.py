#11.	Đếm số các kí tự là chữ số trong xâu S cho trước
n=input('Nhập vb: ')
dem=0
for i in n:
    if i.isdigit():
        dem+=1
print(dem)