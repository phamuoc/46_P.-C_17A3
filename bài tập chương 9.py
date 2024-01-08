#1.1
def sign(n):
    if n>0:
        a=1
    elif n<0:
        a=-1
    else:
        a=0
    return a
n=float(input('nhập số:'))
print(sign(n))

#1.2
def tinh_can(nam):
    a=nam%10
    if a==0:
     can="canh"
    if a==1:
     can="tân"
    if a==2:
     can="nhâm"
    if a==3:
     can="quý"
    if a==4:
     can="giáp"
    if a==5:
     can="ất"
    if a==6:
     can="bính"
    if a==7:
     can="đinh"
    if a==8:
     can="mậu"
    if a==9:
     can="kỷ"
    return can
def tinh_chi(nam):
    b=nam%12
    if b==0:
     chi="thân"
    if b==1:
     chi="dậu"
    if b==2:
     chi="tuất"
    if b==3:
     chi="hợi"
    if b==4:
     chi="tý"
    if b==5:
     chi="sửu"
    if b==6:
     chi="dần"
    if b==7:
     chi="mão"
    if b==8:
     chi="thìn"
    if b==9:
     chi="tỵ"
    if b==10:
     chi="ngọ"
    if b==11:
     chi="mùi"
    return chi
nam=int(input("nhập năm:"))
print('năm',nam,'lịch âm là năm',tinh_can(nam),tinh_chi(nam))

#1.3
def BMI(can_nang,chieu_cao):
    BMI=can_nang/(chieu_cao*chieu_cao)
    print('chỉ số BMI:%.2f'%BMI)
    if BMI<18.5:
        print('đánh giá theo chỉ số:Gầy')
    elif BMI>=18.5 and BMI<25:
        print('đánh giá theo chỉ số:Bình Thường')
    else:
        print('đánh giá theo chỉ số:Thừa Cân')
    return 
a=float(input('nhập cân nặng(kg):'))
b=float(input('nhập chiều cao(m):'))
BMI(a,b)

#1.4
def tinh_S(A,B):
    S=((A**2)+1)**B
    print('S=',S)
    return 
n=float(input('nhập số n:'))
x=float(input('nhập số x:'))
tinh_S(n,x)

#1.5
def tinh_A(n,x):
    A=((x**2)+x+1)**n+((x**2)-x+1)**n
    print('S=',A)
    return 
n=float(input('nhập số n:'))
x=float(input('nhập số x:'))
tinh_A(n,x)

#1.6
n=float(input('xin mời nhập số:'))
def kiem_tra_so_nguyen_to(n):
    if n<2:
        print(n,'không phải là số nguyên tố')
    else:
        for i in range(2,int(n**0.5)+1):
               if n%i==0:
                     print(n,'không phải là số nguyên tố')
                     break   
        else:
                   print(n,'là số nguyên tố')
    return 

kiem_tra_so_nguyen_to(n)

#1.7
def ham_tra_ve_phan_nguyen(a,b):
    return a//b
a=int(input('nhập số a:'))
b=int(input('nhập số b:'))
    
print(f'phần nguyên của phép chia={ham_tra_ve_phan_nguyen(a,b)}')

#1.8
n=int(input('nhập số:'))
s=0
def kiem_tra_so_hoan_hao(n,s):   
 for i in range(1,n-1):
        if n%i==0:
            s+=i
 return s

kiem_tra_so_hoan_hao(n,s)
if n==1:
    print('1 là số hoàn hảo')
elif s==n:
    print(n,'là số hoàn hảo')
else:
    print(n,'là số không hoàn hảo')

#1.9
r=float(input('nhập bán kính:'))
a=float(input('nhập chiều dài:'))
b=float(input('nhập chiều rộng:'))
s=lambda r:3.14*(r**2)
p=lambda r:3.14*2*r
S=lambda a,b:a*b
P=lambda a,b:(a+b)*2
print('diện tích hình tròn:',s(r))
print('chu vi hình tròn:',p(r))
print('diện tích hình chữ nhật:',S(a,b))
print('chu vi hình chữ nhật:',P(a,b))

