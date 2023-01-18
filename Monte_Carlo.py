import random
import matplotlib.pyplot as plt

y1 = 6
y2 = 0
x = 6

#indeksi loma
yn1 = 6
n1 = 1         #vakuum
yn2 = 4
n2 = 1.33      #voda
yn3 = 2
n3 = 1.5       #staklo

listaY = [y1, yn2, yn3, y2]
listaN = [n1, n2, n3]


def t(n, x1, x2, y1, y2,c = 299792458):
    return (n*((x2-x1)**2 + (y2-y1)**2)**0.5)/c


def next_position(x, currentX):
    d = round(random.uniform(0, x - currentX), 2)
    currentX += d
    return currentX


tMin = 10
for j in range(100):  #za 100 pokušaja
    listaX = [0]
    currentX = 0
    tUk = 0
    for i in range(len(listaY)-1):
        currentX = next_position(x, currentX)
        listaX.append(currentX)
    listaX.pop()
    listaX.append(6)
    plt.plot(listaX, listaY)

    for k in range(len(listaX) - 1):
        tUk += t(listaN[k], listaX[k], listaX[k+1], listaY[k], listaY[k+1])
    if tUk < tMin:
        tMin = tUk
        listaXmin = listaX.copy()
        listaYmin = listaY.copy()


print(listaXmin)

plt.plot([0,6], [yn2, yn2], color = "grey", linestyle = "dashed")
plt.plot([0,6], [yn3, yn3], color = "grey", linestyle = "dashed")

plt.show()

plt.plot(listaXmin, listaYmin)
plt.plot([0,6], [yn2, yn2], color = "grey", linestyle = "dashed")
plt.plot([0,6], [yn3, yn3], color = "grey", linestyle = "dashed")
plt.show()


#sad triba pamtit tg(theta), vrime koje računamo iz v i n







#triba napravit da se lomi za nasumičnu količinu iz intervala [-x, x]



#triba usporedit vrimena za svaku liniju