#first-one 
import keyword
a=keyword.kwlist
si=[]
def decrypt_clue(text):
 q=open(text)
 s=q.read()
 for i in a:
  if i in s:
   si.append(i)
 return(si)
n="/Users/tina/Desktop/mysterious.txt"
answer11=decrypt_clue(n)
answer1=[str(s) for s in answer11]

#second-one
def solve_puzzles(puzzles):
    s=[]
    q=[]
    z=open(puzzles)
    w=z.readlines()
    for i in w:
     q.append(i)
    
    b=['()\n','{}\n','0\n','[]\n','False\n','None\n','\n','""\n']
    for i in q:
      if i in b:
       s.append(False)
      else:
       s.append(True)
    return(s)
     
n="/Users/tina/Desktop/puzzles.txt"
answer22=solve_puzzles(n)
answer2=[str(s) for s in answer22]

#third-1
def calculate_magic_number(start,end):
    l=[]
    k=True
    
    while k==True:
        x=float(input("enter number from 0 to 1:"))
        c=x*(end-start)+start
        l.append(c)
        a=input("do you want to continue (y/n)?")
        if a=="n":
            k=False
    return(l)
start=int(input("enter first num :"))
end=int(input("enter second num :"))
answer33=calculate_magic_number(start,end)
answer3=[str(s) for s in answer33]

#third-2
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
  ans=int(input("enetr the decimal number:"))
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
 return(f,t)
answer44=exam_number()       
answer4=[str(s) for s in answer44]
#third-3
import string
def check_pass():
    x=int(input("enter number(the number of time you want to enter username and password):"))
    list1=[]
    for i in range (x):
        a=input("enter name:")
        b=input("enter pass:")
        s=(a,b)
        list1.append(s)
    z=False
    c=False
    r=False
    w=string.punctuation
    list2=[]
    for i in list1:
        n=i[0]
        p=i[1]
        p=str(p)
        if len(p)>=8:
         for x in p:
            if x.isupper()==True:
                z=True
            elif x.islower()==True:
                c=True
            elif x in w:
                r=True
         if r==True and z==True and c==True:
            list2.append(n)
    return(list2)    
answer55=[check_pass()]
answer5=[str(s[0]) for s in answer55]

#last-one
def unlock_vault(clue):
 
 x=clue[0]
 k=x[0]
 return (k)
p1=unlock_vault(answer1)
p2=unlock_vault(answer2)
p3=unlock_vault(answer3)
p4=unlock_vault(answer4)
p5=unlock_vault(answer5)
for i in [p1,p2,p3,p4,p5]:
  print(i,end="")
