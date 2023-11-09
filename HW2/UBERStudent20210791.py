#!/usr/bin/python3

import sys
from datetime import datetime
wday["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
uber_d = dict()
openf=sys.argv[1]
with open(openf, "rt") as f:
  for line in f:
    line = line.strip()
    text = line.split(",")
    date = text[1]
    datetime_date = datetime.strptime(date, '%m/%d/%Y')
    week = wday[datetime_date.weekday()]  
    regins=text[0]+','+week+" "+text[2]
    trips=text[3]
    if regins not in uber_d:
      uber_d[regins]=trips
      
closef=sys.argv[2]
with open(closef, "wt") as f:
  for key,value in uber_d.itmes():
    f.write("%s,%s\n" %(key,value))
