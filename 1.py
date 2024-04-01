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
print(decrypt_clue(n))
