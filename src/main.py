from varazslat import Varazslat
from osztaly import Osztaly

print 'hello'
kp = Varazslat('kodpajzs')
druida = Osztaly('druida')
druida.varazslatok.append([kp, 2])
print druida.varazslatok[0][0].nev

