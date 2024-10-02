import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

print("""Você gostaria de montar um gráfico?:\n 
    Digite s -> SIM e n -> NÃO\n
      """)

r = input('Resposta:') 
if r.lower() != 'n':
    nmr = int(input('Quantidade de produtos:'))
    for i in range(nmr):
        n = float(input('Numeração dos produtos:'))
        x.append(n)
         
    for i in range(nmr):
        z = float(input('Quantidade vendida:'))
        y.append(z)

    plt.plot(x, y, label='Dados')
    plt.xlabel('Número de produtos')
    plt.ylabel('Quantidade de vendas')
    plt.title('Gráfico Expositório')
    plt.yticks(y)
    plt.xticks(x)
    plt.legend()
    plt.show()
else:
    print('Tudo bem, OBRIGADO!')
