'''
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.
'''

def accum(s):
  inc = 0
  result = ''
  for c in s:
    result += c.upper() + c.lower() * inc + '-'
    inc += 1
  return result[:-1]
  
def oneLiner(s):
  return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
