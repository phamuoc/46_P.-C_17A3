#1.1
print("** ** ******     **     **     ******")
print("** ** **         **     **     **  **")
print("***** ******     **     **     **  **")
print("** ** **         **     **     **  **")
print("** ** ******     ****** ****** ******")

#1.2
x=10
y=5
tổng=x+y
hiệu=x-y
tích=x*y
thương=x/y
print("tổng của",x, '+', y, "=", tổng)
print("hiệu của",x, "-", y, "=", hiệu)
print("tích của",x, "*", y, "=", tích)
print("thương của",x, "/", y, "=", thương)

#1.3
ten_hang="sữa hộp vina milk"
so_luong= 5
don_gia= 25000
tien= so_luong * don_gia
print("tiền phải trả", don_gia, '*', so_luong, "=", tien)


#1.4 
import math
a= float(input("nhập độ dài cạnh a:"))
b= float(input("nhập độ dài cạnh b:"))
c= float(input("nhập độ dài cạnh c:"))
p= (a + b + c) / 2
s= math.sqrt(p * (p-a) * (p-b) * (p-c))
print("diện tích tam giác là:", s)
