#9.	Kiểm tra xem một xâu có phải là palindrome hay không.
n=input('Nhập văn bản: ')
d=n[::-1]
if d==n:
    print('Xâu này là palindrome')
else:
    print('Xâu này ko là palindrome')