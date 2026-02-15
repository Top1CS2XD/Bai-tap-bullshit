d=int(input())
m=int(input())
y=int(input())
if (1<=d<=31) and (1<=m<=12) and (1900<=y<=2019):
    if (y%4==0) or (y%100==0) or (y%400==0):
        if (m==2) and (d==29):
            print('Bạn này 4 năm sinh nhật 1 lần')
    else:
        print("Bạn này 1 nam sinh nhật 1 lần")