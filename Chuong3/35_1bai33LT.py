x=float(input('x='))
y=float(input('y='))
a=str(input('Phep toan:'))
if a=='/':
    if y==0:
        print("Khong hop le")
    else:
        t=x/y
elif a=='-':t=x-y
elif a=='*':t=x*y
elif a=='+':t=x+y
print(x,a,y,'=',round(t,1),sep='')

    