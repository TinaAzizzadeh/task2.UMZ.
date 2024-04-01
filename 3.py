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
print(calculate_magic_number(start,end))
