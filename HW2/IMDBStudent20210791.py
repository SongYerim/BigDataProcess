#!/usr/bin/python3
import sys

openf = sys.argv[1]
genre_d = dict()
with open(openf, "rt") as f:
  for line in f:
    line = line.strip()
    text = line.split("::")
    genre = text[2]
    genre = genre.split("|")
    for i in genre:
      if i in genre_d:
        genre_d[i] = 1
      else:
        genre_d[i] += 1
name = genre_d.keys()
count - genre_d.values()
z = zip(name, count)

closef=sys.argv[2] 
with open(closef, "wt") as f:
  for key,value in z:
    f.write(key+" "+str(value)"\n")
    
