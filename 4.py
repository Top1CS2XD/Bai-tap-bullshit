vb=input('Nhập chuỗi: ')
ds=vb.split(' ')
dodai=0
for i in ds:
    if len(i)>dodai:
        dodai=len(i)
        dainhat=i
print(dainhat)