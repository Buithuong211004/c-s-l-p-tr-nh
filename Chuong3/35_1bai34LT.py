t=float(input(''))
l=float(input(''))
h=float(input(''))
d=(h+t*2+l*3)/6
if d<3:
    y='Kem'
elif d>=3 and d<5:
    y='Yeu'
elif d>=5 and d<6:
    y='Trung binh'
elif d>=6 and d<7:
    y='Trung binh Kha'
elif d>=7 and d<8:
    y='Kha'
elif d>=8 and d<9:
    y='Gioi'
elif d>=9 and d<10:
    y='Xuat sac'
print(y)