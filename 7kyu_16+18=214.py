'''
For this Kata you will have to forget how to add two numbers together.

In simple terms, our method does not like the principle of carrying over
numbers and just writes down every number it calculates :-)
'''

def add(num1, num2):
  a = []
  count = 1
  num1 = str(num1)
  num2 = str(num2)
  if len(num1) < len(num2):
    num1 = num1.zfill(len(num2))
  if len(num1) > len(num2):
    num2 = num2.zfill(len(num1))
  for j in num2:
    b = int(num1[len(num1)-count]) + int(num2[len(num2)-count])
    d = str(b)
    count += 1
    a.insert(0,d)
  return int("".join(a))

def oneliner(num1, num2):
  return int(str(add(a//10,b//10))+str(a%10+b%10)) if a*b else a+b

print(add(16, 18))
