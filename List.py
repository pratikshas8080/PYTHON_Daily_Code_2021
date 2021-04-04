lst=[91,52,4,1,0,3,6,00,10,20]
var=type(lst)
var=lst[2]
var=lst[1:4]
lst.append(100)
print(var)

#List2
lst2=[91,52,4,1,0,3,6,00,10,20]
var1=len(lst2)
lst2.append(100)
print(var1)
print(lst2)

#List3
lst3=[91,52,4,1,0,3,6,00,10,20]
lst3.insert(1,92)#first index value then which no need to insert that number
print(lst3)

#List4
lst4=[91,52,4,1,0,3,6,00,10,20]
lst4.remove(52)
lst4.pop() #Last Element Remove
del lst4[6]
print(lst4)

#List5
lst5=[91,52,4,1,0,3,6,00,10,20]
lst5.clear() #Clear All List
print(lst5)
