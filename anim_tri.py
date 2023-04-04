import random
import matplotlib.pyplot as plt
import numpy as np
import time
import matplotlib.animation as animation

def genererUneListe(N):
    uneListe = list()
    for n in range(0,N,1):
        uneListe.append(random.randint(0, 100))
    return uneListe

def triParSelection(laListe, list_of_pos):
    
    for i in range(len(laListe)):
        min = i
        for j in range(i+1, len(laListe)):
            if laListe[j] < laListe[min]:
                min = j
        if min != i:
            laListe[i], laListe[min] = laListe[min], laListe[i]
            list_of_pos.append(laListe.copy())
            

L = 7
x_list = np.arange(L)

new_list = genererUneListe(L)
old_list = new_list.copy()

sorted_list = list()

triParSelection(new_list, sorted_list)



fig = plt.figure(figsize=(8,6))
axes = fig.add_subplot(1,1,1)
axes.set_ylim(0, 150)


##########################



def animate(i):  
       
    plt.bar(x_list, sorted_list[i])
       
       
            
            
##########################
anim = animation.FuncAnimation(fig, animate, frames=500, interval=100, blit=False)


print(old_list, sorted_list)