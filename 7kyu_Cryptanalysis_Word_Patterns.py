'''
In cryptanalysis, words patterns can be a useful tool in cracking simple ciphers.

A word pattern is a description of the patterns of letters occurring in a word, where each letter is
given an integer code in order of appearance. So the first letter is given the code 0, and second is
then assigned 1 if it is different to the first letter or 0 otherwise, and so on.

As an example, the word "hello" would become "0.1.2.2.3". For this task case-sensitivity is ignored,
so "hello", "helLo" and "heLlo" will all return the same word pattern.

Your task is to return the word pattern for a given word. All words provided will be non-empty strings
of alphabetic characters only, i.e. matching the regex "[a-zA-Z]+".
'''

def word_pattern(word):
  chars = dict()
  pattern = ""
  for c in word.lower():
    if not chars:
      chars[c] = 0
      pattern = "0"
    else:
      if c not in chars:
        chars[c] = max(chars.values()) + 1
      pattern = ".".join([pattern, str(chars.get(c))])
  return pattern

print(word_pattern('Hippopotomonstrosesquippedaliophobia'))

'''
def word_pattern(s):
    return '.'.join(str(list(dict.fromkeys(s.lower())).index(i)) for i in s.lower())
'''
