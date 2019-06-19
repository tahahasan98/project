#1
radius = float(input("Radius is: "))
pi = 3.14
area = radius * radius * pi
print ("The area of a circle with radius", radius,)
print (area)

#2
fname = input("Enter your First Name: ")
lname = input("Enter your Last Name: ")
print ("Hello  " + lname + " " + fname)

#3
values = input("Input some comma separated numbers: ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

#4
def getfile():
    name = input("The file name is: ")
    extension = name.split('.')
    print ('The extension is ', repr(extension[-1]))
getfile()

#5
color_list = ["Red","Green","White" ,"Black"]
print( "%s %s"%(color_list[0],color_list[-1]))

#6
def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2

print(difference(45))
print(difference(12))



#8
text = input("enter your text").lower()

text_2 = text.split("is", 1)

if text_2[0] == "":

    print(text.capitalize())

else:

    print("is", text)

#9

def number():
    str=input("enter a string : ")
    count=int(input("enter a count to make of copies : "))
    if(len(str)>0):
        print(str*count)
    else:
        print("string is invalid")

number()

#10
num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")

#11
def list_count(num):
  count = 0
  for nums in num:
    if nums == 4:
      count = count + 1

  return count

print(list_count([3, 4, 4, 3, 4]))

#12
def two_first(word, n):
    if len(word)>=2:
        for p in word[:1]:
            for d in word[1:2]:
                return n*(p+d)
        else:
            return n*word
print(two_first("Test", 3))

#13
Vowel = ["a", "e", "i" , "o" , "u"]

def check_letter(str):
    if str in Vowel :
        print("entered letter is vowel")
    else:
        print ("entered letter is consonant")

check_letter(str)

#14
def is_group_member(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))

#15
num=int(input('Enter a number:'))
def funct1(num):
    if num in range(900,1100) or num in range(1900,2100):
        return(True)
    else:
        return(False)
print(funct1(num))