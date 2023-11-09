#!/usr/bin/python3

f = open("movies_exp.txt", "rt")
animation=0;children=0;comedy=0;adventure=0;fantasy=0;romance=0;drama=0;action=0;crime=0;thriller=0;horror=0;sci=0;doc=0
for line in f:
  line = line.strip()
  text = line.split("::")
  genre = text[2]
  genre = genre.split("|")
  for i in genre:
    if i == "Animation":
      animation += 1
    elif i == "Children's":
      children += 1
    elif i == "Comedy":
      comedy += 1
    elif i == "Adventure":
      adventure += 1
    elif i == "Fantasy":
      fantasy += 1
    elif i == "Romance":
      romance += 1
    elif i == "Drama":
      drama += 1
    elif i == "Action":
      action += 1
    elif i == "Crime":
      crime += 1
    elif i == "Thriller":
      thriller += 1
    elif i == "Horror":
      horror += 1
    elif i == "Sci-Fi":
      sci += 1
    elif i == "Documentary":
      doc += 1
g1 = ["Animation", "Children's", "Comedy", "Adventure", "Fantasy", "Romance", "Drama", "Action", "Crime", "Thriller", "Horror", "Sci-Fi", "Documentary"]
g2 = [animation, children, comedy, adventure, fantasy, romance, drama, action, crime, thriller, horror, sci, doc]
countgenre = zip(g1,g2)
f = open("movieoutput.txt", "wt")
for line1,line2 in countgenre:
  f.write("%s %d\n" %(line1,line2))
f.close()
    
