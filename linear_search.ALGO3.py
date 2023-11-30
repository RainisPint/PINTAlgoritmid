def linear_search(minu_list, otsitav): #teen definitsiooni
    for i in range(len(minu_list)):
        if minu_list[i] == otsitav:
            return i               #tagastab indeksi, kui element on leitud
    return -1                      #tagastab -1, kui elementi pole leitud


minu_list = [2, 7, 9, 12, 20, 15, 77, 33, 44, 55, 23, 21, 11]
otsitav_element = 11

tulemus = linear_search(minu_list, otsitav_element) # kutusn defi uuesti välja

if tulemus != -1: #kontrollib, kas lineaarotsingu tulemusena saadud indeks ei ole -1, kui tulemus on erinev, siis see on õige vastus
    print(f"{otsitav_element} on listis {tulemus}. kohal")
else:
    print(f"{otsitav_element} ei leitud listist")
