from math import sqrt

def jump_search(list, otsitav):
    n = len(list)
    hüpe = int(sqrt(n))                       #hüppame massiivis ringi, samm on ruutjuur massiivi pikkusest
    i = 0
    
    
    while i < n and list[i] < otsitav:                     #hüppame kuni leitakse suurem või võrdne element
        i += hüpe

  
    for j in range(max(0, i - hüpe), min(i, n)):         #lineaarne otsing hüppeintervalli sees
        if list[j] == otsitav:
            return j                                     #tagasta indeks, kui element on leitud

    return -1                                            #tagasta -1, kui elementi pole leitud


minu_list = [2, 4, 7, 11, 17, 21, 30, 36, 38, 47, 55, 59] #peab olema sorteeritud
otsitav_element = 36


tulemus = jump_search(minu_list, otsitav_element) #kutsume defi välja


if tulemus != -1:  #kontrollib, kas lineaarotsingu tulemusena saadud indeks ei ole -1, kui tulemus on erinev, siis see on õige vastus
    print(f"{otsitav_element} on listis {tulemus}. kohal")
else:
    print(f"{otsitav_element} ei leitud listist.")


