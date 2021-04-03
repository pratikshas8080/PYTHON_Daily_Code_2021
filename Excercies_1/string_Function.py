name="    Pratiksha   "
print(name)
#Strip remove the blank Spaces
print(name.strip())
print(len(name))

Last_name="Sawandkar"
print(Last_name[2:5])
print(Last_name)
var=Last_name.lower()
print(var)
var2=Last_name.replace("r" , "t")
print(var2)
var3=Last_name.lower()
print(var3)

#Remove , Using The replace method
friends="Pratiksha, Sudarsha, Kattyani, Priya"
var4=friends.replace(","," ")
print(var4)
var5=friends.replace(", ","\n")
print(var5)

#concat String 
str1="Pratiksha"
str2="Balaji"
str3="Sawandkar"

str4=str1+" "+str2+ " "+str3
print(str4)

#Used Place Holders
temp="This is a {} and is a good girl name {}".format(str1, str2)
print(temp)

str5="Maya"
temp1=f"this is a {str1} and she is good girl {str5}"
print(temp1)

#Operators
a=20
b=60

print(a + b) # Addition
print (a - b) #Sub
print (a * b) #Mul
print (a / b) #Div
print (a ** b) #Exponentiation
print (a // b) #Floot Division
print (a % b) #Modula