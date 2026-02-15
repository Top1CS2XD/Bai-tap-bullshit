#12.	Đếm số các kí tự là chữ cái tiếng Anh trong xâu S cho trước
s=input('Nhập vb: ')
dem=0
for i in s:
    if i.isalpha():
        dem+=1
print(dem)