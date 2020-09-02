'''
Complete the function to convert an integer into a string of the Turkish name.

input will always be an integer 0-99;
output should always be lower case.
'''
def get_turkish_number(num):
  dict_ones = {
    0: "sıfır",
    1: "bir",
    2: "iki",
    3: "üç",
    4: "dört",
    5: "beş",
    6: "altı",
    7: "yedi",
    8: "sekiz",
    9: "dokuz"
  }
  
  dict_tens = {
    1: "on",
    2: "yirmi",
    3: "otuz",
    4: "kırk",
    5: "elli",
    6: "altmış",
    7: "yetmiş",
    8: "seksen",
    9: "doksan"
  }
  
  if num < 10:
    return dict_ones[num]
  ones = num % 10
  tens = num / 10
  if ones == 0:
    return dict_tens[tens]
  return dict_tens[int(tens)] + " " + dict_ones[ones]
    

print(get_turkish_number(55))
