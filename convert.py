#!/usr/bin/env python
import sys
import os.path

def parse_file(inf):
  f = open(inf, "r")
  parsed = []
  prevCount = 0
  itemizes = 0
  for line in f:
    #first just deal with *s
    count = 0
    if line[0] == '*':
      count = countChar(line, '*')
      #if it is the same as the line before, it is an item
      #if count is greater, it begins a new sub item
      #if it is less than, then an itemize is concluded
      newLine = "\\item " + line[count+1:] + "\n"
      if count == prevCount:
        parsed.append(newLine)
      elif count > prevCount:
        itemizes += 1
        parsed.append("\\begin{itemize}\n")
        parsed.append(newLine)
      else:
        dif = prevCount - count
        for i in range(dif):
          parsed.append("\end{itemize}\n")
        parsed.append(newLine)
        itemizes = count
      prevCount = count
    elif line[0] == '=':
      for i in range(itemizes):
        parsed.append("\end{itemize}\n")
        itemizes = 0
      eqcount = countChar(line, '=')
      rest = line[eqcount+1:-(eqcount+3)]
      size = "\\textbf"
      if eqcount == 1:
        size += "{\LARGE "
      elif eqcount == 2:
        size += "{\Large "
      elif eqcount == 3:
        size += "{\large "
      else:
        size += "{\normalsize "
      size += rest
      size += "}\n"
      parsed.append(size)
      #parsed.append("\\begin{itemize}\n")
      #itemizes += 1
      prevCount = 0
  for i in range(itemizes):
    parsed.append("\end{itemize}\n")
  f.close()
  return parsed

def print_latex(of, parsed):
  f = open(of, "w")
  f.write("""
\documentclass[12pt]{article}
\\begin{document}
\\begin{center}
\\textbf{\LARGE Title} \\\\
\end{center}
  """
  )
  for line in parsed:
    f.write(line)
  f.write("\\end{document}")
  f.close()

def countChar(line, char):
  count = 0
  for ch in line:
    if ch == char:
      count += 1
    else:
      break
  return count

def main():
  if not len(sys.argv) == 3:
    print "Usage: name.py <inputfile.txt> <outputfile.tex>"
    return
  fname = sys.argv[1]
  ofname = sys.argv[2]

  parsedNotes = parse_file(fname)
  print_latex(ofname, parsedNotes)

if __name__ == "__main__":
  main()
