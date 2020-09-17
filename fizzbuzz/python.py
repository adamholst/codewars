def fizzbuzz(n):
  for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
      print('FizzBuzz')
    elif i % 3 == 0:
      print('Fizz')
    elif i % 5 == 0:
      print('Buzz')
    else:
      print(i)
      
def oneLiner(n):
  for i in range(n):print(i%3//2*'Fizz'+i%5//4*'Buzz'or i+1)
