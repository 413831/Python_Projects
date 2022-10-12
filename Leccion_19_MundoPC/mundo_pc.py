from mundo_pc.Raton import Raton
from mundo_pc.Teclado import Teclado
from mundo_pc.Monitor import Monitor
from mundo_pc.Computadora import Computadora
from mundo_pc.Orden import Orden

teclado1 = Teclado('Genius')
raton1 = Raton('Genius','USB')
raton2 = Raton('Logitech','USB')
monitor1 = Monitor('Samsung', 20)
monitor2 = Monitor('LG', 18)
computadora1 = Computadora('PC Gamer',monitor1,teclado1,raton1)
computadora2 = Computadora('PC Standard',monitor2,teclado1,raton2)

#print(computadora1)
#print(computadora2)

orden = Orden([computadora1,computadora2])
print(orden)