class Osztaly:

  def  __init__(self, nev, jellemek):
    self.nev = nev
    self.jellemek = jellemek
    self.spells = []

  def kompatibilis(o1, o2, o3):
    if o1.jellemek[0] == '+' and o2.jellemek[0] == '+' and o3.jellemek[0] == '+':
      return True
    if o1.jellemek[1] == '+' and o2.jellemek[1] == '+' and o3.jellemek[1] == '+':
      return True
    if o1.jellemek[2] == '+' and o2.jellemek[2] == '+' and o3.jellemek[2] == '+':
      return True
    return False

  def addSpell(self, spell):
    self.spells.append(spell)
