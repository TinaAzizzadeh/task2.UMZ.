import string
def check_pass():
    x=int(input("enter your number(the number of time you want to enter username and password):"))
    list1=[]
    for i in range (x):
        a=input("enter username:")
        b=input("enter password:")
        s=(a,b)
        list1.append(s)
    print("all the username and password: ",list1)
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
print(check_pass())
