
i=1
while(i<10):
  element=list[i]
  j=i
  i=i+1

  while(j>0 and list[j-1]>element):
    list[j]=list[j-1]
    j=j-1

  list[j]=element

i=0
while(i<10):
  print (list[i])
  i=i+1
