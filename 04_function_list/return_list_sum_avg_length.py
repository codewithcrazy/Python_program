# write a program to return a list [sum, avg, length] from user defined function of a list.

def fun(list,n):
  newList=[]
  sum=0
  for i in range(0,len(list)):
    sum+=list[i]
  avg=sum/n
  newList.append(sum)
  newList.append(avg)
  newList.append(len(list))
  return newList
list=[1,2,3,4,5,6]
n=len(list)
ans=fun(list,n)
print(ans)