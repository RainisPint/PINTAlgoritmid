# Ülesanne 1: Lineaarotsing (Linear Search) 
 # 1. Rakendage Linear Search algoritm vabalt valitud programmeerimiskeeles. 

linear_search.algo3.py file

2. Analüüsige oma algoritmi aja- ja ruumikomplekssust. 
Ajakomplektssus: 
Kuna linear search läbib kõik elemendid ükshaaval, kuni leitakse õige element siis halvimal juhul peab see läbima kogu massiivi ehk tema ajaline keerukus on seega O(n).
Parimal juhul on selle ajaline keerukus O(1).
Ruumikomplektssus: 
Täiendavat ruumi ei ole vaja, kuna otsing toimub ainult ette antud massiivis, ehk ruumikomplektsus on O(1).

4. Arutlege lühidal, kuidas Linear Search algoritmi saab kasutada 
reaalmaailma rakendustes ja millised on selle piirangud. 

Hea kasutada: 
Väiksed järjendid, töötab hästi kui andmed ei ole sorteeritud, hea ühekordsete 
otsingutoimingute jaoks sortimata järjendis, koodi lihtsuse eelistamine.

Reaalmaailma rakendused: 
Raamatute leidmine riiulilt ehk otsib niikaua kuni leiab õige (kui see pole just väga pikk või suur riiul).
Kontaktide otsing, otsib konkreetset inimest kontaktiloendis.
Mingi nime leidmine kuskilt andmestikust ehk sisestada otsitav väärtus ja linear search leiab selle väärtuse talle etteantud listist.
     
Piirangud:
Ebaefektiivne suurte järjendite jaoks, sest võib olla aeglane, kontrollides iga elementi.
Ei sobi sorteeritud järjenditele.
Pole optimaalne suurte andmebaaside puhul, st. et lineaarsest otsingust võivad olla osad algoritmid kiiremad, nagu nt indekseerimine.
Kui andmed on järjestatud, siis võiks kasutada selle asemel hoopis binary searchi, sest see võimaldab poolitamist ja kiiremat leidmist, kui linear search, kus igat elementi kontrollitakse ühekaupa.


# Ülesanne 2: Kahendotsingu (Binary Search) rakendamine ja analüüs 
1. Kirjutage programm, mis teostab Binary Search'i sorteeritud täisarvude massiivil. 
Binary Searchi näide pythonis:

binary_search.algo3.py file

2. Võrrelge teoreetilises analüüsis valminud Binary Search'i ja Linear Search'i aegkomplekssust. 

Binary Search: 
Aegkomplekssus on O(log n), parimal juhul O(1), kus n on massiivi pikkus. Binary search jagab otsinguintervalli pooleks igal sammul ehk selle tõttu hoiab ta aega kokku. Otsimise aeg on seotud logaritmiliselt massiivi suurusega, on parem suuremate massiivide korral.


Linear Search: 
Aegkomplekssus on O(n), kus n on massiivi pikkus. Linear search käib
kõikelemendid läbi ükshaaval, ehk ajaline komplekssus sõltub ka 
andmemahu suurusest.


3. Tooge näide stsenaariumist, kus Binary Search on kasulikum kui Linear Search, ja selgitage miks. 

Oletame näiteks, et n = 1000 ehk võrdleme ajakomplekssust. Kui linear 
search on see O(n), siis binary search  O(log n). Ehk kui n on elementide 
arv, siis linear searchi võib kuluda elemendi leidmiseks O(1000) sammu. 
Küll aga binary search kuluks selleks O(log2(1000)) = 10 sammu. Seega on 
binary search efektiivne suurte andmemahtudega töötamisel. Linear search 
läbib selle elementide kaupa, Binary aga lõikab massiivi iga sammuga 
pooleks, vähendades otsitava ala suurust.

# Ülesanne 3: Jump Search 
1. Kirjutage lühike ülevaade Jump Search algoritmist, sealhulgas selle põhiprintsiibid ja pseudo-koodi näide.

jump_search.algo3.py file

Põhiprintsiibid: 
Jump Search on mõeldud sorteeritud massiividele. Selle põhimõte on see, et algoritm hüppab kindlate sammude kaupa sorteeritud massiivis ja kontrollib, kas otsitav element on hüpete vahelisel alal. 
Töötab hüppamise teel fikseeritud arv sammude kaupa edasi, selle asemel, et kontrollida iga elementi. 
Pärast hüpet, kui element on suurem, viib läbi lineaarotsingu eelmises bloks, kui elementi pole leondis siis otsing lüppeb. 


3. Võrrelge Jump Search'i ajalist komplekssust Linear Searchi ja Binary Searchiga. 

Jump Searchi ajaline komplekssus on O(√n) või siis O(sqrt(n)). See tuleneb hüppamisest ja lineaarostingust. Jump Search on efektiivsem kui lineaarotsing aga vähem efektiivsem kui Binary search ja Ternary Search.

3. Arutlege lühidalt stsenaariumite üle, kus Jump Search võib olla efektiivsem võrreldes Linear Searchi ja Binary Searchiga.

Kui massiivis on suured muutused, ehk elementide väärtused võivad minna väga suureks, siis jump search annab sellistes olukordades eelise binary searchi ees, kus ta võib olla rohkem tundlikum suurtele muutustele.
Suurte massiivide puhul on jump search parem binary searchist ja ka Linear Searchist, sest see vajab tegutsemiseks vähem mälu ja on ka kiirem.
Kui massiivid on sorteeritud, kulub jump searchil õige elemendi leidmiseks vähem aega.



# Ülesanne 4: Kolmikotsing ja Kahendotsing (Ternary Search vs Binary Search) 
1. Kirjutage lühike ülevaade Ternary Search algoritmist, sealhulgas selle põhiprintsiibid ja pseudo-koodi näide.

