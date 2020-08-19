import numpy as np
import math
import matplotlib.pyplot as plt
from ipywidgets import widgets,interact

@interact(n=(3,20,0.5),continuous_update=True)
def ret(n):
    x = np.arange(1,n,1)
    y1 = np.ones(x.shape)
    y2 = np.log2(x)
    y4 = x
    y3 = x*np.log2(x)
    y5 = x**2
    y6 = x**3
    y7 = 2**x
    y8 = 3**x
    y9 = []
    for i in range(len(x)):
        y9.append(math.factorial(i))
    
    plt.figure(figsize=(7,7))
    plt.plot(x,y1)
    plt.plot(x,y2)
    plt.plot(x,y3)
    plt.plot(x,y4)
    plt.plot(x,y5)
    plt.plot(x,y6)
    plt.plot(x,y7)
    plt.plot(x,y8)
    plt.plot(x,y9)
    plt.legend(['c','log2(x)','x*log2(x)','x','x^2','x^3','2^x','3^x','x!'])
    plt.show()
