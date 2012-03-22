#!/usr/bin/env python
import sys
import enchant
import itertools

def permute(string, numchars):
  words = {}
  count = 0
  d = enchant.Dict("en_US")
  #l = list(string)
  perms = itertools.permutations(string, int(numchars))
  #now have a spellchecker and all permutations
  #keep only words which are valid and <= numchars and not seen before
  while True:
    try:
      word = perms.next()
      wd = "".join(word) #convert list to word
      if len(wd) <= numchars and d.check(wd) and wd not in words:
        print wd
        count += 1
        words[wd] = 1
    except StopIteration:
      break
  print count, " possible words"

def main():
  if not len(sys.argv) == 3:
    print "usage: ./permuter.py <charstring> <numchars>"
    return
  permute(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
  main()
