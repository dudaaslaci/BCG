from varazslat import Varazslat
from osztaly import Osztaly
from itertools import izip
import csv
from Tkinter import *

osztalyok = {}
varazslatok = {}

a = izip(*csv.reader(open('/home/ldudas/git/BCG/data/MUD_Osztalyok.csv', 'rb') , delimiter=',', quotechar='|'))
for row in a:
  osztaly = Osztaly(row[0], row[1])
  osztalyok[row[0]] = osztaly
  for x in range(2, len(row)):
    if len(row[x]) > 1:
      parts = row[x].split(' ')
      varazslatnev = " ".join(parts[1:len(parts)])
      if varazslatnev in varazslatok:
        varazslat = varazslatok[varazslatnev][0]
      else:
        varazslat = Varazslat(varazslatnev)
        varazslatok[varazslatnev] = [varazslat, []]
      varazslatok[varazslatnev][1].append(row[0])

kombok=[]

for o1 in osztalyok:
  for o2 in osztalyok:
    for o3 in osztalyok:
      if o1 != o2 and o1 != o3 and o2 != o3 and Osztaly.kompatibilis(osztalyok[o1], osztalyok[o2], osztalyok[o3]):
        kombok.append([o1, o2, o3])

root = Tk()

w = Label(root, text="Hello, world!")
w.pack()

root.mainloop()