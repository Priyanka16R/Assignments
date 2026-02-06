message=" Hello Love"
print(message.strip())
print(message.upper())
print(message.replace("LOve","Python"))
print(message[1])
print(message[5:8])
text="python programming"
print(text[::-1])
print(text[2:-3])
print(text[2:0:-1])
word="python programming is a interprted language"
s=word.split()
print(s)
print(s[0])
print(s[4])
for i in s:{
print(" "+i)
}
print("I love \"python programming\"")# inlcude special character in output
print("-----------List----------")
list1=["Mango",3,4,"onion"]
list1.append(7)
print(list1) 

print(list1.index(3))
print(list1.append(4))
list1.count(4)
print(list1)
list2=[89,43,22,23,54,54,33]
list2.sort()
print(list2)
c=list2.pop()
print(c)
import numpy as np
num=np.argmax(list2)
print(num)
print("--------tuples-------")
tuple1=(23,4,6,66,6,4,22,9)
print(tuple1)
print(tuple1.count(6))
print(tuple1.index(66))
print("-------lambda-------------")
sum=lambda a,b:a+b
print(sum(1,2))
num=lambda x:x*x*x
print(num(2))
print("------map--------")
values=[1,2,3,4,5,6,7,8]
print(map(lambda x:x+3,values))
print(list(map(lambda x:x+3,values)))
print("----------filter-------")
print(list(filter(lambda x:x%2==0,values)))
print("---------reduce-------")
from functools import reduce
print(reduce(lambda x,y:x+y,values))