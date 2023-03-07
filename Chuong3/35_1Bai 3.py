a=int(input('Tien thu='))
if  a<=100:
    i=float(a*550)
elif  a<=150:
   i=float(100*550+(a-100)*750)
elif a<=200:
    i=float(100*550+50*750+(a-100-50)*950)
else:
  i=float(100*550+50*750+50*950+(a-100-50-50)*1350)
print('Phai tra=',i+i*0.1,sep="")