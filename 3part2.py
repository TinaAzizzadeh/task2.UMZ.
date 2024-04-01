import random
import time
def exam_number():
 t0=time.perf_counter()
 
 t=0
 f=0
 while time.perf_counter() - t0 <20 :
  a=""
  for i in range(4):
   x=str(random.randint(0,1))
   a+=x
  print(a)
  ans=int(input("enetr the decimal value of number:"))
  n=int(a)
  sum=0
  i=0
  while(n>0):
   r=n%10
   sum+=r*2**i
   i+=1
   n=n//10
  if sum==ans:
    t+=1
  else:
    f+=1
 return(t,f)
print(exam_number())      