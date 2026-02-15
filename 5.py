#Tìm từ xuất hiện nhiều nhất trong một xâu, các từ cách nhau bởi một dấu cách
vb=input('Nhập chuỗi: ')
ds=vb.split(' ')
demtu=0
dainhat=0
for i in ds:
    dem=ds.count(i)
    if dem>demtu:
        demtu=dem
        dainhat=i
print(dainhat)