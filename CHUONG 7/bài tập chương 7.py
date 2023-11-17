#1.1
a=float(input("nhập x:"))
S=1+a+a**3/3+a**5/5
print("S=1+x+x^3/3+x^5/5=",S)

#1.2
result=1+2
print('result=',result)
original_result=result
result=result-1
print('result=',result)
original_result=result
result=result*2
original_result=result 
print('result=',result)
result=result ** 3
original_result=result 
print('result=',result)
result=result+8
original_result=result
print('result=',result)
result=result%7
original_result=result
print('result=',result)
result =result//2
original_result=result
print('result=',result)

#1.3
result=5
print('result', result)
result-=1
print('result', result)
result+=3
print('result', result)
result=result
print('result', result)
result=True
print('not result =', not result)

#1.4
x=10
y=4
print("x=%d,y=%d"%(x,y))
equivelence=x==y
print("x==y is",equivelence)
equivelence=x!=y
print("x!=y is",equivelence)
equivelence=x>y
print("x>y is",equivelence)
x=8
y=9
print("x=%d,y=%d"%(x,y))
equivelence=x>=y
print("x>=y is",equivelence)
equivelence=x<y
print("x<y is",equivelence)
equivelence=x<=y
print("x<=y is",equivelence)

#1.5
x=15
y=12
print("binary of x=",bin(x),"binary of y=",bin(y))
print("x&y=",bin(x&y))
print("x|y=",bin(x|y))
print("x^y=",bin(x^y))
print("~x",bin(~x))
print("x<<2=",bin(x<<y))
print("x>>2=",bin(x>>y))

#1.6
x=True
y=False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:",not x)
print("x is y:",x is y)
print("x is not y:",x is not y)

#1.7
a=int(input("số tiền muốn đổi:"))
so_to_1=a//500000
tien_con_lai1=a%500000
so_to_2=tien_con_lai1//200000
tien_con_lai2=tien_con_lai1%200000
so_to_3=tien_con_lai2//100000
tien_con_lai3=tien_con_lai2%100000
so_to_4=tien_con_lai3//50000
tien_con_lai4=tien_con_lai3%50000
print("số tờ 500k:",so_to_1)
print("số tờ 200k:",so_to_2)
print("số tờ 100k:",so_to_3)
print("số tờ 50k:",so_to_4)
print("sô tiền thừa:",tien_con_lai4)