def binary_search(minu_list, otsitav):
    low, high = 0, len(minu_list) - 1   #määrame algväärtused 
    while low <= high:
        keskmine = (low + high) // 2         #leiame keskmine indeksi ja selle väärtuse
        keskmine_vaartus = minu_list[keskmine]

        if keskmine_vaartus == otsitav:          #kontrollime, kas keskmine väärtus on otsitav element
            return keskmine                  #kui element leitud tagastab indeksi
        elif keskmine_vaartus < otsitav:
            low = keskmine + 1               #otsib paremalpool keskpunkti
        else:
            high = keskmine - 1              #otsib vasakulpool keskpunkti
    return -1                           #tagastab -1, kui elementi pole leitud


minu_list = [1, 2, 5, 7, 8, 9, 10, 22, 44, 100] #peab olema sorteeritud
otsitav = 100

tulemus = binary_search(minu_list, otsitav)

if tulemus != -1: #kontrollib, kas lineaarotsingu tulemusena saadud indeks ei ole -1, kui tulemus on erinev, siis see on õige vastus
    print(f"{otsitav} on listis {tulemus}. kohal")
else:
    print(f"{otsitav} ei leitud listist.")
