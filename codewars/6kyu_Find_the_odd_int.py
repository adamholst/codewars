'''
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
'''

def find_it(seq):
  result = 0
  for num in seq:
      result = result ^ num
  return result
  
def oneLiner(seq):
  return [x for x in seq if seq.count(x) % 2][0]
