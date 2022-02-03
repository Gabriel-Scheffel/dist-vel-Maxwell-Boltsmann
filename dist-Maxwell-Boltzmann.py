import matplotlib.pyplot as plt
import numpy as np


def MB_speed(v, m, T):
    """
    :param v: velocidades das moléculas
    :param m: massa da molécula estudada
    :param T: temperatura da atmosfera
    :return: função de densidade de probabilidade
    Calcula a distribuição de velocidades para um gás ideal
    conhecida como distribuição de Maxwell-Boltzmann.
    """
    kB = 1.38e-23  # constante de Boltzmann
    return (m/(2*np.pi*kB*T))**1.5 * 4*np.pi * v**2 * np.exp(-m*v**2/(2*kB*T))


v = np.arange(0, 8000, 1)                   # distribuição das velocidades
el = int(input('Massa(u): '))               # massa atômica u do elemento
mass = el * 1.66e-27                        # massa da molécula em kg
temp1 = int(input('Temperatura 1(K): '))    # temperatura da atmosfera 1
temp2 = int(input('Temperatura 2(K): '))    # temperatura da atmosfera 2

plt.plot(v, MB_speed(v, mass, temp1), 'b', label=f'T={temp1} K')
plt.plot(v, MB_speed(v, mass, temp2), 'r--', label=f'T={temp2} K')
plt.title('Distribuição de Velocidade para a molécula')  # você pode trocar 'molécula' pelo nome do elemnto usado ;)
plt.xlabel('v(m/s)')
plt.ylabel('f(v)')
plt.legend()
plt.show()

"""
 Alguns valores para exemplo:
 Elemento argônio(Ar) - massa(u) = 40
 temperaturas t1=196 K t2=415 K
"""