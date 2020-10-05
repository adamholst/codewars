'''
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
'''

def square_digits(num):
  lst = []
  lst2 = []
  new_num = str(num)
  for i in new_num:
    lst.append(int(i))
  for i in lst:
    i = i ** 2
    lst2.append(i)
  result = ''.join(map(str, lst2))
  return int(result)

def oneLiner(num):
  return int(''.join(str(int(i)**2) for i in str(num)))
