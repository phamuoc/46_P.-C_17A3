#1.1
print("**    **   ******   **      **      ******")
print("**    **   **       **      **      **  **")
print("********   ******   **      **      **  **")
print("**    **   **       **      **      **  **")
print("**    **   ******   ******  ******  ******")

#1.2
ten_hang = "Sữa hộp Vina Milk"
so_luong = 5
don_gia = 25000
tien_phai_tra = so_luong * don_gia
print("Tên hàng:", ten_hang)
print("Số lượng:", so_luong)
print("Đơn giá:", don_gia, "vnđ")
print("Tiền phải trả:", "{:,}".format(tien_phai_tra), "vnđ")

#1.3
x = 10
y = 5
tong = x + y
hieu = x - y
tich = x * y
thuong = x / y
print("x =", x, ", y =", y)
print("Tổng x + y =", tong)
print("Hiệu x - y =", hieu)
print("Tích x * y =", tich)
print("Thương x / y =", thuong)

#1.4
a=(5-3)//2
b=8-(3*2)-(1+1)
print(a)
print(b)

#1.5
so_luong = int(input("Nhập số lượng: "))
don_gia = float(input("Nhập đơn giá: "))
thanh_tien = so_luong * don_gia
print("Thành tiền:", so_luong, "*", don_gia, "=", thanh_tien)

#1.6
a=int(input("số kẹo alcie có:"))
b=int(input("số kẹo bob có:"))
c=int(input("số kẹo carol có:"))
print("số kẹo thừa sẽ đạp đi:",(a+b+c)%3)

#1.7
a=float(input("nhập độ C:"))
print("độ F=",1.8*a+32)

#1.8
a=input("nhập chuỗi s1:")
b=input("nhập chuỗi s2:")
c=input("nhập chuỗi s3:")
d=int(input("nhập index:"))
print("chiều dài chuỗi s1=",len(a))
print("chiều dài chuỗi s2=",len(b))
print("chiều dài chuỗi s3=",len(c))
print("chuỗi s4 =",a[d:])
print("chuỗi s2 lập lại 2 lần",b*2)

#1.9
a=float(input("lãi xuất năm(%):"))
b=int(input("số tiền gửi:"))
c=int(input("số tháng gửi:"))
d =(b*c)*(a/100/12)
print("tiền lãi=",d)
print("tiền vốn+lãi",d+b)