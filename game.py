
def board(b):
  print(b[0]+"|"+b[1]+"|"+b[2])
  print(b[3]+"|"+b[4]+"|"+b[5])
  print(b[6]+"|"+b[7]+"|"+b[8])

def check(b):
  if(b[0]==b[1]==b[2]!="-"):
    return b[0]
  elif(b[3]==b[4]==b[5]!="-"):
    return b[3]
  elif(b[6]==b[7]==b[8]!="-"):
    return b[6]
  elif(b[0]==b[4]==b[8]!="-"):
    return b[0]
  elif(b[6]==b[4]==b[2]!="-"):
    return b[2]
  elif(b[0]==b[3]==b[6]!="-"):
    return b[0]
  elif(b[1]==b[4]==b[7]!="-"):
    return b[1]
  elif(b[2]==b[5]==b[8]!="-"):
    return b[2]
  else:
    return ""


option="y"
while(option!="n"):
 print('''- | - | -
- | - | -
- | - | - '''
  )
 b=["-","-","-","-","-","-","-","-","-"]
 count=1
 res=""
 c=""
 p=[0,0,0,0,0,0,0,0,0]
 while(count<=9):
  if((count-1)%2==0):
    c="Player 1 turn,"
  else:
    c="Player 2 turn,"
  k=int(input(c+" please enter the position "))
  if(k not in p):
    p[k-1]=k
    if((count-1)%2==0):
      b[k-1]="X"
      board(b)
    else:
      b[k-1]="O"
      board(b)
    if(count>=5):
      res=check(b)
      if(res!=""):
        break
    count=count+1
  else:
    print("sorry, this aleady choosen")
    count=count
 if(res=="X"):
  print("Player 1 is winner ")
 elif(res=="O"):
  print("Player 2 is winner ")
 else:
  print("Hey,relax its Draw")
 
 option=input("Do u want to play again y/n ")

