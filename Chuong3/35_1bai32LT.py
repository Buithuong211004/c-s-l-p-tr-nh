a=int(input('M1='))
b=int(input('M2='))
c=int(input('M3='))
S=int(input('S='))
if S<=100:
    t=S*a
elif S<=150:
    t=100*a+(S-100)*b
else:
    t=100*a+50*b+(S-100-50)*c
print('Phai tra=',t,sep='')
    