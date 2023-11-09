#!/usr/bin/python3

wday["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
regins=[];eday=[];vehicles=[];trips=[]
f = open("uber_exp.txt", "rt")
for line in f:
  line = line.strip()
  text = line.split(",")
  day = text[1]
  day = day.split("/")
  day = day[1]
  if day == "1" or day == "8" or day == "15":
    eday.append(wday[3])
  elif day == "2" or day == "9":
    eday.append(wday[4])
  elif day == "3" or day == "10":
    eday.append(wday[5])
  elif day == "4" or day == "11":
    eday.append(wday[6])
  elif day == "5" or day == "12":
    eday.append(wday[0])
  elif day == "6" or day == "13":
    eday.append(wday[1])
  else:
    eday.append(wday[2])
  regins.append(text[0])
  vehicles.append(text[2])
  trips.append(text[3])
z = sorted(zip(regins,eday,vehicles,trips))

f=open("uberoupput.txt", "wt")
for i,j,k,l in z:
  f.write("%s,%s %s,%s\n" %(i,j,k,l))
f.close()
