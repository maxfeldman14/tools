#!/usr/bin/env python
import sys
import enchant
import itertools

def permute(string, numchars):
  d = enchant.Dict("en_US")
  l = list(string)
  perms = list(itertools.permutations(l))
  #now have a spellchecker and all permutations
  #keep only words which are valid and <= numchars
  for word in perms:
    wd = "".join(word) #convert list to word
    if len(wd) <= numchars and d.check(wd):
      print wd

def main():
  if not len(sys.argv) == 3:
    print "usage: ./permuter.py <charstring> <numchars>"
    return
  permute(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
  main()
