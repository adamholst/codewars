'''
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!
'''

def create_phone_number(n):
  ph_num = ['(', 'x', 'x', 'x', ')', ' ', 'x', 'x', 'x', '-', 'x', 'x', 'x', 'x']
  for num in n:
    ph_num[1] = n[0]
    ph_num[2] = n[1]
    ph_num[3] = n[2]
    ph_num[6] = n[3]
    ph_num[7] = n[4]
    ph_num[8] = n[5]
    ph_num[10] = n[6]
    ph_num[11] = n[7]
    ph_num[12] = n[8]
    ph_num[13] = n[9]
  return ''.join(str(item) for item in ph_num)

def oneLiner(n):
  return '({}{}{}) {}{}{}-{}{}{}{}'.format(*n)
