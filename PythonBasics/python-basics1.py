string1 = "Length of this String"
print ("length of this string is", len(string1))

test_str = "www.google.com"
res = {}
for keys in test_str:
    res[keys] = res.get(keys, 0) + 1
print ("Letter Frequency", str(res))
string2 = 'Environment'
print("First and Last 2 Characters in this string = " , string2[0:2] + string2[-2:])


def change_letter(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]
  return str1
print(change_letter('why wont this work'))


def rearrange_letters(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]
  return new_a + ' ' + new_b
print(rearrange_letters('abcdefg', 'hijklmnop'))



def add_ing(str2):
  length = len(str2)
  if length > 2:
    if str2[-3:] == 'ing':
      str2 += 'ly'
    else:
      str2 += 'ing'
  return str2
print(add_ing('abc'))



str3 = "The man is not that poor!"
not_location = str3.find('not')
poor_location = str3.find('poor')
if not_location < poor_location and not_location!=-1:
    str3 = str3 [:not_location] + "good" + str3[poor_location+4:]
print(str3)



def longestword():
    list1 =["Pizza", "Burgers", "Pineapple"]
    longest = list1[0]
    for item in list1:
        if len(item) > len(longest):
            longest = item
    return len(longest)
print(longestword())



def remove_letter(str, n):
    first_letter = str[:n]
    last_letter = str[n + 1:]
    return first_letter + last_letter
print(remove_letter('bananas', 0))
print(remove_letter('bananas', 4))


def change_word(str4):
    return str4 [-1:]+str4[1:-1]+str4[:1]
print(change_word('Jaguar'))



def odd_values_string(str):
    for i in range(0,len(str),2):
        print(str[i],end='')
print (odd_values_string('Banana'))

sentence = 'this is the sentence for this question.'

from collections import Counter

def a_sentence():
    b_sentence = input('Enter a sentence: ')
    c_sentence = b_sentence[:-1]
    words = c_sentence.split()
    a = Counter(words)
    return a
print(a_sentence())

word = input('enter the words:')
answer = word.upper()
answer1 = word.lower()
print(answer, answer1)

w = ['red', 'white', 'black', 'red', 'green', 'black']
print(*(sorted(set(w))))