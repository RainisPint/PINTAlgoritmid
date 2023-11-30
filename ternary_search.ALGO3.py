def ternary_search(arr, target):
    algus = 0                #algus ja lopp on massiivi otsitavad alad
    lõpp = len(arr) - 1
    
    while algus <= lõpp: 
        kolmandik = (lõpp - algus) // 3
        m1 = algus + kolmandik
        m2 = lõpp - kolmandik
        
        if arr[m1] == target:            #element leitud esimeses kolmandikus
            return m1  
        elif arr[m2] == target:          #element leitud kolmandas kolmandikus
            return m2  
        elif target < arr[m1]:           #otsi esimeses kolmandikus
            lõpp = m1 - 1  
        elif target > arr[m2]:           #otsi kolmandas kolmandikus
            algus = m2 + 1  
        else:                            #otsi teises kolmandikus
            algus = m1 + 1
            lõpp = m2 - 1         
    
    return -1                     #elementi ei leitud


sorteeritud_list = [2, 3, 5, 12, 16, 19, 34, 37, 45, 46, 70]
otsitav = 46
vastus = ternary_search(sorteeritud_list, otsitav)

if vastus != -1:
    print(f"{otsitav} on listis {vastus}. kohal")
else:
    print(f"Element {otsitav} puudub massiivis.")
