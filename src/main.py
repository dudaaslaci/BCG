from varazslat import Varazslat
from osztaly import Osztaly
from data import Data
from frame import MainFrame


from Tkinter import *

data=Data()
data.read()

root = Tk()
root.geometry("350x300+300+300")
app = MainFrame(root)


i = 0
for oszt in data.classes:
  app.createClassButton(oszt, i%5 + 1, i/5)
  i =i +1
  print i
root.mainloop()