Ternary_search.algo3.py file
 
Ternary Search on sarnane Binary Searchile aga  jagab massiivi kolmeks osaks ja kontrollib, kas nõutav on ühes kolmest osast.
Ternary Searchi näide pythonis:

2. Võrrelge Ternary Search'i ja Binary Search'i aegkomplekssust. (Kas mõõdetud tulemus, teoreetiline võrdlus, vms) 

Ajaline komplekssus halvimal juhul O(log3 n), parimal juhul O(1), Keskmisel 
juhul O(log3 n). Komplekssust mõjutavad otsinguruumi suurus ja sihtväärtuse 
koht massiivis.

3. Arutlege lühidalt, kas Binary Search on üldiselt tõhusam kui Ternary Search ning millistes olukordades. 

Üldiselt võiks Binary Search olla efektiivsem kui Ternary Search, sest jagab 
massiivi kolme asemel kaheks osaks, kuid kui massiivis on korduvaid 
elemente, siis jätab Ternary need vahele ehk on kiirem kui Binary. Samuti on 
hea kasutada Ternary Searchi kui element asub suurel alal või on teada,millises 
kolmandikus element asub.


# Ülesanne 5: Otsingualgoritmide praktiline rakendamine 
Valige reaalmaailma probleem, kus otsingualgoritmi saab rakendada, ja kirjeldage konkreetse algoritmi sobivust stsenaariumi jaoks. Näited sellistest reaalmaailma probleemidest hõlmavad: 
1. Konkreetse raamatu otsimine raamatukogu kataloogist. 
2. Toote otsimine veebipoest. 
3. Saadaolevate lendude leidmine lennufirma broneerimissüsteemis. 4. Patsiendi andmete tõhus taastamine haigla andmebaasist. 
5. Kiire kontakti leidmine telefoni- või e-posti rakenduses. 
6. Konkreetse filmi või saate otsimine voogedastusplatvormil. 
7. Konkreetse faili või kausta leidmine arvutis. 
8. Sõna otsimine sõnaraamatust. 
9. Kasutaja või konkreetse sisu otsimine sotsiaalmeedia platvormidel. 10. Konkreetse eseme otsimine ettevõtte süsteemis. 
Pärast ühe nende stsenaariumide või mõne muu sarnase reaalmaailma probleemi valimist kirjeldage, milline otsingualgoritm oleks kõige tõhusam ja miks. Arutage ka potentsiaalseid modifikatsioone, mis võiksid algoritmi teie valitud rakenduse jaoks optimeerida. Pidage meeles, et tuleb arvestada andmete omadusi, nagu suurus, struktuur ja uuendamise sagedus.
Reaalmaailma probleem: Konkreetse raamatu otsimine raamatukogu kataloogist
Kuna raamatuid on palju siis just selle õige leidmine võib olla tüütu ja aeganõudev.
Raamatu otsimiseks võiks kasutada näiteks Binary Searchi, sest tavaliselt ongi raamatukogus raamat kas pealkirja või autori järgi järjestatud ehk sorteeritud, mis sobib Binary searchile.
Binary search oleks hea aja efektiivsuselt, sest binary search on logaritmilise ajakomplekssusega.
Kui raamatukogu külastaja teaks ette juba, millist raamatut ta kas autori või pealkirja järgi tahab, siis saaks algoritmi tööd optimeerida, söötes talle ette nt juba listi, kus on ainult konkreetse autori teosed või sama algustähega pealkirjade loetelu.
Samuti võib luua populaarsemaid otsingukriteeriume, mis kiirendaks otsimist.
Uuendamise sagedus ei tohiks Raamatukogus olla väga tihe seega Binary search peaks olema sellisele reaalmaailma probleemile sobilik. Isegi kui tulevad uued raamatud, saab need panna kuhugi teise listi mille nimi võiks olla “uued tooted”, nii saaks eraldada vanad head raamatud uutest.



# Boonusülesanne (2 punkti): 
Kirjeldage lühidalt Fibonacci Search algoritmi ja selgitage, kuidas seda saab kasutada suuremahuliste andmete sorteeritud massiivides. Töötage välja konkreetne stsenaarium, kus Fibonacci Search oleks efektiivsem kui teised otsingualgoritmid, näiteks Binary Search või Ternary Search. Selgitage, miks valitud stsenaariumis on Fibonacci Search parem valik, arvestades andmestruktuuri omadusi ja otsinguvajadusi.

Fibonacci Search algoritm:
Sarnaneb Binary Searchiga, kuid kasutab Fibonacci arve otsinguintervalli määrmaiseks. Jagab masiivi kaheks osaks. Eemaldab mittevajalikud elemendid.

Seda saab kasutada suuremahuliste andmete sorteeritud massiivides, kui määratakse Fibonacci arvud, mis on suuremad või võrdsed massiivi pikkusega. On vähem efektiivsem, kui tegu on väikese massiiviga. Massiiv jagatakse kaheks osaks, kasutades Fibonacci arve ja võrreldes neid otsitava väärtusega. Protsess kordub, kuni leitakse otsitav element. Võib kasutada ka andmebaasi otsingus, tekstiotsingus vüi suurtes sorteeritud loendites. On kiirem suuremate loendite jaoks.

Efektiivne Fibonacci stsenaarium oleks siis, kui suuremahulise massiivi keskel on otsitav element, siis jüuaks Fibonacc selleni kiiremini kui Binary Search või Ternary Search. Kuna Fibonaccil kuluks otsitava elemndi jaoks vähem samme, siis oleks ta ka ajakomplekssuselt parem valik. 
