import random
def Nhap():
    while True:
        n=int(input('Nguoi:'))
        if n==1:
            return n
        elif n==2:
            return n
        elif n==3:
            return n
        
a=Nhap()
r=random.randint(1,3)
print('May:',r)


if r==a:
        print('Ket qua: Hoa')
elif r>a:
        print('Ket qua: May thang')
elif r<a:
        print('Ket qua: Nguoi thang')
    
