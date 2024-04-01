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
print(solve_puzzles(n))