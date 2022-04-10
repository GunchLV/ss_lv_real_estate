
import requests
from bs4 import BeautifulSoup
import pandas as pd

def savac_datus(tab, vieta, pardod_izire, col_skaits):
    for v in range(0, len(visi)):
        rinda = []
        pirmais = visi[v].get_text().split('b>')
        rinda.append(pirmais[0])
        try:
            for i in range(0,col_skaits):
                parejie = soup.find_all(class_='msga2-o pp6')[i+v+(col_skaits-1)*v].get_text()
                if i == 0:
                    a = str(soup.find_all(class_='msga2-o pp6')[v+(col_skaits-1)*v])
                    a = a[40:][:-5]
                    a = a.replace('<br/>',', ')
                    rinda.append(a)
                else:
                    rinda.append(parejie)
            rinda.append(vieta[:-1])
            rinda.append(pardod_izire)
            tab.loc[len(tab)] = rinda
        except:
            break
    return tab


tabula = pd.DataFrame(columns=['Teksts','Adrese','Istabas','m2','Stāvs','Sērija','Cena m2','Cena',
                               'Vieta','Darījuma tips'])
adreses_sakums = 'https://www.ss.com/lv/real-estate/'
ipasuma_tips = 'flats/'
darijuma_tips = ['sell/','hand_over/']
'''
adresu_saraksts = ['jurmala/','riga-region/baldone/','riga-region/balozi/','riga-region/olaine/',
                   'riga-region/salaspils/','riga-region/saulkrasti/','riga-region/sigulda/']
'''
adresu_saraksts = ['jurmala/asari/','jurmala/bulduri/','jurmala/dubulti/','jurmala/dzintari/',
                   'jurmala/jaundubulti/','jurmala/jaunkemeri/','jurmala/kauguri/','jurmala/kemeri/',
                   'jurmala/lielupe/','jurmala/majori/','jurmala/melluzi/','jurmala/priedaine/',
                   'jurmala/pumpuri/','jurmala/sloka/','jurmala/vaivari/','jurmala/valteri/',
                   'riga-region/baldone/','riga-region/balozi/','riga-region/olaine/',
                   'riga-region/salaspils/','riga-region/saulkrasti/','riga-region/sigulda/',
                   'riga-region/vangazi/','riga-region/babites-pag/','riga-region/carnikavas-nov/',
                   'riga-region/daugmales-pag/','riga-region/garkalnes-nov/','riga-region/incukalna-nov/',
                   'riga-region/kekavas-pag/','riga-region/krimuldas-pag/','riga-region/malpils-pag/',
                   'riga-region/marupes-pag/','riga-region/olaines-pag/','riga-region/ropazu-nov/',
                   'riga-region/salaspils-l-t/','riga-region/saulkrastu-l-t/','riga-region/sejas-nov/',
                   'riga-region/stopinu-nov','aizkraukle-and-reg/','aluksne-and-reg/',
                  'balvi-and-reg/','bauska-and-reg/','cesis-and-reg/','daugavpils-and-reg/daugavpils/',
                   'daugavpils-and-reg/ilukste/','daugavpils-and-reg/eglaines-pag/','daugavpils-and-reg/kalkunes-pag/',
                   'daugavpils-and-reg/naujenes-pag/','daugavpils-and-reg/skrudalienas-pag/'
                  'dobele-and-reg/','gulbene-and-reg/','jekabpils-and-reg/','jelgava-and-reg/',
                  'kraslava-and-reg/','kuldiga-and-reg/','liepaja-and-reg/aizpute/','liepaja-and-reg/durbe/',
                   'liepaja-and-reg/grobina/','liepaja-and-reg/liepaja/','liepaja-and-reg/grobinas-pag/',
                   'liepaja-and-reg/nicas-pag/','liepaja-and-reg/otanku-pag/','liepaja-and-reg/priekules-pag/',
                   'liepaja-and-reg/tadaiku-pag/','liepaja-and-reg/vainodes-pag/','liepaja-and-reg/vergales-pag/',
                   'limbadzi-and-reg/','ludza-and-reg/','madona-and-reg/','ogre-and-reg/','preili-and-reg/',
                  'rezekne-and-reg/','saldus-and-reg/','talsi-and-reg/','tukums-and-reg/',
                  'valka-and-reg/','valmiera-and-reg/','ventspils-and-reg/','riga/centre/',
                  'riga/agenskalns/','riga/aplokciems/','riga/bergi/','riga/bierini/','riga/bolderaya/',
                  'riga/breksi/','riga/chiekurkalns/','riga/darzciems/','riga/daugavgriva/',
                  'riga/dreilini/','riga/dzeguzhkalns/','riga/grizinkalns/','riga/ilguciems/',
                  'riga/imanta/','riga/jaunciems/','riga/jaunmilgravis/','riga/yugla/',
                  'riga/katlakalns/','riga/kengarags/','riga/kipsala/','riga/kliversala/',
                  'riga/krasta-st-area/','riga/mangali/','riga/maskavas-priekshpilseta/','riga/mezhapark/',
                  'riga/mezhciems/','riga/plyavnieki/','riga/purvciems/','riga/shampeteris-pleskodale/',
                  'riga/sarkandaugava/','riga/shkirotava/','riga/teika/','riga/tornjakalns/',
                  'riga/vecaki/','riga/vecdaugava/','riga/vecmilgravis/','riga/vecriga/',
                  'riga/voleri/','riga/zasulauks/','riga/ziepniekkalns/','riga/zolitude/',
                  'riga/vef/']
