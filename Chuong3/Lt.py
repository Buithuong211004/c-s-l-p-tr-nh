n=int(input('nhap n='))
S=0
for i in range(1,n+1):
    print('so thu',i,':',end='')
    x=int(input())
    if x<0:
        continue
    elif x==0:
        break
    else:
        S=S+x
print('S=',S)
   

    
    



  