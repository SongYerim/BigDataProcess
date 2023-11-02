#!/usr/bin/python3
from openpyxl import load_workbook

wb = load_workbook(filename='student.xlsx')
ws = wb['Sheet1']

total=[]
for r in range(2,76):
  total.append(ws.cell(row=r,column=7).value)
total.sort(reverse=True)

stu_cnt=len(total)
a=total[11]
a0=total[int(stu_cnt*0.3)-1]
b=total[35]
b0=total[int(stu_cnt*0.7)-1]
c=total[61]
for r in range(2,76):
  tmp = ws.cell(row=r, column=7).value
  if tmp >= a:
    ws.cell(row=r,column=8,value='A+')
  elif tmp >= a0:
    ws.cell(row=r,column=8,value='A0')
  elif tmp >= b:
    ws.cell(row=r,column=8,value='B+')
  elif tmp >= b0:
    ws.cell(row=r,column=8,value='B0')
  elif tmp >= c:
    ws.cell(row=r,column=8,value='C+')
  elif tmp >= 40:
    ws.cell(row=r,column=8,value='C0')
  else:
    ws.cell(row=r,column=8,value='F')
wb.save(filename='student.xlsx')