#'''

kopejais_skaits_visam = len(darijuma_tips) * len(adresu_saraksts)
pec_kartas = 0

for adrese in range(0,len(adresu_saraksts)):
    for darijums in range(0,len(darijuma_tips)):
        saite = adreses_sakums + ipasuma_tips + adresu_saraksts[adrese] + darijuma_tips[darijums]
        page = requests.get(saite)
        soup = BeautifulSoup(page.content, 'html.parser')
        visi = soup.find_all(class_='am')
        tabula = savac_datus(tabula, adresu_saraksts[adrese], darijuma_tips[darijums], 7)
        #print(saite)
        pec_kartas = pec_kartas + 1
        print(str(pec_kartas) + '/' + str(kopejais_skaits_visam), end='\r')
        for lapa in range(2,150):
            page = requests.get(saite + "page{}.html".format(lapa))
            soup = BeautifulSoup(page.content, 'html.parser')
            lpp_nr = soup.find_all(class_='navi')
            nr_list=[]
            for nr in lpp_nr:
                if len(nr.get_text().split(' ')[0]) < 4:
                    nr_list.append(nr.get_text().split(' ')[0])
            try:
                if lapa <= int(max(nr_list)):
                    visi = soup.find_all(class_='am')
                    tabula = savac_datus(tabula, adresu_saraksts[adrese], darijuma_tips[darijums], 7)
                    #print(str(saite) + str(lapa), end='\r')
                    print(str(pec_kartas) + '/' + str(kopejais_skaits_visam), end='\r')
                else:
                    #print(str(saite) + str(lapa))
                    print(str(pec_kartas) + '/' + str(kopejais_skaits_visam), end='\r')
                    break
            except:
                break
            
tabula=tabula.drop_duplicates(subset=['Teksts','Vieta','Istabas','Stāvs','m2'])
tabula['Stāvs'] = tabula['Stāvs'].str.replace('/',' no ')
tabula['Darījuma tips'] = tabula['Darījuma tips'].str.replace('sell/','pārdod')
tabula['Darījuma tips'] = tabula['Darījuma tips'].str.replace('hand_over/','izīrē')
tabula['Adrese'] = tabula['Adrese'].str.replace('<b>','')
tabula['Adrese'] = tabula['Adrese'].str.replace('</b>','')
tabula['Avots'] = 'ss.lv'
tabula.insert(0, 'Tips', 'dzīvoklis')


tabula2 = pd.DataFrame(columns=['Teksts','Adrese','m2','Cena m2','Cena','Darījuma tips'])
tabula3 = pd.DataFrame(columns=['Teksts','Adrese','m2','Cena m2','Cena','Darījuma tips'])

