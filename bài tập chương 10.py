#1.1
n=float(input('xin mời nhập số thứ nhất:'))
f=float(input('xin mời nhập số thứ hai:'))
print('max=',max(n,f))
print('min=',min(n,f))

#1.2
a=float(input('xin mời nhập số a:'))
print('|',a,'|=',abs(a))

#1.3
x=float(input('xin mời nhập số x:'))
n=float(input('xin mời nhập số n:'))
print('S=',pow(pow(x,2)+1,n))

#1.4
x=float(input('xin mời nhập số x:'))
n=float(input('xin mời nhập số n:'))
print('S=',pow(pow(x,2)+x+1,n)+pow(pow(x,2)-x+1,n))

#1.5
#1.6
a=int(input('xin mời nhập số a:'))
b=int(input('xin mời nhập số b:'))
c=int(input('xin mời nhập số c:'))
if a==0:
    print('phương trình có nghiệm:x=',-c/b)
else:
    delta=pow(b,2)-4*a*c
    if delta==0:
        print('phương trình có nghiệm:x=',-b/(2*a))
    elif delta>0:
        print('phương trình có nghiệm x1=',(-b-(delta**0.5))/(2*a)) 
        print('phương trình có nghiệm x2=',(-b+(delta**0.5))/(2*a)) 
    else:
        print('phương tình vô nghiệm') 

#1.7
import string
a=str(input('nhập chuỗi:'))
s_sub=str(input('nhập chuỗi con s_sub:'))
s_find=str(input('nhập chuỗi tìm s_find:'))
s_replace=str(input('nhập chuỗi thay thế s_replace:'))
print('chuỗi sau khi loại bỏ khoảng trắng ở đầu và cuối:',a.strip())
print('số lần s_sub xuất hiện trong chuỗi',a.count(s_sub))
print('chuỗi s sau khi tìm kiếm và thay thế:',a.replace(s_find,s_replace))

#1.8
from datetime import datetime
import time
import calendar
ngay=int(input("xin mời nhập ngày: "))
thang=int(input("xin mời nhập tháng: "))
nam=int(input("xin mời nhập năm: "))
ngay_thang_nam=datetime(nam,thang,ngay)
print("Ngày tháng năm vừa nhập là: ",ngay_thang_nam.strftime("%d-%m-%Y"))
calendar.isleap(nam)
if calendar.isleap == True:
    print(f"Năm {nam} là năm nhuận ")
else:
    print(f"Năm {nam} không là năm nhuận")
calendar.weekday(nam,thang,ngay)
if calendar.weekday(nam,thang,ngay) == 0:
    print(f"{ngay} - {thang} - {nam} là Thứ Hai")
elif calendar.weekday(nam,thang,ngay) == 1:
    print(f"{ngay} - {thang} - {nam} là Thứ Ba")
elif calendar.weekday(nam,thang,ngay) == 2:
    print(f"{ngay} - {thang} - {nam} là Thứ Tư")
elif calendar.weekday(nam,thang,ngay) == 3:
    print(f"{ngay} - {thang} - {nam} là Thứ Năm")
elif calendar.weekday(nam,thang,ngay) == 4:
    print(f"{ngay} - {thang} - {nam} là Thứ Sáu")
elif calendar.weekday(nam,thang,ngay) == 5:
    print(f"{ngay} - {thang} - {nam} là Thứ Bảy")
else:
    print(f"{ngay} - {thang} - {nam} là Chủ Nhật")
so_ngay = calendar.monthrange(nam, thang)[1]
print(f"Số ngày trong tháng {thang} là: {so_ngay}")