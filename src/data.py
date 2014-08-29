from itertools import izip
import csv
from varazslat import Varazslat
from osztaly import Osztaly

class Data:

  def __init__(self):
    self.classes = {}
    self.spells = {}


  def read(self):
    a = izip(*csv.reader(open('/home/ldudas/git/BCG/data/MUD_Osztalyok.csv', 'rb') , delimiter=',', quotechar='|'))
    for row in a:
      osztaly = Osztaly(row[0], row[1])
      self.classes[row[0]] = osztaly
      for x in range(2, len(row)):
        if len(row[x]) > 1:
          parts = row[x].split(' ')
          varazslatnev = " ".join(parts[1:len(parts)])
          osztaly.spells.append(varazslatnev)
          if varazslatnev in self.spells:
            varazslat = self.spells[varazslatnev][0]
          else:
            varazslat = Varazslat(varazslatnev)
            self.spells[varazslatnev] = [varazslat, []]
            self.spells[varazslatnev][1].append(row[0])
