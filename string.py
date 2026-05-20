#string Operations in python
#print string
str = "I am "
print(str)

#indexing
index = "Harshad"
print(index[0])

#concatnating
merge = str + "" + index
print(merge)

#reapetating
print((index + " ") * 3)

#string membership operators
str1 = "    I am learning python"
print("sweet" in str1)

#common string methods
print(str1.upper())
print(str1.lower())
print(str1.strip())
print(str1.find("g"))
print(str1.replace("Harshad","Shubham"))

#string splitting
words = str1.split()
print(words)