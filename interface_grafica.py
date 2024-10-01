import matplotlib.pyplot as plt
import sys
import numpy as np

x = [ ]
y = [ ]

print('Você gostaria de montar um gráfico? (s/n): ')
r = input('s caso SIM e n caso NÃO: ') 
if r != 's':
    print('PARA QUÊ VOCÊ ME INICOU?')

else:   
    cnt1 = 0
    nmr = int(input('nmr:'))
    for i in range(0, nmr):
        n = float(input('n:'))
        x.append(n)
        cnt1 += 1 

    cnt2 = 0
    for i in range(0, nmr):
        z = float(input('z:'))
        y.append(z)
        cnt2 += 1 


plt.plot(x,y)
plt.show()