def savac_datus2(tab, pardod_izire='pārdod'):
    for v in range(0, len(visi)):
        rinda = []
        pirmais = visi[v].get_text().split('b>')
        rinda.append(pirmais[0])
        for i in range(0,4):
            parejie = soup.find_all(class_='msga2-o pp6')[i+v+3*v].get_text()
            if i == 0:
                a = str(soup.find_all(class_='msga2-o pp6')[v+3*v])
                a = a[40:][:-5]
                a = a.replace('<br/>',', ')
                rinda.append(a)
            else:
                rinda.append(parejie)
        rinda.append(pardod_izire)
        tab.loc[len(tab)] = rinda
    return tab

saite = 'https://www.ss.com/lv/real-estate/premises/garrets/sell'
page = requests.get(saite)
soup = BeautifulSoup(page.content, 'html.parser')
visi = soup.find_all(class_='am')
tabula2 = savac_datus2(tabula2)
tabula2.insert(3, 'Stāvs', 'bēniņi')

saite = 'https://www.ss.com/lv/real-estate/premises/basements-and-semi-basements/sell'
page = requests.get(saite)
soup = BeautifulSoup(page.content, 'html.parser')
visi = soup.find_all(class_='am')
tabula3 = savac_datus2(tabula3)
tabula3.insert(3, 'Stāvs', 'pagrabs')

tabula23 = pd.concat([tabula2,tabula3], ignore_index=True)
tabula23['Avots'] = 'ss.lv'
tabula23.insert(0, 'Tips', 'telpas')
tabula23['Adrese'] = tabula23['Adrese'].str.replace('<b>','')
tabula23['Adrese'] = tabula23['Adrese'].str.replace('</b>','')


tabula4 = pd.DataFrame(columns=['Teksts','Adrese','m2','Stāvi','Istabas','Zemes platība','Cena',
                                'Vieta','Darījuma tips'])
ipasuma_tips = 'homes-summer-residences/'

# te bija adreses no dzīvokļu skripta

pec_kartas = 0

for adrese in range(0,len(adresu_saraksts)):
    for darijums in range(0,len(darijuma_tips)):
        saite = adreses_sakums + ipasuma_tips + adresu_saraksts[adrese] + darijuma_tips[darijums]
        page = requests.get(saite)
        soup = BeautifulSoup(page.content, 'html.parser')
        visi = soup.find_all(class_='am')
        tabula4 = savac_datus(tabula4, adresu_saraksts[adrese], darijuma_tips[darijums], 6)
        #print(saite)
        pec_kartas = pec_kartas + 1
        print(str(pec_kartas) + '/' + str(kopejais_skaits_visam), end='\r')
        for lapa in range(2,150):
            page = requests.get(saite + "page{}.html".format(lapa))
            soup = BeautifulSoup(page.content, 'html.parser')
            lpp_nr = soup.find_all(class_='navi')
            nr_list=[]
            for nr in lpp_nr:
                if len(nr.get_text().split(' ')[0]) < 4:
                    nr_list.append(nr.get_text().split(' ')[0])
            try:
                if lapa <= int(max(nr_list)):
                    visi = soup.find_all(class_='am')
                    tabula4 = savac_datus(tabula4, adresu_saraksts[adrese], darijuma_tips[darijums], 6)
                    #print(str(saite) + str(lapa), end='\r')
                    print(str(pec_kartas) + '/' + str(kopejais_skaits_visam), end='\r')
                else:
                    #print(str(saite) + str(lapa))
                    print(str(pec_kartas) + '/' + str(kopejais_skaits_visam), end='\r')
                    break
            except:
                break
            
tabula4=tabula4.drop_duplicates(subset=['Teksts','Vieta','Istabas','Stāvi','m2'])
tabula4['Darījuma tips'] = tabula4['Darījuma tips'].str.replace('sell/','pārdod')
tabula4['Darījuma tips'] = tabula4['Darījuma tips'].str.replace('hand_over/','izīrē')
tabula4['Adrese'] = tabula4['Adrese'].str.replace('<b>','')
tabula4['Adrese'] = tabula4['Adrese'].str.replace('</b>','')
tabula4['Avots'] = 'ss.lv'
tabula4.insert(0, 'Tips', 'māja')
