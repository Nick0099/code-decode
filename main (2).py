coding= input("Are the words coded of decoded(y/n)").upper()
sword= input("Enter the word to be coded or decoded: ")
iword= sword.split(" ")
if(coding=="Y"):
  nwords = []
  for word in iword:
    if(len(word)>=3):
      r1 = "ksd"
      r2 = "kjs"
      stnew = r1+ word[1:] + word[0] + r2
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))

else:
  nwords = []
  for word in iword:
    if(len(word)>=3): 
      stnew = word[3:-3]
      stnew = stnew[-1] + stnew[:-1]
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))
