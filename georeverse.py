import csv
import io
import numpy as np
from scipy.spatial import distance


def read_world_cities():
    all_cities = []
    all_lat_lon = []
    f = io.StringIO(world_cities)
    reader = csv.reader(f, delimiter=',')
    for city in reader:
        if city:
            all_cities.append({"city":city[1], "state": city[8], "country":city[5], "latitude":city[2], "longitude":city[3]})
            all_lat_lon.append([city[2], city[3]])
    all_lat_lon = np.array(all_lat_lon)
    return all_cities, all_lat_lon


def georeverse(point):
    all_cities, all_lat_lon = read_world_cities()
    result = all_lat_lon[distance.cdist([point], all_lat_lon).argmin()]
    for city in all_cities:
        if result[0] == city['latitude'] and result[1] == city['longitude']:
            return city
    return None


world_cities = '''
Qal eh-ye Now,Qal eh-ye,34.98300013,63.13329964,2997,Afghanistan,AF,AFG,Badghis
Chaghcharan,Chaghcharan,34.5167011,65.25000063,15000,Afghanistan,AF,AFG,Ghor
Lashkar Gah,Lashkar Gah,31.58299802,64.35999955,201546,Afghanistan,AF,AFG,Hilmand
Zaranj,Zaranj,31.11200108,61.88699752,49851,Afghanistan,AF,AFG,Nimroz
Tarin Kowt,Tarin Kowt,32.63329815,65.86669865,10000,Afghanistan,AF,AFG,Uruzgan
Zareh Sharan,Zareh Sharan,32.85000016,68.41670453,13737,Afghanistan,AF,AFG,Paktika
Asadabad,Asadabad,34.86600004,71.15000459,48400,Afghanistan,AF,AFG,Kunar
Taloqan,Taloqan,36.72999904,69.54000364,64256,Afghanistan,AF,AFG,Takhar
Mahmud-E Eraqi,Mahmud-E Eraqi,35.01669608,69.33330065,7407,Afghanistan,AF,AFG,Kapisa
Mehtar Lam,Mehtar Lam,34.65000001,70.16670052,17345,Afghanistan,AF,AFG,Laghman
Baraki Barak,Baraki Barak,33.9667021,68.96670354,22305,Afghanistan,AF,AFG,Logar
Aybak,Aybak,36.26100015,68.04000051,24000,Afghanistan,AF,AFG,Samangan
Mayda Shahr,Mayda Shahr,34.45000209,68.79999663,35008,Afghanistan,AF,AFG,Wardak
Karokh,Karokh,34.48676963,62.59177608,14388.5,Afghanistan,AF,AFG,Hirat
Sheberghan,Sheberghan,36.65798077,65.73830237,74441,Afghanistan,AF,AFG,Jawzjan
Pol-e Khomri,Pol-e Khomri,35.95107302,68.70111894,41029,Afghanistan,AF,AFG,Baghlan
Balkh,Balkh,36.75011985,66.89973018,147426,Afghanistan,AF,AFG,Balkh
Meymaneh,Meymaneh,35.93022158,64.77009273,199795,Afghanistan,AF,AFG,Faryab
Andkhvoy,Andkhvoy,36.93165916,65.10149369,50469,Afghanistan,AF,AFG,Faryab
Qalat,Qalat,32.11226341,66.8867594,12191,Afghanistan,AF,AFG,Zabul
Ghazni,Ghazni,33.56331179,68.41782873,129892.5,Afghanistan,AF,AFG,Ghazni
Feyzabad,Feyzabad,37.12976076,70.57924719,52490,Afghanistan,AF,AFG,Badakhshan
Kondoz,Kondoz,36.72795066,68.87252966,210855.5,Afghanistan,AF,AFG,Kunduz
Jalalabad,Jalalabad,34.44152692,70.43610347,401697,Afghanistan,AF,AFG,Nangarhar
Charikar,Charikar,35.01826174,69.16791215,53676,Afghanistan,AF,AFG,Parwan
Gardiz,Gardiz,33.60005373,69.21462764,82680.5,Afghanistan,AF,AFG,Paktya
Bamian,Bamian,34.82106447,67.52103593,61863,Afghanistan,AF,AFG,Bamyan
Baghlan,Baghlan,36.13933026,68.69925858,163598.5,Afghanistan,AF,AFG,Baghlan
Farah,Farah,32.39172955,62.09681921,58604,Afghanistan,AF,AFG,Farah
Herat,Herat,34.33000917,62.16999304,439232.5,Afghanistan,AF,AFG,Hirat
Mazar-e Sharif,Mazar-e Sharif,36.69999371,67.10002803,365432.5,Afghanistan,AF,AFG,Balkh
Kandahar,Kandahar,31.61002016,65.69494584,613871,Afghanistan,AF,AFG,Kandahar
Kabul,Kabul,34.51669029,69.18326005,3160266,Afghanistan,AF,AFG,Kabul
Mariehamn,Mariehamn,60.09699618,19.94900447,10682,Aland,AX,ALD,Finstr?m
Kruje,Kruje,41.51899817,19.79700359,21286,Albania,AL,ALB,Durr?s
Fier,Fier,40.73000402,19.5730026,69747.5,Albania,AL,ALB,Fier
Lushnje,Lushnje,40.94000113,19.71600348,41469,Albania,AL,ALB,Fier
Puke,Puke,42.03330302,19.88330448,6495,Albania,AL,ALB,Shkod?r
Bajram Curri,Bajram Curri,42.33330007,20.08330257,7967,Albania,AL,ALB,Kuk?s
Kukes,Kukes,42.08300107,20.43399653,17832,Albania,AL,ALB,Kuk?s
Sarande,Sarande,39.87700212,19.99999859,15147,Albania,AL,ALB,Vlor?
Erseke,Erseke,40.33330213,20.68329651,7890,Albania,AL,ALB,Kor??
Pogradec,Pogradec,40.89999612,20.66400062,35000,Albania,AL,ALB,Kor??
Korce,Korce,40.61667601,20.76666353,58259,Albania,AL,ALB,Kor??
Berat,Berat,40.70999705,19.97199958,46866,Albania,AL,ALB,Berat
Corovode,Corovode,40.51670403,20.23329663,14046,Albania,AL,ALB,Berat
Gramsh,Gramsh,40.86669601,20.19999652,11556,Albania,AL,ALB,Elbasan
Librazhd,Librazhd,41.20000211,20.3667036,12691,Albania,AL,ALB,Elbasan
Tepelene,Tepelene,40.2832981,20.03329854,11955,Albania,AL,ALB,Gjirokast?r
Permet,Permet,40.23399605,20.35199756,10686,Albania,AL,ALB,Gjirokast?r
Gjirokaster,Gjirokaster,40.07899809,20.14900256,23437,Albania,AL,ALB,Gjirokast?r
Peshkopi,Peshkopi,41.6833021,20.43330349,14848,Albania,AL,ALB,Dib?r
Burrel,Burrel,41.62599908,20.01600053,15405,Albania,AL,ALB,Dib?r
Lezhe,Lezhe,41.78799914,19.65400254,18695,Albania,AL,ALB,Lezh?
Rreshen,Rreshen,41.78330106,19.81670459,10064,Albania,AL,ALB,Lezh?
Vlore,Vlore,40.47736005,19.49823075,89508.5,Albania,AL,ALB,Vlor?
Elbasan,Elbasan,41.12150677,20.08382808,132956.5,Albania,AL,ALB,Elbasan
Durres,Durres,41.3177997,19.44820797,132233,Albania,AL,ALB,Durr?s
Shkoder,Shkoder,42.06845156,19.51884965,122006,Albania,AL,ALB,Shkod?r
Tirana,Tirana,41.32754071,19.81888301,658318,Albania,AL,ALB,Durr?s
Jijel,Jijel,36.82199703,5.76600356,148000,Algeria,DZ,DZA,Jijel
Tizi-Ouzou,Tizi-Ouzou,36.80000111,4.033332556,144000,Algeria,DZ,DZA,Tizi Ouzou
Bordj Bou Arreridj,Bordj Bou Arreridj,36.05900401,4.629996466,134500,Algeria,DZ,DZA,Bordj Bou Arr?ridj
M'sila,M'sila,35.7000031,4.545000584,125000,Algeria,DZ,DZA,M'Sila
Guelma,Guelma,36.46600213,7.427997486,123590,Algeria,DZ,DZA,Guelma
Oum el Bouaghi,Oum el Bouaghi,35.84999715,7.149996522,100821,Algeria,DZ,DZA,Oum el Bouaghi
Timimoun,Timimoun,29.23652163,0.269998737,26568,Algeria,DZ,DZA,Adrar
Sidi bel Abbes,Sidi bel Abbes,35.19034426,-0.639971559,200186.5,Algeria,DZ,DZA,Sidi Bel Abb?s
Tlimcen,Tlimcen,34.89041424,-1.32000757,181059,Algeria,DZ,DZA,Tlemcen
Beni Ounif,Beni Ounif,32.04926984,-1.251381268,5628,Algeria,DZ,DZA,B?char
Abadla,Abadla,31.01708478,-2.733306317,14364,Algeria,DZ,DZA,B?char
Sefra,Sefra,32.76041506,-0.579949383,51118,Algeria,DZ,DZA,Na?ma
Skikda,Skikda,36.88042198,6.899981647,193941.5,Algeria,DZ,DZA,Skikda
Djanet,Djanet,24.5529057,9.482252969,666,Algeria,DZ,DZA,Illizi
I-n-Amenas,I-n-Amenas,28.0503408,9.550000772,216,Algeria,DZ,DZA,Illizi
In Amguel,In Amguel,23.69394004,5.164738727,3030,Algeria,DZ,DZA,Tamanghasset
El Bayadh,El Bayadh,33.6903583,1.009953571,67413,Algeria,DZ,DZA,El Bayadh
El Oued,El Oued,33.37040367,6.859984089,177497,Algeria,DZ,DZA,Biskra
Hassi Messaoud,Hassi Messaoud,31.70234011,6.054451862,18124,Algeria,DZ,DZA,Ouargla
Chlef,Chlef,36.17041363,1.319960489,449167,Algeria,DZ,DZA,Chlef
Mascara,Mascara,35.40040895,0.14003251,108230,Algeria,DZ,DZA,Mascara
Mostaganem,Mostaganem,35.940376,0.089983885,159177,Algeria,DZ,DZA,Mostaganem
Saida,Saida,34.84039146,0.14003251,134855,Algeria,DZ,DZA,Sa?da
Tiarat,Tiarat,35.38043601,1.319960489,184195,Algeria,DZ,DZA,Tiaret
Bejaia,Bejaia,36.76037762,5.070015827,274520,Algeria,DZ,DZA,B?ja?a
Blida,Blida,36.4203467,2.829997517,388174,Algeria,DZ,DZA,Blida
Bouira,Bouira,36.38047833,3.900009724,110144,Algeria,DZ,DZA,Bouira
Medea,Medea,36.27040753,2.770001179,145863.5,Algeria,DZ,DZA,M?d?a
Souk Ahras,Souk Ahras,36.29038047,7.949995075,134947,Algeria,DZ,DZA,Souk Ahras
Tebessa,Tebessa,35.41043418,8.120010537,171742,Algeria,DZ,DZA,T?bessa
Adrar,Adrar,27.86999005,-0.289967083,56910,Algeria,DZ,DZA,Adrar
Reggane,Reggane,26.69998395,0.166645873,22351.5,Algeria,DZ,DZA,Adrar
Bechar,Bechar,31.61110537,-2.230003704,142415.5,Algeria,DZ,DZA,B?char
Tindouf,Tindouf,27.67418805,-8.147782025,18270,Algeria,DZ,DZA,Tindouf
Illizi,Illizi,26.48335634,8.466604369,7293,Algeria,DZ,DZA,Illizi
Arak,Arak,25.2799931,3.749993041,423251,Algeria,DZ,DZA,Tamanghasset
I-n-Salah,I-n-Salah,27.21664492,2.466608845,28632,Algeria,DZ,DZA,Tamanghasset
El Golea,El Golea,30.56662132,2.883327595,32049,Algeria,DZ,DZA,Gharda?a
Laghouat,Laghouat,33.80998924,2.880020303,108279,Algeria,DZ,DZA,Laghouat
Touggourt,Touggourt,33.0999809,6.05998124,91499,Algeria,DZ,DZA,Ouargla
Ouargla,Ouargla,31.96997235,5.340025186,176271,Algeria,DZ,DZA,Ouargla
Biskra,Biskra,34.85997683,5.73002722,202103,Algeria,DZ,DZA,Biskra
Djelfa,Djelfa,34.67998781,3.250023558,170901,Algeria,DZ,DZA,Djelfa
Setif,Setif,36.18002545,5.399969847,274744,Algeria,DZ,DZA,S?tif
Batna,Batna,35.56995933,6.170000365,269467,Algeria,DZ,DZA,Batna
Annaba,Annaba,36.92000612,7.759980834,355047,Algeria,DZ,DZA,Annaba
Constantine,Constantine,36.35998863,6.599948281,527638,Algeria,DZ,DZA,Constantine
Oran,Oran,35.71000246,-0.61997278,721992,Algeria,DZ,DZA,Oran
Tamanrasset,Tamanrasset,22.78500327,5.522804727,71808,Algeria,DZ,DZA,Tamanghasset
Ghardaia,Ghardaia,32.48999229,3.669997923,125480,Algeria,DZ,DZA,Gharda?a
Algiers,Algiers,36.7630648,3.05055253,2665831.5,Algeria,DZ,DZA,Alger
Pago Pago,Pago Pago,-14.2766105,-170.7066451,12038,American Samoa,AS,ASM,
Andorra,Andorra,42.50000144,1.516485961,38127,Andorra,AD,AND,
Mucusso,Mucusso,-18.01953449,21.42999914,100,Angola,AO,AGO,Cuando Cubango
Lucapa,Lucapa,-8.419603659,20.74001542,25578,Angola,AO,AGO,Lunda Norte
Capenda-Camulemba,Capenda-Camulemba,-9.4195943,18.43002722,79842.5,Angola,AO,AGO,Lunda Norte
Saurimo,Saurimo,-9.659579652,20.39001094,40907,Angola,AO,AGO,Lunda Sul
Muconda,Muconda,-10.59962563,21.31998002,2324,Angola,AO,AGO,Lunda Sul
Cacolo,Cacolo,-10.14962726,19.2600024,984,Angola,AO,AGO,Lunda Sul
Caxito,Caxito,-8.579542217,13.65998246,15665.5,Angola,AO,AGO,Bengo
Camabatela,Camabatela,-8.189591859,15.37000728,12731,Angola,AO,AGO,Cuanza Norte
Ndalatando,Ndalatando,-9.299549948,14.90998368,8144,Angola,AO,AGO,Cuanza Norte
Quibala,Quibala,-10.72959186,14.97995357,5248.5,Angola,AO,AGO,Cuanza Sul
Calulo,Calulo,-9.999610577,14.90001013,795,Angola,AO,AGO,Cuanza Sul
Waku Kungo,Waku Kungo,-11.35952757,15.1199967,11519.5,Angola,AO,AGO,Cuanza Sul
Songo,Songo,-7.349591452,14.84998734,10579,Angola,AO,AGO,U?ge
Mbanza-Congo,Mbanza-Congo,-6.269605694,14.23999874,42201,Angola,AO,AGO,Zaire
Nzeto,Nzeto,-7.229598776,12.86003129,19705.5,Angola,AO,AGO,Zaire
Soyo,Soyo,-6.129614239,12.36998368,65329,Angola,AO,AGO,Zaire
Cabinda,Cabinda,-5.55962319,12.18999467,78905.5,Angola,AO,AGO,Cabinda
Calucinga,Calucinga,-11.31958169,16.19998246,531,Angola,AO,AGO,Bi?
Camacupa,Camacupa,-12.01959064,17.46998246,19489,Angola,AO,AGO,Bi?
Cubal,Cubal,-13.03958006,14.23999874,4837,Angola,AO,AGO,Benguela
Mavinga,Mavinga,-15.7895414,20.36003861,30000,Angola,AO,AGO,Cuando Cubango
Cuito Caunavale,Cuito Caunavale,-15.15960569,19.16998205,149,Angola,AO,AGO,Cuando Cubango
Luiana,Luiana,-17.36954832,22.99998083,150,Angola,AO,AGO,Cuando Cubango
Ondjiva,Ondjiva,-17.06961831,15.73003699,8748,Angola,AO,AGO,Cunene
Chitado,Chitado,-17.31962889,13.92001827,468.5,Angola,AO,AGO,Cunene
Chibemba,Chibemba,-15.74959552,14.0800085,1502,Angola,AO,AGO,Hu?la
Chibia,Chibia,-15.1896297,13.69000647,1411,Angola,AO,AGO,Hu?la
Quipungo,Quipungo,-14.82954832,14.55000565,186,Angola,AO,AGO,Hu?la
Luau,Luau,-10.7095414,22.23000199,9964,Angola,AO,AGO,Moxico
Cangamba,Cangamba,-13.69959145,19.86001745,1307,Angola,AO,AGO,Moxico
Lumbala Nguimbo,Lumbala Nguimbo,-14.09961871,21.44002437,25,Angola,AO,AGO,Moxico
Cazombo,Cazombo,-11.88957273,22.90003861,298,Angola,AO,AGO,Moxico
Dundo,Dundo,-7.380028871,20.82998409,11985,Angola,AO,AGO,Lunda Norte
Ambriz,Ambriz,-7.85498696,13.12502803,17000,Angola,AO,AGO,Bengo
Dondo,Dondo,-9.690017071,14.43001298,2353,Angola,AO,AGO,Cuanza Norte
Sumbe,Sumbe,-11.21002765,13.8499967,29638.5,Angola,AO,AGO,Cuanza Sul
Uige,Uige,-7.620014222,15.04997514,56787.5,Angola,AO,AGO,U?ge
Kuito,Kuito,-12.38003375,16.93998897,113955,Angola,AO,AGO,Bi?
Lobito,Lobito,-12.37000853,13.54123002,170733,Angola,AO,AGO,Benguela
Xangongo,Xangongo,-16.74002602,14.96998002,447,Angola,AO,AGO,Cunene
Luena,Luena,-11.79004393,19.90001501,17276.5,Angola,AO,AGO,Moxico
T?mbua,Tombua,-15.80003172,11.85998897,40000,Angola,AO,AGO,Namibe
Malanje,Malanje,-9.540000388,16.34002559,106451,Angola,AO,AGO,Malanje
Benguela,Benguela,-12.57826455,13.40723303,142017,Angola,AO,AGO,Benguela
Lubango,Lubango,-14.91000853,13.49001868,114086.5,Angola,AO,AGO,Hu?la
Namibe,Namibe,-15.19004311,12.16002234,128130.5,Angola,AO,AGO,Namibe
Menongue,Menongue,-14.66661253,17.69999426,13030,Angola,AO,AGO,Cuando Cubango
Huambo,Huambo,-12.74998533,15.76000932,986000,Angola,AO,AGO,Huambo
Luanda,Luanda,-8.838286114,13.23442704,3562086,Angola,AO,AGO,Luanda
Artigas Base,Artigas Base,-62.17388669,-58.86386407,34.5,Antarctica,AQ,ATA,
Capitan Arturo Prat Station,Capitan Arturo Prat Station,-62.49950682,-59.68331852,41,Antarctica,AQ,ATA,
Marambio Station,Vicecomodoro Marambio Station,-64.23288939,-56.6500153,102.5,Antarctica,AQ,ATA,
Zucchelli Station,Terra Nova Bay,-74.61919259,164.2190271,60,Antarctica,AQ,ATA,
Rothera Station,Rothera Station,-67.5647756,-68.12354055,76,Antarctica,AQ,ATA,
Palmer Station,Palmer Station,-64.76241335,-64.0468756,30.5,Antarctica,AQ,ATA,
Base Presidente Montalva,Teniente Rodolfo Marsh Station,-62.18274357,-58.90765233,115,Antarctica,AQ,ATA,
Carlini Station,Teniente Jubany Station,-62.22414386,-58.65047599,40,Antarctica,AQ,ATA,
King Sejong Station,King Sejong Station,-62.2248534,-58.77159876,53.5,Antarctica,AQ,ATA,
Great Wall Station,Great Wall Station,-62.21631997,-58.9666956,26,Antarctica,AQ,ATA,
Escudero Base,Escudero Station,-62.19496251,-58.95266582,20,Antarctica,AQ,ATA,
Elephant Island,"Elephant Island, South Shetland Islands",-61.99958901,-57.99998458,3,Antarctica,AQ,ATA,
Scott Base,Scott Base,-77.84693819,166.7491023,49.5,Antarctica,AQ,ATA,
McMurdo Station,McMurdo Station,-77.73228239,166.8694157,600,Antarctica,AQ,ATA,
Zhongshan Station,Zhongshan Station,-69.43406299,76.33929808,42.5,Antarctica,AQ,ATA,
Vostok,Vostok,-78.46628416,106.8000337,19,Antarctica,AQ,ATA,
Peter I Island,Peter I Island,-68.83286701,90.49999508,0.5,Antarctica,AQ,ATA,
Mirny Station,Mirny Station,-66.57552952,93.00628846,114.5,Antarctica,AQ,ATA,
Mawson Station,Mawson Station,-67.61452032,62.87500073,40,Antarctica,AQ,ATA,
Davis Station,Davis Station,-68.77767439,78.14073509,45,Antarctica,AQ,ATA,
Concordia Research Station,Concordia Research Station,-74.66630939,124.1670357,15,Antarctica,AQ,ATA,
Casey Station,Casey Station,-66.28608614,110.536214,125,Antarctica,AQ,ATA,
Amundsen?Scott South Pole Station,Amundsen?Scott South Pole Station,-89.98289386,139.2669926,125,Antarctica,AQ,ATA,
Wasa Station,Wasa Station,-73.0496122,-13.41671106,5,Antarctica,AQ,ATA,
Troll Station,Troll Station,-72.01629026,2.533323119,25.5,Antarctica,AQ,ATA,
Svea Station,Svea Station,-74.58290363,-11.21669031,5,Antarctica,AQ,ATA,
Novolazarevskaya Station,Novolazarevskaya Station,-71.30123475,-11.8502129,35,Antarctica,AQ,ATA,
Neumayer Station III,Neumayer,-70.89039668,-7.838438004,40,Antarctica,AQ,ATA,
Maitri Station,Maitri Station,-70.7821796,11.7304584,33,Antarctica,AQ,ATA,
Halley Station,Halley Station,-76.09226319,-26.4741567,43,Antarctica,AQ,ATA,
Belgrano Station,General Belgrano Station,-77.86632078,-34.61668319,57,Antarctica,AQ,ATA,
Camp Sobral,Doctor Sobral,-81.17908472,-40.50153152,20,Antarctica,AQ,ATA,
Aboa Station,Aboa Station,-75.04959349,-13.41671106,15,Antarctica,AQ,ATA,
San Mart?n Station,San Mart?n Station,-68.1163216,-67.0999976,19,Antarctica,AQ,ATA,
Gen. O'Higgins Station,General Bernado O'Higgins Station,-63.32841823,-57.88959352,30,Antarctica,AQ,ATA,
Esperanza Station,Esperanza Station,-63.37532865,-57.02590151,152.5,Antarctica,AQ,ATA,
Orcadas Station,Orcadas Station,-60.7328963,-44.73330082,29.5,Antarctica,AQ,ATA,
Signy Research Station,Signy Island,-60.63130815,-45.60070332,4,Antarctica,AQ,ATA,
Dumont d'Urville Station,Dumont d'Urville Station,-66.77505091,139.9636836,75,Antarctica,AQ,ATA,
Showa Station,Showa Station,-69.03039249,39.7460831,50,Antarctica,AQ,ATA,
Saint John's,Saint John's,17.11803652,-61.85003382,29862.5,Antigua and Barbuda,AG,ATG,
28 de Noviembre,28 de Noviembre,-51.65003986,-72.30001612,5300,Argentina,AR,ARG,Santa Cruz
Gobernador Gregores,Gobernador Gregores,-48.76659829,-70.25001205,2519,Argentina,AR,ARG,Santa Cruz
Comondante Luis Piedrabuena,Comondante Luis Piedrabuena,-49.97454865,-68.90347273,410,Argentina,AR,ARG,Santa Cruz
Paso Rio Mayo,Paso Rio Mayo,-45.68337563,-70.26657434,1825,Argentina,AR,ARG,Chubut
Alto Rio Sanguer,Alto Rio Sanguer,-45.03328611,-70.83328394,1548,Argentina,AR,ARG,Chubut
El Maiten,El Maiten,-42.05000568,-71.16662276,4269,Argentina,AR,ARG,Chubut
Puerto Madryn,Puerto Madryn,-42.77001341,-65.04001998,61159,Argentina,AR,ARG,Chubut
Trelew,Trelew,-43.25003579,-65.3299506,93128.5,Argentina,AR,ARG,Chubut
Las Heras,Las Heras,-32.82503904,-68.80167668,66663,Argentina,AR,ARG,Mendoza
San Martin,San Martin,-33.06998533,-68.49001612,99974,Argentina,AR,ARG,Mendoza
Uspallata,Uspallata,-32.59311522,-69.34598454,2390,Argentina,AR,ARG,Mendoza
Cutral Co,Cutral Co,-38.94001463,-69.24002202,47597,Argentina,AR,ARG,Neuqu?n
Punta Alta,Punta Alta,-38.87996662,-62.0799681,55969.5,Argentina,AR,ARG,Ciudad de Buenos Aires
San Nicolas,San Nicolas,-33.33002114,-60.24000289,117123.5,Argentina,AR,ARG,Ciudad de Buenos Aires
Campana,Campana,-34.15999632,-58.95997766,77149.5,Argentina,AR,ARG,Ciudad de Buenos Aires
Chacabuco,Chacabuco,-34.65004393,-60.48998763,26645,Argentina,AR,ARG,Ciudad de Buenos Aires
Mercedes,Mercedes,-34.66001748,-59.44002588,48408.5,Argentina,AR,ARG,Ciudad de Buenos Aires
Lincoln,Lincoln,-34.88000405,-61.53994938,19924,Argentina,AR,ARG,Ciudad de Buenos Aires
Chivilcoy,Chivilcoy,-34.89995115,-60.03998926,43719,Argentina,AR,ARG,Ciudad de Buenos Aires
Veinticinco de Mayo,Veinticinco de Mayo,-35.42999632,-60.17998071,18749,Argentina,AR,ARG,Ciudad de Buenos Aires
Nueve de Julio,Nueve de Julio,-35.44596434,-60.88998906,26716,Argentina,AR,ARG,Ciudad de Buenos Aires
Dolores,Dolores,-36.33004474,-57.68997766,21586.5,Argentina,AR,ARG,Ciudad de Buenos Aires
Pedro Luro,Pedro Luro,-39.48334064,-62.68331629,7100,Argentina,AR,ARG,Ciudad de Buenos Aires
Tres Arroyos,Tres Arroyos,-38.3699719,-60.26994938,34773.5,Argentina,AR,ARG,Ciudad de Buenos Aires
Coronel Suarez,Coronel Suarez,-37.46661619,-61.9166189,20713,Argentina,AR,ARG,Ciudad de Buenos Aires
Balcarce,Balcarce,-37.83331216,-58.24999516,18967,Argentina,AR,ARG,Ciudad de Buenos Aires
25 de Mayo,25 de Mayo,-37.80003253,-67.68329533,17430,Argentina,AR,ARG,R?o Negro
General Roca,General Roca,-39.01995807,-67.60996647,38578,Argentina,AR,ARG,R?o Negro
Comallo,Comallo,-41.03332355,-70.26657434,741,Argentina,AR,ARG,R?o Negro
Ingeniero Jacobacci,Ingeniero Jacobacci,-41.30002562,-69.58330855,5719,Argentina,AR,ARG,R?o Negro
General Conesa,General Conesa,-40.10004718,-64.43328699,2958,Argentina,AR,ARG,R?o Negro
Choele Choel,Choele Choel,-39.26660968,-65.68331405,9895.5,Argentina,AR,ARG,R?o Negro
San Francisco,San Francisco,-31.43003375,-62.08996749,43231,Argentina,AR,ARG,C?rdoba
Alta Gracia,Alta Gracia,-31.65999388,-64.4299797,30593,Argentina,AR,ARG,C?rdoba
Villa Maria,Villa Maria,-32.41002562,-63.26002527,76701,Argentina,AR,ARG,C?rdoba
Bell Ville,Bell Ville,-32.60003986,-62.67995732,29605,Argentina,AR,ARG,C?rdoba
Villa Rumipal,Villa Rumipal,-32.18332111,-64.48328394,1269,Argentina,AR,ARG,C?rdoba
Villa Carlos Paz,Villa Carlos Paz,-31.42000853,-64.50000126,60256,Argentina,AR,ARG,C?rdoba
Chumbicha,Chumbicha,-28.86662433,-66.23330632,2572,Argentina,AR,ARG,Catamarca
Tinogasta,Tinogasta,-28.06662148,-67.56658411,587,Argentina,AR,ARG,Catamarca
Abra Pampa,Abra Pampa,-22.7166638,-65.6999797,4480,Argentina,AR,ARG,Jujuy
Humahuaca,Humahuaca,-23.19999347,-65.34994938,11369,Argentina,AR,ARG,Jujuy
Susques,Susques,-23.41667275,-66.4833169,1093,Argentina,AR,ARG,Jujuy
Chepes,Chepes,-31.34998696,-66.5999506,6020,Argentina,AR,ARG,La Rioja
Yacuiba,Yacuiba,-22.03003904,-63.69999841,64811,Argentina,AR,ARG,Salta
Tartagal,Tartagal,-22.55000731,-63.81001754,59996.5,Argentina,AR,ARG,Salta
Joaquin V. Gonzalez,Joaquin V. Gonzalez,-25.08334105,-64.18335392,13376,Argentina,AR,ARG,Salta
General Guemes,General Guemes,-24.6666223,-65.04996769,19828,Argentina,AR,ARG,Salta
Trancas,Trancas,-26.21665688,-65.28331262,1599,Argentina,AR,ARG,Tucum?n
Presidencia Roque Saenz Pena,Presidencia Roque Saenz Pena,-26.7900069,-60.45001591,75958,Argentina,AR,ARG,Chaco
Pampa del Infierno,Pampa del Infierno,-26.51658689,-61.16658716,2921,Argentina,AR,ARG,Chaco
Villa Angela,Villa Angela,-27.58329181,-60.7166663,30051,Argentina,AR,ARG,Chaco
Ingeniero Guillermo N. Juarez,Ingeniero Guillermo N. Juarez,-23.90000242,-61.84998214,6453,Argentina,AR,ARG,Formosa
Comandante Fontana,Comandante Fontana,-25.33329995,-59.68331852,4277,Argentina,AR,ARG,Formosa
Doctor Pedro P. Pena,Doctor Pedro P. Pena,-22.47998574,-62.29998051,6143,Argentina,AR,ARG,Formosa
San Lorenzo,San Lorenzo,-28.12000324,-58.76998926,25833.5,Argentina,AR,ARG,Corrientes
Corrientes,Corrientes,-27.48996417,-58.80998682,339945,Argentina,AR,ARG,Corrientes
Concepcion del Uruguay,Concepcion del Uruguay,-32.47999551,-58.23999577,48275,Argentina,AR,ARG,Entre R?os
Victoria,Victoria,-32.61001341,-60.17998071,20032.5,Argentina,AR,ARG,Entre R?os
Gualeguay,Gualeguay,-33.15003213,-59.34000615,25913,Argentina,AR,ARG,Entre R?os
Parana,Parana,-31.73332273,-60.53334416,226852,Argentina,AR,ARG,Entre R?os
Villa Constitucion,Villa Constitucion,-33.23002724,-60.35002202,30282.5,Argentina,AR,ARG,Santa Fe
Rafaela,Rafaela,-31.25004474,-61.49997766,69649,Argentina,AR,ARG,Santa Fe
Eldorado,Eldorado,-26.20001707,-54.59998539,17365,Argentina,AR,ARG,Misiones
Rodeo,Rodeo,-30.21558592,-69.1399506,701,Argentina,AR,ARG,San Juan
Las Plumas,Las Plumas,-43.41627887,-67.24998845,605,Argentina,AR,ARG,Chubut
Gastre,Gastre,-42.28296303,-69.23330408,557,Argentina,AR,ARG,Chubut
Telsen,Telsen,-42.39959674,-66.95000676,493,Argentina,AR,ARG,Chubut
Malargue,Malargue,-35.46611815,-69.58330855,11847,Argentina,AR,ARG,Mendoza
Tunuyan,Tunuyan,-33.56618244,-69.01667647,22834,Argentina,AR,ARG,Mendoza
La Paz,La Paz,-33.46613686,-67.54999597,4400,Argentina,AR,ARG,Mendoza
Chos Malal,Chos Malal,-37.38295205,-70.26657434,8556,Argentina,AR,ARG,Neuqu?n
Las Lajas,Las Lajas,-38.51626788,-70.36659408,1218,Argentina,AR,ARG,Neuqu?n
Zarate,Zarate,-34.08956134,-59.04002446,86192,Argentina,AR,ARG,Ciudad de Buenos Aires
Carhue,Carhue,-37.1828609,-62.73331323,7190,Argentina,AR,ARG,Ciudad de Buenos Aires
Darregueira,Darregueira,-37.69957355,-63.16659428,3412,Argentina,AR,ARG,Ciudad de Buenos Aires
Juarez,Juarez,-37.66551878,-59.80002975,10609,Argentina,AR,ARG,Ciudad de Buenos Aires
Mar de Ajo,Mar de Ajo,-36.71622272,-56.67660283,13610,Argentina,AR,ARG,Ciudad de Buenos Aires
Lobos,Lobos,-35.184895,-59.09467228,18278,Argentina,AR,ARG,Ciudad de Buenos Aires
Chascomus,Chascomus,-35.56621539,-58.01662439,21054,Argentina,AR,ARG,Ciudad de Buenos Aires
Junin,Junin,-34.58456989,-60.95887374,66141.5,Argentina,AR,ARG,Ciudad de Buenos Aires
La Plata,La Plata,-34.90961465,-57.95996118,440388.5,Argentina,AR,ARG,Ciudad de Buenos Aires
Pergamino,Pergamino,-33.89959878,-60.56998275,71448,Argentina,AR,ARG,Ciudad de Buenos Aires
Lujan,Lujan,-34.57960895,-59.10999435,69744.5,Argentina,AR,ARG,Ciudad de Buenos Aires
Azul,Azul,-36.7796297,-59.86999964,43407.5,Argentina,AR,ARG,Ciudad de Buenos Aires
Villalonga,Villalonga,-39.88285114,-62.58332239,2838,Argentina,AR,ARG,Ciudad de Buenos Aires
Victorica,Victorica,-36.21625324,-65.45002079,4458,Argentina,AR,ARG,La Pampa
General Pico,General Pico,-35.65959471,-63.77001998,46483,Argentina,AR,ARG,La Pampa
San Antonio Oeste,San Antonio Oeste,-40.73287677,-64.93328231,8492,Argentina,AR,ARG,R?o Negro
Sierra Colorado,Sierra Colorado,-40.58286009,-67.79998071,1522,Argentina,AR,ARG,R?o Negro
Mercedes,Mercedes,-33.68958576,-65.4699679,49345,Argentina,AR,ARG,San Luis
Rio Tercero,Rio Tercero,-32.1796004,-64.12002446,38049.5,Argentina,AR,ARG,C?rdoba
Belen,Belen,-27.64959267,-67.03328333,11359,Argentina,AR,ARG,Catamarca
Rinconada,Rinconada,-22.43290851,-66.16659204,6209.5,Argentina,AR,ARG,Jujuy
San Pedro,San Pedro,-24.21962116,-64.87000452,55249,Argentina,AR,ARG,Jujuy
Libertador General San Martin,Libertador General San Martin,-23.81954222,-64.78998356,47559,Argentina,AR,ARG,Jujuy
Chilecito,Chilecito,-29.16552081,-67.49999903,20343,Argentina,AR,ARG,La Rioja
Chamical,Chamical,-30.34958291,-66.3166604,8989,Argentina,AR,ARG,La Rioja
Los Blancos,Los Blancos,-23.59960732,-62.60003972,1145,Argentina,AR,ARG,Salta
Cafayate,Cafayate,-26.08291828,-65.96660425,9478,Argentina,AR,ARG,Salta
Cerrillos,Cerrillos,-24.89963133,-65.48330042,11498,Argentina,AR,ARG,Salta
San Antonio de los Cobres,San Antonio de los Cobres,-24.18293089,-66.35001754,4000,Argentina,AR,ARG,Salta
Anatuya,Anatuya,-28.46613198,-62.83330713,14133,Argentina,AR,ARG,Santiago del Estero
Frias,Frias,-28.64958331,-65.14998743,13594,Argentina,AR,ARG,Santiago del Estero
Monte Quemado,Monte Quemado,-25.79962807,-62.86658675,11387,Argentina,AR,ARG,Santiago del Estero
Juan Jose Castelli,Juan Jose Castelli,-25.9495414,-60.61664657,9421,Argentina,AR,ARG,Chaco
Charata,Charata,-27.21628579,-61.19999597,18297,Argentina,AR,ARG,Chaco
Las Lomitas,Las Lomitas,-24.69959186,-60.60000676,7683,Argentina,AR,ARG,Formosa
Mercedes,Mercedes,-29.1795768,-58.0799797,22872.5,Argentina,AR,ARG,Corrientes
Concordia,Concordia,-31.38957111,-58.02998275,132760.5,Argentina,AR,ARG,Entre R?os
Sunchales,Sunchales,-30.93290648,-61.56661442,12655,Argentina,AR,ARG,Santa Fe
San Justo,San Justo,-30.78288979,-60.58328943,9607,Argentina,AR,ARG,Santa Fe
Vera,Vera,-29.4661743,-60.21659347,9979,Argentina,AR,ARG,Santa Fe
Reconquista,Reconquista,-29.13952757,-59.65001306,86640.5,Argentina,AR,ARG,Santa Fe
Venado Tuerto,Venado Tuerto,-33.74958209,-61.97000065,52079,Argentina,AR,ARG,Santa Fe
Esquel,Esquel,-42.90003131,-71.31661361,20048,Argentina,AR,ARG,Chubut
Zapala,Zapala,-38.90001707,-70.06666406,19152,Argentina,AR,ARG,Neuqu?n
Olavarria,Olavarria,-36.90003579,-60.3299974,65059,Argentina,AR,ARG,Ciudad de Buenos Aires
Tandil,Tandil,-37.32001015,-59.15004358,84799.5,Argentina,AR,ARG,Ciudad de Buenos Aires
Viedma,Viedma,-40.79995278,-63.0000153,54031,Argentina,AR,ARG,Ciudad de Buenos Aires
San Luis,San Luis,-33.29999713,-66.35001754,308146,Argentina,AR,ARG,San Luis
Rio Cuarto,Rio Cuarto,-33.13003335,-64.34998458,135959.5,Argentina,AR,ARG,C?rdoba
San Salvador de Jujuy,San Salvador de Jujuy,-24.1833443,-65.30002995,258739,Argentina,AR,ARG,Jujuy
San Ramon de la Nueva Oran,San Ramon de la Nueva Oran,-23.13999713,-64.32001225,69461.5,Argentina,AR,ARG,Salta
Goya,Goya,-29.13999266,-59.26998458,71274.5,Argentina,AR,ARG,Corrientes
Puerto San Julian,Puerto San Julian,-49.30000242,-67.71665247,2347,Argentina,AR,ARG,Santa Cruz
Perito Moreno,Perito Moreno,-46.60001219,-70.93335535,3766,Argentina,AR,ARG,Santa Cruz
Rio Grande,Rio Grande,-53.79144552,-67.6989952,31095,Argentina,AR,ARG,Tierra del Fuego
Ushuaia,Ushuaia,-54.79000324,-68.31000126,50483.5,Argentina,AR,ARG,Tierra del Fuego
Sarmiento,Sarmiento,-45.60002155,-69.08331323,5185,Argentina,AR,ARG,Chubut
San Rafael,San Rafael,-34.60002114,-68.33333317,79523.5,Argentina,AR,ARG,Mendoza
Necochea,Necochea,-38.55998615,-58.74999048,70562,Argentina,AR,ARG,Ciudad de Buenos Aires
Rio Colorado,Rio Colorado,-38.96657632,-64.08328251,11499,Argentina,AR,ARG,La Pampa
Catamarca,Catamarca,-28.47000771,-65.78000065,162586,Argentina,AR,ARG,Catamarca
La Rioja,La Rioja,-29.40995034,-66.84996118,147130,Argentina,AR,ARG,La Rioja
Santiago del Estero,Santiago del Estero,-27.78333128,-64.26665633,317549.5,Argentina,AR,ARG,Santiago del Estero
Resistencia,Resistencia,-27.45999184,-58.99002751,368455.5,Argentina,AR,ARG,Chaco
Gualeguaychu,Gualeguaychu,-33.02001422,-58.52000452,55860.5,Argentina,AR,ARG,Entre R?os
El Calafate,El Calafate,-50.33332436,-72.30001612,6329,Argentina,AR,ARG,Santa Cruz
San Juan,San Juan,-31.55002643,-68.51998845,433892,Argentina,AR,ARG,San Juan
Rawson,Rawson,-43.3000069,-65.09999048,25062.5,Argentina,AR,ARG,Chubut
Neuquen,Neuquen,-38.95003986,-68.05999068,213823.5,Argentina,AR,ARG,Neuqu?n
Santa Rosa,Santa Rosa,-36.6200012,-64.29998763,97693.5,Argentina,AR,ARG,La Pampa
San Carlos de Bariloche,San Carlos de Bariloche,-41.14995726,-71.29999964,91953,Argentina,AR,ARG,R?o Negro
Salta,Salta,-24.78335936,-65.41663782,484646,Argentina,AR,ARG,Salta
Tucum?n,San Miguel de Tucuman,-26.81600014,-65.21662419,678803.5,Argentina,AR,ARG,Tucum?n
Formosa,Formosa,-26.17283527,-58.1828158,202272,Argentina,AR,ARG,Formosa
Santa Fe,Santa Fe,-31.62387205,-60.69000126,393504,Argentina,AR,ARG,Santa Fe
Rosario,Rosario,-32.95112954,-60.66630762,1094784.5,Argentina,AR,ARG,Santa Fe
Puerto Deseado,Puerto Deseado,-47.75001951,-65.89996749,3305,Argentina,AR,ARG,Santa Cruz
Rio Gallegos,Rio Gallegos,-51.63329669,-69.21658675,77183,Argentina,AR,ARG,Santa Cruz
Comodoro Rivadavia,Comodoro Rivadavia,-45.87003091,-67.49999903,123291,Argentina,AR,ARG,Chubut
Mendoza,Mendoza,-32.88333006,-68.81661117,827815,Argentina,AR,ARG,Mendoza
Bahia Blanca,Bahia Blanca,-38.74002684,-62.2650214,279041,Argentina,AR,ARG,Ciudad de Buenos Aires
Mar del Plata,Mar del Plata,-38.00002033,-57.57998438,554916,Argentina,AR,ARG,Ciudad de Buenos Aires
C?rdoba,Cordoba,-31.39995807,-64.18229456,1374467.5,Argentina,AR,ARG,C?rdoba
Posadas,Posadas,-27.3578321,-55.88510735,334589.5,Argentina,AR,ARG,Misiones
Buenos Aires,Buenos Aires,-34.60250161,-58.39753137,11862073,Argentina,AR,ARG,Ciudad de Buenos Aires
Ashtarak,Ashtarak,40.3016667,44.3591667,18779,Armenia,AM,ARM,Aragatsotn
Ijevan,Ijevan,40.8755556,45.1491667,14737,Armenia,AM,ARM,Tavush
Artashat,Artashat,39.9538889,44.5505556,20562,Armenia,AM,ARM,Ararat
Gavarr,Gavarr,40.3588889,45.1266667,21680,Armenia,AM,ARM,Gegharkunik
Yeghegnadzor,Yeghegnadzor,39.7611111,45.3333333,8200,Armenia,AM,ARM,Vayots Dzor
Gyumri,Gyumri,40.78943402,43.84749385,140277.5,Armenia,AM,ARM,Shirak
Vanadzor,Vanadzor,40.81276593,44.48828162,89295,Armenia,AM,ARM,Lori
Yerevan,Yerevan,40.18115074,44.51355139,1097742.5,Armenia,AM,ARM,Erevan
Oranjestad,Oranjestad,12.53038373,-70.02899195,50887.5,Aruba,AW,ABW,
Central Coast,Central Coast,-33.42004148,151.3000048,3026,Australia,AU,AUS,New South Wales
Sunshine Coast,Sunshine Coast,-26.67998777,153.0500272,57215.5,Australia,AU,AUS,Queensland
Bourke,Bourke,-30.1,145.9333333,2475,Australia,AU,AUS,New South Wales
Pine Creek,Pine Creek,-13.81617348,131.816698,505,Australia,AU,AUS,Northern Territory
Adelaide River,Adelaide River,-13.2495414,131.0999975,237,Australia,AU,AUS,Northern Territory
McMinns Lagoon,McMinns Lagoon,-12.53289264,131.0500264,5025,Australia,AU,AUS,Northern Territory
Newcastle Waters,Newcastle Waters,-17.55279295,133.4672432,10,Australia,AU,AUS,Northern Territory
Ravensthorpe,Ravensthorpe,-33.58287392,120.0333345,639,Australia,AU,AUS,Western Australia
Wagin,Wagin,-33.29958372,117.3499841,1037.5,Australia,AU,AUS,Western Australia
Roebourne,Roebourne,-20.7829317,117.1333048,11281.5,Australia,AU,AUS,Western Australia
Pannawonica,Pannawonica,-21.63657469,116.3250337,686,Australia,AU,AUS,Western Australia
Tom Price,Tom Price,-22.69346108,117.7930578,1822,Australia,AU,AUS,Western Australia
Kalbarri,Kalbarri,-27.66618081,114.1666642,1537,Australia,AU,AUS,Western Australia
Mount Magnet,Mount Magnet,-28.06620807,117.8166739,424,Australia,AU,AUS,Western Australia
Morawa,Morawa,-29.21626707,116.0000406,259,Australia,AU,AUS,Western Australia
Port Denison,Port Denison,-29.28282632,114.9166442,1213,Australia,AU,AUS,Western Australia
Merredin,Merredin,-31.48284707,118.2666723,2054,Australia,AU,AUS,Western Australia
Mount Barker,Mount Barker,-34.632784,117.6666056,1771.5,Australia,AU,AUS,Western Australia
Katanning,Katanning,-33.69955931,117.5500752,3140,Australia,AU,AUS,Western Australia
Narrogin,Narrogin,-32.93288776,117.1666361,3995,Australia,AU,AUS,Western Australia
Gingin,Gingin,-31.34957355,115.9000468,1446,Australia,AU,AUS,Western Australia
Bunbury,Bunbury,-33.34428384,115.6502429,26683.5,Australia,AU,AUS,Western Australia
Kwinana,Kwinana,-32.23939004,115.7702356,18817.5,Australia,AU,AUS,Western Australia
Southern Cross,Southern Cross,-31.216145,119.3166857,187,Australia,AU,AUS,Western Australia
Kaltukatjara,Kaltukatjara,-25.78841429,128.9973352,355,Australia,AU,AUS,Northern Territory
Queanbeyan,Queanbeyan,-35.3546004,149.2113468,32408,Australia,AU,AUS,Australian Capital Territory
Tweed Heads,Tweed Heads,-28.1825834,153.5466377,33065,Australia,AU,AUS,New South Wales
Ivanhoe,Ivanhoe,-32.89960814,144.3000187,265,Australia,AU,AUS,New South Wales
Wilcannia,Wilcannia,-31.56620115,143.3833304,442,Australia,AU,AUS,New South Wales
Merimbula,Merimbula,-36.89962238,149.9000386,3607.5,Australia,AU,AUS,New South Wales
Echuca,Echuca,-36.12959186,144.750017,13460,Australia,AU,AUS,New South Wales
Deniliquin,Deniliquin,-35.5295768,144.9500048,6019.5,Australia,AU,AUS,New South Wales
Nowra,Nowra,-34.88284625,150.6000476,61036.5,Australia,AU,AUS,New South Wales
Ulladulla,Ulladulla,-35.34953611,150.4700297,6811,Australia,AU,AUS,New South Wales
Batemans Bay,Batemans Bay,-35.68961871,150.2073067,5604,Australia,AU,AUS,New South Wales
Cooma,Cooma,-36.23955931,149.1200345,5661.5,Australia,AU,AUS,New South Wales
Tumut,Tumut,-35.30959023,148.2200378,4873,Australia,AU,AUS,New South Wales
Leeton,Leeton,-34.54493406,146.3973067,6277,Australia,AU,AUS,New South Wales
Young,Young,-34.30959959,148.2900077,6422,Australia,AU,AUS,New South Wales
Cowra,Cowra,-33.82962889,148.6800097,5729.5,Australia,AU,AUS,New South Wales
Forbes,Forbes,-33.38960407,148.0199983,4076.5,Australia,AU,AUS,New South Wales
Goulburn,Goulburn,-34.74957273,149.7101794,16444,Australia,AU,AUS,New South Wales
Kiama,Kiama,-34.70957518,150.8400329,10379,Australia,AU,AUS,New South Wales
Katoomba,Katoomba,-33.70694904,150.320013,20334.5,Australia,AU,AUS,New South Wales
Richmond,Richmond,-33.59951373,150.7399873,9720,Australia,AU,AUS,New South Wales
Lithgow,Lithgow,-33.49610919,150.152788,10338,Australia,AU,AUS,New South Wales
Parkes,Parkes,-33.12956826,148.170015,7160,Australia,AU,AUS,New South Wales
Bathurst,Bathurst,-33.41962807,149.5700329,6111,Australia,AU,AUS,New South Wales
Maitland,Maitland,-32.72096271,151.555028,10026.5,Australia,AU,AUS,New South Wales
Singleton,Singleton,-32.56949909,151.1600134,8340.5,Australia,AU,AUS,New South Wales
Mudgee,Mudgee,-32.58960122,149.5801098,5391,Australia,AU,AUS,New South Wales
Muswellbrook,Muswellbrook,-32.26956907,150.890004,8171,Australia,AU,AUS,New South Wales
Taree,Taree,-31.89760211,152.4618461,30131.5,Australia,AU,AUS,New South Wales
Kempsey,Kempsey,-31.08736733,152.8220308,10681,Australia,AU,AUS,New South Wales
Gunnedah,Gunnedah,-30.9870117,150.2622904,6204,Australia,AU,AUS,New South Wales
Coffs Harbour,Coffs Harbour,-30.3070532,153.1122973,48961,Australia,AU,AUS,New South Wales
Narrabri,Narrabri,-30.33190957,149.7874357,6105.5,Australia,AU,AUS,New South Wales
Inverell,Inverell,-29.7667761,151.1125744,6845.5,Australia,AU,AUS,New South Wales
Yamba,Yamba,-29.42299136,153.353312,1806,Australia,AU,AUS,New South Wales
Ballina,Ballina,-28.86135333,153.5679801,13997.5,Australia,AU,AUS,New South Wales
Wagga Wagga,Wagga Wagga,-35.12215981,147.3399882,45549,Australia,AU,AUS,New South Wales
Scone,Scone,-32.07960651,150.8501098,4624,Australia,AU,AUS,New South Wales
Byron Bay,Byron Bay,-28.65650796,153.6128869,5244.5,Australia,AU,AUS,New South Wales
Berri,Berri,-34.28293455,140.6000378,4523,Australia,AU,AUS,South Australia
Peterborough,Peterborough,-32.96616738,138.8333239,1351,Australia,AU,AUS,South Australia
Wallaroo,Wallaroo,-33.9328784,137.6332938,2442,Australia,AU,AUS,South Australia
Clare,Clare,-33.8328845,138.6000048,2729,Australia,AU,AUS,South Australia
Meningie,Meningie,-35.69954059,139.3333451,850,Australia,AU,AUS,South Australia
Kingston South East,Kingston South East,-36.83280475,139.8500577,206,Australia,AU,AUS,South Australia
Bordertown,Bordertown,-36.31619546,140.7666426,1976,Australia,AU,AUS,South Australia
Penola,Penola,-37.38295205,140.8166654,1513,Australia,AU,AUS,South Australia
Kingoonya,Kingoonya,-30.89957518,135.2999996,50,Australia,AU,AUS,South Australia
Kimba,Kimba,-33.14961871,136.4333671,636,Australia,AU,AUS,South Australia
Streaky Bay,Streaky Bay,-32.81187176,134.2149296,614.5,Australia,AU,AUS,South Australia
Cowell,Cowell,-33.68286782,136.9166451,537,Australia,AU,AUS,South Australia
Tumby Bay,Tumby Bay,-34.38292845,136.0833109,1791,Australia,AU,AUS,South Australia
Andamooka,Andamooka,-30.43097329,137.1655704,528,Australia,AU,AUS,South Australia
Woomera,Woomera,-31.14958576,136.8000114,450,Australia,AU,AUS,South Australia
Port Pirie,Port Pirie,-33.19106321,137.9900162,12417,Australia,AU,AUS,South Australia
Gawler,Gawler,-34.60735919,138.7263537,15542.5,Australia,AU,AUS,South Australia
Murray Bridge,Murray Bridge,-35.12960122,139.2600162,14185.5,Australia,AU,AUS,South Australia
Victor Harbor,Victor Harbor,-35.55960081,138.6173164,7489,Australia,AU,AUS,South Australia
Hamilton,Hamilton,-37.73119953,142.0234135,6992.5,Australia,AU,AUS,Victoria
Ouyen,Ouyen,-35.06619424,142.3166772,912,Australia,AU,AUS,Victoria
Colac,Colac,-38.33953449,143.5800109,7450,Australia,AU,AUS,Victoria
Stawell,Stawell,-37.05961261,142.7600093,4596,Australia,AU,AUS,Victoria
Horsham,Horsham,-36.70960814,142.1900183,11985.5,Australia,AU,AUS,Victoria
Ararat,Ararat,-37.27954751,142.9099743,5464,Australia,AU,AUS,Victoria
Maryborough,Maryborough,-37.04958738,143.729976,5838.5,Australia,AU,AUS,Victoria
Bairnsdale,Bairnsdale,-37.82959145,147.6099975,9427,Australia,AU,AUS,Victoria
Sale,Sale,-38.10957436,147.0600052,17701.5,Australia,AU,AUS,Victoria
Traralgon,Traralgon,-38.19959471,146.5300118,16982.5,Australia,AU,AUS,Victoria
Wonthaggi,Wonthaggi,-38.60949217,145.5900175,4471.5,Australia,AU,AUS,Victoria
Cranbourne,Cranbourne,-38.09960081,145.2833695,249955,Australia,AU,AUS,Victoria
Ballarat,Ballarat,-37.55958209,143.8400468,73404,Australia,AU,AUS,Victoria
Melton,Melton,-37.68954832,144.570028,29750,Australia,AU,AUS,Victoria
Seymour,Seymour,-37.03423948,145.1273067,3693,Australia,AU,AUS,Victoria
Shepparton,Shepparton,-36.37458982,145.3913732,33430.5,Australia,AU,AUS,Victoria
Cobram,Cobram,-35.91963051,145.6500138,4659,Australia,AU,AUS,Victoria
Swan Hill,Swan Hill,-35.33961424,143.5400134,9073,Australia,AU,AUS,Victoria
Sunbury,Sunbury,-37.56960732,144.7100195,18677.5,Australia,AU,AUS,Victoria
Proserpine,Proserpine,-20.41623574,148.5834781,3976,Australia,AU,AUS,Queensland
Theodore,Theodore,-24.94949909,150.0833349,246,Australia,AU,AUS,Queensland
Eidsvold,Eidsvold,-25.36621784,151.1333483,459,Australia,AU,AUS,Queensland
Barcaldine,Barcaldine,-23.56617267,145.2833695,1068,Australia,AU,AUS,Queensland
Winton,Winton,-22.39962889,143.0332743,1157,Australia,AU,AUS,Queensland
Longreach,Longreach,-23.44959064,144.2500476,2894,Australia,AU,AUS,Queensland
Caboolture,Caboolture,-27.08296059,152.9499816,26495.5,Australia,AU,AUS,Queensland
Warwick,Warwick,-28.22924721,152.0203226,10024,Australia,AU,AUS,Queensland
Kingaroy,Kingaroy,-26.53896279,151.840592,7494.5,Australia,AU,AUS,Queensland
Dalby,Dalby,-27.19385822,151.2657434,9818.5,Australia,AU,AUS,Queensland
Bongaree,Bongaree,-27.07872313,153.1508996,10327.5,Australia,AU,AUS,Queensland
Gympie,Gympie,-26.18859658,152.6709289,11338,Australia,AU,AUS,Queensland
Ingham,Ingham,-18.64957355,146.1666231,5996.5,Australia,AU,AUS,Queensland
Birdsville,Birdsville,-25.89962197,139.3666247,283,Australia,AU,AUS,Queensland
Bedourie,Bedourie,-24.34958738,139.4666186,142,Australia,AU,AUS,Queensland
Boulia,Boulia,-22.89959837,139.9000288,402.5,Australia,AU,AUS,Queensland
Richmond,Richmond,-20.71626911,143.1333199,296,Australia,AU,AUS,Queensland
Burketown,Burketown,-17.71609048,139.5666125,186.5,Australia,AU,AUS,Queensland
Hervey Bay,Hervey Bay,-25.28870319,152.8409444,25114,Australia,AU,AUS,Queensland
Biloela,Biloela,-24.39356403,150.4960746,4366.5,Australia,AU,AUS,Queensland
Yeppoon,Yeppoon,-23.13291746,150.7567305,6450.5,Australia,AU,AUS,Queensland
Emerald,Emerald,-23.51222247,148.1673278,7489,Australia,AU,AUS,Queensland
Moranbah,Moranbah,-22.00156533,148.0380334,7357,Australia,AU,AUS,Queensland
Charters Towers,Charters Towers,-20.08090737,146.2587105,8369.5,Australia,AU,AUS,Queensland
Ayr,Ayr,-19.57024087,147.3994677,7166,Australia,AU,AUS,Queensland
Atherton,Atherton,-17.27027789,145.469353,6132.5,Australia,AU,AUS,Queensland
Port Douglas,Port Douglas,-16.48458812,145.4587219,2004.5,Australia,AU,AUS,Queensland
Smithton,Smithton,-40.83292234,145.1166613,3351,Australia,AU,AUS,Tasmania
Scottsdale,Scottsdale,-41.14949217,147.5166699,1683.5,Australia,AU,AUS,Tasmania
Bicheno,Bicheno,-41.87838825,148.2886124,177,Australia,AU,AUS,Tasmania
Oatlands,Oatlands,-42.29960285,147.3666015,1157,Australia,AU,AUS,Tasmania
Queenstown,Queenstown,-42.08292356,145.5500199,1658,Australia,AU,AUS,Tasmania
Kingston,Kingston,-42.99113686,147.3084139,12652,Australia,AU,AUS,Tasmania
Tennant Creek,Tennant Creek,-19.65002928,134.200015,3490.5,Australia,AU,AUS,Northern Territory
Yulara,Yulara,-25.24054075,130.9888932,930,Australia,AU,AUS,Northern Territory
Erldunda,Erldunda,-25.23330605,133.1999727,10,Australia,AU,AUS,Northern Territory
Norseman,Norseman,-32.20001259,121.7666137,1004,Australia,AU,AUS,Western Australia
Halls Creek,Halls Creek,-18.26670286,127.7667126,1209,Australia,AU,AUS,Western Australia
Kununurra,Kununurra,-15.76659707,128.7333203,5229.5,Australia,AU,AUS,Western Australia
Derby,Derby,-17.29999184,123.9666345,3199,Australia,AU,AUS,Western Australia
Onslow,Onslow,-21.65759354,115.0962959,573,Australia,AU,AUS,Western Australia
Exmouth,Exmouth,-21.93109987,114.1233469,1085,Australia,AU,AUS,Western Australia
Carnarvon,Carnarvon,-24.89983803,113.6501066,7392,Australia,AU,AUS,Western Australia
Newman,Newman,-23.36659829,119.7333011,2678,Australia,AU,AUS,Western Australia
Meekatharra,Meekatharra,-26.59999266,118.4832999,654,Australia,AU,AUS,Western Australia
Three Springs,Three Springs,-29.53330198,115.7499784,190,Australia,AU,AUS,Western Australia
Manjimup,Manjimup,-34.23332518,116.1500057,4016.5,Australia,AU,AUS,Western Australia
Northam,Northam,-31.65658323,116.6533858,5330,Australia,AU,AUS,Western Australia
Esperance,Esperance,-33.857307,121.8888973,7205,Australia,AU,AUS,Western Australia
Leonara,Leonara,-28.88150714,121.3280358,227,Australia,AU,AUS,Western Australia
Laverton,Laverton,-28.62700071,122.4040425,316,Australia,AU,AUS,Western Australia
Wyndham,Wyndham,-15.37395953,128.3600614,734.5,Australia,AU,AUS,Western Australia
Albury,Albury,-36.06003538,146.9200138,68534,Australia,AU,AUS,New South Wales
Forster-Tuncurry,Forster-Tuncurry,-32.19313963,152.5266483,13275.5,Australia,AU,AUS,New South Wales
Port Macquarie,Port Macquarie,-31.44501992,152.9186657,42070,Australia,AU,AUS,New South Wales
Tamworth,Tamworth,-31.10261188,150.9171342,35080,Australia,AU,AUS,New South Wales
Grafton,Grafton,-29.71199909,152.9376827,7871.5,Australia,AU,AUS,New South Wales
Moree,Moree,-29.469895,149.8300687,8062,Australia,AU,AUS,New South Wales
Goondiwindi,Goondiwindi,-28.55480874,150.325284,4251,Australia,AU,AUS,New South Wales
Lismore,Lismore,-28.81665322,153.2931132,28065.5,Australia,AU,AUS,New South Wales
Wollongong,Wollongong,-34.41538125,150.890004,201319.5,Australia,AU,AUS,New South Wales
Ceduna,Ceduna,-32.09913464,133.6622674,1252.5,Australia,AU,AUS,South Australia
Mount Gambier,Mount Gambier,-37.83134845,140.7650406,21818.5,Australia,AU,AUS,South Australia
Port Augusta,Port Augusta,-32.49002073,137.7700297,11186.5,Australia,AU,AUS,South Australia
Warrnambool,Warrnambool,-38.37999713,142.4700012,29882,Australia,AU,AUS,Victoria
Mildura,Mildura,-34.18500771,142.1513643,33324.5,Australia,AU,AUS,Victoria
Geelong,Geelong,-38.16749505,144.3956335,149336,Australia,AU,AUS,Victoria
Camooweal,Camooweal,-19.91673134,138.1166752,187,Australia,AU,AUS,Queensland
Quilpie,Quilpie,-26.61663247,144.2500476,560,Australia,AU,AUS,Queensland
Charleville,Charleville,-26.40000486,146.2500288,1900,Australia,AU,AUS,Queensland
Hughenden,Hughenden,-20.85000771,144.2000248,421,Australia,AU,AUS,Queensland
Caloundra,Caloundra,-26.80003213,153.1333296,33737,Australia,AU,AUS,Queensland
Roma,Roma,-26.55937498,148.7907006,4560.5,Australia,AU,AUS,Queensland
Toowoomba,Toowoomba,-27.56453327,151.9555204,86711,Australia,AU,AUS,Queensland
Georgetown,Georgetown,-18.30003416,143.5332955,818,Australia,AU,AUS,Queensland
Thargomindah,Thargomindah,-27.99995888,143.816689,203,Australia,AU,AUS,Queensland
Weipa,Weipa,-12.66663125,141.8666272,2830,Australia,AU,AUS,Queensland
Karumba,Karumba,-17.48333982,140.8334086,173,Australia,AU,AUS,Queensland
Cloncurry,Cloncurry,-20.69999103,140.4999922,1202,Australia,AU,AUS,Queensland
Maryborough,Maryborough,-25.54910073,152.7209,18920.5,Australia,AU,AUS,Queensland
Bundaberg,Bundaberg,-24.87906411,152.3508968,46062,Australia,AU,AUS,Queensland
Gladstone,Gladstone,-23.8533386,151.2467264,29055,Australia,AU,AUS,Queensland
Bowen,Bowen,-20.00132566,148.208669,10983,Australia,AU,AUS,Queensland
Innisfail,Innisfail,-17.53134723,146.0386722,9707,Australia,AU,AUS,Queensland
Mackay,Mackay,-21.14389158,149.1500069,66053.5,Australia,AU,AUS,Queensland
Burnie,Burnie,-41.06660317,145.9166642,18490.5,Australia,AU,AUS,Tasmania
Launceston,Launceston,-41.44983559,147.1301818,65106.5,Australia,AU,AUS,Tasmania
Katherine,Katherine,-14.46662474,132.266593,8171.5,Australia,AU,AUS,Northern Territory
Busselton,Busselton,-33.65640949,115.3486592,9595,Australia,AU,AUS,Western Australia
Mandurah,Mandurah,-32.52348259,115.7470567,52866,Australia,AU,AUS,Western Australia
Broome,Broome,-17.96177069,122.2307681,11890.5,Australia,AU,AUS,Western Australia
Kalgoorlie,Kalgoorlie,-30.73539915,121.4600175,32058,Australia,AU,AUS,Western Australia
Albany,Albany,-35.0169466,117.8916048,25179,Australia,AU,AUS,Western Australia
Port Hedland,Port Hedland,-20.31040241,118.6060315,8997,Australia,AU,AUS,Western Australia
Karratha,Karratha,-20.73037677,116.8700134,16636,Australia,AU,AUS,Western Australia
Geraldton,Geraldton,-28.76663043,114.5999711,27065,Australia,AU,AUS,Western Australia
Griffith,Griffith,-34.29001422,146.0400158,11664.5,Australia,AU,AUS,New South Wales
Orange,Orange,-33.27999835,149.0999841,36708,Australia,AU,AUS,New South Wales
Dubbo,Dubbo,-32.25995726,148.5973274,30467.5,Australia,AU,AUS,New South Wales
Armidale,Armidale,-30.51231199,151.667476,21793.5,Australia,AU,AUS,New South Wales
Broken Hill,Broken Hill,-31.94995034,141.4331136,17232.5,Australia,AU,AUS,New South Wales
Port Lincoln,Port Lincoln,-34.73324298,135.86658,12438.5,Australia,AU,AUS,South Australia
Whyalla,Whyalla,-33.02502684,137.5614119,21102,Australia,AU,AUS,South Australia
Portland,Portland,-38.33999957,141.5900032,10324.5,Australia,AU,AUS,Victoria
Bendigo,Bendigo,-36.75999266,144.2800199,68790,Australia,AU,AUS,Victoria
Wangaratta,Wangaratta,-36.36001707,146.3,11369.5,Australia,AU,AUS,Victoria
Windorah,Windorah,-25.43324217,142.6501969,158,Australia,AU,AUS,Queensland
Mount Isa,Mount Isa,-20.72386554,139.490028,27596,Australia,AU,AUS,Queensland
Rockhampton,Rockhampton,-23.36391111,150.5200008,59024.5,Australia,AU,AUS,Queensland
Cairns,Cairns,-16.88783986,145.7633309,132107,Australia,AU,AUS,Queensland
Gold Coast,Gold Coast,-28.08150429,153.4482458,429954.5,Australia,AU,AUS,Queensland
Devonport,Devonport,-41.19266757,146.3311017,17932.5,Australia,AU,AUS,Tasmania
Darwin,Darwin,-12.42535398,130.8500386,82973,Australia,AU,AUS,Northern Territory
Alice Springs,Alice Springs,-23.70099648,133.8800345,26949,Australia,AU,AUS,Northern Territory
Canberra,Canberra,-35.28302855,149.1290262,280866,Australia,AU,AUS,Australian Capital Territory
Newcastle,Newcastle,-32.84534788,151.8150122,816285.5,Australia,AU,AUS,New South Wales
Adelaide,Adelaide,-34.93498777,138.6000048,990677,Australia,AU,AUS,South Australia
Townsville,Townsville,-19.24995034,146.7699971,129212,Australia,AU,AUS,Queensland
Brisbane,Brisbane,-27.45503091,153.0350927,1393176.5,Australia,AU,AUS,Queensland
Hobart,Hobart,-42.85000853,147.2950297,64285,Australia,AU,AUS,Tasmania
Perth,Perth,-31.95501463,115.8399987,1206108,Australia,AU,AUS,Western Australia
Melbourne,Melbourne,-37.82003131,144.9750162,2131812.5,Australia,AU,AUS,Victoria
Sydney,Sydney,-33.92001097,151.1851798,4135711,Australia,AU,AUS,New South Wales
Bregenz,Bregenz,47.51669707,9.766701588,26928,Austria,AT,AUT,Vorarlberg
Eisenstadt,Eisenstadt,47.83329908,16.53329747,13165,Austria,AT,AUT,Burgenland
Wiener Neustadt,Wiener Neustadt,47.81598187,16.24995357,60621.5,Austria,AT,AUT,Nieder?sterreich
Graz,Graz,47.0777582,15.41000484,242780,Austria,AT,AUT,Steiermark
Klagenfurt,Klagenfurt,46.62034426,14.3100203,88588,Austria,AT,AUT,K?rnten
Linz,Linz,48.31923281,14.28878129,265161.5,Austria,AT,AUT,Ober?sterreich
Passau,Passau,48.56704714,13.46660925,50000,Austria,AT,AUT,Ober?sterreich
Salzburg,Salzburg,47.81047833,13.0400203,178274,Austria,AT,AUT,Salzburg
Innsbruck,Innsbruck,47.28040733,11.4099906,133840.5,Austria,AT,AUT,Tirol
Vienna,Vienna,48.20001528,16.36663896,2065500,Austria,AT,AUT,Wien
Gadabay,Gadabay,40.5655556,45.8161111,8657,Azerbaijan,AZ,AZE,Gadabay
Goranboy,Goranboy,40.6102778,46.7897222,7333,Azerbaijan,AZ,AZE,Goranboy
Tovuz,Tovuz,40.9922222,45.6288889,12626,Azerbaijan,AZ,AZE,Tovuz
Agdam,Agdam,40.9052778,45.5563889,0,Azerbaijan,AZ,AZE,Tovuz
Qabala,Qabala,40.9813889,47.8458333,11867,Azerbaijan,AZ,AZE,Qabala
Oguz,Oguz,41.0708333,47.4583333,6876,Azerbaijan,AZ,AZE,Oguz
Ganca,Ganca,40.68499595,46.35002844,301699.5,Azerbaijan,AZ,AZE,Ganca
Yevlax,Yevlax,40.61719647,47.15003129,50014,Azerbaijan,AZ,AZE,Yevlax
Sumqayt,Sumqayt,40.58001528,49.62998328,272154.5,Azerbaijan,AZ,AZE,Sumqayit
Ali Bayramli,Ali Bayramli,39.93230288,48.92025915,70452,Azerbaijan,AZ,AZE,?li Bayramli
Goycay,Goycay,40.65342165,47.74058956,35031.5,Azerbaijan,AZ,AZE,G?y?ay
Lankaran,Lankaran,38.7540027,48.85106441,60180,Azerbaijan,AZ,AZE,Astara
Saki,Saki,41.19232932,47.17054683,63579.5,Azerbaijan,AZ,AZE,S?ki
Stepanakert,Stepanakert,39.81564333,46.75196773,57473,Azerbaijan,AZ,AZE,Xocali
Kapan,Kapan,39.20152061,46.41498572,37724,Azerbaijan,AZ,AZE,Z?ngilan
Naxcivan,Naxcivan,39.2092204,45.41220455,79771,Azerbaijan,AZ,AZE,Nax?ivan
Baku,Baku,40.39527203,49.86221716,2007150,Azerbaijan,AZ,AZE,Baki
Manama,Manama,26.23613629,50.58305172,360697,Bahrain,BH,BHR,
Tangail,Tangail,24.24997845,89.92003048,180144,Bangladesh,BD,BGD,Dhaka
Sylhet,Sylhet,24.90355613,91.87360632,237000,Bangladesh,BD,BGD,Sylhet
Mymensingh,Mymensingh,24.75041302,90.3800024,330126,Bangladesh,BD,BGD,Dhaka
Jamalpur,Jamalpur,24.90042971,89.95000281,167900,Bangladesh,BD,BGD,Dhaka
Narayanganj,Narayanganj,23.62040448,90.49999508,223622,Bangladesh,BD,BGD,Dhaka
Jessore,Jessore,23.17043194,89.19997107,243987,Bangladesh,BD,BGD,Khulna
Barisal,Barisal,22.70040895,90.37498979,202242,Bangladesh,BD,BGD,Barisal
Comilla,Comilla,23.47041363,91.16998002,389411,Bangladesh,BD,BGD,Chittagong
Pabna,Pabna,24.00038129,89.24999385,137888,Bangladesh,BD,BGD,Rajshahi
Nawabganj,Nawabganj,24.58039756,88.34999711,142361,Bangladesh,BD,BGD,Rajshahi
Saidpur,Saidpur,25.80042645,88.99998328,232209,Bangladesh,BD,BGD,Rajshahi
Rangpur,Rangpur,25.75001609,89.28001786,285564,Bangladesh,BD,BGD,Rajshahi
Khulna,Khulna,22.839987,89.56000077,1447669.5,Bangladesh,BD,BGD,Khulna
Rajshahi,Rajshahi,24.37498374,88.6050203,755066.5,Bangladesh,BD,BGD,Rajshahi
Dhaka,Dhaka,23.72305971,90.40857947,9899167,Bangladesh,BD,BGD,Dhaka
Chittagong,Chittagong,22.32999229,91.79996741,4224611,Bangladesh,BD,BGD,Chittagong
Bridgetown,Bridgetown,13.10200258,-59.61652674,143865,Barbados,BB,BRB,Saint Michael
Baranavichy,Baranavichy,53.13684572,26.01344031,156514.5,Belarus,BY,BLR,Brest
Polatsk,Polatsk,55.48938946,28.78598425,79216,Belarus,BY,BLR,Vitsyebsk
Maladzyechna,Maladzyechna,54.31878908,26.86532629,96055,Belarus,BY,BLR,Minsk
Pinsk,Pinsk,52.12786338,26.09405554,120838.5,Belarus,BY,BLR,Brest
Mazyr,Mazyr,52.04595624,29.27215613,100936,Belarus,BY,BLR,Homyel'
Mahilyow,Mahilyow,53.89850466,30.32465002,343527,Belarus,BY,BLR,Mahilyow
Babruysk,Babruysk,53.12656211,29.19278113,212821.5,Belarus,BY,BLR,Mahilyow
Orsha,Orsha,54.51531455,30.42154333,130276.5,Belarus,BY,BLR,Vitsyebsk
Lida,Lida,53.88847943,25.28464758,99126,Belarus,BY,BLR,Hrodna
Hrodna,Hrodna,53.67787213,23.83409013,285867,Belarus,BY,BLR,Hrodna
Barysaw,Barysaw,54.22600405,28.49215206,127694.5,Belarus,BY,BLR,Minsk
Homyel,Homyel,52.43001548,31.00000932,472337.5,Belarus,BY,BLR,Homyel'
Vitsyebsk,Vitsyebsk,55.18871014,30.18533036,333318.5,Belarus,BY,BLR,Vitsyebsk
Brest,Brest,52.09998395,23.69998979,266775,Belarus,BY,BLR,Brest
Minsk,Minsk,53.89997744,27.56662716,1691069,Belarus,BY,BLR,Minsk
Mons,Mons,50.44599911,3.939003561,91277,Belgium,BE,BEL,Hainaut
Hasselt,Hasselt,50.96400317,5.483997561,69222,Belgium,BE,BEL,Limburg
Arlon,Arlon,49.68330313,5.816700472,26179,Belgium,BE,BEL,Arlon
Gent,Gent,51.02999758,3.700021931,337914.5,Belgium,BE,BEL,East Flanders
Liege,Liege,50.62999615,5.580010537,472803,Belgium,BE,BEL,Liege
Brugge,Brugge,51.22037355,3.230024779,131589,Belgium,BE,BEL,Brugge
Namur,Namur,50.47039349,4.870028034,97155.5,Belgium,BE,BEL,Namur
Charleroi,Charleroi,50.42039654,4.450001992,272749.5,Belgium,BE,BEL,Charleroi
Antwerpen,Antwerpen,51.22037355,4.415017048,689902.5,Belgium,BE,BEL,Antwerp
Brussels,Brussels,50.83331708,4.333316608,1381011,Belgium,BE,BEL,Brussels
El Cayo,El Cayo,17.15599807,-89.06100252,13451,Belize,BZ,BLZ,Cayo
Corozal,Corozal,18.39799811,-88.3880005,8724,Belize,BZ,BLZ,Corozal
Dangriga,Dangriga,16.97003522,-88.22000045,8506,Belize,BZ,BLZ,Stann Creek
Belize City,Belize City,17.49871096,-88.18837447,62244.5,Belize,BZ,BLZ,Belize
Orange Walk,Orange Walk,18.09043194,-88.5599797,18066.5,Belize,BZ,BLZ,Orange Walk
Punta Gorda,Punta Gorda,16.1003467,-88.81001612,6387,Belize,BZ,BLZ,Toledo
Belmopan,Belmopan,17.25203351,-88.767073,14300.5,Belize,BZ,BLZ,Cayo
Lokossa,Lokossa,6.615000092,1.715004457,86971,Benin,BJ,BEN,Mono
Kandi,Kandi,11.13036582,2.940016641,73483,Benin,BJ,BEN,Alibori
Ouidah,Ouidah,6.360372741,2.089991006,83503,Benin,BJ,BEN,Atlantique
Abomey,Abomey,7.190399596,1.98999711,82154,Benin,BJ,BEN,Zou
Natitingou,Natitingou,10.32041526,1.389982054,65356.5,Benin,BJ,BEN,Atakora
Djougou,Djougou,9.700427265,1.680041869,152708.5,Benin,BJ,BEN,Donga
Parakou,Parakou,9.340009988,2.620036172,176303,Benin,BJ,BEN,Borgou
Porto-Novo,Porto-Novo,6.483310973,2.616625528,267084,Benin,BJ,BEN,Ou?m?
Cotonou,Cotonou,6.400008564,2.519990599,726292,Benin,BJ,BEN,Ou?m?
Hamilton,Hamilton,32.29419029,-64.78393742,32910,Bermuda,BM,BMU,
Paro,Paro,27.3833011,89.51670065,15000,Bhutan,BT,BTN,Thimphu
Punakha,Punakha,27.63330305,89.83330266,5000,Bhutan,BT,BTN,Punakha
Wangdue Prodrang,Wangdue Prodrang,27.43329603,89.91669667,5000,Bhutan,BT,BTN,Wangdi Phodrang
Thimphu,Thimphu,27.47298586,89.63901404,88930.5,Bhutan,BT,BTN,Thimphu
Punata,Punata,-17.55000242,-65.83997115,20758.5,Bolivia,BO,BOL,Cochabamba
Cliza,Cliza,-17.58999998,-65.9299915,12235,Bolivia,BO,BOL,Cochabamba
Quillacollo,Quillacollo,-17.39998574,-66.27999597,227052,Bolivia,BO,BOL,Cochabamba
Puerto Villarroel,Puerto Villarroel,-16.87004393,-64.78001001,1778,Bolivia,BO,BOL,Cochabamba
Tarabuco,Tarabuco,-19.18003213,-64.91994979,2364,Bolivia,BO,BOL,Chuquisaca
Guayaramerin,Guayaramerin,-10.82999917,-65.4099974,36008,Bolivia,BO,BOL,El Beni
Santa Ana,Santa Ana,-13.7600012,-65.57996118,234478,Bolivia,BO,BOL,El Beni
Baures,Baures,-13.58001219,-63.58005742,2422,Bolivia,BO,BOL,El Beni
Sica Sica,Sica Sica,-17.33001585,-67.72998499,1006,Bolivia,BO,BOL,La Paz
Rurrenabaque,Rurrenabaque,-14.46001015,-67.55999536,11749,Bolivia,BO,BOL,La Paz
Sorata,Sorata,-15.79000649,-68.66005742,2190,Bolivia,BO,BOL,La Paz
Achacachi,Achacachi,-16.08332192,-68.66656865,8447,Bolivia,BO,BOL,La Paz
Viacha,Viacha,-16.65000568,-68.2999502,34776,Bolivia,BO,BOL,La Paz
Quime,Quime,-16.98001137,-67.22001612,3224.5,Bolivia,BO,BOL,La Paz
Llallagua,Llallagua,-18.42002684,-66.63999984,28069,Bolivia,BO,BOL,Potos?
Uncia,Uncia,-18.46999795,-66.57002995,4723,Bolivia,BO,BOL,Potos?
Uyuni,Uyuni,-20.46000568,-66.82998824,11616,Bolivia,BO,BOL,Potos?
Villa Martin,Villa Martin,-20.76655027,-67.7833409,10,Bolivia,BO,BOL,Potos?
Betanzos,Betanzos,-19.55995726,-65.45002079,4629.5,Bolivia,BO,BOL,Potos?
Portachuelo,Portachuelo,-17.36003986,-63.40001673,9982,Bolivia,BO,BOL,Santa Cruz
Samaipata,Samaipata,-18.18004148,-63.77001998,2926,Bolivia,BO,BOL,Santa Cruz
Cuevo,Cuevo,-20.45003213,-63.52998295,953,Bolivia,BO,BOL,Santa Cruz
San Carlos,San Carlos,-17.39998574,-63.72999658,5266.5,Bolivia,BO,BOL,Santa Cruz
San Lorenzo,San Lorenzo,-21.47994342,-64.77001062,3000,Bolivia,BO,BOL,Tarija
Entre Rios,Entre Rios,-21.53001788,-64.18999435,2685,Bolivia,BO,BOL,Tarija
Aiquile,Aiquile,-18.18954995,-65.18001144,5844,Bolivia,BO,BOL,Cochabamba
Padilla,Padilla,-19.29961139,-64.30996118,2276.5,Bolivia,BO,BOL,Chuquisaca
Camargo,Camargo,-20.63958128,-65.20998377,4715,Bolivia,BO,BOL,Chuquisaca
Reyes,Reyes,-14.30958006,-67.37000696,7376,Bolivia,BO,BOL,El Beni
San Borja,San Borja,-14.81962645,-66.84996118,19640,Bolivia,BO,BOL,El Beni
Magdalena,Magdalena,-13.2600834,-64.05276758,3445,Bolivia,BO,BOL,El Beni
San Ramon,San Ramon,-13.28959064,-64.70998845,5439.5,Bolivia,BO,BOL,El Beni
Puerto Heath,Puerto Heath,-12.49961302,-68.66656865,10,Bolivia,BO,BOL,La Paz
Charana,Charana,-17.5996118,-69.46659733,197,Bolivia,BO,BOL,La Paz
Puerto Acosta,Puerto Acosta,-15.49958494,-69.16666732,1123,Bolivia,BO,BOL,La Paz
Apolo,Apolo,-14.71958087,-68.41999455,4189,Bolivia,BO,BOL,La Paz
Coroico,Coroico,-16.18962034,-67.72001144,2361,Bolivia,BO,BOL,La Paz
Coro Coro,Coro Coro,-17.1696122,-68.44996688,1884,Bolivia,BO,BOL,La Paz
Sabaya,Sabaya,-19.01626951,-68.38327844,573,Bolivia,BO,BOL,Oruro
Challapata,Challapata,-18.89958413,-66.77999129,8565,Bolivia,BO,BOL,Oruro
Llica,Llica,-19.84960366,-68.25003076,553,Bolivia,BO,BOL,Potos?
Potosi,Potosi,-19.56956907,-65.75002832,160576,Bolivia,BO,BOL,Potos?
Villazon,Villazon,-22.07959674,-65.5999858,33734,Bolivia,BO,BOL,Potos?
Tupiza,Tupiza,-21.43958413,-65.72000431,25499.5,Bolivia,BO,BOL,Potos?
Montero,Montero,-17.34960122,-63.26002527,83821,Bolivia,BO,BOL,Santa Cruz
Piso Firme,Piso Firme,-13.68295164,-61.86662195,72,Bolivia,BO,BOL,Santa Cruz
Robore,Robore,-18.3295414,-59.75998051,9959,Bolivia,BO,BOL,Santa Cruz
Puerto Quijarro,Puerto Quijarro,-17.77960081,-57.77002446,10392,Bolivia,BO,BOL,Santa Cruz
San Ignacio,San Ignacio,-16.36960936,-60.96001062,24480,Bolivia,BO,BOL,Santa Cruz
Ascension,Ascension,-15.69957273,-63.07998458,12085,Bolivia,BO,BOL,Santa Cruz
San Javier,San Javier,-16.28961424,-62.50001998,4210,Bolivia,BO,BOL,Santa Cruz
San Rafael,San Rafael,-16.77950682,-60.6799502,1201,Bolivia,BO,BOL,Santa Cruz
Vallegrande,Vallegrande,-18.48958331,-64.10999923,6857.5,Bolivia,BO,BOL,Santa Cruz
Puerto Suarez,Puerto Suarez,-18.94955524,-57.8499679,17273,Bolivia,BO,BOL,Santa Cruz
Charagua,Charagua,-19.79958087,-63.2199502,3025,Bolivia,BO,BOL,Santa Cruz
Villamontes,Villamontes,-21.24956989,-63.50001062,18761,Bolivia,BO,BOL,Tarija
Bermejo,Bermejo,-22.72958291,-64.34998458,36544,Bolivia,BO,BOL,Tarija
Cochabamba,Cochabamba,-17.41001097,-66.16997685,804138,Bolivia,BO,BOL,Cochabamba
Oruro,Oruro,-17.97995034,-67.12999577,227592.5,Bolivia,BO,BOL,Oruro
Camiri,Camiri,-20.05000486,-63.51998356,19212.5,Bolivia,BO,BOL,Santa Cruz
Cobija,Cobija,-11.03334593,-68.73330876,35511,Bolivia,BO,BOL,Pando
San Matias,San Matias,-16.35999754,-58.42001062,6352,Bolivia,BO,BOL,Santa Cruz
San Jos?,San Jose,-17.85003579,-60.77999577,9211,Bolivia,BO,BOL,Santa Cruz
Trinidad,Trinidad,-14.83337238,-64.89997685,69333.5,Bolivia,BO,BOL,El Beni
Tarija,Tarija,-21.51668537,-64.749986,155513,Bolivia,BO,BOL,Tarija
Sucre,Sucre,-19.04097085,-65.25951563,223287,Bolivia,BO,BOL,Chuquisaca
Riberalta,Riberalta,-10.98301308,-66.10000696,74014,Bolivia,BO,BOL,El Beni
La Paz,La Paz,-16.49797361,-68.14998519,1201399.5,Bolivia,BO,BOL,La Paz
Santa Cruz,Santa Cruz,-17.75391762,-63.22599634,1859530.5,Bolivia,BO,BOL,Santa Cruz
Zenica,Zenica,44.21997398,17.91998083,151388,Bosnia and Herzegovina,BA,BIH,Zenica-Doboj
Mostar,Mostar,43.35049217,17.82003861,133792.5,Bosnia and Herzegovina,BA,BIH,Herzegovina-Neretva
Tuzla,Tuzla,44.5504706,18.6800378,143410,Bosnia and Herzegovina,BA,BIH,Tuzla
Prijedor,Prijedor,44.98039268,16.70000362,70602.5,Bosnia and Herzegovina,BA,BIH,Serbian Republic
Banja Luka,Banja Luka,44.78040489,17.17997432,221422,Bosnia and Herzegovina,BA,BIH,Serbian Republic
Sarajevo,Sarajevo,43.8500224,18.38300167,662816.5,Bosnia and Herzegovina,BA,BIH,Sarajevo
Mochudi,Mochudi,-24.377004,26.15200256,39700,Botswana,BW,BWA,Kgatleng
Ghanzi,Ghanzi,-21.69961994,21.63996049,6306,Botswana,BW,BWA,Ghanzi
Lokhwabe,Lokhwabe,-24.16959837,21.83002641,1473,Botswana,BW,BWA,Kgalagadi
Lehututu,Lehututu,-23.96961058,21.87002397,1942,Botswana,BW,BWA,Kgalagadi
Tshabong,Tshabong,-26.00948606,22.40001745,9679,Botswana,BW,BWA,Kgalagadi
Tsau,Tsau,-20.15961058,22.45996212,1409,Botswana,BW,BWA,North-West
Nokaneng,Nokaneng,-19.66961465,22.26999955,1763,Botswana,BW,BWA,North-West
Mohembo,Mohembo,-18.29956907,21.8000024,757,Botswana,BW,BWA,North-West
Maun,Maun,-19.98959511,23.42000688,47059,Botswana,BW,BWA,North-West
Kasane,Kasane,-17.80957314,25.15003048,7774.5,Botswana,BW,BWA,North-West
Nata,Nata,-20.20947833,26.19001868,2492.5,Botswana,BW,BWA,Central
Mopipi,Mopipi,-21.17954832,24.88002112,3301,Botswana,BW,BWA,Central
Palapye,Palapye,-22.55961912,27.13001298,27179,Botswana,BW,BWA,Central
Lobatse,Lobatse,-25.2196118,25.68002397,50343.5,Botswana,BW,BWA,South-East
Kanye,Kanye,-24.96960122,25.33999304,45773.5,Botswana,BW,BWA,Southern
Molepolole,Molepolole,-24.3999719,25.5100085,57713,Botswana,BW,BWA,Kweneng
Francistown,Francistown,-21.17003986,27.50001623,89179.5,Botswana,BW,BWA,Central
Mahalapye,Mahalapye,-23.09999957,26.82000606,47607.5,Botswana,BW,BWA,Central
Serowe,Serowe,-22.39001707,26.71003861,47996,Botswana,BW,BWA,Central
Gaborone,Gaborone,-24.64631346,25.91194779,183827,Botswana,BW,BWA,South-East
Grajau,Grajau,-5.809995505,-46.14998438,30217,Brazil,BR,BRA,Maranh?o
Presidente Dutra,Presidente Dutra,-5.250029685,-44.51998051,30330,Brazil,BR,BRA,Maranh?o
Itapecuru Mirim,Itapecuru Mirim,-3.400013409,-44.36001611,22347,Brazil,BR,BRA,Maranh?o
Sao Jose de Ribamar,Sao Jose de Ribamar,-2.549987774,-44.06998214,41521,Brazil,BR,BRA,Maranh?o
Santa Ines,Santa Ines,-3.659997539,-45.39003076,58511.5,Brazil,BR,BRA,Maranh?o
Rosario,Rosario,-2.940041485,-44.26002222,6798,Brazil,BR,BRA,Maranh?o
Timon,Timon,-5.114999167,-42.84496647,203157,Brazil,BR,BRA,Maranh?o
Capanema,Capanema,-1.190019105,-47.17999903,45831,Brazil,BR,BRA,Par?
Portel,Portel,-1.949972718,-50.81998356,10855,Brazil,BR,BRA,Par?
Itupiranga,Itupiranga,-5.120011781,-49.30002466,21301,Brazil,BR,BRA,Par?
Pimenta Bueno,Pimenta Bueno,-11.64002724,-61.20999536,25762,Brazil,BR,BRA,Rond?nia
Ponta Pora,Ponta Pora,-22.53000853,-55.7299681,75047,Brazil,BR,BRA,Mato Grosso do Sul
Maracaju,Maracaju,-21.610013,-55.18002751,18156,Brazil,BR,BRA,Mato Grosso do Sul
Jardim,Jardim,-21.47994342,-56.15001998,21252.5,Brazil,BR,BRA,Mato Grosso do Sul
Tres Lagoas,Tres Lagoas,-20.79001137,-51.72000615,64217.5,Brazil,BR,BRA,Mato Grosso do Sul
Guanhaes,Guanhaes,-18.78000486,-42.95002466,16761.5,Brazil,BR,BRA,Minas Gerais
Leopoldina,Leopoldina,-21.53001788,-42.64004358,37412,Brazil,BR,BRA,Minas Gerais
Nova Lima,Nova Lima,-19.98003497,-43.8500214,60413.5,Brazil,BR,BRA,Minas Gerais
Pouso Alegre,Pouso Alegre,-22.22000161,-45.94002303,102517.5,Brazil,BR,BRA,Minas Gerais
Itauna,Itauna,-20.06003009,-44.57002914,70233,Brazil,BR,BRA,Minas Gerais
Caratinga,Caratinga,-19.79002073,-42.13999658,47517.5,Brazil,BR,BRA,Minas Gerais
Diamantina,Diamantina,-18.23998615,-43.60998438,25184.5,Brazil,BR,BRA,Minas Gerais
Nanuque,Nanuque,-17.83995888,-40.35002832,27210.5,Brazil,BR,BRA,Minas Gerais
Barbacena,Barbacena,-21.22001097,-43.77000045,101628.5,Brazil,BR,BRA,Minas Gerais
Pocos de Caldas,Pocos de Caldas,-21.78002846,-46.56998458,125498.5,Brazil,BR,BRA,Minas Gerais
Guaxupe,Guaxupe,-21.29003253,-46.7099502,43379.5,Brazil,BR,BRA,Minas Gerais
Sao Joao del Rei,Sao Joao del Rei,-21.1300423,-44.24999699,68731.5,Brazil,BR,BRA,Minas Gerais
Muriae,Muriae,-21.1300423,-42.38998132,76728.5,Brazil,BR,BRA,Minas Gerais
Passos,Passos,-20.71001626,-46.60998214,85136.5,Brazil,BR,BRA,Minas Gerais
Conselheiro Lafaiete,Conselheiro Lafaiete,-20.6700187,-43.78999923,102926,Brazil,BR,BRA,Minas Gerais
Formiga,Formiga,-20.46000568,-45.43002832,46076.5,Brazil,BR,BRA,Minas Gerais
Frutal,Frutal,-20.03000608,-48.94002079,26797,Brazil,BR,BRA,Minas Gerais
Iturama,Iturama,-19.72997272,-50.2000214,21048.5,Brazil,BR,BRA,Minas Gerais
Ituiutaba,Ituiutaba,-18.97001911,-49.45998906,63978,Brazil,BR,BRA,Minas Gerais
Araguari,Araguari,-18.64001341,-48.19998845,79910.5,Brazil,BR,BRA,Minas Gerais
Almenara,Almenara,-16.17003497,-40.70000696,22173.5,Brazil,BR,BRA,Minas Gerais
Varzea Grande,Varzea Grande,-15.65001504,-56.14002059,242088,Brazil,BR,BRA,Mato Grosso
C?ceres,Caceres,-16.0500423,-57.51001449,85274,Brazil,BR,BRA,Mato Grosso
Santana do Livramento,Santana do Livramento,-30.88004148,-55.53000615,87312,Brazil,BR,BRA,Rio Grande do Sul
Canoas,Canoas,-29.91999673,-51.17998743,466661,Brazil,BR,BRA,Rio Grande do Sul
Quarai,Quarai,-30.38002033,-56.45994938,18462,Brazil,BR,BRA,Rio Grande do Sul
Santa Vitoria do Palmar,Santa Vitoria do Palmar,-33.52003538,-53.36998295,21826,Brazil,BR,BRA,Rio Grande do Sul
Sao Lourenco do Sul,Sao Lourenco do Sul,-31.36998574,-51.98001611,21673,Brazil,BR,BRA,Rio Grande do Sul
Canela,Canela,-29.36003091,-50.81001001,47167,Brazil,BR,BRA,Rio Grande do Sul
Sao Gabriel,Sao Gabriel,-30.32002399,-54.32002832,41849.5,Brazil,BR,BRA,Rio Grande do Sul
Rosario do Sul,Rosario do Sul,-30.25000242,-54.92001754,28596.5,Brazil,BR,BRA,Rio Grande do Sul
Cachoeira do Sul,Cachoeira do Sul,-30.02996417,-52.90998519,61871,Brazil,BR,BRA,Rio Grande do Sul
Osorio,Osorio,-29.87999917,-50.26999129,30882,Brazil,BR,BRA,Rio Grande do Sul
Santa Cruz do Sul,Santa Cruz do Sul,-29.71003538,-52.44003972,109869,Brazil,BR,BRA,Rio Grande do Sul
Sao Luiz Gonzaga,Sao Luiz Gonzaga,-28.41001137,-54.95998926,27798.5,Brazil,BR,BRA,Rio Grande do Sul
Santo Angelo,Santo Angelo,-28.30004393,-54.28003076,65013,Brazil,BR,BRA,Rio Grande do Sul
Carazinho,Carazinho,-28.2900187,-52.80004358,49145,Brazil,BR,BRA,Rio Grande do Sul
Erechim,Erechim,-27.63000731,-52.26999841,85365.5,Brazil,BR,BRA,Rio Grande do Sul
Guaira,Guaira,-24.08996499,-54.2699797,28897.5,Brazil,BR,BRA,Paran?
Palmas,Palmas,-26.47999998,-51.99998906,29794.5,Brazil,BR,BRA,Paran?
Arapongas,Arapongas,-23.41000649,-51.43004968,91203.5,Brazil,BR,BRA,Paran?
Paranagua,Paranagua,-25.52787556,-48.53445345,135071,Brazil,BR,BRA,Paran?
Sao Jose dos Pinhais,Sao Jose dos Pinhais,-25.57002968,-49.18000615,472180,Brazil,BR,BRA,Paran?
Guarapuava,Guarapuava,-25.38001544,-51.48002079,123381.5,Brazil,BR,BRA,Paran?
Rio Negro,Rio Negro,-26.10002317,-49.79002059,44301.5,Brazil,BR,BRA,Paran?
Apucarana,Apucarana,-23.54999795,-51.4700214,102577,Brazil,BR,BRA,Paran?
Lapa,Lapa,-25.76004393,-49.72999841,19934.5,Brazil,BR,BRA,Paran?
Irati,Irati,-25.47003579,-50.65996749,41602,Brazil,BR,BRA,Paran?
Castro,Castro,-24.79002562,-50.00998132,38417.5,Brazil,BR,BRA,Paran?
Telemaco Borba,Telemaco Borba,-24.32995034,-50.61999577,53793.5,Brazil,BR,BRA,Paran?
Jacarezinho,Jacarezinho,-23.15994424,-49.97998316,33551,Brazil,BR,BRA,Paran?
Concordia,Concordia,-27.23003172,-52.03001306,46124.5,Brazil,BR,BRA,Santa Catarina
Blumenau,Blumenau,-26.9200248,-49.0899858,286326,Brazil,BR,BRA,Santa Catarina
Brusque,Brusque,-27.12998615,-48.9300214,81163.5,Brazil,BR,BRA,Santa Catarina
Ararangua,Ararangua,-28.94000486,-49.49998661,42198.5,Brazil,BR,BRA,Santa Catarina
Jaragua do Sul,Jaragua do Sul,-26.47999998,-49.09998519,128803.5,Brazil,BR,BRA,Santa Catarina
Tubarao,Tubarao,-28.48003294,-49.02001591,79760,Brazil,BR,BRA,Santa Catarina
Laguna,Laguna,-28.48003294,-48.77997888,32532,Brazil,BR,BRA,Santa Catarina
Joacaba,Joacaba,-27.17003538,-51.4999679,31196,Brazil,BR,BRA,Santa Catarina
Cacador,Cacador,-26.77000812,-51.02002303,57155.5,Brazil,BR,BRA,Santa Catarina
Canoinhas,Canoinhas,-26.17996662,-50.4000092,40180,Brazil,BR,BRA,Santa Catarina
Camocim,Camocim,-2.89999225,-40.85002364,27794.5,Brazil,BR,BRA,Cear?
Russas,Russas,-4.940022767,-37.97999211,33613.5,Brazil,BR,BRA,Cear?
Sobral,Sobral,-3.690021547,-40.35002832,148439.5,Brazil,BR,BRA,Cear?
Iguatu,Iguatu,-6.359987774,-39.29998906,56638,Brazil,BR,BRA,Cear?
Quixada,Quixada,-4.969995098,-39.02000615,30723.5,Brazil,BR,BRA,Cear?
Caninde,Caninde,-4.35003294,-39.30998845,32085,Brazil,BR,BRA,Cear?
Campo Maior,Campo Maior,-4.820030091,-42.18001998,24089.5,Brazil,BR,BRA,Piau?
Barras,Barras,-4.250039043,-42.29998682,11951.5,Brazil,BR,BRA,Piau?
Rio Largo,Rio Largo,-9.48000405,-35.83996769,110966,Brazil,BR,BRA,Alagoas
Palmeira dos Indios,Palmeira dos Indios,-9.416597067,-36.61663863,41095,Brazil,BR,BRA,Alagoas
Santa Cruz Cabralia,Santa Cruz Cabralia,-16.28000242,-39.0299797,9980.5,Brazil,BR,BRA,Bahia
Paulo Afonso,Paulo Afonso,-9.330659161,-38.26565943,85350,Brazil,BR,BRA,Bahia
Brumado,Brumado,-14.20999957,-41.67002527,29300,Brazil,BR,BRA,Bahia
Jaguaquara,Jaguaquara,-13.5299894,-39.96999984,30554.5,Brazil,BR,BRA,Bahia
Itapetinga,Itapetinga,-15.24998777,-40.24998275,43224,Brazil,BR,BRA,Bahia
Ubaitaba,Ubaitaba,-14.30001992,-39.33001306,27411.5,Brazil,BR,BRA,Bahia
Cachoeiro de Itapemirim,Cachoeiro de Itapemirim,-20.85000771,-41.12998071,174808.5,Brazil,BR,BRA,Esp?rito Santo
Barra Mansa,Barra Mansa,-22.56003253,-44.1699502,166719,Brazil,BR,BRA,Rio de Janeiro
Nova Iguacu,Nova Iguacu,-22.74002155,-43.46996708,844583,Brazil,BR,BRA,Rio de Janeiro
Duque de Caxias,Duque de Caxias,-22.76999388,-43.30997685,842890,Brazil,BR,BRA,Rio de Janeiro
Niteroi,Niteroi,-22.90001178,-43.09998967,993920,Brazil,BR,BRA,Rio de Janeiro
Cabo Frio,Cabo Frio,-22.88998655,-42.03997685,184980,Brazil,BR,BRA,Rio de Janeiro
Macae,Macae,-22.37999184,-41.78999211,133083,Brazil,BR,BRA,Rio de Janeiro
Miracema,Miracema,-21.41002521,-42.19996708,22564.5,Brazil,BR,BRA,Rio de Janeiro
Apodi,Apodi,-5.650005271,-37.80000309,8586,Brazil,BR,BRA,Rio Grande do Norte
Santa Cruz,Santa Cruz,-6.219996319,-36.02998194,22003.5,Brazil,BR,BRA,Rio Grande do Norte
Morrinhos,Morrinhos,-17.73004311,-49.10998458,27841,Brazil,BR,BRA,Goi?s
Ceres,Ceres,-15.30331785,-49.60519983,18658.5,Brazil,BR,BRA,Goi?s
Catalao,Catalao,-18.18004148,-47.9500037,53646.5,Brazil,BR,BRA,Goi?s
Cristalina,Cristalina,-16.76999835,-47.61002446,25627.5,Brazil,BR,BRA,Goi?s
Trindade,Trindade,-16.65000568,-49.49998661,93113,Brazil,BR,BRA,Goi?s
Ipora,Ipora,-16.45001788,-51.12999048,23354,Brazil,BR,BRA,Goi?s
Inhumas,Inhumas,-16.35999754,-49.49998661,36122,Brazil,BR,BRA,Goi?s
Itaberai,Itaberai,-16.01996662,-49.80996769,18710.5,Brazil,BR,BRA,Goi?s
Santo Andre,Santo Andre,-23.65283405,-46.52781661,662373,Brazil,BR,BRA,S?o Paulo
Pindamonhangaba,Pindamonhangaba,-22.91995888,-45.47002588,123985,Brazil,BR,BRA,S?o Paulo
Rio Claro,Rio Claro,-22.40996417,-47.56002751,177710,Brazil,BR,BRA,S?o Paulo
Ourinhos,Ourinhos,-22.97003335,-49.86998987,96994,Brazil,BR,BRA,S?o Paulo
Itanhaem,Itanhaem,-24.17998533,-46.80002222,82722,Brazil,BR,BRA,S?o Paulo
Jaboticabal,Jaboticabal,-21.25003497,-48.32998051,60780.5,Brazil,BR,BRA,S?o Paulo
Braganca Paulista,Braganca Paulista,-22.95003457,-46.5499858,126386,Brazil,BR,BRA,S?o Paulo
Jundiai,Jundiai,-23.19999347,-46.8799915,413568.5,Brazil,BR,BRA,S?o Paulo
Sao Jose dos Campos,Sao Jose dos Campos,-23.19999347,-45.87994918,695322.5,Brazil,BR,BRA,S?o Paulo
Guaratingueta,Guaratingueta,-22.81996499,-45.18999129,154730,Brazil,BR,BRA,S?o Paulo
Pirassununga,Pirassununga,-21.99004148,-47.42998377,51698,Brazil,BR,BRA,S?o Paulo
Americana,Americana,-22.74994342,-47.32998987,337747,Brazil,BR,BRA,S?o Paulo
Piracicaba,Piracicaba,-22.70999754,-47.63999679,329530,Brazil,BR,BRA,S?o Paulo
Sao Joao da Boa Vista,Sao Joao da Boa Vista,-21.98001626,-46.78999699,68666,Brazil,BR,BRA,S?o Paulo
Sao Carlos,Sao Carlos,-22.02001382,-47.88998153,175219,Brazil,BR,BRA,S?o Paulo
Tupa,Tupa,-21.92999347,-50.5199502,51798.5,Brazil,BR,BRA,S?o Paulo
Penapolis,Penapolis,-21.41002521,-50.08000289,44795,Brazil,BR,BRA,S?o Paulo
Presidente Prudente,Presidente Prudente,-22.12000771,-51.39000045,199722,Brazil,BR,BRA,S?o Paulo
Registro,Registro,-24.49004393,-47.83998458,49485,Brazil,BR,BRA,S?o Paulo
Tatui,Tatui,-23.35001015,-47.8600092,81936,Brazil,BR,BRA,S?o Paulo
Avare,Avare,-23.1100248,-48.9300214,70709,Brazil,BR,BRA,S?o Paulo
Garca,Garca,-22.22000161,-49.65997685,38460,Brazil,BR,BRA,S?o Paulo
Catanduva,Catanduva,-21.14001585,-48.97996668,105238,Brazil,BR,BRA,S?o Paulo
Batatais,Batatais,-20.89000527,-47.58999984,44061,Brazil,BR,BRA,S?o Paulo
Barretos,Barretos,-20.55002602,-48.58001693,97562,Brazil,BR,BRA,S?o Paulo
Marilia,Marilia,-22.21002806,-49.95001083,191083.5,Brazil,BR,BRA,S?o Paulo
Itu,Itu,-23.26004148,-47.30001754,228878,Brazil,BR,BRA,S?o Paulo
Itapetininga,Itapetininga,-23.58999551,-48.03999821,120889,Brazil,BR,BRA,S?o Paulo
Jaboatao,Jaboatao,-8.110010153,-35.02004358,681214,Brazil,BR,BRA,Pernambuco
Olinda,Olinda,-7.999991029,-34.8499506,659554,Brazil,BR,BRA,Pernambuco
Cabo de Santo Agostinho,Cabo de Santo Agostinho,-8.289999167,-35.02999129,144662,Brazil,BR,BRA,Pernambuco
Carpina,Carpina,-7.840000795,-35.26000309,118134,Brazil,BR,BRA,Pernambuco
Arcoverde,Arcoverde,-8.420017071,-37.06999597,53066,Brazil,BR,BRA,Pernambuco
Manacapuru,Manacapuru,-3.289580873,-60.6199797,55780.5,Brazil,BR,BRA,Amazonas
Maues,Maues,-3.389626446,-57.72002751,27518,Brazil,BR,BRA,Amazonas
Pedreiras,Pedreiras,-4.569606101,-44.67002303,13638,Brazil,BR,BRA,Maranh?o
Codo,Codo,-4.479585756,-43.8799679,83288,Brazil,BR,BRA,Maranh?o
Coroata,Coroata,-4.12958128,-44.15000309,34129,Brazil,BR,BRA,Maranh?o
Chapadinha,Chapadinha,-3.739527569,-43.35999964,29807.5,Brazil,BR,BRA,Maranh?o
Pinheiro,Pinheiro,-2.519602032,-45.0899974,24912,Brazil,BR,BRA,Maranh?o
Barra do Corda,Barra do Corda,-5.509600404,-45.25996118,48901,Brazil,BR,BRA,Maranh?o
Viana,Viana,-3.209585756,-45.00000289,15808.5,Brazil,BR,BRA,Maranh?o
Colinas,Colinas,-6.039542217,-44.2399976,13562.5,Brazil,BR,BRA,Maranh?o
Viseu,Viseu,-1.196478659,-46.14001083,9992.5,Brazil,BR,BRA,Par?
Capitao Poco,Capitao Poco,-1.74962319,-47.09000452,32704,Brazil,BR,BRA,Par?
Castanhal,Castanhal,-1.28959959,-47.93003076,125314.5,Brazil,BR,BRA,Par?
Salinopolis,Salinopolis,-0.609486065,-47.33998926,32384.5,Brazil,BR,BRA,Par?
Alenquer,Alenquer,-1.939585756,-54.78999964,26290,Brazil,BR,BRA,Par?
Oriximina,Oriximina,-1.759596742,-55.86998539,35300,Brazil,BR,BRA,Par?
Xinguara,Xinguara,-7.100614401,-49.94804712,4047,Brazil,BR,BRA,Par?
Jacund?,Jacunda,-4.599578431,-49.38996749,51375,Brazil,BR,BRA,Par?
Uruara,Uruara,-3.82959959,-54.02999435,10,Brazil,BR,BRA,Par?
Altamira,Altamira,-3.199612204,-52.21000208,56769,Brazil,BR,BRA,Par?
Paragominas,Paragominas,-2.959575176,-47.49000594,38095.5,Brazil,BR,BRA,Par?
Cameta,Cameta,-2.239619121,-49.509986,22705,Brazil,BR,BRA,Par?
Rolim de Moura,Rolim de Moura,-11.73020262,-61.78063237,24516,Brazil,BR,BRA,Rond?nia
Ariquemes,Ariquemes,-9.939614239,-63.07998458,58096,Brazil,BR,BRA,Rond?nia
Abuna,Abuna,-9.69539142,-65.35971623,1929,Brazil,BR,BRA,Rond?nia
Tocantinopolis,Tocantinopolis,-6.319576804,-47.41998438,8750,Brazil,BR,BRA,Tocantins
Gurupi,Gurupi,-11.71960895,-49.05998763,45595.5,Brazil,BR,BRA,Tocantins
Aquidauana,Aquidauana,-20.46961749,-55.79001611,38053,Brazil,BR,BRA,Mato Grosso do Sul
Paranaiba,Paranaiba,-19.6795882,-51.20001205,25278.5,Brazil,BR,BRA,Mato Grosso do Sul
Sete Lagoas,Sete Lagoas,-19.44962807,-44.24999699,195032,Brazil,BR,BRA,Minas Gerais
Divinopolis,Divinopolis,-20.14953367,-44.89998316,181457,Brazil,BR,BRA,Minas Gerais
Ipatinga,Ipatinga,-19.4796004,-42.51999923,318320,Brazil,BR,BRA,Minas Gerais
Araxa,Araxa,-19.5795943,-46.95001306,70159.5,Brazil,BR,BRA,Minas Gerais
Lavras,Lavras,-21.24956989,-45.0099506,70436,Brazil,BR,BRA,Minas Gerais
Uba,Uba,-21.11960366,-42.95002466,81698.5,Brazil,BR,BRA,Minas Gerais
Campo Belo,Campo Belo,-20.88959186,-45.2799858,42042.5,Brazil,BR,BRA,Minas Gerais
Ponte Nova,Ponte Nova,-20.40962116,-42.8999502,40377,Brazil,BR,BRA,Minas Gerais
Curvelo,Curvelo,-18.75959267,-44.429986,45937,Brazil,BR,BRA,Minas Gerais
Paracatu,Paracatu,-17.19958453,-46.86999211,51673.5,Brazil,BR,BRA,Minas Gerais
Bocaiuva,Bocaiuva,-17.10961587,-43.81004968,22528.5,Brazil,BR,BRA,Minas Gerais
Aracuai,Aracuai,-16.85960529,-42.06994918,15301.5,Brazil,BR,BRA,Minas Gerais
Janauba,Janauba,-15.79961831,-43.30997685,38641,Brazil,BR,BRA,Minas Gerais
Juina,Juina,-11.3995768,-59.50002222,980,Brazil,BR,BRA,Mato Grosso
Barra do Garcas,Barra do Garcas,-15.87961342,-52.25999903,41214.5,Brazil,BR,BRA,Mato Grosso
Pontes e Lacerda,Pontes e Lacerda,-15.21960203,-59.3499797,22694.5,Brazil,BR,BRA,Mato Grosso
Barra do Bugres,Barra do Bugres,-15.06958535,-57.19000818,22386,Brazil,BR,BRA,Mato Grosso
Rondonopolis,Rondonopolis,-16.4694999,-54.63998295,146794,Brazil,BR,BRA,Mato Grosso
Uruguaiana,Uruguaiana,-29.76961831,-57.08998845,97736.5,Brazil,BR,BRA,Rio Grande do Sul
Sao Borja,Sao Borja,-28.65960854,-56.00997685,48450.5,Brazil,BR,BRA,Rio Grande do Sul
Novo Hamburgo,Novo Hamburgo,-29.70962197,-51.13998987,557017,Brazil,BR,BRA,Rio Grande do Sul
Rio Grande,Rio Grande,-32.04947915,-52.12000757,143150,Brazil,BR,BRA,Rio Grande do Sul
Camaqua,Camaqua,-30.83963051,-51.81000065,45112.5,Brazil,BR,BRA,Rio Grande do Sul
Bento Goncalves,Bento Goncalves,-29.1694999,-51.51996668,92561.5,Brazil,BR,BRA,Rio Grande do Sul
Vacaria,Vacaria,-28.49961831,-50.94000208,47275.5,Brazil,BR,BRA,Rio Grande do Sul
Ijui,Ijui,-28.38954751,-53.91994938,59047,Brazil,BR,BRA,Rio Grande do Sul
Santa Rosa,Santa Rosa,-27.86952757,-54.4599681,59119,Brazil,BR,BRA,Rio Grande do Sul
Maringa,Maringa,-23.4095414,-51.92996749,320029.5,Brazil,BR,BRA,Paran?
Cascavel,Cascavel,-24.95957599,-53.46002914,229300,Brazil,BR,BRA,Paran?
Campo Murao,Campo Murao,-24.04960569,-52.41998926,74173,Brazil,BR,BRA,Paran?
Foz do Iguacu,Foz do Iguacu,-25.52346922,-54.52998967,366989,Brazil,BR,BRA,Paran?
Sao Francisco do Sul,Sao Francisco do Sul,-26.23960122,-48.59998987,24354.5,Brazil,BR,BRA,Santa Catarina
Porto Uniao,Porto Uniao,-26.23960122,-51.07996769,50242.5,Brazil,BR,BRA,Santa Catarina
Itajai,Itajai,-26.89961261,-48.68001083,241421,Brazil,BR,BRA,Santa Catarina
Imbituba,Imbituba,-28.22960895,-48.66001205,28380,Brazil,BR,BRA,Santa Catarina
Lajes,Lajes,-27.80958291,-50.30998885,139972,Brazil,BR,BRA,Santa Catarina
Granja,Granja,-3.119513734,-40.83999841,17233,Brazil,BR,BRA,Cear?
Crato,Crato,-7.229598776,-39.42000757,164149.5,Brazil,BR,BRA,Cear?
Itapipoca,Itapipoca,-3.499542217,-39.58002364,31041,Brazil,BR,BRA,Cear?
Paracuru,Paracuru,-3.399548321,-39.04003076,19860,Brazil,BR,BRA,Cear?
Acarau,Acarau,-2.889605287,-40.11999068,21024.5,Brazil,BR,BRA,Cear?
Taua,Taua,-5.999492982,-40.31003076,29188,Brazil,BR,BRA,Cear?
Crateus,Crateus,-5.165590394,-40.66600387,40338,Brazil,BR,BRA,Cear?
Baturite,Baturite,-4.329569073,-38.87998885,17797.5,Brazil,BR,BRA,Cear?
Ipu,Ipu,-4.319595521,-40.72005742,14479.5,Brazil,BR,BRA,Cear?
Floriano,Floriano,-6.769575176,-43.0299681,35923,Brazil,BR,BRA,Piau?
Piripiri,Piripiri,-4.269572735,-41.78999211,32639,Brazil,BR,BRA,Piau?
Penedo,Penedo,-10.26961994,-36.58002588,37515.5,Brazil,BR,BRA,Alagoas
Itabuna,Itabuna,-14.78960244,-39.28001611,213799,Brazil,BR,BRA,Bahia
Itamaraju,Itamaraju,-17.0395943,-39.52994918,35055,Brazil,BR,BRA,Bahia
Guanambi,Guanambi,-14.22958494,-42.78998275,45730,Brazil,BR,BRA,Bahia
Porto Seguro,Porto Seguro,-16.42960569,-39.08002832,72031,Brazil,BR,BRA,Bahia
Valenca,Valenca,-13.3596122,-39.08002832,56584.5,Brazil,BR,BRA,Bahia
Serrinha,Serrinha,-11.64958738,-39.01000676,52953.5,Brazil,BR,BRA,Bahia
Tucano,Tucano,-10.96962889,-38.78999435,16199,Brazil,BR,BRA,Bahia
Senhor do Bonfim,Senhor do Bonfim,-10.44960895,-40.19001225,43577,Brazil,BR,BRA,Bahia
Remanso,Remanso,-9.599583314,-42.10999841,37945,Brazil,BR,BRA,Bahia
Itambe,Itambe,-15.23960081,-40.62998539,15450.5,Brazil,BR,BRA,Bahia
Bom Jesus da Lapa,Bom Jesus da Lapa,-13.2495414,-43.44002059,40691,Brazil,BR,BRA,Bahia
Itaberaba,Itaberaba,-12.5196118,-40.2999797,31722,Brazil,BR,BRA,Bahia
Sao Mateus,Sao Mateus,-18.72962034,-39.85998071,63375.5,Brazil,BR,BRA,Esp?rito Santo
Patos,Patos,-7.019585756,-37.29000838,85720.5,Brazil,BR,BRA,Para?ba
Volta Redonda,Volta Redonda,-22.51956989,-44.09496769,352971,Brazil,BR,BRA,Rio de Janeiro
Petropolis,Petropolis,-22.50949298,-43.19998356,279381,Brazil,BR,BRA,Rio de Janeiro
Nova Cruz,Nova Cruz,-6.469593487,-35.43999211,22563.5,Brazil,BR,BRA,Rio Grande do Norte
Caico,Caico,-6.459619935,-37.10001998,42378,Brazil,BR,BRA,Rio Grande do Norte
Acu,Acu,-5.57962197,-36.91005742,33303,Brazil,BR,BRA,Rio Grande do Norte
Estancia,Estancia,-11.26961058,-37.45002446,50690,Brazil,BR,BRA,Sergipe
Caracarai,Caracarai,1.816231505,-61.12767481,11368,Brazil,BR,BRA,Roraima
Porto Santana,Porto Santana,-0.039598369,-51.17998743,68849,Brazil,BR,BRA,Amap?
Rio Verde,Rio Verde,-17.81959837,-50.92997685,48318,Brazil,BR,BRA,Goi?s
Pires do Rio,Pires do Rio,-17.29952675,-48.27998356,21688,Brazil,BR,BRA,Goi?s
Anapolis,Anapolis,-16.31958657,-48.9599679,278595.5,Brazil,BR,BRA,Goi?s
Goianesia,Goianesia,-15.30962238,-49.1300092,39217.5,Brazil,BR,BRA,Goi?s
Niquelandia,Niquelandia,-14.46962197,-48.47002364,19785,Brazil,BR,BRA,Goi?s
Itumbiara,Itumbiara,-18.39961465,-49.21000431,65343.5,Brazil,BR,BRA,Goi?s
Jatai,Jatai,-17.87959471,-51.75000431,57135,Brazil,BR,BRA,Goi?s
Mineiros,Mineiros,-17.56953611,-52.55998071,28247,Brazil,BR,BRA,Goi?s
Formosa,Formosa,-15.53947915,-47.33998926,62585.5,Brazil,BR,BRA,Goi?s
Sao Jose do Rio Preto,Sao Jose do Rio Preto,-20.79962319,-49.38996749,358243.5,Brazil,BR,BRA,S?o Paulo
Limeira,Limeira,-22.54954222,-47.40001144,241071,Brazil,BR,BRA,S?o Paulo
Taubate,Taubate,-23.01953937,-45.55999455,327600.5,Brazil,BR,BRA,S?o Paulo
Jau,Jau,-22.28960976,-48.57001754,102565.5,Brazil,BR,BRA,S?o Paulo
Assis,Assis,-22.65961302,-50.41998214,79133,Brazil,BR,BRA,S?o Paulo
Itapeva,Itapeva,-23.97958413,-48.88002446,55324,Brazil,BR,BRA,S?o Paulo
Botucatu,Botucatu,-22.87959959,-48.44999903,94938.5,Brazil,BR,BRA,S?o Paulo
Novo Horizonte,Novo Horizonte,-21.45958291,-49.2200037,29554,Brazil,BR,BRA,S?o Paulo
Andradina,Andradina,-20.90959064,-51.37994938,45715,Brazil,BR,BRA,S?o Paulo
Fernandopolis,Fernandopolis,-20.2696297,-50.26004358,55587,Brazil,BR,BRA,S?o Paulo
Barreiros,Barreiros,-8.829604473,-35.20000676,35472.5,Brazil,BR,BRA,Pernambuco
Salgueiro,Salgueiro,-8.059625632,-39.13002527,31565,Brazil,BR,BRA,Pernambuco
Goiana,Goiana,-7.559604473,-34.99999312,57764.5,Brazil,BR,BRA,Pernambuco
Timbauba,Timbauba,-7.499608135,-35.32002527,51327.5,Brazil,BR,BRA,Pernambuco
Bacabal,Bacabal,-4.229988588,-44.79998926,57296.5,Brazil,BR,BRA,Maranh?o
Braganca,Braganca,-1.05002765,-46.76999821,56864.5,Brazil,BR,BRA,Par?
Obidos,Obidos,-1.910026836,-55.52000676,26278.5,Brazil,BR,BRA,Par?
Guajara-Miram,Guajara-Miram,-10.80002684,-65.34994938,51852.5,Brazil,BR,BRA,Rond?nia
Porto Nacional,Porto Nacional,-10.70003294,-48.41994918,9129,Brazil,BR,BRA,Tocantins
Dourados,Dourados,-22.23002684,-54.80999841,144743.5,Brazil,BR,BRA,Mato Grosso do Sul
Governador Valadares,Governador Valadares,-18.87002521,-41.97000696,201317,Brazil,BR,BRA,Minas Gerais
Pirapora,Pirapora,-17.33001585,-44.92998132,55910,Brazil,BR,BRA,Minas Gerais
Juiz de Fora,Juiz de Fora,-21.77000324,-43.3749858,464764.5,Brazil,BR,BRA,Minas Gerais
Santa Maria,Santa Maria,-29.68331867,-53.80000838,239211.5,Brazil,BR,BRA,Rio Grande do Sul
Passo Fundo,Passo Fundo,-28.25002114,-52.41998926,164047,Brazil,BR,BRA,Rio Grande do Sul
Xapeco,Xapeco,-27.10001382,-52.64002751,154794,Brazil,BR,BRA,Santa Catarina
Joinville,Joinville,-26.31995807,-48.83994938,710737.5,Brazil,BR,BRA,Santa Catarina
Juazeiro do Norte,Juazeiro do Norte,-7.210013409,-39.32001367,222861,Brazil,BR,BRA,Cear?
Nova Vicosa,Nova Vicosa,-17.88000812,-39.37001062,30250,Brazil,BR,BRA,Bahia
Alagoinhas,Alagoinhas,-12.13999673,-38.42999048,123379,Brazil,BR,BRA,Bahia
Juazeiro,Juazeiro,-9.420007712,-40.49996749,95132,Brazil,BR,BRA,Bahia
Vit?ria,Vitoria,-20.32399331,-40.36599634,1008328,Brazil,BR,BRA,Esp?rito Santo
Joao Pessoa,Joao Pessoa,-7.10113513,-34.87607117,803441.5,Brazil,BR,BRA,Para?ba
Campina Grande,Campina Grande,-7.230012188,-35.88001693,383098.5,Brazil,BR,BRA,Para?ba
Nova Friburgo,Nova Friburgo,-22.25999917,-42.54004968,162676,Brazil,BR,BRA,Rio de Janeiro
Aracatuba,Aracatuba,-21.20998574,-50.45000615,166305,Brazil,BR,BRA,S?o Paulo
Sena Madureira,Sena Madureira,-9.070003236,-68.66997929,23354,Brazil,BR,BRA,Acre
Fonte Boa,Fonte Boa,-2.513814271,-66.09160954,13974.5,Brazil,BR,BRA,Amazonas
Eirunepe,Eirunepe,-6.66002114,-69.87380762,19462.5,Brazil,BR,BRA,Amazonas
Manicore,Manicore,-5.812165915,-61.29748356,17802,Brazil,BR,BRA,Amazonas
Barcelos,Barcelos,-0.97499347,-62.92389592,9968.5,Brazil,BR,BRA,Amazonas
Tonantins,Tonantins,-2.872707093,-67.80189274,2722,Brazil,BR,BRA,Amazonas
Tefe,Tefe,-3.36001585,-64.69998906,48189.5,Brazil,BR,BRA,Amazonas
Coari,Coari,-4.079971905,-63.12998153,51897.5,Brazil,BR,BRA,Amazonas
Sao Cabriel da Cachoeira,Sao Cabriel da Cachoeira,-0.133236065,-67.08330611,15231,Brazil,BR,BRA,Amazonas
Novo Airao,Novo Airao,-2.620784486,-60.94378422,9049,Brazil,BR,BRA,Amazonas
Itacoatiara,Itacoatiara,-3.140029278,-58.43998356,51509,Brazil,BR,BRA,Amazonas
Parintins,Parintins,-2.610035788,-56.74000981,64428,Brazil,BR,BRA,Amazonas
Natal,Natal,-6.983825664,-60.26994938,980588,Brazil,BR,BRA,Amazonas
Crato,Crato,-7.46389972,-63.03996118,164149.5,Brazil,BR,BRA,Amazonas
Imperatriz,Imperatriz,-5.520039043,-47.49000594,203339.5,Brazil,BR,BRA,Maranh?o
Balsas,Balsas,-7.520020326,-46.04999048,39761.5,Brazil,BR,BRA,Maranh?o
Breves,Breves,-1.680015036,-50.4900037,46818.5,Brazil,BR,BRA,Par?
Jacareacanga,Jacareacanga,-6.266608461,-57.65000594,31661,Brazil,BR,BRA,Par?
Tucurui,Tucurui,-3.679996319,-49.71999903,38472,Brazil,BR,BRA,Par?
Itaituba,Itaituba,-4.258617331,-55.92502079,78532,Brazil,BR,BRA,Par?
Conceicao do Araguaia,Conceicao do Araguaia,-8.250001608,-49.29002527,27115,Brazil,BR,BRA,Par?
Abaetetuba,Abaetetuba,-1.724530694,-48.88488014,78735,Brazil,BR,BRA,Par?
Principe da Beira,Principe da Beira,-12.41667234,-64.41664718,956,Brazil,BR,BRA,Rond?nia
Araguaina,Araguaina,-7.190014629,-48.21001367,50444,Brazil,BR,BRA,Tocantins
Palmas,Palmas,-10.23773558,-48.2877867,215793.5,Brazil,BR,BRA,Tocantins
Teofilo Otoni,Teofilo Otoni,-17.87003457,-41.50000981,86865,Brazil,BR,BRA,Minas Gerais
Uberaba,Uberaba,-19.7799955,-47.9500037,234807,Brazil,BR,BRA,Minas Gerais
Januaria,Januaria,-15.47999957,-44.36998967,25753,Brazil,BR,BRA,Minas Gerais
Mato Grosso,Mato Grosso,-15.00002887,-59.95002059,1612,Brazil,BR,BRA,Mato Grosso
Aripuana,Aripuana,-9.169997133,-60.64000431,26983,Brazil,BR,BRA,Mato Grosso
Sinop,Sinop,-11.84998859,-55.45998458,8961,Brazil,BR,BRA,Mato Grosso
Jaguarao,Jaguarao,-32.5600423,-53.36998295,26020,Brazil,BR,BRA,Rio Grande do Sul
Bage,Bage,-31.32001463,-54.10001591,102519,Brazil,BR,BRA,Rio Grande do Sul
Londrina,Londrina,-23.30003904,-51.17998743,496035,Brazil,BR,BRA,Paran?
Criciuma,Criciuma,-28.68002073,-49.38996749,183085.5,Brazil,BR,BRA,Santa Catarina
Aracati,Aracati,-4.559994284,-37.77003076,28126.5,Brazil,BR,BRA,Cear?
Ico,Ico,-6.400037009,-38.84999068,15820,Brazil,BR,BRA,Cear?
Parnaiba,Parnaiba,-2.910017478,-41.76996749,125699,Brazil,BR,BRA,Piau?
Picos,Picos,-7.079995505,-41.43998763,47694.5,Brazil,BR,BRA,Piau?
Arapiraca,Arapiraca,-9.750013409,-36.66999455,177115,Brazil,BR,BRA,Alagoas
Jequie,Jequie,-13.85002155,-40.07999312,131524.5,Brazil,BR,BRA,Bahia
Ilheus,Ilheus,-14.7800423,-39.05000431,193060.5,Brazil,BR,BRA,Bahia
Canavieiras,Canavieiras,-15.64004148,-38.96000981,26375,Brazil,BR,BRA,Bahia
Santa Maria da Vitoria,Santa Maria da Vitoria,-13.38999795,-44.21002527,13176,Brazil,BR,BRA,Bahia
Irece,Irece,-11.29999632,-41.87001306,48079.5,Brazil,BR,BRA,Bahia
Xique-Xique,Xique-Xique,-10.82002562,-42.73001225,18633,Brazil,BR,BRA,Bahia
Linhares,Linhares,-19.38999347,-40.05002079,86413,Brazil,BR,BRA,Esp?rito Santo
Campos,Campos,-21.74995278,-41.32002079,378943,Brazil,BR,BRA,Rio de Janeiro
Mossoro,Mossoro,-5.190033347,-37.34000533,202294,Brazil,BR,BRA,Rio Grande do Norte
Aracaju,Aracaju,-10.90002073,-37.11996708,587765.5,Brazil,BR,BRA,Sergipe
Laranjal do Jari,Laranjal do Jari,-0.850039857,-52.48001144,43344,Brazil,BR,BRA,Amap?
Amapa,Amapa,2.049989847,-50.80001062,1947,Brazil,BR,BRA,Amap?
Vila Velha,Vila Velha,3.21666282,-51.21665186,742413.5,Brazil,BR,BRA,Amap?
Santos,Santos,-23.95372393,-46.33294266,1060201.5,Brazil,BR,BRA,S?o Paulo
Bauru,Bauru,-22.33002073,-49.08001225,307929.5,Brazil,BR,BRA,S?o Paulo
Iguape,Iguape,-24.72000405,-47.56994938,23602.5,Brazil,BR,BRA,S?o Paulo
Franca,Franca,-20.53002724,-47.39001205,281149.5,Brazil,BR,BRA,S?o Paulo
Garanhuns,Garanhuns,-8.890014222,-36.50003076,107115,Brazil,BR,BRA,Pernambuco
Caruaru,Caruaru,-8.280025616,-35.98001083,238732.5,Brazil,BR,BRA,Pernambuco
Rio Branco,Rio Branco,-9.966589336,-67.80000655,257642,Brazil,BR,BRA,Acre
S?o Lu?s,Sao Luis,-2.515984681,-44.26599085,524692.5,Brazil,BR,BRA,Maranh?o
Porto Velho,Porto Velho,-8.750022767,-63.90001205,289534.5,Brazil,BR,BRA,Rond?nia
Alvorada,Alvorada,-12.47000242,-49.08200179,9273,Brazil,BR,BRA,Tocantins
Corumba,Corumba,-19.01601113,-57.65000594,70035.5,Brazil,BR,BRA,Mato Grosso do Sul
Belo Horizonte,Belo Horizonte,-19.91502602,-43.91500452,3974112,Brazil,BR,BRA,Minas Gerais
Montes Claros,Montes Claros,-16.72002724,-43.86002079,300022,Brazil,BR,BRA,Minas Gerais
Uberlandia,Uberlandia,-18.89999754,-48.27998356,484862,Brazil,BR,BRA,Minas Gerais
Colider,Colider,-10.81728676,-55.45057947,27139,Brazil,BR,BRA,Mato Grosso
Alta Floresta,Alta Floresta,-9.900030091,-55.90998295,40466,Brazil,BR,BRA,Mato Grosso
Cuiaba,Cuiaba,-15.56960651,-56.08498519,603143.5,Brazil,BR,BRA,Mato Grosso
Pelotas,Pelotas,-31.75001422,-52.33002059,299270,Brazil,BR,BRA,Rio Grande do Sul
Caxias do Sul,Caxias do Sul,-29.17999022,-51.17003972,377580.5,Brazil,BR,BRA,Rio Grande do Sul
Ponta Grossa,Ponta Grossa,-25.09000731,-50.16004968,271321.5,Brazil,BR,BRA,Paran?
Teresina,Teresina,-5.095000388,-42.7800092,746860.5,Brazil,BR,BRA,Piau?
Maceio,Maceio,-9.619995505,-35.72997441,1000215.5,Brazil,BR,BRA,Alagoas
Vitoria da Conquista,Vitoria da Conquista,-14.85001219,-40.83999841,272320.5,Brazil,BR,BRA,Bahia
Barreiras,Barreiras,-12.13999673,-45.00000289,86245.5,Brazil,BR,BRA,Bahia
Vila Velha,Vila Velha,-20.36760822,-40.31798893,742413.5,Brazil,BR,BRA,Esp?rito Santo
Natal,Natal,-5.780023174,-35.24000431,925521.5,Brazil,BR,BRA,Rio Grande do Norte
Campinas,Campinas,-22.90001178,-47.10002975,1911277,Brazil,BR,BRA,S?o Paulo
Sorocaba,Sorocaba,-23.49000161,-47.46998132,561071.5,Brazil,BR,BRA,S?o Paulo
Ribeirao Preto,Ribeirao Preto,-21.17003986,-47.82998519,520774,Brazil,BR,BRA,S?o Paulo
Petrolina,Petrolina,-9.380010153,-40.50996688,227817.5,Brazil,BR,BRA,Pernambuco
Cruzeiro do Sul,Cruzeiro do Sul,-7.629987774,-72.66996769,56862,Brazil,BR,BRA,Acre
Manaus,Manaus,-3.100031719,-60.00001754,1636622,Brazil,BR,BRA,Amazonas
Caxias,Caxias,-4.833000876,-43.35002608,134640,Brazil,BR,BRA,Maranh?o
Santarem,Santarem,-2.433250713,-54.69997929,209737.5,Brazil,BR,BRA,Par?
Maraba,Maraba,-5.349971905,-49.11597905,166182,Brazil,BR,BRA,Par?
Vilhena,Vilhena,-12.71660236,-60.11659957,63231,Brazil,BR,BRA,Rond?nia
Ji-Parana,Ji-Parana,-10.83330646,-61.96700342,65016,Brazil,BR,BRA,Rond?nia
Campo Grande,Campo Grande,-20.45003213,-54.61662521,687723,Brazil,BR,BRA,Mato Grosso do Sul
Florianopolis,Florianopolis,-27.57998452,-48.52002059,568783,Brazil,BR,BRA,Santa Catarina
Feira de Santana,Feira de Santana,-12.25001585,-38.9700092,449194.5,Brazil,BR,BRA,Bahia
Boa Vista,Boa Vista,2.816092955,-60.66599756,202299.5,Brazil,BR,BRA,Roraima
Macap?,Macapa,0.033007018,-51.0500212,433781.5,Brazil,BR,BRA,Amap?
Belem,Belem,-1.450003236,-48.48002303,1787368.5,Brazil,BR,BRA,Par?
Brasilia,Brasilia,-15.78334023,-47.91605229,3139979.5,Brazil,BR,BRA,Distrito Federal
Porto Alegre,Porto Alegre,-30.05001463,-51.20001205,2644870.5,Brazil,BR,BRA,Rio Grande do Sul
Curitiba,Curitiba,-25.420013,-49.3199976,2291430,Brazil,BR,BRA,Paran?
Fortaleza,Fortaleza,-3.750017884,-38.57998132,2958717.5,Brazil,BR,BRA,Cear?
Salvador,Salvador,-12.9699719,-38.47998743,3081422.5,Brazil,BR,BRA,Bahia
Goiania,Goiania,-16.72002724,-49.30002466,1596597.5,Brazil,BR,BRA,Goi?s
Recife,Recife,-8.075645326,-34.91560551,2564549,Brazil,BR,BRA,Pernambuco
Rio de Janeiro,Rio de Janeiro,-22.92502317,-43.22502079,6879087.5,Brazil,BR,BRA,Rio de Janeiro
Sao Paulo,Sao Paulo,-23.55867959,-46.62501998,14433147.5,Brazil,BR,BRA,S?o Paulo
Bandar Seri Begawan,Bandar Seri Begawan,4.883331115,114.9332841,218250,Brunei,BN,BRN,Brunei and Muara
Lovec,Lovec,43.13799911,24.71900459,42211,Bulgaria,BG,BGR,Lovech
Montana,Montana,43.41400203,23.23700161,47445,Bulgaria,BG,BGR,Montana
Razgrad,Razgrad,43.53399903,26.53599663,38285,Bulgaria,BG,BGR,Razgrad
Sliven,Sliven,42.67937034,26.33001013,87346.5,Bulgaria,BG,BGR,Sliven
Plovdiv,Plovdiv,42.15397605,24.7539823,319089.5,Bulgaria,BG,BGR,Plovdiv
Pernik,Pernik,42.60999473,23.02271846,80625,Bulgaria,BG,BGR,Pernik
Vratsa,Vratsa,43.20998395,23.56253048,68287,Bulgaria,BG,BGR,Vratsa
Shumen,Shumen,43.27000612,26.92935339,75487.5,Bulgaria,BG,BGR,Shumen
Khaskovo,Khaskovo,41.94378216,25.5632869,72805,Bulgaria,BG,BGR,Haskovo
Stara Zagora,Stara Zagora,42.42313275,25.6227148,128315.5,Bulgaria,BG,BGR,Stara Zagora
Pleven,Pleven,43.42376935,24.61337073,110445.5,Bulgaria,BG,BGR,Pleven
Turnovo,Turnovo,43.08624473,25.65552934,53115,Bulgaria,BG,BGR,Veliko Tarnovo
Kyustendil,Kyustendil,42.28427818,22.6911108,49676.5,Bulgaria,BG,BGR,Kyustendil
Dobrich,Dobrich,43.58505149,27.83999548,73813,Bulgaria,BG,BGR,Dobrich
Varna,Varna,43.21564252,27.89528926,245522,Bulgaria,BG,BGR,Varna
Ruse,Ruse,43.85369143,25.97333939,170254,Bulgaria,BG,BGR,Ruse
Burgas,Burgas,42.51460004,27.47464311,174254,Bulgaria,BG,BGR,Burgas
Sofia,Sofia,42.68334943,23.31665401,1029913.5,Bulgaria,BG,BGR,Grad Sofiya
Fada Ngourma,Fada Ngourma,12.05499605,0.360999451,33910,Burkina Faso,BF,BFA,Gourma
Orodara,Orodara,10.97399705,-4.907996452,18632,Burkina Faso,BF,BFA,K?n?dougou
Solenzo,Solenzo,12.1833333,-4.0833333,10385,Burkina Faso,BF,BFA,Banwa
Nouna,Nouna,12.7289971,-3.860000519,29048,Burkina Faso,BF,BFA,Kossi
Dedougou,Dedougou,12.455001,-3.464000439,45341,Burkina Faso,BF,BFA,Mou Houn
Gorom Gorom,Gorom Gorom,14.45000398,-0.233297546,6691,Burkina Faso,BF,BFA,Oudalan
Djibo,Djibo,14.09900404,-1.627001421,22223,Burkina Faso,BF,BFA,Soum
Tougan,Tougan,13.06899899,-3.069998409,17590,Burkina Faso,BF,BFA,Sourou
Kombissiri,Kombissiri,12.06399605,-1.333997543,30137,Burkina Faso,BF,BFA,Baz?ga
Ziniare,Ziniare,12.57699605,-1.293002442,12703,Burkina Faso,BF,BFA,Oubritenga
Yako,Yako,12.95399712,-2.262995501,22904,Burkina Faso,BF,BFA,Passor?
Reo,Reo,12.33349214,-2.466944513,37535,Burkina Faso,BF,BFA,Sangui?
Leo,Leo,11.09400299,-2.097998529,26884,Burkina Faso,BF,BFA,Sissili
Sapouy,Sapouy,11.5544444,-1.7736111,3837,Burkina Faso,BF,BFA,Ziro
Boulsa,Boulsa,12.65699714,-0.568997532,17489,Burkina Faso,BF,BFA,Namentenga
Zorgo,Zorgo,12.24299707,-0.611000429,23892,Burkina Faso,BF,BFA,Ganzourgou
Koupela,Koupela,12.17700004,-0.356003514,32052,Burkina Faso,BF,BFA,Kouritenga
Po,Po,11.16900002,-1.134998478,17924,Burkina Faso,BF,BFA,Nahouri
Manga,Manga,11.66200198,-1.064996408,15173,Burkina Faso,BF,BFA,Zoundw?ogo
Diebougou,Diebougou,10.95200113,-3.248000411,12732,Burkina Faso,BF,BFA,Bougouriba
Gaoua,Gaoua,10.32499811,-3.174002407,28023,Burkina Faso,BF,BFA,Poni
Bogande,Bogande,12.96900003,-0.1379965,9854,Burkina Faso,BF,BFA,Gnagna
Dori,Dori,14.0339971,-0.027998519,37806,Burkina Faso,BF,BFA,S?no
Sebba,Sebba,13.4364122,0.530443,3273,Burkina Faso,BF,BFA,Yagha
Diapaga,Diapaga,12.07700108,1.796004571,26013,Burkina Faso,BF,BFA,Tapoa
Koudougou,Koudougou,12.25047833,-2.369995159,85339,Burkina Faso,BF,BFA,Boulkiemd?
Ouahigouya,Ouahigouya,13.5704236,-2.419992108,70300,Burkina Faso,BF,BFA,Yatenga
Kaya,Kaya,13.09037539,-1.090047446,39623,Burkina Faso,BF,BFA,Sanmatenga
Tenkodogo,Tenkodogo,11.78040367,-0.369703818,37883,Burkina Faso,BF,BFA,Boulgou
Banfora,Banfora,10.63044802,-4.760004315,45903.5,Burkina Faso,BF,BFA,Komo?
Bobo Dioulasso,Bobo Dioulasso,11.1799752,-4.289981325,346035,Burkina Faso,BF,BFA,Houet
Ouagadougou,Ouagadougou,12.37031598,-1.524723756,992228.5,Burkina Faso,BF,BFA,Kadiogo
Cankuzo,Cankuzo,-3.166703921,30.51669662,6585,Burundi,BI,BDI,Cankuzo
Karusi,Karusi,-3.099995968,30.16299648,10705,Burundi,BI,BDI,Karuzi
Rutana,Rutana,-3.93100195,29.99300455,20893,Burundi,BI,BDI,Rutana
Ruyigi,Ruyigi,-3.481001905,30.2439966,38458,Burundi,BI,BDI,Ruyigi
Bubanza,Bubanza,-3.083300984,29.36670351,12728,Burundi,BI,BDI,Bubanza
Kayanza,Kayanza,-2.899997879,29.5667016,19443,Burundi,BI,BDI,Kayanza
Makamba,Makamba,-4.133303903,29.79999964,19642,Burundi,BI,BDI,Makamba
Ngozi,Ngozi,-2.912003884,29.82500157,21506,Burundi,BI,BDI,Ngozi
Kirundo,Kirundo,-2.5847222,30.0972222,6083,Burundi,BI,BDI,Kirundo
Muramvya,Muramvya,-3.260997006,29.61199862,18041,Burundi,BI,BDI,Muramvya
Bururi,Bururi,-3.950729147,29.61657955,20066.5,Burundi,BI,BDI,Bururi
Muyinga,Muyinga,-2.852346579,30.31726029,71076,Burundi,BI,BDI,Muyinga
Gitega,Gitega,-3.426006654,29.84359411,23167,Burundi,BI,BDI,Muramvya
Bujumbura,Bujumbura,-3.37608722,29.36000606,331700,Burundi,BI,BDI,Bujumbura Mairie
Kampong Spoe,Kampong Spoe,11.4519961,104.5189986,33231,Cambodia,KH,KHM,K?mp?ng Sp?
Kampong Thum,Kampong Thum,12.71199613,104.8889977,19951,Cambodia,KH,KHM,K?mp?ng Thum
Prey Veng,Prey Veng,11.48399998,105.3240036,74000,Cambodia,KH,KHM,Prey V?ng
Phnum Tbeng Meanchey,Phnum Tbeng Meanchey,13.816701,104.9667037,24380,Cambodia,KH,KHM,Preah Vih?ar
Stoeng Treng,Stoeng Treng,13.52300408,105.9740016,29665,Cambodia,KH,KHM,St?ng Tr?ng
Kracheh,Kracheh,12.46899612,106.0239967,19975,Cambodia,KH,KHM,Kr?ch?h
Senmonorom,Senmonorom,12.44999711,107.1999997,7944,Cambodia,KH,KHM,M?nd?l Kiri
Lumphat,Lumphat,13.50700214,106.9810026,19205,Cambodia,KH,KHM,R?t?n?kiri
Svay Rieng,Svay Rieng,11.0799991,105.8010036,23956,Cambodia,KH,KHM,Svay Rieng
Sisophon,Sisophon,13.58375612,102.9833158,36760,Cambodia,KH,KHM,B?nt?ay M?anchey
Krong Koh Kong,Krong Koh Kong,11.61753897,102.9849329,30285,Cambodia,KH,KHM,Ka?h Kong
Pursat,Pursat,12.53369102,103.9166955,32961,Cambodia,KH,KHM,Pouthisat
Kampong Cham,Kampong Cham,12.00044191,105.4500386,72491.5,Cambodia,KH,KHM,K?mp?ng Cham
Kompong Chhnang,Kompong Chhnang,12.25047833,104.6666239,65817,Cambodia,KH,KHM,K?mp?ng Chhnang
Kampot,Kampot,10.61708966,104.1833459,36398,Cambodia,KH,KHM,K?mp?t
Takeo,Takeo,10.98375978,104.7833093,15264,Cambodia,KH,KHM,Tak?v
Battambang,Battambang,13.10001304,103.2000468,152608.5,Cambodia,KH,KHM,Batd?mb?ng
Siem Reap,Siem Reap,13.36663759,103.8500329,97199,Cambodia,KH,KHM,Siemr?ab
Phnom Penh,Phnom Penh,11.55003013,104.9166345,1466000,Cambodia,KH,KHM,Phnom Penh
Buea,Buea,4.155003087,9.231003513,90088,Cameroon,CM,CMR,Sud-Ouest
Bafang,Bafang,5.170393696,10.17998816,86916.5,Cameroon,CM,CMR,Ouest
Foumban,Foumban,5.730385355,10.89999589,64399,Cameroon,CM,CMR,Ouest
Bafoussam,Bafoussam,5.490425841,10.40994828,290768,Cameroon,CM,CMR,Ouest
Kumba,Kumba,4.640374368,9.439981647,131122,Cameroon,CM,CMR,Sud-Ouest
Eyumojok,Eyumojok,5.750358296,8.983317015,5798,Cameroon,CM,CMR,Sud-Ouest
Limbe,Limbe,4.030385761,9.190022744,142290,Cameroon,CM,CMR,Sud-Ouest
Kribi,Kribi,2.940426452,9.910030476,31473,Cameroon,CM,CMR,Sud
Nkongsamba,Nkongsamba,4.960406513,9.940002806,105069,Cameroon,CM,CMR,Littoral
Edea,Edea,3.800477314,10.11999182,109506.5,Cameroon,CM,CMR,Littoral
Wum,Wum,6.400421976,10.07002071,42601,Cameroon,CM,CMR,Nord-Ouest
Kumbo,Kumbo,6.220381286,10.68000932,89728,Cameroon,CM,CMR,Nord-Ouest
Bafia,Bafia,4.750393493,11.23000159,41201,Cameroon,CM,CMR,Centre
Mbalmayo,Mbalmayo,3.520391051,11.50001094,53501.5,Cameroon,CM,CMR,Centre
Eseka,Eseka,3.650408955,10.76661902,14102,Cameroon,CM,CMR,Centre
Bertoua,Bertoua,4.580429707,13.67998124,153286.5,Cameroon,CM,CMR,Est
Abong Mbang,Abong Mbang,3.983696105,13.18331905,7698,Cameroon,CM,CMR,Est
Batouri,Batouri,4.433694477,14.366606,42271,Cameroon,CM,CMR,Est
Belabo,Belabo,4.933689798,13.30000443,11455.5,Cameroon,CM,CMR,Est
Meiganga,Meiganga,6.520492166,14.28996985,54864.5,Cameroon,CM,CMR,Adamaoua
Ngaoundere,Ngaoundere,7.320365823,13.57998734,134322.5,Cameroon,CM,CMR,Adamaoua
Tibati,Tibati,6.46698122,12.63332678,22096,Cameroon,CM,CMR,Adamaoua
Kontcha,Kontcha,7.967018859,12.23329952,5846,Cameroon,CM,CMR,Adamaoua
Guider,Guider,9.930387389,13.94001705,83319,Cameroon,CM,CMR,Nord
Mbe,Mbe,7.850436828,13.6000378,3950,Cameroon,CM,CMR,Nord
Douala,Douala,4.060409769,9.709991006,1622041,Cameroon,CM,CMR,Littoral
Ebolowa,Ebolowa,2.900015481,11.15000647,83687.5,Cameroon,CM,CMR,Sud
Bamenda,Bamenda,5.959983743,10.15001583,419567,Cameroon,CM,CMR,Nord-Ouest
Garoua,Garoua,9.30001243,13.39002478,365436.5,Cameroon,CM,CMR,Nord
Maroua,Maroua,10.59556643,14.32469641,260656,Cameroon,CM,CMR,Extr?me-Nord
Yaounde,Yaounde,3.866700662,11.51665076,1335793.5,Cameroon,CM,CMR,Centre
Selkirk,Selkirk,50.15002545,-96.88332178,9819.5,Canada,CA,CAN,Manitoba
Berens River,Berens River,52.36655682,-97.03331262,522.5,Canada,CA,CAN,Manitoba
Pukatawagan,Pukatawagan,55.73327639,-101.3166171,431,Canada,CA,CAN,Manitoba
Gimli,Gimli,50.63330345,-96.99998133,2316,Canada,CA,CAN,Manitoba
Island Lake,Island Lake,53.96658836,-94.7665776,10,Canada,CA,CAN,Manitoba
Melville,Melville,50.93331097,-102.7999891,4226,Canada,CA,CAN,Saskatchewan
Weyburn,Weyburn,49.66656659,-103.8500025,9302.5,Canada,CA,CAN,Saskatchewan
La Ronge,La Ronge,55.10000755,-105.3000173,3427,Canada,CA,CAN,Saskatchewan
Stony Rapids,Stony Rapids,59.26657493,-105.8332664,152,Canada,CA,CAN,Saskatchewan
Camrose,Camrose,53.01669802,-112.8166386,15747,Canada,CA,CAN,Alberta
Hinton,Hinton,53.39998212,-117.5833503,10077,Canada,CA,CAN,Alberta
Vegreville,Vegreville,53.49997601,-112.0499671,5745.5,Canada,CA,CAN,Alberta
Stettler,Stettler,52.33296714,-112.6832876,5449.5,Canada,CA,CAN,Alberta
Lac La Biche,Lac La Biche,54.77193972,-111.964701,2952.5,Canada,CA,CAN,Alberta
Wetaskiwin,Wetaskiwin,52.96657188,-113.3832966,11562.5,Canada,CA,CAN,Alberta
Meander River,Meander River,59.03328168,-117.6829824,200,Canada,CA,CAN,Alberta
Creston,Creston,49.09996035,-116.516697,4816,Canada,CA,CAN,British Columbia
Cranbrook,Cranbrook,49.5166791,-115.7666653,17990,Canada,CA,CAN,British Columbia
Terrace,Terrace,54.49999249,-128.5833248,14772,Canada,CA,CAN,British Columbia
Chilliwack,Chilliwack,49.16664878,-121.949983,51942,Canada,CA,CAN,British Columbia
Hall Beach,Hall Beach,68.76746684,-81.23608303,654,Canada,CA,CAN,Nunavut
Lutselke,Lutselke,62.40005292,-110.7333291,102,Canada,CA,CAN,Northwest Territories
Hay River,Hay River,60.84999249,-115.7000027,3774,Canada,CA,CAN,Northwest Territories
D?line,Deline,65.18334556,-123.4166635,393.5,Canada,CA,CAN,Northwest Territories
Paulatuk,Paulatuk,69.38332176,-123.9833214,294,Canada,CA,CAN,Northwest Territories
Tsiigehtchic,Tsiigehtchic,67.43328575,-133.7499862,175,Canada,CA,CAN,Northwest Territories
Owen Sound,Owen Sound,44.56664532,-80.84998519,22625,Canada,CA,CAN,Ontario
Orillia,Orillia,44.59997662,-79.41666183,33830.5,Canada,CA,CAN,Ontario
Kapuskasing,Kapuskasing,49.4166852,-82.43332524,8732,Canada,CA,CAN,Ontario
Thessalon,Thessalon,46.24997927,-83.55000126,1416.5,Canada,CA,CAN,Ontario
Geraldton,Geraldton,49.71664105,-86.96664026,1290,Canada,CA,CAN,Ontario
Belleville,Belleville,44.16666974,-77.38334924,43990,Canada,CA,CAN,Ontario
Sarnia,Sarnia,42.96663963,-82.3999681,113585,Canada,CA,CAN,Ontario
Peterborough,Peterborough,44.29996909,-78.33326542,79752,Canada,CA,CAN,Ontario
Oshawa,Oshawa,43.87999473,-78.84997807,349476,Canada,CA,CAN,Ontario
London,London,42.9699986,-81.24998661,340900,Canada,CA,CAN,Ontario
Kitchener,Kitchener,43.44999514,-80.50000655,413056.5,Canada,CA,CAN,Ontario
New Liskeard,New Liskeard,47.50000633,-79.66664657,5203,Canada,CA,CAN,Ontario
Brockville,Brockville,44.5892796,-75.69531275,25172,Canada,CA,CAN,Ontario
Big Beaver House,Big Beaver House,52.94998374,-89.88328394,10,Canada,CA,CAN,Ontario
Port-Menier,Port-Menier,49.82257774,-64.34799504,263,Canada,CA,CAN,Qu?bec
Riviere-du-Loup,Riviere-du-Loup,47.83329348,-69.53331161,16403,Canada,CA,CAN,Qu?bec
Drummondville,Drummondville,45.88333498,-72.4833641,56806,Canada,CA,CAN,Qu?bec
Sherbrooke,Sherbrooke,45.40000531,-71.89998885,134549.5,Canada,CA,CAN,Qu?bec
Cap-Chat,Cap-Chat,49.09996035,-66.68330469,1475,Canada,CA,CAN,Qu?bec
Baie-Comeau,Baie-Comeau,49.22266604,-68.15799504,8808,Canada,CA,CAN,Qu?bec
Natashquan,Natashquan,50.19134076,-61.81065637,722,Canada,CA,CAN,Qu?bec
Eastmain,Eastmain,52.23333498,-78.51669092,335,Canada,CA,CAN,Qu?bec
Schefferville,Schefferville,54.80000002,-66.81665572,471,Canada,CA,CAN,Qu?bec
Salluit,Salluit,62.18259849,-75.65950098,106,Canada,CA,CAN,Qu?bec
Amos,Amos,48.56663373,-78.11666366,10475.5,Canada,CA,CAN,Qu?bec
Joliette,Joliette,46.03332583,-73.43330611,40066.5,Canada,CA,CAN,Qu?bec
St.-Jerome,St.-Jerome,45.7666496,-73.99998987,66693.5,Canada,CA,CAN,Qu?bec
St-Augustin,St-Augustin,51.2423102,-58.64699935,3961,Canada,CA,CAN,Qu?bec
Rouyn-Noranda,Rouyn-Noranda,48.25001223,-79.03324854,24312.5,Canada,CA,CAN,Qu?bec
La Sarre,La Sarre,48.8000045,-79.20003422,6366.5,Canada,CA,CAN,Qu?bec
New Glasgow,New Glasgow,45.58327578,-62.63331934,19883.5,Canada,CA,CAN,Nova Scotia
Liverpool,Liverpool,44.03995913,-64.72001367,4331,Canada,CA,CAN,Nova Scotia
Amherst,Amherst,45.81656903,-64.21658187,8631.5,Canada,CA,CAN,Nova Scotia
Baddeck,Baddeck,46.09998842,-60.75397669,852,Canada,CA,CAN,Nova Scotia
Deer Lake,Deer Lake,49.17440025,-57.42691878,3953,Canada,CA,CAN,Newfoundland and Labrador
La Scie,La Scie,49.96701337,-55.58300033,817,Canada,CA,CAN,Newfoundland and Labrador
Hopedale,Hopedale,55.44996035,-60.21667098,442,Canada,CA,CAN,Newfoundland and Labrador
Happy Valley - Goose Bay,Happy Valley - Goose Bay,53.29998822,-60.29999923,4309.5,Canada,CA,CAN,Newfoundland and Labrador
Port Hope Simpson,Port Hope Simpson,52.53329083,-56.30001083,197,Canada,CA,CAN,Newfoundland and Labrador
Tofino,Tofino,49.15207146,-125.9031487,1655,Canada,CA,CAN,British Columbia
Steinbach,Steinbach,49.51709251,-96.68330815,9668,Canada,CA,CAN,Manitoba
Nelson House,Nelson House,55.80045575,-98.85002344,2500,Canada,CA,CAN,Manitoba
Shamattawa,Shamattawa,55.85037518,-92.08327885,870,Canada,CA,CAN,Manitoba
Oxford House,Oxford House,54.95040428,-95.26659876,184,Canada,CA,CAN,Manitoba
Yorkton,Yorkton,51.21706626,-102.4665469,14377.5,Canada,CA,CAN,Saskatchewan
Swift Current,Swift Current,50.28373822,-107.766611,14804.5,Canada,CA,CAN,Saskatchewan
Biggar,Biggar,52.05040041,-107.9832902,2130,Canada,CA,CAN,Saskatchewan
Kindersley,Kindersley,51.46697349,-109.1332976,4316,Canada,CA,CAN,Saskatchewan
Meadow Lake,Meadow Lake,54.13011843,-108.4347356,5081.5,Canada,CA,CAN,Saskatchewan
Hudson Bay,Hudson Bay,52.8504291,-102.3832961,1909,Canada,CA,CAN,Saskatchewan
Lethbridge,Lethbridge,49.70049217,-112.8332784,64594,Canada,CA,CAN,Alberta
Brooks,Brooks,50.56705426,-111.9000021,13453.5,Canada,CA,CAN,Alberta
Lake Louise,Lake Louise,51.43369387,-116.1832807,1248,Canada,CA,CAN,Alberta
Athabasca,Athabasca,54.71703351,-113.2665853,2399.5,Canada,CA,CAN,Alberta
Fort Chipewyan,Fort Chipewyan,58.71709943,-111.1499962,3222,Canada,CA,CAN,Alberta
Bella Bella,Bella Bella,52.14840476,-128.1172809,1400,Canada,CA,CAN,British Columbia
Sandspit,Sandspit,53.24040529,-131.8332815,538,Canada,CA,CAN,British Columbia
Campbell River,Campbell River,50.01708783,-125.2499882,29941.5,Canada,CA,CAN,British Columbia
Port Hardy,Port Hardy,50.71707094,-127.4999801,2295,Canada,CA,CAN,British Columbia
Nanaimo,Nanaimo,49.14602021,-123.9342911,82698,Canada,CA,CAN,British Columbia
Quesnel,Quesnel,52.98367678,-122.4832837,13788,Canada,CA,CAN,British Columbia
Abbotsford,Abbotsford,49.05037681,-122.2999874,151683,Canada,CA,CAN,British Columbia
Dawson Creek,Dawson Creek,55.76696942,-120.233266,10676.5,Canada,CA,CAN,British Columbia
Penticton,Penticton,49.50037518,-119.5832799,34035,Canada,CA,CAN,British Columbia
Nelson,Nelson,49.48365786,-117.2832911,10796,Canada,CA,CAN,British Columbia
Lillooet,Lillooet,50.68371381,-121.9332656,2893,Canada,CA,CAN,British Columbia
Powell River,Powell River,49.88371096,-124.5499793,7999.5,Canada,CA,CAN,British Columbia
Revelstoke,Revelstoke,51.0004645,-118.1833395,7600.5,Canada,CA,CAN,British Columbia
Burns Lake,Burns Lake,54.21701235,-125.7665975,2633,Canada,CA,CAN,British Columbia
Dease Lake,Dease Lake,58.45034568,-130.033288,303,Canada,CA,CAN,British Columbia
Coral Harbour,Coral Harbour,64.15377016,-83.17658736,834,Canada,CA,CAN,Nunavut
Baker Lake,Baker Lake,64.31699017,-96.01665633,1584,Canada,CA,CAN,Nunavut
Norman Wells,Norman Wells,65.28372703,-126.8499681,650,Canada,CA,CAN,Northwest Territories
Fort McPherson,Fort McPherson,67.49152508,-134.8949809,1069,Canada,CA,CAN,Northwest Territories
Burwash Landing,Burwash Landing,61.35037539,-139.0000017,73,Canada,CA,CAN,Yukon
Orangeville,Orangeville,43.91707257,-80.08333948,30812,Canada,CA,CAN,Ontario
Little Current,Little Current,45.96702496,-81.93332992,1595,Canada,CA,CAN,Ontario
Chapleau,Chapleau,47.83370689,-83.40001042,2663,Canada,CA,CAN,Ontario
Wawa,Wawa,48.00041506,-84.78333683,2174,Canada,CA,CAN,Ontario
Hearst,Hearst,49.70049217,-83.66658329,4894.5,Canada,CA,CAN,Ontario
Marathon,Marathon,48.75039512,-86.36665104,4627,Canada,CA,CAN,Ontario
Sioux Lookout,Sioux Lookout,50.26296429,-91.9166482,4570,Canada,CA,CAN,Ontario
Red Lake,Red Lake,51.03369244,-93.83330123,1765,Canada,CA,CAN,Ontario
Deer Lake,Deer Lake,52.61703249,-94.06659448,3743,Canada,CA,CAN,Ontario
Cat Lake,Cat Lake,51.71703575,-91.79998865,277,Canada,CA,CAN,Ontario
Cornwall,Cornwall,45.01705711,-74.73333012,47601.5,Canada,CA,CAN,Ontario
Kingston,Kingston,44.23371991,-76.48330082,108297.5,Canada,CA,CAN,Ontario
Barrie,Barrie,44.38376243,-79.7000037,150886.5,Canada,CA,CAN,Ontario
Parry Sound,Parry Sound,45.33370445,-80.03300663,6787,Canada,CA,CAN,Ontario
Wiarton,Wiarton,44.73368939,-81.13330123,2182,Canada,CA,CAN,Ontario
Cobalt,Cobalt,47.38370852,-79.68331222,1372,Canada,CA,CAN,Ontario
Cochrane,Cochrane,49.06701662,-81.01656417,4441,Canada,CA,CAN,Ontario
Nipigon,Nipigon,49.01704551,-88.24997278,1204,Canada,CA,CAN,Ontario
Atikokan,Atikokan,48.75039512,-91.61658899,3625,Canada,CA,CAN,Ontario
Rimouski,Rimouski,48.43374778,-68.51668115,35584,Canada,CA,CAN,Qu?bec
Saint-Georges,Saint-Georges,46.117145,-70.66665328,26149,Canada,CA,CAN,Qu?bec
Victoriaville,Victoriaville,46.05040489,-71.96667729,37963,Canada,CA,CAN,Qu?bec
Chevery,Chevery,50.48132306,-59.60978296,284,Canada,CA,CAN,Qu?bec
Mistassini,Mistassini,50.41706341,-73.86658716,2645,Canada,CA,CAN,Qu?bec
Kangirsuk,Kangirsuk,60.02482322,-69.99909713,549,Canada,CA,CAN,Qu?bec
Shawinigan,Shawinigan,46.55037437,-72.733323,41751.5,Canada,CA,CAN,Qu?bec
Matagami,Matagami,49.75038576,-77.63328231,1574.5,Canada,CA,CAN,Qu?bec
Mont-Laurier,Mont-Laurier,46.55037437,-75.50002751,11642,Canada,CA,CAN,Qu?bec
Pembroke,Pembroke,45.85026206,-77.11664718,15551,Canada,CA,CAN,Qu?bec
Radisson,Radisson,53.78362795,-77.61656498,270,Canada,CA,CAN,Qu?bec
Saint John,Saint John,45.26704185,-66.07667505,71153,Canada,CA,CAN,New Brunswick
Edmundston,Edmundston,47.37941937,-68.3332815,17894,Canada,CA,CAN,New Brunswick
Shelburne,Shelburne,43.76560895,-65.31935694,2553,Canada,CA,CAN,Nova Scotia
Antigonish,Antigonish,45.62691652,-61.99819015,5871,Canada,CA,CAN,Nova Scotia
Windsor,Windsor,44.98059938,-64.12911951,3759,Canada,CA,CAN,Nova Scotia
Digby,Digby,44.62258506,-65.7604928,3000.5,Canada,CA,CAN,Nova Scotia
Stephenville,Stephenville,48.55040733,-58.56656498,6666,Canada,CA,CAN,Newfoundland and Labrador
Argentia,Argentia,47.30043194,-53.98999679,1063,Canada,CA,CAN,Newfoundland and Labrador
St. Anthony,St. Anthony,51.3837486,-55.5999502,224,Canada,CA,CAN,Newfoundland and Labrador
Channel-Port aux Basques,Channel-Port aux Basques,47.56700482,-59.15004358,3232,Canada,CA,CAN,Newfoundland and Labrador
Buchans,Buchans,48.81703188,-56.86659123,685,Canada,CA,CAN,Newfoundland and Labrador
Trout River,Trout River,49.48365786,-58.11664413,452,Canada,CA,CAN,Newfoundland and Labrador
Churchill Falls,Churchill Falls,53.52640851,-63.98067896,75,Canada,CA,CAN,Newfoundland and Labrador
Forteau,Forteau,51.45038535,-56.94999699,448,Canada,CA,CAN,Newfoundland and Labrador
Trepassey,Trepassey,46.73697797,-53.36329085,398,Canada,CA,CAN,Newfoundland and Labrador
Brochet,Brochet,57.88322268,-101.6665957,278,Canada,CA,CAN,Manitoba
Lynn Lake,Lynn Lake,56.85002993,-101.0499667,482,Canada,CA,CAN,Manitoba
Gillam,Gillam,56.34998293,-94.69996668,1281,Canada,CA,CAN,Manitoba
North Battleford,North Battleford,52.76663576,-108.2833494,15721.5,Canada,CA,CAN,Saskatchewan
Prince Albert,Prince Albert,53.20002016,-105.7499899,29643.5,Canada,CA,CAN,Saskatchewan
Courtenay,Courtenay,49.68333559,-124.9999777,28946,Canada,CA,CAN,British Columbia
Kelowna,Kelowna,49.89998903,-119.4833118,110207.5,Canada,CA,CAN,British Columbia
Pangnirtung,Pangnirtung,66.13331341,-65.75002832,1320,Canada,CA,CAN,Nunavut
Holman,Holman,70.73336855,-117.7499809,449,Canada,CA,CAN,Northwest Territories
Dryden,Dryden,49.78332949,-92.83333643,7862,Canada,CA,CAN,Ontario
Attawapiskat,Attawapiskat,52.91662661,-82.43332524,1802,Canada,CA,CAN,Ontario
Hamilton,Hamilton,43.24998151,-79.82999577,620501,Canada,CA,CAN,Ontario
Windsor,Windsor,42.33329327,-83.03334029,265068.5,Canada,CA,CAN,Ontario
Trois-Rivi?res,Trois Rivieres,46.34997316,-72.54994918,118051,Canada,CA,CAN,Qu?bec
Sept-?les,Sept-Iles,50.31608767,-66.36001693,25686,Canada,CA,CAN,Qu?bec
Corner Brook,Corner Brook,48.94999534,-57.93334782,19742,Canada,CA,CAN,Newfoundland and Labrador
Norway House,Norway House,53.96658836,-97.83328963,5500,Canada,CA,CAN,Manitoba
Flin Flon,Flin Flon,54.76659121,-101.8833008,6197.5,Canada,CA,CAN,Manitoba
Dauphin,Dauphin,51.15001609,-100.0499502,8747.5,Canada,CA,CAN,Manitoba
The Pas,The Pas,53.81662335,-101.2333147,4928.5,Canada,CA,CAN,Manitoba
Uranium City,Uranium City,59.56655662,-108.6165849,89,Canada,CA,CAN,Saskatchewan
Moose Jaw,Moose Jaw,50.39998435,-105.5500021,31436.5,Canada,CA,CAN,Saskatchewan
Jasper,Jasper,52.88332115,-118.0833714,3504.5,Canada,CA,CAN,Alberta
Medicine Hat,Medicine Hat,50.03331423,-110.6833322,58382,Canada,CA,CAN,Alberta
Red Deer,Red Deer,52.26664044,-113.8000411,74225,Canada,CA,CAN,Alberta
Banff,Banff,51.17799888,-115.5719227,6897,Canada,CA,CAN,Alberta
Grand Prairie,Grand Prairie,55.16664431,-118.7999943,41153.5,Canada,CA,CAN,Alberta
Smithers,Smithers,54.76659121,-127.1665896,5841.5,Canada,CA,CAN,British Columbia
Kamloops,Kamloops,50.66666058,-120.3332858,68671,Canada,CA,CAN,British Columbia
Williams Lake,Williams Lake,52.1166496,-122.1499966,12361,Canada,CA,CAN,British Columbia
Prince George,Prince George,53.91666892,-122.7666515,64132.5,Canada,CA,CAN,British Columbia
Fort Nelson,Fort Nelson,58.81670575,-122.5329706,6315,Canada,CA,CAN,British Columbia
Pond Inlet,Pond Inlet,72.68498069,-78.00005579,1549,Canada,CA,CAN,Nunavut
Cape Dorset,Cape Dorset,64.31251972,-76.53857863,1326,Canada,CA,CAN,Nunavut
Kimmirut,Kimmirut,62.85002545,-69.88331608,385,Canada,CA,CAN,Nunavut
Gjoa Haven,Gjoa Haven,68.63329002,-95.91666244,1109,Canada,CA,CAN,Nunavut
Grise Fiord,Grise Fiord,76.44165061,-82.94998621,23,Canada,CA,CAN,Nunavut
Alert,Alert,82.48332318,-62.24998356,97.5,Canada,CA,CAN,Nunavut
Ennadai,Ennadai,61.13328269,-100.883336,0,Canada,CA,CAN,Nunavut
Rankin Inlet,Rankin Inlet,62.81666831,-92.09531946,2403,Canada,CA,CAN,Nunavut
Fort Resolution,Fort Resolution,61.16658815,-113.682994,448,Canada,CA,CAN,Northwest Territories
Fort Simpson,Fort Simpson,61.84998313,-121.3332764,283,Canada,CA,CAN,Northwest Territories
Inuvik,Inuvik,68.34997398,-133.6999893,3022,Canada,CA,CAN,Northwest Territories
Tuktoyaktuk,Tuktoyaktuk,69.45477459,-133.0492013,899.5,Canada,CA,CAN,Northwest Territories
Watson Lake,Watson Lake,60.1166264,-128.80003,802,Canada,CA,CAN,Yukon
Lansdowne House,Lansdowne House,52.21664349,-87.88332849,120,Canada,CA,CAN,Ontario
Moosonee,Moosonee,51.28060244,-80.65798141,1725,Canada,CA,CAN,Ontario
Sudbury,Sudbury,46.49998985,-80.96664474,119182,Canada,CA,CAN,Ontario
Kenora,Kenora,49.76668968,-94.46664758,10852,Canada,CA,CAN,Ontario
Gaspe,Gaspe,48.83731488,-64.49336084,3504,Canada,CA,CAN,Qu?bec
Mingan,Mingan,50.3017589,-64.01726532,588,Canada,CA,CAN,Qu?bec
Dolbeau,Dolbeau,48.86658958,-72.23332768,13126.5,Canada,CA,CAN,Qu?bec
Val d'Or,Val d'Or,48.11663535,-77.76663334,20625,Canada,CA,CAN,Qu?bec
Ivugivik,Ivugivik,62.41664105,-77.89998438,156,Canada,CA,CAN,Qu?bec
Inukjuak,Inukjuak,58.47000856,-78.13599064,1597,Canada,CA,CAN,Qu?bec
Chicoutimi,Chicoutimi,48.43330853,-71.06670638,53940,Canada,CA,CAN,Qu?bec
Moncton,Moncton,46.08334861,-64.76667749,89051,Canada,CA,CAN,New Brunswick
Fredericton,Fredericton,45.94999758,-66.63330774,44525,Canada,CA,CAN,New Brunswick
Bathurst,Bathurst,47.59997438,-65.64998275,5303.5,Canada,CA,CAN,New Brunswick
Yarmouth,Yarmouth,43.83079447,-66.1125812,7433,Canada,CA,CAN,Nova Scotia
Gander,Gander,48.94999534,-54.54998845,3345,Canada,CA,CAN,Newfoundland and Labrador
Cartwright,Cartwright,53.70140663,-57.01214114,505,Canada,CA,CAN,Newfoundland and Labrador
Rigolet,Rigolet,54.17660138,-58.44732162,124,Canada,CA,CAN,Newfoundland and Labrador
Port Burwell,Port Burwell,60.26646222,-64.74109766,2762,Canada,CA,CAN,Newfoundland and Labrador
Thompson,Thompson,55.74994204,-97.86662093,13097,Canada,CA,CAN,Manitoba
Brandon,Brandon,49.83327476,-99.94998214,27326,Canada,CA,CAN,Manitoba
Fort Smith,Fort Smith,60.00001853,-111.8833364,518,Canada,CA,CAN,Alberta
Fort McMurray,Fort McMurray,56.7333187,-111.3833153,21863,Canada,CA,CAN,Alberta
Peace River,Peace River,56.23332338,-117.2832911,5014.5,Canada,CA,CAN,Alberta
Fort St. John,Fort St. John,56.24998903,-120.8332811,18089,Canada,CA,CAN,British Columbia
Iqaluit,Iqaluit,63.75045938,-68.50019175,6124,Canada,CA,CAN,Nunavut
Cambridge Bay,Cambridge Bay,69.11695559,-105.0333153,1477,Canada,CA,CAN,Nunavut
Kugluktuk,Kugluktuk,67.79866282,-115.1253504,1302,Canada,CA,CAN,Nunavut
Chesterfield Inlet,Chesterfield Inlet,63.33829022,-90.70008163,374,Canada,CA,CAN,Nunavut
Arviat,Arviat,61.10859211,-94.05860672,1868,Canada,CA,CAN,Nunavut
Taloyoak,Taloyoak,69.5333126,-93.53331954,774,Canada,CA,CAN,Nunavut
Igloolik,Igloolik,69.25653506,-81.79359213,1612,Canada,CA,CAN,Nunavut
Dawson City,Dawson,64.0666437,-139.4166687,1319,Canada,CA,CAN,Yukon
Timmins,Timmins,48.46658815,-81.33331486,33937.5,Canada,CA,CAN,Ontario
North Bay,North Bay,46.30000205,-79.44999313,45988.5,Canada,CA,CAN,Ontario
Kuujjuarapik,Kuujjuarapik,55.28149518,-77.76583236,1243,Canada,CA,CAN,Qu?bec
Kuujjuaq,Kuujjuaq,58.10000531,-68.39999577,1273,Canada,CA,CAN,Qu?bec
Sydney,Sydney,46.06611452,-60.17998071,37538,Canada,CA,CAN,Nova Scotia
Labrador City,Labrador City,52.94143129,-66.91587447,8840,Canada,CA,CAN,Newfoundland and Labrador
Winnipeg,Winnipeg,49.88298749,-97.16599186,603688,Canada,CA,CAN,Manitoba
Churchill,Churchill,58.76598533,-94.1659941,961.5,Canada,CA,CAN,Manitoba
Regina,Regina,50.45003298,-104.6170099,176183,Canada,CA,CAN,Saskatchewan
Saskatoon,Saskatoon,52.17003135,-106.6699854,194075.5,Canada,CA,CAN,Saskatchewan
Calgary,Calgary,51.08299176,-114.0799982,1012661,Canada,CA,CAN,Alberta
Prince Rupert,Prince Rupert,54.31667035,-130.3299882,14708,Canada,CA,CAN,British Columbia
Victoria,Victoria,48.43328269,-123.3500009,270491.5,Canada,CA,CAN,British Columbia
Arctic Bay,Arctic Bay,73.03330568,-85.16662093,604,Canada,CA,CAN,Nunavut
Resolute,Resolute,74.68333417,-94.90000615,239.5,Canada,CA,CAN,Nunavut
Repulse Bay,Repulse Bay,66.52946689,-86.28293502,874,Canada,CA,CAN,Nunavut
Yellowknife,Yellowknife,62.44201418,-114.3969814,18658.5,Canada,CA,CAN,Northwest Territories
Fort Good Hope,Fort Good Hope,66.26661277,-128.6333218,597,Canada,CA,CAN,Northwest Territories
Whitehorse,Whitehorse,60.71671897,-135.0499844,23274,Canada,CA,CAN,Yukon
Ottawa,Ottawa,45.4166968,-75.7000153,978564.5,Canada,CA,CAN,Ontario
Fort Severn,Fort Severn,55.98333864,-87.64998356,125,Canada,CA,CAN,Ontario
Thunder Bay,Thunder Bay,48.44615013,-89.27497481,98354,Canada,CA,CAN,Ontario
Qu?bec,Quebec,46.83996909,-71.24561019,576386,Canada,CA,CAN,Qu?bec
Halifax,Halifax,44.65002525,-63.60000452,290992.5,Canada,CA,CAN,Nova Scotia
St. John?s,St. John's,47.58498822,-52.68100692,115325.5,Canada,CA,CAN,Newfoundland and Labrador
Nain,Nain,56.54735147,-61.6860454,1151,Canada,CA,CAN,Newfoundland and Labrador
Charlottetown,Charlottetown,46.24928164,-63.13132512,36847.5,Canada,CA,CAN,Prince Edward Island
Edmonton,Edmonton,53.55002464,-113.4999819,885195.5,Canada,CA,CAN,Alberta
Montr?al,Montr?al,45.49999921,-73.58329696,3017278,Canada,CA,CAN,Qu?bec
Vancouver,Vancouver,49.27341658,-123.1216442,1458415,Canada,CA,CAN,British Columbia
Toronto,Toronto,43.69997988,-79.42002079,4573710.5,Canada,CA,CAN,Ontario
Mindelo,Mindelo,16.88376141,-25.0000092,62962,Cape Verde,CV,CPV,
Praia,Praia,14.91669802,-23.51668889,101111.5,Cape Verde,CV,CPV,
George Town,George Town,19.28043683,-81.32998173,2770.5,Cayman Islands,KY,CYM,
Mobaye,Mobaye,4.320000059,21.17999753,19431,Central African Republic,CF,CAF,Basse-Kotto
Mbaiki,Mbaiki,3.870421365,17.99997595,43566,Central African Republic,CF,CAF,Lobaye
Carnot,Carnot,4.933689798,15.8666178,32298,Central African Republic,CF,CAF,Mamb?r?-Kad??
Bozoum,Bozoum,6.316990376,16.38333044,25440.5,Central African Republic,CF,CAF,Ouham-Pend?
Kaga Bandoro,Kaga Bandoro,6.980386575,19.18000728,42673.5,Central African Republic,CF,CAF,Nana-Gr?bizi
Zemio,Zemio,5.033657856,25.13328731,19239,Central African Republic,CF,CAF,Haut-Mbomou
Yakossi,Yakossi,5.617007262,23.31665401,409.5,Central African Republic,CF,CAF,Mbomou
Nola,Nola,3.533697732,16.06660559,25301,Central African Republic,CF,CAF,Sangha-Mba?r?
Sibut,Sibut,5.733770161,19.08332068,26304.5,Central African Republic,CF,CAF,K?mo
Bossangoa,Bossangoa,6.483724384,17.44998368,45246,Central African Republic,CF,CAF,Ouham
Birao,Birao,10.28369916,22.78330155,5641,Central African Republic,CF,CAF,Vakaga
Ouadda,Ouadda,8.06709027,22.40001745,3424.5,Central African Republic,CF,CAF,Haute-Kotto
Bangassou,Bangassou,4.733753681,22.81663285,28601,Central African Republic,CF,CAF,Mbomou
Bossembele,Bossembele,5.267002786,17.65002315,7287,Central African Republic,CF,CAF,Bangui
Berberati,Berberati,4.249958922,15.7800081,60605,Central African Republic,CF,CAF,Mamb?r?-Kad??
Bria,Bria,6.533307921,21.9832987,24985.5,Central African Republic,CF,CAF,Haute-Kotto
Bouar,Bouar,5.950010192,15.59996741,31476.5,Central African Republic,CF,CAF,Nana-Mamb?r?
Bambari,Bambari,5.761959655,20.66720333,47322.5,Central African Republic,CF,CAF,Ouaka
Ndele,Ndele,8.409136575,20.65304398,7355.5,Central African Republic,CF,CAF,Bamingui-Bangoran
Obo,Obo,5.399992085,26.50002559,12837,Central African Republic,CF,CAF,Haut-Mbomou
Bangui,Bangui,4.366644306,18.55828813,727348,Central African Republic,CF,CAF,Bangui
Lai,Lai,9.395001123,16.30500349,19382,Chad,TD,TCD,Tandjil?
Zouar,Zouar,20.458737,16.52776607,204,Chad,TD,TCD,Bet
Bol,Bol,13.45895754,14.71469844,3303,Chad,TD,TCD,Lac
Ati,Ati,13.21706016,18.33328894,24723.5,Chad,TD,TCD,Batha
Oum Hadjer,Oum Hadjer,13.30041424,19.68333573,11582.5,Chad,TD,TCD,Batha
Mongo,Mongo,12.18373822,18.6999849,27763,Chad,TD,TCD,Gu?ra
Doba,Doba,8.650439676,16.8500203,26966.5,Chad,TD,TCD,Logone Oriental
Pala,Pala,9.350422789,14.96662105,17835,Chad,TD,TCD,Mayo-Kebbi Est
Bongor,Bongor,10.28594708,15.38716386,112229.5,Chad,TD,TCD,Mayo-Kebbi Est
Kelo,Kelo,9.317065652,15.80000688,69378.5,Chad,TD,TCD,Tandjil?
Fada,Fada,17.18472495,21.59024776,448,Chad,TD,TCD,Bet
Faya Largeau,Faya Largeau,17.91666994,19.11670365,13400,Chad,TD,TCD,Bet
Mao,Mao,14.11943402,15.31331824,15040,Chad,TD,TCD,Kanem
Biltine,Biltine,14.53325889,20.91669714,6682.5,Chad,TD,TCD,Wadi Fira
Sarh,Sarh,9.149969909,18.39002966,135862,Chad,TD,TCD,Mandoul
Am Timan,Am Timan,11.03329165,20.28329911,29664,Chad,TD,TCD,Salamat
Moundou,Moundou,8.549980691,16.09001501,145936,Chad,TD,TCD,Logone Oriental
Ndjamena,Ndjamena,12.11309654,15.04914831,835193.5,Chad,TD,TCD,Hadjer-Lamis
Abeche,Abeche,13.83999371,20.82998409,116252.5,Chad,TD,TCD,Ouadda?
Rio Verde,Rio Verde,-52.64997882,-71.46660445,358,Chile,CL,CHL,Magallanes y Ant?rtica Chilena
Cuya,Cuya,-19.11667682,-70.13330082,20,Chile,CL,CHL,Tarapac?
Chuquicamata,Chuquicamata,-22.31999551,-68.92998926,11941,Chile,CL,CHL,Antofagasta
Maria Elena,Maria Elena,-22.35001951,-69.66999577,2370,Chile,CL,CHL,Antofagasta
Tierra Amarilla,Tierra Amarilla,-27.4800423,-70.27998438,10733,Chile,CL,CHL,Atacama
Combarbala,Combarbala,-31.18002317,-70.99999211,5134,Chile,CL,CHL,Coquimbo
San Bernardo,San Bernardo,-33.59997882,-70.69998458,243950,Chile,CL,CHL,Regi?n Metropolitana de Santiago
San Felipe,San Felipe,-32.75000486,-70.7200092,49256.5,Chile,CL,CHL,Valpara?so
Vina del Mar,Vina del Mar,-33.02998777,-71.53998499,399042.5,Chile,CL,CHL,Valpara?so
La Ligua,La Ligua,-32.45999673,-71.24002914,25761,Chile,CL,CHL,Valpara?so
Quillota,Quillota,-32.87997109,-71.26000208,73732.5,Chile,CL,CHL,Valpara?so
Nueva Imperial,Nueva Imperial,-38.74002684,-72.96002751,13322.5,Chile,CL,CHL,La Araucan?a
Loncoche,Loncoche,-39.37001422,-72.62999597,8653.5,Chile,CL,CHL,La Araucan?a
Villarica,Villarica,-39.28004555,-72.22999455,16818,Chile,CL,CHL,La Araucan?a
Tolten,Tolten,-39.21659053,-73.21233798,2293,Chile,CL,CHL,La Araucan?a
Lonquimay,Lonquimay,-38.43332721,-71.23328536,8519.5,Chile,CL,CHL,La Araucan?a
Angol,Angol,-37.79000731,-72.71001693,38384.5,Chile,CL,CHL,La Araucan?a
Collipulli,Collipulli,-37.95997109,-72.43000818,11307.5,Chile,CL,CHL,La Araucan?a
La Union,La Union,-40.28995807,-73.0899679,22843,Chile,CL,CHL,Los R?os
Rio Bueno,Rio Bueno,-40.34003253,-72.96002751,13059.5,Chile,CL,CHL,Los R?os
Coronel,Coronel,-37.02995034,-73.1600153,78594.5,Chile,CL,CHL,B?o-B?o
Talcahuano,Talcahuano,-36.71668781,-73.11665877,270521,Chile,CL,CHL,B?o-B?o
Quirihue,Quirihue,-36.28002195,-72.53000208,6529,Chile,CL,CHL,B?o-B?o
Curanilahue,Curanilahue,-37.48000039,-73.34000431,22352.5,Chile,CL,CHL,B?o-B?o
Santa Barbara,Santa Barbara,-37.67001463,-72.01998153,3494,Chile,CL,CHL,B?o-B?o
Pichilemu,Pichilemu,-34.38003457,-71.99998275,11603,Chile,CL,CHL,Libertador General Bernardo O'Higgins
San Fernando,San Fernando,-34.58002236,-70.98996688,60746,Chile,CL,CHL,Libertador General Bernardo O'Higgins
Puerto Varas,Puerto Varas,-41.32999795,-72.98999984,19569,Chile,CL,CHL,Los Lagos
Calbuco,Calbuco,-41.75220107,-73.14159106,6933.5,Chile,CL,CHL,Los Lagos
Castro,Castro,-42.48076159,-73.76233415,25184.5,Chile,CL,CHL,Los Lagos
Chonchi,Chonchi,-42.61002317,-73.80994979,381,Chile,CL,CHL,Los Lagos
Linares,Linares,-35.83999713,-71.58998194,75275,Chile,CL,CHL,Maule
Cauquenes,Cauquenes,-35.96004148,-72.31998906,24155,Chile,CL,CHL,Maule
Cochrane,Cochrane,-47.26627643,-72.54994918,4441,Chile,CL,CHL,Ais?n del General Carlos Ib??ez del Campo
Lagunas,Lagunas,-20.98286782,-69.68330245,10,Chile,CL,CHL,Tarapac?
Pozo Almonte,Pozo Almonte,-20.2696297,-69.80001367,10830,Chile,CL,CHL,Tarapac?
Toconao,Toconao,-23.18288857,-68.01663416,378,Chile,CL,CHL,Antofagasta
Huasco,Huasco,-28.4695943,-71.22000452,2558,Chile,CL,CHL,Atacama
Diego de Almagro,Diego de Almagro,-26.36961912,-70.04999841,18137,Chile,CL,CHL,Atacama
Caldera,Caldera,-27.06962807,-70.83002832,10259,Chile,CL,CHL,Atacama
Coquimbo,Coquimbo,-29.95291461,-71.34361454,159082.5,Chile,CL,CHL,Coquimbo
Vicuna,Vicuna,-30.02949909,-70.73998214,13496,Chile,CL,CHL,Coquimbo
Illapel,Illapel,-31.62960814,-71.17000757,24578,Chile,CL,CHL,Coquimbo
Salamanca,Salamanca,-31.77957314,-70.97996749,16739.5,Chile,CL,CHL,Coquimbo
Los Andes,Los Andes,-32.82958657,-70.59999068,53135,Chile,CL,CHL,Valpara?so
San Antonio,San Antonio,-33.59951373,-71.60998071,94971.5,Chile,CL,CHL,Valpara?so
Victoria,Victoria,-38.23954059,-72.34001367,17989.5,Chile,CL,CHL,La Araucan?a
Carahue,Carahue,-38.70948606,-73.16998885,8592,Chile,CL,CHL,La Araucan?a
Los Lagos,Los Lagos,-39.84951984,-72.82998377,12813,Chile,CL,CHL,Los R?os
Lota,Lota,-37.08958494,-73.1600153,32702,Chile,CL,CHL,B?o-B?o
Lebu,Lebu,-37.6095532,-73.64998539,16624.5,Chile,CL,CHL,B?o-B?o
Quellon,Quellon,-43.09960569,-73.59998845,7029,Chile,CL,CHL,Los Lagos
Constitucion,Constitucion,-35.32958901,-72.41998295,26902.5,Chile,CL,CHL,Maule
Villa O'Higgins,Villa O'Higgins,-48.46790851,-72.55997441,175,Chile,CL,CHL,Santa Cruz
Puerto Aisen,Puerto Aisen,-45.3999304,-72.70001754,8067,Chile,CL,CHL,Ais?n del General Carlos Ib??ez del Campo
Puerto Natales,Puerto Natales,-51.71830442,-72.51168278,10393,Chile,CL,CHL,Magallanes y Ant?rtica Chilena
Puerto Williams,Puerto Williams,-54.93330198,-67.61671025,2381,Chile,CL,CHL,Magallanes y Ant?rtica Chilena
Temuco,Temuco,-38.73000161,-72.57999903,252015,Chile,CL,CHL,La Araucan?a
Tocopilla,Tocopilla,-22.09003538,-70.18998987,22355.5,Chile,CL,CHL,Antofagasta
Calama,Calama,-22.45001341,-68.91998987,134336.5,Chile,CL,CHL,Antofagasta
Mejillones,Mejillones,-23.09999957,-70.44999984,2041,Chile,CL,CHL,Antofagasta
Taltal,Taltal,-25.40001422,-70.47002446,8947.5,Chile,CL,CHL,Antofagasta
Vallenar,Vallenar,-28.57000161,-70.76000676,37876.5,Chile,CL,CHL,Atacama
Chanaral,Chanaral,-29.03002521,-71.43001754,13543,Chile,CL,CHL,Atacama
Ovalle,Ovalle,-30.59003335,-71.20005742,72984,Chile,CL,CHL,Coquimbo
Chillan,Chillan,-36.60000242,-72.10599695,149874,Chile,CL,CHL,B?o-B?o
Rancagua,Rancagua,-34.17002155,-70.73998214,222981.5,Chile,CL,CHL,Libertador General Bernardo O'Higgins
Osorno,Osorno,-40.56999266,-73.1600153,144952,Chile,CL,CHL,Los Lagos
Ancud,Ancud,-41.86996499,-73.82997441,24241,Chile,CL,CHL,Los Lagos
Talca,Talca,-35.45500771,-71.67000289,186283.5,Chile,CL,CHL,Maule
Curico,Curico,-34.97999795,-71.24002914,108074.5,Chile,CL,CHL,Maule
Coihaique,Coihaique,-45.56999754,-72.07000431,43221,Chile,CL,CHL,Ais?n del General Carlos Ib??ez del Campo
Arica,Arica,-18.50002195,-70.28998377,178446.5,Chile,CL,CHL,Arica y Parinacota
Copiapo,Copiapo,-27.35999795,-70.33998071,117316.5,Chile,CL,CHL,Atacama
La Serena,La Serena,-29.89999795,-71.24997685,151290,Chile,CL,CHL,Coquimbo
Los Angeles,Los Angeles,-37.46000161,-72.35998661,135334.5,Chile,CL,CHL,B?o-B?o
Punta Arenas,Punta Arenas,-53.16498615,-70.93999577,106296,Chile,CL,CHL,Magallanes y Ant?rtica Chilena
Iquique,Iquique,-20.24999266,-70.12996769,223012,Chile,CL,CHL,Tarapac?
Antofagasta,Antofagasta,-23.64999184,-70.40000289,295539,Chile,CL,CHL,Antofagasta
Valparaiso,Valparaiso,-33.04776447,-71.62101363,434969,Chile,CL,CHL,Valpara?so
Valdivia,Valdivia,-39.7950012,-73.24502303,146509,Chile,CL,CHL,Los R?os
Concepcion,Concepcion,-36.83001422,-73.05002202,550864,Chile,CL,CHL,B?o-B?o
Puerto Montt,Puerto Montt,-41.4699894,-72.92997766,167341.5,Chile,CL,CHL,Los Lagos
Santiago,Santiago,-33.45001382,-70.66704085,2883305.5,Chile,CL,CHL,Regi?n Metropolitana de Santiago
Yumen,Yumen,39.83003522,97.72999304,233097,China,CN,CHN,Gansu
Linxia,Linxia,35.60000917,103.2000468,368478.5,China,CN,CHN,Gansu
Zhuozhou,Zuozhou,39.54005292,115.789976,415000,China,CN,CHN,Beijing
Sanming,Sanming,26.2299868,117.5800476,104941.5,China,CN,CHN,Fujian
Huizhou,Huizhou,23.07997235,114.3999833,289201,China,CN,CHN,Guangdong
Chaozhou,Chaozhou,23.68003908,116.630028,424787,China,CN,CHN,Guangdong
Gyangze,Gyangze,28.95000165,89.63332963,10000,China,CN,CHN,Xizang
Dali,Dali,34.79525209,109.937775,109696,China,CN,CHN,Shaanxi
Yangquan,Yangquan,37.86997398,113.5700081,851801.5,China,CN,CHN,Shanxi
Shiyan,Shiyan,32.57003908,110.7799975,653823.5,China,CN,CHN,Hubei
Danjiangkou,Danjiangkou,32.5200163,111.5000052,92008,China,CN,CHN,Hubei
Shashi,Shashi,30.32002138,112.2299865,509390,China,CN,CHN,Hubei
Anlu,Anlu,31.26998924,113.670002,71198,China,CN,CHN,Hubei
Zixing,Zixing,25.96997683,113.4000443,6618,China,CN,CHN,Hunan
Deyang,Deyang,31.13333091,104.3999735,152194,China,CN,CHN,Sichuan
Tengchong,Tengchong,25.03331565,98.46658891,126058,China,CN,CHN,Yunnan
Mengzi,Mengzi,23.3619448,103.4061324,303341,China,CN,CHN,Yunnan
Chuxiong,Chuxiong,25.03641624,101.5455741,254370,China,CN,CHN,Yunnan
Hengshui,Hengshui,37.71998313,115.7000073,456356,China,CN,CHN,Hebei
Xuanhua,Xuanhua,40.59440716,115.0243379,391583.5,China,CN,CHN,Hebei
Luohe,Luohe,33.57000388,114.02998,417356,China,CN,CHN,Henan
Beipiao,Beipiao,41.81001772,120.7600085,191757,China,CN,CHN,Liaoning
Wafangdian,Wafangdian,39.62591331,121.9959537,303217.5,China,CN,CHN,Liaoning
Zhucheng,Zhucheng,35.98995953,119.3800927,881963.5,China,CN,CHN,Shandong
Hangu,Hangu,39.23195803,117.7769864,270581,China,CN,CHN,Tianjin
Xinyi,Xinyi,34.38000612,118.3500264,962656,China,CN,CHN,Jiangsu
Yangzhou,Yangzhou,32.39999778,119.4300122,539715,China,CN,CHN,Jiangsu
Linhai,Linhai,28.85000775,121.1199865,202348,China,CN,CHN,Zhejiang
Huangyan,Huangyan,28.65001996,121.2500044,174580.5,China,CN,CHN,Zhejiang
Daan,Daan,45.49999921,124.2999991,84795.5,China,CN,CHN,Jilin
Changling,Changling,44.26999676,123.9899922,46703.5,China,CN,CHN,Jilin
Tonghua,Tonghua,41.67997398,125.7499882,27227,China,CN,CHN,Jilin
Baishan,Baishan,41.90001223,126.4299983,330000,China,CN,CHN,Jilin
Yanji,Yanji,42.88230369,129.5127559,407848.5,China,CN,CHN,Jilin
Ergun Zuoqi,Ergun Zuoqi,50.78332013,121.5166548,42849,China,CN,CHN,Nei Mongol
Shangdu,Shangdu,41.54943931,113.5338863,18831,China,CN,CHN,Nei Mongol
Orongen Zizhiqi,Orongen Zizhiqi,50.56666669,123.7166756,40128,China,CN,CHN,Nei Mongol
Zalantun,Zalantun,48.00000165,122.7199922,135128,China,CN,CHN,Nei Mongol
Wuchuan,Wuchuan,41.09551353,111.4408357,23776,China,CN,CHN,Nei Mongol
Hanggin Houqi,Hanggin Houqi,40.88469952,107.140013,39954,China,CN,CHN,Nei Mongol
Anda,Anda,46.39999595,125.3200402,181402,China,CN,CHN,Heilongjiang
Qinggang,Qinggang,46.69002993,126.1000443,60955,China,CN,CHN,Heilongjiang
Angangxi,Angangxi,47.16005292,123.8000297,24317,China,CN,CHN,Heilongjiang
Hulan Ergi,Hulan Ergi,47.20997235,123.6100154,277671.5,China,CN,CHN,Heilongjiang
Qingan,Qingan,46.87185345,127.5118444,53206,China,CN,CHN,Heilongjiang
Baiquan,Baiquan,47.60183474,126.0818542,52679.5,China,CN,CHN,Heilongjiang
Suileng,Suileng,47.24599082,127.1059777,57456.5,China,CN,CHN,Heilongjiang
Linkou,Linkou,45.28189882,130.2518839,66426.5,China,CN,CHN,Heilongjiang
Longxi,Longxi,35.04763979,104.6394421,355037,China,CN,CHN,Gansu
Pingliang,Pingliang,35.53037518,106.6800927,157706,China,CN,CHN,Gansu
Anxi,Anxi,40.50043357,95.79998165,17886,China,CN,CHN,Gansu
Minxian,Minxian,34.4361784,104.0305904,67826,China,CN,CHN,Gansu
Jinchang,Jinchang,38.49569806,102.1739078,141670,China,CN,CHN,Gansu
Guide,Guide,36.04509829,101.4241862,7642,China,CN,CHN,Gansu
Qinzhou,Qinzhou,21.95042889,108.6199743,173186,China,CN,CHN,Guangxi
Pingxiang,Pingxiang,22.09737083,106.7566772,31109,China,CN,CHN,Guangxi
Yishan,Yishan,24.50037661,108.6666898,47062,China,CN,CHN,Guangxi
Beihai,Beihai,21.4804059,109.1000484,567289,China,CN,CHN,Guangxi
Hechi,Hechi,23.09653465,109.6091129,3275189.5,China,CN,CHN,Guangxi
Tongren,Tongren,27.68041506,109.1300207,104441.5,China,CN,CHN,Guizhou
Fengjie,Fengjie,31.05044191,109.5166638,49168,China,CN,CHN,Chongqing
Changping,Changping,40.22476564,116.1943957,372410.5,China,CN,CHN,Beijing
Shaowu,Shaowu,27.30038658,117.5000008,56889.5,China,CN,CHN,Fujian
Longyan,Longyan,25.18041262,117.0300036,367896,China,CN,CHN,Fujian
Zhangzhou,Zhangzhou,24.52037539,117.6700162,2434799.5,China,CN,CHN,Fujian
Putian,Putian,25.43034568,119.0200114,376558,China,CN,CHN,Fujian
Fuan,Fuan,27.07042645,119.6200264,81761.5,China,CN,CHN,Fujian
Changting,Changting,25.8669857,116.3166621,87458,China,CN,CHN,Fujian
Nanping,Nanping,26.63037579,118.1699857,192364,China,CN,CHN,Fujian
Ninde,Ninde,26.68037274,119.5300577,189623.5,China,CN,CHN,Fujian
Jieshou,Jieshou,33.25043683,115.3500028,141993,China,CN,CHN,Anhui
Tongling,Tongling,30.95044802,117.7800354,437710,China,CN,CHN,Anhui
Maanshan,Maanshan,31.73040041,118.4800443,1000121,China,CN,CHN,Anhui
Fuyang,Fuyang,32.90040651,115.82,170023,China,CN,CHN,Anhui
Yangjiang,Yangjiang,21.85040916,111.9700024,751181.5,China,CN,CHN,Guangdong
Meizhou,Meizhou,24.30049217,116.1199816,279571,China,CN,CHN,Guangdong
Heyuan,Heyuan,23.7304236,114.6800179,269280.5,China,CN,CHN,Guangdong
Qingyuan,Qingyuan,23.7003996,113.0300927,706717,China,CN,CHN,Guangdong
Zhaoqing,Zhaoqing,23.05041343,112.4500248,420984.5,China,CN,CHN,Guangdong
Lianxian,Lianxian,24.78152224,112.3825354,148233,China,CN,CHN,Guangdong
Jiangmen,Jiangmen,22.58039044,113.0800122,532419,China,CN,CHN,Guangdong
Maoming,Maoming,21.92040489,110.8700179,1217715,China,CN,CHN,Guangdong
Gar,Gar,32.20039756,79.98332434,5250,China,CN,CHN,Xizang
Turpan,Turpan,42.93537539,89.1650378,178863.5,China,CN,CHN,Xinjiang Uygur
Quiemo,Quiemo,38.13375633,85.53332149,32494,China,CN,CHN,Xinjiang Uygur
Koktokay,Koktokay,47.00037274,89.46662146,60000,China,CN,CHN,Xinjiang Uygur
Hancheng,Hancheng,35.47043052,110.429993,140092,China,CN,CHN,Shaanxi
Weinan,Weinan,34.50043805,109.5000756,172321,China,CN,CHN,Shaanxi
Shuozhou,Shuozhou,39.30037762,112.4200008,408068.5,China,CN,CHN,Shanxi
Xinzhou,Xinzhou,38.41043194,112.7199825,216805,China,CN,CHN,Shanxi
Jincheng,Jincheng,35.50037701,112.8300016,520000,China,CN,CHN,Shanxi
Jiexiu,Jiexiu,37.04002464,111.8999808,77178,China,CN,CHN,Shanxi
Changzhi,Changzhi,36.18387534,113.1052819,706000,China,CN,CHN,Shanxi
Guangshui,Guangshui,31.62038129,114.0000077,145885.5,China,CN,CHN,Hubei
Jingmen,Jingmen,31.03039146,112.1000203,400000,China,CN,CHN,Hubei
Zicheng,Zicheng,30.30043601,111.5000052,198212.5,China,CN,CHN,Hubei
Shishou,Shishou,29.70039512,112.400002,177099,China,CN,CHN,Hubei
Xiaogan,Xiaogan,30.92039817,113.9000138,160437,China,CN,CHN,Hubei
Puqi,Puqi,29.72041974,113.880015,169027.5,China,CN,CHN,Hubei
Yunxian,Yunxian,32.80816408,110.8136389,133558,China,CN,CHN,Hubei
Jinshi,Jinshi,29.63210472,111.851715,178453,China,CN,CHN,Hunan
Chenzhou,Chenzhou,25.80042645,113.0300927,251017.5,China,CN,CHN,Hunan
Zhijiang,Zhijiang,27.44094647,109.6780493,113907,China,CN,CHN,Hunan
Xiangtan,Xiangtan,27.85043052,112.9000232,2183454,China,CN,CHN,Hunan
Zigong,Zigong,29.40000002,104.780002,897480.5,China,CN,CHN,Sichuan
Yaan,Yaan,29.98042971,103.0800024,340000,China,CN,CHN,Sichuan
Langzhong,Langzhong,31.57593955,105.9655627,60542,China,CN,CHN,Sichuan
Rongzhag,Rongzhag,30.95044802,101.9166626,52500,China,CN,CHN,Sichuan
Simao,Simao,22.78068829,100.9781669,162725,China,CN,CHN,Yunnan
Wenshan,Wenshan,23.3723576,104.2496984,108396,China,CN,CHN,Yunnan
Zhanyi,Zhanyi,25.6004645,103.8166499,652604,China,CN,CHN,Yunnan
Huize,Huize,26.35041872,103.4166744,5170,China,CN,CHN,Yunnan
Chengde,Chengde,40.96037966,117.9300004,377629,China,CN,CHN,Hebei
Cangzhou,Cangzhou,38.32038576,116.8700134,527681,China,CN,CHN,Hebei
Baoding,Baoding,38.87042971,115.4800207,1051326,China,CN,CHN,Hebei
Huanghua,Hunanghua,38.37043439,117.330037,104243,China,CN,CHN,Hebei
Dingzhou,Dingzhou,38.50042645,114.9999983,152934,China,CN,CHN,Hebei
Nangong,Nangong,37.37039207,115.3700016,82386,China,CN,CHN,Hebei
Linqing,Linqing,36.85039797,115.6800085,110046,China,CN,CHN,Hebei
Xiangtai,Xiangtai,37.04997235,114.5000288,611739,China,CN,CHN,Hebei
Puyang,Puyang,35.70039064,114.9799996,666322,China,CN,CHN,Henan
Hebi,Hebi,35.95037539,114.2200459,244662,China,CN,CHN,Henan
Xuchang,Xuchang,34.02038983,113.8200187,449258,China,CN,CHN,Henan
Zhoukou,Zhoukou,33.63041363,114.6300468,377061,China,CN,CHN,Henan
Dengzhou,Dengzhou,32.68036826,112.0800215,59338,China,CN,CHN,Henan
Tieling,Tieling,42.30037539,123.8199768,336953.5,China,CN,CHN,Liaoning
Chaoyang,Chaoyang,41.55042116,120.4199776,440150.5,China,CN,CHN,Liaoning
Huanren,Huanren,41.25633059,125.3459818,91384,China,CN,CHN,Liaoning
Zhuanghe,Zhuanghe,39.6822923,122.9618896,170947,China,CN,CHN,Liaoning
Yishui,Yishui,35.79043683,118.6199841,94115,China,CN,CHN,Shandong
Shanxian,Shanxian,34.79042035,116.0799841,74459,China,CN,CHN,Shandong
Pingyi,Pingyi,35.51042808,117.6200451,78254,China,CN,CHN,Shandong
Pingdu,Pingdu,36.79037579,119.9400069,91077,China,CN,CHN,Shandong
Laiwu,Laiwu,36.2004118,117.6600427,124108,China,CN,CHN,Shandong
Buizhou,Buizhou,37.37039207,118.0200207,115893,China,CN,CHN,Shandong
Liaocheng,Liaocheng,36.4304236,115.9700166,226930,China,CN,CHN,Shandong
Rizhao,Rizhao,35.43038129,119.4500109,555693.5,China,CN,CHN,Shandong
Dezhou,Dezhou,37.45041302,116.3000223,379555,China,CN,CHN,Shandong
Linchuan,Linchuan,27.97034568,116.3600187,241104,China,CN,CHN,Jiangxi
Fengcheng,Fengcheng,28.20040916,115.7700288,61469,China,CN,CHN,Jiangxi
Jian,Jian,27.13042279,114.9999983,490221,China,CN,CHN,Jiangxi
Shangrao,Shangrao,28.47039268,117.9699979,922421.5,China,CN,CHN,Jiangxi
Jingdezhen,Jingdezhen,29.27042137,117.1800203,383931.5,China,CN,CHN,Jiangxi
Taizhou,Taizhou,32.4904057,119.9000093,612356,China,CN,CHN,Jiangsu
Shuyang,Shuyang,34.12986635,118.7733597,1770000,China,CN,CHN,Jiangsu
Lianyungang,Lianyungang,34.60043194,119.170028,715600,China,CN,CHN,Jiangsu
Lishui,Lishui,28.45041974,119.9000093,135861.5,China,CN,CHN,Zhejiang
Jiaojing,Jiaojing,28.6804057,121.4499922,471152,China,CN,CHN,Zhejiang
Quzhou,Quzhou,28.97043968,118.8699947,226108,China,CN,CHN,Zhejiang
Fuyu,Fuyu,45.18038047,124.8200191,247804.5,China,CN,CHN,Jilin
Dunhua,Dunhua,43.35049217,128.2200183,170357,China,CN,CHN,Jilin
Nongan,Nongan,44.43040041,125.1700752,141482,China,CN,CHN,Jilin
Taonan,Taonan,45.33042299,122.7800402,114715,China,CN,CHN,Jilin
Liuhe,Liuhe,42.27885215,125.7173287,67956.5,China,CN,CHN,Jilin
Huinan,Huinan,42.62293968,126.2614298,43261.5,China,CN,CHN,Jilin
Panshi,Panshi,42.94263592,126.0561193,83208,China,CN,CHN,Jilin
Jiaohe,Jiaohe,43.71628379,127.3459631,90420,China,CN,CHN,Jilin
Linjiang,Linjiang,41.83634686,126.9359623,76732,China,CN,CHN,Jilin
Wangqing,Wangqing,43.32478314,129.7343444,79825,China,CN,CHN,Jilin
Helong,Helong,42.53475384,129.0043632,83032.5,China,CN,CHN,Jilin
Shulan,Shulan,44.40910972,126.9487264,78092,China,CN,CHN,Jilin
Jiutai,Jiutai,44.14473309,125.8443493,190257,China,CN,CHN,Jilin
Alxa Zuoqi,Alxa Zuoqi,38.83901044,105.6686299,56387,China,CN,CHN,Nei Mongol
Linxi,Linxi,43.51707115,118.0333016,679,China,CN,CHN,Nei Mongol
Kailu,Kailu,43.58373374,121.1999816,2809,China,CN,CHN,Nei Mongol
Bairin Zuoqi,Bairin Zuoqi,43.98370933,119.1833606,48540,China,CN,CHN,Nei Mongol
Yitulihe,Yitulihe,50.65162274,121.5166548,19645,China,CN,CHN,Nei Mongol
Yakeshi,Yakeshi,49.28041445,120.7300362,107047,China,CN,CHN,Nei Mongol
Bugt,Bugt,48.78380393,121.9333736,17457,China,CN,CHN,Nei Mongol
Wuyuan,Wuyuan,41.08962242,108.2721919,30057,China,CN,CHN,Nei Mongol
Bayan Obo,Bayan Obo,41.76764305,109.9711063,27476,China,CN,CHN,Nei Mongol
Fengzhen,Fengzhen,40.45469993,113.1443493,85809,China,CN,CHN,Nei Mongol
Suihua,Suihua,46.63042116,126.9799906,250903,China,CN,CHN,Heilongjiang
Shuangyashan,Shuangyashan,46.67041872,131.3500081,500000,China,CN,CHN,Heilongjiang
Shangzhi,Shangzhi,45.22042971,127.9700077,89699.5,China,CN,CHN,Heilongjiang
Fujin,Fujin,47.2703821,132.019993,80092.5,China,CN,CHN,Heilongjiang
Yian,Yian,47.88039654,125.2999898,39924,China,CN,CHN,Heilongjiang
Tailai,Tailai,46.3903583,123.409976,71307.5,China,CN,CHN,Heilongjiang
Longjiang,Longjiang,47.34040367,123.1800158,87115,China,CN,CHN,Heilongjiang
Gannan,Gannan,47.92036826,123.5100215,46854.5,China,CN,CHN,Heilongjiang
Hailun,Hailun,47.45042279,126.9300195,104848.5,China,CN,CHN,Heilongjiang
Mishan,Mishan,45.55038373,131.8800016,80459,China,CN,CHN,Heilongjiang
Tieli,Tieli,46.95037579,128.0500028,109228.5,China,CN,CHN,Heilongjiang
Shuangcheng,Shuangcheng,45.35034426,126.2799816,118525,China,CN,CHN,Heilongjiang
Zhaodong,Zhaodong,46.08042889,125.98,167193,China,CN,CHN,Heilongjiang
Lanxi,Lanxi,46.2663607,126.2759509,67011,China,CN,CHN,Heilongjiang
Keshan,Keshan,48.02633079,125.8659501,72403,China,CN,CHN,Heilongjiang
Nancha,Nancha,47.13635927,129.285948,104570.5,China,CN,CHN,Heilongjiang
Xinqing,Xinqing,48.23634381,129.5059346,42617.5,China,CN,CHN,Heilongjiang
Hulin,Hulin,45.76902671,132.9922334,42559,China,CN,CHN,Heilongjiang
Boli,Boli,45.75636599,130.5759468,83317,China,CN,CHN,Heilongjiang
Ningan,Ningan,44.33133669,129.4659371,54636,China,CN,CHN,Heilongjiang
Jyekundo,Jyekundo,33.01662681,96.73330969,16500,China,CN,CHN,Gansu
Liuzhou,Liuzhou,24.28000246,109.2500134,1436030.5,China,CN,CHN,Guangxi
Xingyi,Xingyi,25.09041811,104.8900211,539536,China,CN,CHN,Guizhou
Anshun,Anshun,26.25039899,105.9300093,600468,China,CN,CHN,Guizhou
Zunyi,Zunyi,27.70002626,106.9200264,657646,China,CN,CHN,Guizhou
Wanzhou,Wanxian,30.81999086,108.4000394,1680000,China,CN,CHN,Chongqing
Huaibei,Huaibei,33.95036826,116.7500207,908019.5,China,CN,CHN,Anhui
Wuhu,Wuhu,31.3504236,118.3699735,658762,China,CN,CHN,Anhui
Luan,Luan,31.75034751,116.4800114,1408227.5,China,CN,CHN,Anhui
Bengbu,Bengbu,32.94999005,117.330037,735324,China,CN,CHN,Anhui
Anqing,Anqing,30.49995872,117.0500024,469579,China,CN,CHN,Anhui
Foshan,Foshan,23.03005292,113.1200097,785174,China,CN,CHN,Guangdong
Nagchu,Nagchu,31.48000226,92.05002966,2250,China,CN,CHN,Xizang
Nyingchi,Nyingchi,29.53329938,94.41670691,55,China,CN,CHN,Xizang
Chamdo,Chamdo,31.16668805,97.23327917,93140,China,CN,CHN,Xizang
Korla,Korla,41.72999676,86.15002803,192919,China,CN,CHN,Xinjiang Uygur
Kuqa,Kuqa,41.72774884,82.93637406,89802,China,CN,CHN,Xinjiang Uygur
Tacheng,Tacheng,46.75002626,82.95001664,49796,China,CN,CHN,Xinjiang Uygur
Shihezi,Shihezi,44.29996909,86.02993201,572977,China,CN,CHN,Xinjiang Uygur
Karamay,Karamay,45.58994204,84.8599259,108769,China,CN,CHN,Xinjiang Uygur
Aksu,Aksu,41.15000633,80.25002641,309704.5,China,CN,CHN,Xinjiang Uygur
Sanya,Sanya,18.25910454,109.5040317,253721,China,CN,CHN,Hainan
Haikou,Haikou,20.05000226,110.3200256,1606808.5,China,CN,CHN,Hainan
Hanzhong,Hanzhong,33.12997906,107.0299939,145986,China,CN,CHN,Shaanxi
Baoji,Baoji,34.38000612,107.1499865,800000,China,CN,CHN,Shaanxi
Tongchuan,Tongchuan,35.07998924,109.0299751,252930.5,China,CN,CHN,Shaanxi
Linfen,Linfen,36.08034161,111.520004,533283,China,CN,CHN,Shanxi
Yuci,Yuci,37.68039899,112.7300077,537964.5,China,CN,CHN,Shanxi
Datong,Datong,40.08001996,113.2999987,1462839,China,CN,CHN,Shanxi
Jianmen,Jianmen,30.65005292,113.1600073,937875,China,CN,CHN,Hubei
Yichang,Yichang,30.69997235,111.2800187,675862.5,China,CN,CHN,Hubei
Xiantao,Xiantao,30.3704059,113.4400419,897703,China,CN,CHN,Hubei
Macheng,Macheng,31.17999473,115.0300223,126366,China,CN,CHN,Hubei
Huangshi,Huangshi,30.22000165,115.0999922,688090,China,CN,CHN,Hubei
Zhuzhou,Zhuzhou,27.82999249,113.1500337,894679,China,CN,CHN,Hunan
Yongzhou,Yongzhou,26.23037437,111.6199979,700180.5,China,CN,CHN,Hunan
Yiyang,Yiyang,28.60041058,112.3300321,777304,China,CN,CHN,Hunan
Changde,Changde,29.02999676,111.6800459,993390,China,CN,CHN,Hunan
Shaoyang,Shaoyang,26.99999147,111.2000752,45617,China,CN,CHN,Hunan
Leshan,Leshan,29.56709576,103.7333475,655738.5,China,CN,CHN,Sichuan
Panzhihua,Panzhihua,26.5499931,101.7300073,446298,China,CN,CHN,Sichuan
Fulin,Fulin,29.35000307,102.7167171,1049,China,CN,CHN,Sichuan
Guangyuan,Guangyuan,32.42999595,105.870013,325400,China,CN,CHN,Sichuan
Luzhou,Luzhou,28.87998008,105.380017,1537000,China,CN,CHN,Sichuan
Yibin,Yibin,28.7699868,104.5700406,572055.5,China,CN,CHN,Sichuan
Zhaotang,Zhaotang,27.32038535,103.720015,459200,China,CN,CHN,Yunnan
Lijiang,Lijiang,26.80000368,100.2665824,18445,China,CN,CHN,Yunnan
Yuxi,Yuxi,24.37999636,102.5700077,250077,China,CN,CHN,Yunnan
Dali,Dali,25.70001914,100.1799727,145362.5,China,CN,CHN,Yunnan
Qinhuangdao,Qinhuangdao,39.93036501,119.6200264,881359,China,CN,CHN,Hebei
Langfang,Langfang,39.5203642,116.6799991,694465.5,China,CN,CHN,Hebei
Zhangjiakou,Zhangjiakou,40.83000002,114.9299768,802820.5,China,CN,CHN,Hebei
Tangshan,Tangshan,39.62433718,118.194377,1737974.5,China,CN,CHN,Hebei
Anyang,Anyang,36.07997988,114.3500122,834064.5,China,CN,CHN,Henan
Jiaozuo,Jiaozuo,35.2500047,113.2200036,687270,China,CN,CHN,Henan
Kaifeng,Kaifeng,34.85000327,114.3500122,872000,China,CN,CHN,Henan
Shangqiu,Shangqiu,34.45041526,115.6500362,967109,China,CN,CHN,Henan
Pingdingshan,Pingdingshan,33.73040753,113.2999987,849000,China,CN,CHN,Henan
Xinyang,Xinyang,32.130376,114.0699776,1411944,China,CN,CHN,Henan
Xinxiang,Xinxiang,35.32043968,113.8699898,823300.5,China,CN,CHN,Henan
Luoyang,Luoyang,34.67998781,112.4700752,1552790.5,China,CN,CHN,Henan
Liaoyang,Liaoyang,41.27999839,123.1800158,740945,China,CN,CHN,Liaoning
Dandong,Dandong,40.14360781,124.3935852,750986.5,China,CN,CHN,Liaoning
Yingkow,Yingkow,40.67034568,122.2800191,693079.5,China,CN,CHN,Liaoning
Jinzhou,Jinzhou,41.12036989,121.1000394,780134.5,China,CN,CHN,Liaoning
Fuxin,Fuxin,42.0104706,121.6600052,729525,China,CN,CHN,Liaoning
Benxi,Benxi,41.33038291,123.7500069,923933,China,CN,CHN,Liaoning
Fushun,Fushun,41.86538902,123.8699996,1435323,China,CN,CHN,Liaoning
Jining,Jining,35.40040895,116.5500329,818163.5,China,CN,CHN,Shandong
Weifang,Weifang,36.7204059,119.1001098,973866,China,CN,CHN,Shandong
Taian,Taian,36.19999839,117.1200756,1629000,China,CN,CHN,Shandong
Heze,Heze,35.22998008,115.4500484,796301,China,CN,CHN,Shandong
Laiyang,Laiyang,36.9684011,120.7084354,209797,China,CN,CHN,Shandong
Xinyu,Xinyu,27.80002016,114.9299768,505240,China,CN,CHN,Jiangxi
Ganzhou,Ganzhou,25.91997988,114.9500272,1216134.5,China,CN,CHN,Jiangxi
Jiujiang,Jiujiang,29.72997988,115.9800419,545616,China,CN,CHN,Jiangxi
Changzhou,Changzhou,31.77998395,119.9699792,1138009,China,CN,CHN,Jiangsu
Zhenjiang,Zhenjiang,32.21998293,119.4300122,743276,China,CN,CHN,Jiangsu
Nantong,Nantong,32.0303821,120.8250175,806625.5,China,CN,CHN,Jiangsu
Jiaxing,Jiaxing,30.77040733,120.7499833,727050.5,China,CN,CHN,Zhejiang
Huzhou,Huzhou,30.87037539,120.0999971,694660,China,CN,CHN,Zhejiang
Shaoxing,Shaoxing,30.00037681,120.5700459,599141.5,China,CN,CHN,Zhejiang
Jinhua,Jinhua,29.12004295,119.6499987,617529,China,CN,CHN,Zhejiang
Liaoyuan,Liaoyuan,42.89997703,125.1299743,485898.5,China,CN,CHN,Jilin
Tumen,Tumen,42.9699986,129.8200756,89220,China,CN,CHN,Jilin
Siping,Siping,43.17001223,124.3300232,528811,China,CN,CHN,Jilin
Baicheng,Baicheng,45.62001772,122.8200378,351915.5,China,CN,CHN,Jilin
Wuhai,Wuhai,39.66469647,106.8122294,218427,China,CN,CHN,Nei Mongol
Erenhot,Erenhot,43.66155845,111.9654549,19357,China,CN,CHN,Nei Mongol
Jining,Jining,41.02998781,113.0800122,270236.5,China,CN,CHN,Nei Mongol
Arxan,Arxan,47.18330731,119.9666202,32023,China,CN,CHN,Nei Mongol
Manzhouli,Manzhouli,49.59998151,117.4299792,74214,China,CN,CHN,Nei Mongol
Xilinhot,Xilinhot,43.94433189,116.0443274,116156.5,China,CN,CHN,Nei Mongol
Heihe,Heihe,50.25001935,127.4460087,54923,China,CN,CHN,Heilongjiang
Qitaihe,Qitaihe,45.7999809,130.8500386,397825,China,CN,CHN,Heilongjiang
Yichun,Yichun,47.69994244,128.8999768,443111.5,China,CN,CHN,Heilongjiang
Hegang,Hegang,47.40001243,130.3700162,657833.5,China,CN,CHN,Heilongjiang
Nenjiang,Nenjiang,49.1799813,125.2300199,79685,China,CN,CHN,Heilongjiang
Nehe,Nehe,48.48999758,124.8800154,74937.5,China,CN,CHN,Heilongjiang
Mudangiang,Mudangiang,44.57501691,129.5900122,954957.5,China,CN,CHN,Heilongjiang
Xuanzhou,Xuanzhou,30.9525,118.7552778,866000,China,CN,CHN,Anhui
Zhuhai,Zhuhai,22.2769444,113.5677778,1023000,China,CN,CHN,Guangdong
Xianyang,Xianyang,34.3455556,108.7147222,1126000,China,CN,CHN,Shaanxi
Xiangfan,Xiangfan,32.01999514,112.1300443,765978,China,CN,CHN,Hubei
Suining,Suining,30.5333333,105.5333333,1425000,China,CN,CHN,Sichuan
Lingyuan,Lingyuan,41.24,119.4011111,806000,China,CN,CHN,Liaoning
Weihai,Weihai,37.49997072,122.0999784,356425,China,CN,CHN,Shandong
Yichun,Yichun,27.8333333,114.4,982000,China,CN,CHN,Jiangxi
Yancheng,Yancheng,33.3855556,120.1252778,839000,China,CN,CHN,Jiangsu
Fuyang,Fuyang,30.0533333,119.9519444,771000,China,CN,CHN,Zhejiang
Xiamen,Xiamen,24.44999208,118.080017,1548668.5,China,CN,CHN,Fujian
Nanchong,Nanchong,30.78043256,106.1299971,2174000,China,CN,CHN,Sichuan
Neijiang,Neijiang,29.58037661,105.0500114,1006427,China,CN,CHN,Sichuan
Nanyang,Nanyang,33.00040041,112.5300199,1097766,China,CN,CHN,Henan
Jinxi,Jinxi,40.7503408,120.8299784,1369623.5,China,CN,CHN,Liaoning
Yantai,Yantai,37.53040814,121.4000211,1417666,China,CN,CHN,Shandong
Zaozhuang,Zaozhuang,34.88000144,117.5700223,1164332.5,China,CN,CHN,Shandong
Suzhou,Suzhou,31.30047833,120.620017,1496545.5,China,CN,CHN,Jiangsu
Xuzhou,Xuzhou,34.28001223,117.1800203,1645096.5,China,CN,CHN,Jiangsu
Wuxi,Wuxi,31.57999615,120.2999849,1428823.5,China,CN,CHN,Jiangsu
Jilin,Jilin,43.84997072,126.5500427,2138988.5,China,CN,CHN,Jilin
Zhangye,Zhangye,38.9299868,100.4500337,163478,China,CN,CHN,Gansu
Wuwei,Wuwei,37.92800661,102.6410111,493092,China,CN,CHN,Gansu
Dunhuang,Dunhuang,40.14267763,94.66201493,139225,China,CN,CHN,Gansu
Tianshui,Tianshui,34.60001853,105.9199841,649883.5,China,CN,CHN,Gansu
Dulan,Dulan,36.16658958,98.26660111,50,China,CN,CHN,Gansu
Golmud,Golmud,36.416626,94.88334509,107092,China,CN,CHN,Gansu
Yulin,Yulin,22.62997398,110.1500101,637742.5,China,CN,CHN,Guangxi
Bose,Bose,23.8997156,106.6133268,132942.5,China,CN,CHN,Guangxi
Wuzhou,Wuzhou,23.48002545,111.3200162,354080.5,China,CN,CHN,Guangxi
Lupanshui,Lupanshui,26.59443483,104.8333321,886256,China,CN,CHN,Guizhou
Quanzhou,Quanzhou,24.9000163,118.5799865,823571.5,China,CN,CHN,Fujian
Hefei,Hefei,31.85003135,117.2800142,1711952,China,CN,CHN,Anhui
Suzhou,Suzhou,33.6361111,116.9788889,1964000,China,CN,CHN,Anhui
Zhanjiang,Zhanjiang,21.19998374,110.3800219,1113895,China,CN,CHN,Guangdong
Shaoguan,Shaoguan,24.79997072,113.5799816,674507.5,China,CN,CHN,Guangdong
Xigaze,Xigaze,29.25000917,88.88334957,59314.5,China,CN,CHN,Xizang
Shache,Shache,38.42614158,77.25000281,282391.5,China,CN,CHN,Xinjiang Uygur
Yining,Yining,43.90001935,81.35001094,403489,China,CN,CHN,Xinjiang Uygur
Altay,Altay,47.86659894,88.11662634,140670.5,China,CN,CHN,Xinjiang Uygur
Shizuishan,Shizuishan,39.23327578,106.7690279,109824,China,CN,CHN,Ningxia Hui
Yulin,Yulin,38.28330792,109.7332914,123415,China,CN,CHN,Shaanxi
Ankang,Ankang,32.67998069,109.0200016,1025000,China,CN,CHN,Shaanxi
Houma,Houma,35.61998212,111.2099971,102400,China,CN,CHN,Shanxi
Yueyang,Yueyang,29.38005292,113.1000109,826000,China,CN,CHN,Hunan
Hengyang,Hengyang,26.88002464,112.5900162,887801,China,CN,CHN,Hunan
Mianyang,Mianyang,31.46997703,104.7699768,830068,China,CN,CHN,Sichuan
Xichang,Xichang,27.88001528,102.2999983,253390,China,CN,CHN,Sichuan
Baoshan,Baoshan,25.11997703,99.15000972,925000,China,CN,CHN,Yunnan
Gejiu,Gejiu,23.37997988,103.1500756,142620,China,CN,CHN,Yunnan
Shijianzhuang,Shijianzhuang,38.05001467,114.4799784,2204737,China,CN,CHN,Hebei
Handan,Handan,36.5799752,114.4799784,1494659,China,CN,CHN,Hebei
Anshan,Anshan,41.11502138,122.9400305,1419137.5,China,CN,CHN,Liaoning
Dalian,Dalian,38.92283839,121.6298308,2601153.5,China,CN,CHN,Liaoning
Qingdao,Qingdao,36.08997927,120.3300089,2254122.5,China,CN,CHN,Shandong
Linyi,Linyi,35.07998924,118.329976,1176334.5,China,CN,CHN,Shandong
Huaiyin,Huaiyin,33.58000327,119.0299849,909615,China,CN,CHN,Jiangsu
Wenzhou,Wenzhou,28.0199809,120.6500927,1607836,China,CN,CHN,Zhejiang
Ningbo,Ningbo,29.87997072,121.5500378,1321433.5,China,CN,CHN,Zhejiang
Tongliao,Tongliao,43.61995892,122.2699939,572555,China,CN,CHN,Nei Mongol
Hohhot,Hohhot,40.81997479,111.6599955,1250238.5,China,CN,CHN,Nei Mongol
Chifeng,Chifeng,42.27001548,118.9499898,811827,China,CN,CHN,Nei Mongol
Ulanhot,Ulanhot,46.08001548,122.0800313,203870,China,CN,CHN,Nei Mongol
Hailar,Hailar,49.19998008,119.7000215,221118.5,China,CN,CHN,Nei Mongol
Jiamusi,Jiamusi,46.83002138,130.3500175,784774.5,China,CN,CHN,Heilongjiang
Beian,Beian,48.23900515,126.4820365,154936,China,CN,CHN,Heilongjiang
Daqing,Daqing,46.57995913,125.0000081,948244,China,CN,CHN,Heilongjiang
Jixi,Jixi,45.29995974,130.9700313,684379.5,China,CN,CHN,Heilongjiang
Jiayuguan,Jiayuguan,39.82000999,98.29998409,135337.5,China,CN,CHN,Gansu
Xining,Xining,36.6199986,101.7700048,907765.5,China,CN,CHN,Gansu
Guilin,Guilin,25.2799931,110.280028,818176,China,CN,CHN,Guangxi
Huainan,Huainan,32.62998374,116.9799808,1239327.5,China,CN,CHN,Anhui
Shantou,Shantou,23.37000633,116.6700256,1467486.5,China,CN,CHN,Guangdong
Lhasa,Lhasa,29.64502382,91.10001013,169160,China,CN,CHN,Xizang
Hami,Hami,42.82698407,93.51500484,218960,China,CN,CHN,Xinjiang Uygur
Hotan,Hotan,37.09971092,79.92694535,187865,China,CN,CHN,Xinjiang Uygur
Kashgar,Kashi,39.47633588,75.9699259,472069.5,China,CN,CHN,Xinjiang Uygur
Yinchuan,Yinchuan,38.46797365,106.2730375,657614,China,CN,CHN,Ningxia Hui
Pingxiang,Pingxiang,27.62000531,113.8500427,666561.5,China,CN,CHN,Jiangxi
Qiqihar,Qiqihar,47.34497703,123.9899922,1261682,China,CN,CHN,Heilongjiang
Shenzhen,Shenzhen,22.55237051,114.1221231,4291796,China,CN,CHN,Guangdong
Zibo,Zibo,36.79998761,118.049993,1865385,China,CN,CHN,Shandong
Lanzhou,Lanzhou,36.05602785,103.7920003,2282609,China,CN,CHN,Gansu
Nanning,Nanning,22.81998822,108.3200443,1485394,China,CN,CHN,Guangxi
Guiyang,Guiyang,26.58004295,106.7200386,2416816.5,China,CN,CHN,Guizhou
Chongqing,Chongqing,29.56497703,106.5949816,5214014,China,CN,CHN,Chongqing
Fuzhou,Fuzhou,26.07999595,119.3000459,1892860,China,CN,CHN,Fujian
Guangzhou,Guangzhou,23.1449813,113.3250101,5990912.5,China,CN,CHN,Guangdong
Dongguan,Dongguan,23.0488889,113.7447222,4528000,China,CN,CHN,Guangdong
Xian,Xian,34.27502545,108.8949963,3617406,China,CN,CHN,Shaanxi
Taiyuan,Taiyuan,37.87501243,112.5450577,2817737.5,China,CN,CHN,Shanxi
Wuhan,Wuhan,30.58003135,114.270017,5713603,China,CN,CHN,Hubei
Changsha,Changsha,28.19996991,112.969993,2338969,China,CN,CHN,Hunan
Kunming,Kunming,25.06998008,102.6799751,1977337,China,CN,CHN,Yunnan
Zhengzhou,Zhengzhou,34.75499615,113.6650927,2325062.5,China,CN,CHN,Henan
Shenyeng,Shenyeng,41.80497927,123.4499735,4149596,China,CN,CHN,Liaoning
Jinan,Jinan,36.67498232,116.9950187,2433633,China,CN,CHN,Shandong
Tianjin,Tianjin,39.13002626,117.2000191,5473103.5,China,CN,CHN,Tianjin
Nanchang,Nanchang,28.67999229,115.8799963,2110675.5,China,CN,CHN,Jiangxi
Nanjing,Nanjing,32.05001914,118.7799743,3383005,China,CN,CHN,Jiangsu
Hangzhou,Hangzhou,30.24997398,120.1700187,2442564.5,China,CN,CHN,Zhejiang
Changchun,Changchun,43.86500856,125.3399873,2860210.5,China,CN,CHN,Jilin
Baotou,Baotou,40.65220725,109.8220198,1229664.5,China,CN,CHN,Nei Mongol
Harbin,Harbin,45.74998395,126.6499849,3425441.5,China,CN,CHN,Heilongjiang
Urumqi,Urumqi,43.80501223,87.57500565,1829612.5,China,CN,CHN,Xinjiang Uygur
Chengdu,Chengdu,30.67000002,104.0700195,4036718.5,China,CN,CHN,Sichuan
Beijing,Beijing,39.92889223,116.3882857,9293300.5,China,CN,CHN,Beijing
Shanghai,Shanghai,31.21645245,121.4365047,14797756,China,CN,CHN,Shanghai
Yopal,Yopal,5.346999095,-72.4059986,61029,Colombia,CO,COL,Casanare
San Andres,San Andres,12.56213711,-81.69032658,58257,Colombia,CO,COL,
Sonson,Sonson,5.716613585,-75.31662785,18024.5,Colombia,CO,COL,Antioquia
Sogamoso,Sogamoso,5.719998392,-72.94000289,120071.5,Colombia,CO,COL,Boyac?
Barrancabermeja,Barrancabermeja,7.089992288,-73.84999903,177802,Colombia,CO,COL,Santander
Girardot,Girardot,4.310006937,-74.80999211,121830.5,Colombia,CO,COL,Cundinamarca
Campoalegre,Campoalegre,2.690002461,-75.33001205,17058.5,Colombia,CO,COL,Huila
Tuquerres,Tuquerres,1.089996764,-77.61994979,27081.5,Colombia,CO,COL,Nari?o
Mocoa,Mocoa,1.149993102,-76.62998438,22035,Colombia,CO,COL,Putumayo
Cartago,Cartago,4.749980081,-75.91002832,123170,Colombia,CO,COL,Valle del Cauca
Soledad,Soledad,10.92001691,-74.76999455,520704,Colombia,CO,COL,Atl?ntico
Sabanalarga,Sabanalarga,10.63998232,-74.91998539,65781,Colombia,CO,COL,Atl?ntico
Arjona,Arjona,10.26003135,-75.34998499,47225,Colombia,CO,COL,Bol?var
Magangue,Magangue,9.229990864,-74.74002222,94912,Colombia,CO,COL,Bol?var
Valledupar,Valledupar,10.47999208,-73.25000981,297627.5,Colombia,CO,COL,Cesar
San Jose del Guaviare,San Jose del Guaviare,2.569983947,-72.63999536,21675,Colombia,CO,COL,Meta
Puerto Lopez,Puerto Lopez,4.089994526,-72.96002751,12163.5,Colombia,CO,COL,Meta
Yarumal,Yarumal,7.030590229,-75.5904871,35315,Colombia,CO,COL,Antioquia
Puerto Berrio,Puerto Berrio,6.480442931,-74.42001591,33194,Colombia,CO,COL,Antioquia
Turbo,Turbo,8.100369892,-76.73997766,42257.5,Colombia,CO,COL,Antioquia
Tunja,Tunja,5.550448017,-73.37002832,139445.5,Colombia,CO,COL,Boyac?
Chiquinquira,Chiquinquira,5.620392068,-73.81994918,49634.5,Colombia,CO,COL,Boyac?
Duitama,Duitama,5.830456766,-73.02004968,96598,Colombia,CO,COL,Boyac?
Ayapel,Ayapel,8.330407531,-75.15002303,23120.5,Colombia,CO,COL,C?rdoba
Lorica,Lorica,9.241850605,-75.81600305,46688,Colombia,CO,COL,C?rdoba
Socorro,Socorro,6.460340799,-73.26998275,21323.5,Colombia,CO,COL,Santander
Riohacha,Riohacha,11.5403408,-72.90997888,112808.5,Colombia,CO,COL,La Guajira
Armenia,Armenia,4.534282653,-75.68112757,314797.5,Colombia,CO,COL,Quind?o
Pereira,Pereira,4.81038983,-75.67999068,504434,Colombia,CO,COL,Risaralda
Honda,Honda,5.190340799,-74.74999577,31813.5,Colombia,CO,COL,Tolima
San Vicente del Caguan,San Vicente del Caguan,2.070376199,-74.64002832,1250,Colombia,CO,COL,Caquet?
Florencia,Florencia,1.610404275,-75.61999435,87599,Colombia,CO,COL,Caquet?
Guapi,Guapi,2.560397968,-77.85998682,13853,Colombia,CO,COL,Cauca
Neiva,Neiva,2.931047179,-75.33024459,318566,Colombia,CO,COL,Huila
Garzon,Garzon,2.210393493,-75.64996668,43027,Colombia,CO,COL,Huila
Ipiales,Ipiales,0.830374368,-77.64999964,93673.5,Colombia,CO,COL,Nari?o
Buenaventura,Buenaventura,3.872402425,-77.05045329,246596,Colombia,CO,COL,Valle del Cauca
Tulua,Tulua,4.090382099,-76.21001001,164281.5,Colombia,CO,COL,Valle del Cauca
El Carmen de Bolivar,El Carmen de Bolivar,9.720374368,-75.12999841,54468.5,Colombia,CO,COL,Bol?var
Jurado,Jurado,7.121747456,-77.75640141,2351,Colombia,CO,COL,Choc?
Nuqui,Nuqui,5.685180092,-77.27454844,1487,Colombia,CO,COL,Choc?
Quibdo,Quibdo,5.690413634,-76.66000838,83942,Colombia,CO,COL,Choc?
El Banco,El Banco,9.000340799,-73.98001693,39628.5,Colombia,CO,COL,Magdalena
Cienaga,Cienaga,11.01039899,-74.25000045,109741,Colombia,CO,COL,Magdalena
Sincelejo,Sincelejo,9.290426452,-75.37995732,239787.5,Colombia,CO,COL,Sucre
Tolu,Tolu,9.535837829,-75.57203862,19719.5,Colombia,CO,COL,Sucre
Arauca,Arauca,7.090664082,-70.76163456,46530.5,Colombia,CO,COL,Arauca
Tame,Tame,6.460340799,-71.74002446,25030,Colombia,CO,COL,Arauca
Pamplona,Pamplona,7.390387389,-72.66001998,52917,Colombia,CO,COL,Norte de Santander
Ocana,Ocana,8.240413024,-73.3500037,83401.5,Colombia,CO,COL,Norte de Santander
Orocue,Orocue,4.794551004,-71.34002303,2126.5,Colombia,CO,COL,Casanare
Obando,Obando,3.854039936,-67.90609827,8181.5,Colombia,CO,COL,Guain?a
San Martin,San Martin,3.690406513,-73.68998295,12304,Colombia,CO,COL,Meta
Puerto Carreno,Puerto Carreno,6.185034606,-67.49302271,8038.5,Colombia,CO,COL,Vichada
Bello,Bello,6.329986998,-75.5699974,456304.5,Colombia,CO,COL,Antioquia
Monteria,Monteria,8.757539082,-75.8900037,273809,Colombia,CO,COL,C?rdoba
Bucaramanga,Bucaramanga,7.1300932,-73.12588302,790410,Colombia,CO,COL,Santander
Ibague,Ibague,4.438913797,-75.2322144,415156,Colombia,CO,COL,Tolima
Popayan,Popayan,2.419993102,-76.61001144,258750,Colombia,CO,COL,Cauca
Santa Marta,Santa Marta,11.24720624,-74.20165715,417211,Colombia,CO,COL,Magdalena
Cucuta,Cucuta,7.920019144,-72.51997685,721772,Colombia,CO,COL,Norte de Santander
Villavicencio,Villavicencio,4.153323994,-73.63499923,348240,Colombia,CO,COL,Meta
Tumaco,Tumaco,1.809978657,-78.80998051,86713,Colombia,CO,COL,Nari?o
Manizales,Manizales,5.059986998,-75.52000045,366831,Colombia,CO,COL,Caldas
Pasto,Pasto,1.21360679,-77.28110742,371138.5,Colombia,CO,COL,Nari?o
Barranquilla,Barranquilla,10.95998863,-74.79996688,1521245.5,Colombia,CO,COL,Atl?ntico
Cartagena,Cartagena,10.39973859,-75.51439356,887000,Colombia,CO,COL,Bol?var
Mitu,Mitu,1.198310566,-70.17360844,5917,Colombia,CO,COL,Vaup?s
Leticia,Leticia,-4.220015036,-69.93997929,46012.5,Colombia,CO,COL,Amazonas
Medellin,Medellin,6.275003274,-75.57501001,2648489.5,Colombia,CO,COL,Antioquia
Cali,Cali,3.399959126,-76.49996647,2216418,Colombia,CO,COL,Valle del Cauca
Bogota,Bogota,4.596423563,-74.08334396,7052830.5,Colombia,CO,COL,Bogota
Moroni,Moroni,-11.7041577,43.2402441,85785,Comoros,KM,COM,
Madingou,Madingou,-4.164002942,13.55400049,22760,Congo (Brazzaville),CG,COG,Bouenza
Kinkala,Kinkala,-4.355999897,14.76199861,13882,Congo (Brazzaville),CG,COG,Pool
Ewo,Ewo,-0.879598776,14.82001501,7786.5,Congo (Brazzaville),CG,COG,Cuvette-Ouest
Impfondo,Impfondo,1.640376606,18.04002519,20859,Congo (Brazzaville),CG,COG,Likouala
Sembe,Sembe,1.640376606,14.58002966,6396,Congo (Brazzaville),CG,COG,Sangha
Moloundou,Moloundou,2.033737609,15.21668331,12244,Congo (Brazzaville),CG,COG,Sangha
Owando,Owando,-0.47962319,15.91999955,29011,Congo (Brazzaville),CG,COG,Cuvette
Makoua,Makoua,-0.009574362,15.64001664,10335,Congo (Brazzaville),CG,COG,Cuvette
Sibiti,Sibiti,-3.689608135,13.35002722,20950,Congo (Brazzaville),CG,COG,L?koumou
Mossendjo,Mossendjo,-2.939628073,12.71998816,24583.5,Congo (Brazzaville),CG,COG,Niari
Loubomo,Loubomo,-4.179604066,12.67001705,97929.5,Congo (Brazzaville),CG,COG,Niari
Gamboma,Gamboma,-1.879486065,15.85002966,20877,Congo (Brazzaville),CG,COG,Plateaux
Djambala,Djambala,-2.539600811,14.74999345,9650.5,Congo (Brazzaville),CG,COG,Plateaux
Ouesso,Ouesso,1.609990864,16.05001745,26117.5,Congo (Brazzaville),CG,COG,Sangha
Kayes,Kayes,-4.180017478,13.28000565,60629,Congo (Brazzaville),CG,COG,Bouenza
Pointe-Noire,Pointe-Noire,-4.770007305,11.88003943,602440.5,Congo (Brazzaville),CG,COG,Kouilou
Brazzaville,Brazzaville,-4.259185772,15.28468949,1259445,Congo (Brazzaville),CG,COG,Pool
Buluko,Buluko,-0.756998889,28.52800254,1192,Congo (Kinshasa),CD,COD,Nord-Kivu
Zongo,Zongo,4.330341613,18.61502885,17667,Congo (Kinshasa),CD,COD,?quateur
Libenge,Libenge,3.660434183,18.61998979,17402,Congo (Kinshasa),CD,COD,?quateur
Bongandanga,Bongandanga,1.510358703,21.05002234,2896,Congo (Kinshasa),CD,COD,?quateur
Ikela,Ikela,-1.182939434,23.26657955,291,Congo (Kinshasa),CD,COD,?quateur
Binga,Binga,2.383406188,20.41998328,64639,Congo (Kinshasa),CD,COD,?quateur
Basankusu,Basankusu,1.233708922,19.80002112,52216,Congo (Kinshasa),CD,COD,?quateur
Boende,Boende,-0.219587383,20.8600081,24679.5,Congo (Kinshasa),CD,COD,?quateur
Gbadolite,Gbadolite,4.290369892,21.01994665,35197,Congo (Kinshasa),CD,COD,?quateur
Businga,Businga,3.340376199,20.86998165,31583,Congo (Kinshasa),CD,COD,?quateur
Bosobolo,Bosobolo,4.190375996,19.88001623,8968.5,Congo (Kinshasa),CD,COD,?quateur
Yangambi,Yangambi,0.77037803,24.43002274,18035.5,Congo (Kinshasa),CD,COD,Orientale
Aketi,Aketi,2.740464497,23.7799849,46881,Congo (Kinshasa),CD,COD,Orientale
Mongbwalu,Mongbwalu,1.9504352,30.0332983,2819,Congo (Kinshasa),CD,COD,Orientale
Bafwasende,Bafwasende,1.083847269,27.26659379,149,Congo (Kinshasa),CD,COD,Orientale
Bunia,Bunia,1.560407327,30.24000403,61537,Congo (Kinshasa),CD,COD,Orientale
Wamba,Wamba,2.140423603,27.98996049,82122,Congo (Kinshasa),CD,COD,Orientale
Basoko,Basoko,1.240426858,23.59002234,22953,Congo (Kinshasa),CD,COD,Orientale
Kenge,Kenge,-4.829590231,16.89993974,241,Congo (Kinshasa),CD,COD,Bandundu
Bolobo,Bolobo,-2.159520651,16.23998002,22605.5,Congo (Kinshasa),CD,COD,Bandundu
Kahemba,Kahemba,-7.282928855,19.00001827,45644.5,Congo (Kinshasa),CD,COD,Bandundu
Bulungu,Bulungu,-4.549607321,18.59999101,42310.5,Congo (Kinshasa),CD,COD,Bandundu
Lusanga,Lusanga,-5.582929261,16.51665564,177,Congo (Kinshasa),CD,COD,Bandundu
Mangai,Mangai,-4.039612611,19.53001176,19946,Congo (Kinshasa),CD,COD,Bandundu
Kasongo-Lunda,Kasongo-Lunda,-6.479618715,16.82996985,18748,Congo (Kinshasa),CD,COD,Bandundu
Mushie,Mushie,-3.01962319,16.92004187,24013.5,Congo (Kinshasa),CD,COD,Bandundu
Dibaya,Dibaya,-6.509539369,22.87001461,603,Congo (Kinshasa),CD,COD,Kasa?-Occidental
Mweka,Mweka,-4.839615459,21.5699906,45222,Congo (Kinshasa),CD,COD,Kasa?-Occidental
Luebo,Luebo,-5.349506817,21.41000036,17682.5,Congo (Kinshasa),CD,COD,Kasa?-Occidental
Demba,Demba,-5.509600404,22.25997432,17008.5,Congo (Kinshasa),CD,COD,Kasa?-Occidental
Ilebo,Ilebo,-4.319595521,20.60999752,71125.5,Congo (Kinshasa),CD,COD,Kasa?-Occidental
Moanda,Moanda,-5.922908509,12.35499752,153915,Congo (Kinshasa),CD,COD,Bas-Congo
Kimpese,Kimpese,-5.549597963,14.43332027,10578,Congo (Kinshasa),CD,COD,Bas-Congo
Kasangulu,Kasangulu,-4.579579652,15.17999304,22645,Congo (Kinshasa),CD,COD,Bas-Congo
Mbanza-Ngungu,Mbanza-Ngungu,-5.249616273,14.86001257,141950.5,Congo (Kinshasa),CD,COD,Bas-Congo
Tshela,Tshela,-4.969581687,12.93000118,19896,Congo (Kinshasa),CD,COD,Bas-Congo
Mwenga,Mwenga,-3.038226706,28.43251745,2216,Congo (Kinshasa),CD,COD,Sud-Kivu
Kampene,Kampene,-3.599536114,26.67004106,19719.5,Congo (Kinshasa),CD,COD,Maniema
Kalima,Kalima,-2.509576804,26.43000403,194,Congo (Kinshasa),CD,COD,Maniema
Lubutu,Lubutu,-0.732889385,26.583328,1313,Congo (Kinshasa),CD,COD,Maniema
Kabinda,Kabinda,-6.129614239,24.47999385,37366,Congo (Kinshasa),CD,COD,Kasa?-Oriental
Lubao,Lubao,-5.389556052,25.74999385,26142.5,Congo (Kinshasa),CD,COD,Kasa?-Oriental
Lusambo,Lusambo,-4.969581687,23.4300321,26803,Congo (Kinshasa),CD,COD,Kasa?-Oriental
Gandajika,Gandajika,-6.739602845,23.96002559,105769.5,Congo (Kinshasa),CD,COD,Kasa?-Oriental
Lodja,Lodja,-3.489620342,23.42000688,68244,Congo (Kinshasa),CD,COD,Kasa?-Oriental
Dilolo,Dilolo,-10.69961953,22.33330318,7854,Congo (Kinshasa),CD,COD,Katanga
Nyunzu,Nyunzu,-5.949573549,28.0166772,15397,Congo (Kinshasa),CD,COD,Katanga
Kasaji,Kasaji,-10.36620319,23.44997921,11969,Congo (Kinshasa),CD,COD,Katanga
Luanza,Luanza,-8.699586569,28.69999467,861,Congo (Kinshasa),CD,COD,Katanga
Moba,Moba,-7.059583314,29.71998409,10006,Congo (Kinshasa),CD,COD,Katanga
Bukama,Bukama,-9.20958128,25.8400142,20900.5,Congo (Kinshasa),CD,COD,Katanga
Kaniama,Kaniama,-7.569629701,24.17003861,32946.5,Congo (Kinshasa),CD,COD,Katanga
Kipushi,Kipushi,-11.75960651,27.25000565,87839.5,Congo (Kinshasa),CD,COD,Katanga
Kambove,Kambove,-10.86958331,26.60001949,18934.5,Congo (Kinshasa),CD,COD,Katanga
Kongolo,Kongolo,-5.379479147,26.9799963,68572.5,Congo (Kinshasa),CD,COD,Katanga
Kabalo,Kabalo,-6.049619121,26.91002641,21851,Congo (Kinshasa),CD,COD,Katanga
Beni,Beni,0.490446797,29.45002641,211275.5,Congo (Kinshasa),CD,COD,Nord-Kivu
Lisala,Lisala,2.140010192,21.50999426,64270,Congo (Kinshasa),CD,COD,?quateur
Gemena,Gemena,3.260019347,19.76999711,157847.5,Congo (Kinshasa),CD,COD,?quateur
Buta,Buta,2.819994526,24.74002966,44195,Congo (Kinshasa),CD,COD,Orientale
Watsa,Watsa,3.040006937,29.52996985,17721.5,Congo (Kinshasa),CD,COD,Orientale
Isiro,Isiro,2.75997235,27.62000891,142136,Congo (Kinshasa),CD,COD,Orientale
Bondo,Bondo,3.809959939,23.67001745,20688.5,Congo (Kinshasa),CD,COD,Orientale
Inongo,Inongo,-1.939999167,18.28001054,30181,Congo (Kinshasa),CD,COD,Bandundu
Tshikapa,Tshikapa,-6.409958884,20.77003943,201256.5,Congo (Kinshasa),CD,COD,Kasa?-Occidental
Boma,Boma,-5.829994284,13.04999385,178638,Congo (Kinshasa),CD,COD,Bas-Congo
Bukavu,Bukavu,-2.509990215,28.8400378,331084,Congo (Kinshasa),CD,COD,Sud-Kivu
Uvira,Uvira,-3.369989401,29.14001949,164353,Congo (Kinshasa),CD,COD,Sud-Kivu
Kindu,Kindu,-2.963915996,25.90998409,199306,Congo (Kinshasa),CD,COD,Maniema
Mwene-Ditu,Mwene-Ditu,-7.000000388,23.44000565,153328.5,Congo (Kinshasa),CD,COD,Kasa?-Oriental
Likasi,Likasi,-10.9700423,26.7800085,428411,Congo (Kinshasa),CD,COD,Katanga
Manono,Manono,-7.300033754,27.44999345,46111,Congo (Kinshasa),CD,COD,Katanga
Kamina,Kamina,-8.730023988,25.00998734,101180,Congo (Kinshasa),CD,COD,Katanga
Mbandaka,Mbandaka,0.040035013,18.26001176,229590.5,Congo (Kinshasa),CD,COD,?quateur
Kisangani,Kisangani,0.520005716,25.22000036,558814,Congo (Kinshasa),CD,COD,Orientale
Bandundu,Bandundu,-3.309993063,17.37996212,107997.5,Congo (Kinshasa),CD,COD,Bandundu
Kananga,Kananga,-5.890042299,22.40001745,614273,Congo (Kinshasa),CD,COD,Kasa?-Occidental
Kasongo,Kasongo,-4.450026836,26.66001583,59059,Congo (Kinshasa),CD,COD,Maniema
Mbuji-Mayi,Mbuji-Mayi,-6.150026429,23.59999589,1084880.5,Congo (Kinshasa),CD,COD,Kasa?-Oriental
Kalemie,Kalemie,-5.933295472,29.20001583,176615.5,Congo (Kinshasa),CD,COD,Katanga
Butembo,Butembo,0.130003681,29.28001094,220512,Congo (Kinshasa),CD,COD,Nord-Kivu
Goma,Goma,-1.678799101,29.2217868,144124,Congo (Kinshasa),CD,COD,Nord-Kivu
Bumba,Bumba,2.189981302,22.45996212,128029.5,Congo (Kinshasa),CD,COD,?quateur
Kikwit,Kikwit,-5.030043112,18.85000159,465973,Congo (Kinshasa),CD,COD,Bandundu
Matadi,Matadi,-5.816610088,13.45002112,212985.5,Congo (Kinshasa),CD,COD,Bas-Congo
Kolwezi,Kolwezi,-10.71672443,25.47243974,418000,Congo (Kinshasa),CD,COD,Katanga
Lubumbashi,Lubumbashi,-11.6800248,27.48001745,1114317,Congo (Kinshasa),CD,COD,Katanga
Kinshasa,Kinshasa,-4.329724102,15.31497188,6704351.5,Congo (Kinshasa),CD,COD,Kinshasa City
Rarotonga,Rarotonga,-21.25003497,-159.7500013,2525,Cook Islands,CK,COK,
Heredia,Heredia,9.991997986,-84.12000251,21947,Costa Rica,CR,CRI,Heredia
Cartago,Cartago,9.86997764,-83.92997807,111770,Costa Rica,CR,CRI,Cartago
Golfito,Golfito,8.650026264,-83.149974,6777,Costa Rica,CR,CRI,Puntarenas
Alajuela,Alajuela,10.02002016,-84.23003727,217618.5,Costa Rica,CR,CRI,Alajuela
Canas,Canas,10.42999514,-85.10001001,15365,Costa Rica,CR,CRI,Guanacaste
Sixaola,Sixaola,9.520386575,-82.61998051,1150,Costa Rica,CR,CRI,Lim?n
Puntarenas,Puntarenas,9.970164098,-84.83358954,46376,Costa Rica,CR,CRI,Puntarenas
Ciudad Cortes,Ciudad Cortes,8.960369079,-83.53000248,3515.5,Costa Rica,CR,CRI,Puntarenas
Quesada,Quesada,10.33049217,-84.43997278,29208,Costa Rica,CR,CRI,Alajuela
Liberia,Liberia,10.63375531,-85.433323,41538,Costa Rica,CR,CRI,Guanacaste
La Cruz,La Cruz,11.07042116,-85.6300035,4297.5,Costa Rica,CR,CRI,Guanacaste
Puerto Limon,Puerto Limon,10.00002138,-83.03334029,74041,Costa Rica,CR,CRI,Lim?n
San Jose,San Jose,9.93501243,-84.08405135,642862,Costa Rica,CR,CRI,San Jos?
Sibenik,Sibenik,43.7272222,15.9058333,37112,Croatia,HR,HRV,?ibensko-Kninska
Karlovac,Karlovac,45.48720929,15.54777421,51593,Croatia,HR,HRV,Karlovacka
Rijeka,Rijeka,45.32998374,14.45001176,156082,Croatia,HR,HRV,Primorsko-Goranska
Slavonski Brod,Slavonski Brod,45.16027834,18.01558223,79230,Croatia,HR,HRV,Brodsko-Posavska
Dubrovnik,Dubrovnik,42.66094769,18.09139156,32711,Croatia,HR,HRV,Dubrovacko-Neretvanska
Split,Split,43.52040428,16.46999182,195527.5,Croatia,HR,HRV,Splitsko-Dalmatinska
Zadar,Zadar,44.12013511,15.26226192,59201.5,Croatia,HR,HRV,Zadarska
Pula,Pula,44.86871991,13.84808467,60338.5,Croatia,HR,HRV,Istarska
Osijek,Osijek,45.55038373,18.6800378,91608.5,Croatia,HR,HRV,Osjecko-Baranjska
Zagreb,Zagreb,45.80000673,15.99999467,710746,Croatia,HR,HRV,Grad Zagreb
Ciego de Avila,Ciego de Avila,21.83999636,-78.76194727,122343.5,Cuba,CU,CUB,Ciego de ?vila
Palma Soriano,Palma Soriano,20.21722719,-75.99880843,85110,Cuba,CU,CUB,Santiago de Cuba
San Antonio de los Banos,San Antonio de los Banos,22.89112083,-82.4990835,37676,Cuba,CU,CUB,La Habana
Guines,Guines,22.8361371,-82.02802698,57445,Cuba,CU,CUB,La Habana
Caibarien,Caibarien,22.5157949,-79.47223983,25431,Cuba,CU,CUB,Villa Clara
Placetas,Placetas,22.31580711,-79.65548446,34973,Cuba,CU,CUB,Villa Clara
Cienfuegos,Cienfuegos,22.14444806,-80.44029444,146549.5,Cuba,CU,CUB,Cienfuegos
Nueva Gerona,Nueva Gerona,21.88371462,-82.79999536,22915,Cuba,CU,CUB,Isla de la Juventud
Sancti Spiritus,Sancti Spiritus,21.93014589,-79.44250004,101710.5,Cuba,CU,CUB,Sancti Sp?ritus
Moron,Moron,22.10985069,-78.62748519,57551.5,Cuba,CU,CUB,Ciego de ?vila
Nuevitas,Nuevitas,21.5456474,-77.26444177,46796,Cuba,CU,CUB,Camag?ey
Manzanillo,Manzanillo,20.34375694,-77.11664718,107433,Cuba,CU,CUB,Granma
Bayamo,Bayamo,20.37954287,-76.64329106,177623,Cuba,CU,CUB,Granma
Banes,Banes,20.96291811,-75.71859298,47745.5,Cuba,CU,CUB,Holgu?n
Las Tunas,Las Tunas,20.96012758,-76.95438318,179898,Cuba,CU,CUB,Las Tunas
Artemisa,Artemisa,22.81339947,-82.76188399,46024.5,Cuba,CU,CUB,La Habana
Matanzas,Matanzas,23.04152508,-81.577486,135303,Cuba,CU,CUB,Matanzas
Colon,Colon,22.71958091,-80.90579574,40677,Cuba,CU,CUB,Matanzas
Sagua la Grande,Sagua la Grande,22.80903282,-80.07109216,40752.5,Cuba,CU,CUB,Villa Clara
Pinar del Rio,Pinar del Rio,22.41750633,-83.69808008,173304,Cuba,CU,CUB,Pinar del R?o
Camaguey,Camaguey,21.38082542,-77.91693425,321583.5,Cuba,CU,CUB,Camag?ey
Guantanamo,Guantanamo,20.1452936,-75.20614364,245069.5,Cuba,CU,CUB,Guant?namo
Holguin,Holguin,20.88723798,-76.26305587,309639.5,Cuba,CU,CUB,Holgu?n
Santa Clara,Santa Clara,22.40001385,-79.9666541,234900,Cuba,CU,CUB,Villa Clara
Santiago de Cuba,Santiago de Cuba,20.0250167,-75.82132573,500964,Cuba,CU,CUB,Santiago de Cuba
Havana,Havana,23.13195884,-82.36418217,2082458.5,Cuba,CU,CUB,Ciudad de la Habana
Willemstad,Willemstad,12.20042971,-69.01998377,146813,Curacao,CW,CUW,
Larnaka,Larnaka,34.9170031,33.63599757,48947,Cyprus,CY,CYP,Larnaca
Paphos,Paphos,34.75591516,32.42245666,35961,Cyprus,CY,CYP,Paphos
Lemosos,Lemosos,34.67541445,33.0333219,149486,Cyprus,CY,CYP,Limassol
Nicosia,Nicosia,35.16667645,33.36663489,212376,Cyprus,CY,CYP,
Usti Nad Labem,Usti Nad Labem,50.66299816,14.08100455,94105,Czech Republic,CZ,CZE,Libereck?
Hradec Kralove,Hradec Kralove,50.20599617,15.81200153,95195,Czech Republic,CZ,CZE,Kr?lov?hradeck?
Ceske Budejovice,Ceske Budejovice,48.98001935,14.46003699,97452,Czech Republic,CZ,CZE,Jihocesk?
Liberec,Liberec,50.79995994,15.07999914,99972.5,Czech Republic,CZ,CZE,Libereck?
Olomouc,Olomouc,49.63003135,17.24999589,97829,Czech Republic,CZ,CZE,Moravskoslezsk?
Pizen,Pizen,49.74043805,13.36000077,161043,Czech Republic,CZ,CZE,Karlovarsk?
Jihlava,Jihlava,49.40038129,15.58332759,52010.5,Czech Republic,CZ,CZE,Kraj Vysocina
Zlin,Zlin,49.2304175,17.65002315,101893.5,Czech Republic,CZ,CZE,Kraj Vysocina
Brno,Brno,49.20039349,16.60998328,378918,Czech Republic,CZ,CZE,Kraj Vysocina
Pardubice,Pardubice,50.04041974,15.76000932,97902.5,Czech Republic,CZ,CZE,Kr?lov?hradeck?
Ostrava,Ostrava,49.83035504,18.24998653,396025.5,Czech Republic,CZ,CZE,Moravskoslezsk?
Prague,Prague,50.08333701,14.46597978,582043.5,Czech Republic,CZ,CZE,Prague
Vejle,Vejle,55.70900103,9.534996498,51177,Denmark,DK,DNK,Syddanmark
Hillerod,Hillerod,55.93329907,12.31669854,28313,Denmark,DK,DNK,Hovedstaden
Soro,Soro,55.43299811,11.5667016,7167,Denmark,DK,DNK,Sja?lland
Viborg,Viborg,56.43333701,9.399984089,32944,Denmark,DK,DNK,Midtjylland
Roskilde,Roskilde,55.64997398,12.08333451,42284.5,Denmark,DK,DNK,Sja?lland
Svendborg,Svendborg,55.07042279,10.61665401,28366.5,Denmark,DK,DNK,Syddanmark
Odense,Odense,55.40037681,10.38333492,152076.5,Denmark,DK,DNK,Syddanmark
Esbjerg,Esbjerg,55.46703941,8.450016234,68076,Denmark,DK,DNK,Syddanmark
Frederikshavn,Frederikshavn,57.43368939,10.53329993,22385,Denmark,DK,DNK,Nordjylland
Aalborg,Aalborg,57.03371381,9.916593382,111917.5,Denmark,DK,DNK,Nordjylland
?rhus,Aarhus,56.157204,10.21068396,232325.5,Denmark,DK,DNK,Midtjylland
K?benhavn,Kobenhavn,55.67856419,12.56348575,1085000,Denmark,DK,DNK,Hovedstaden
Dikhil,Dikhil,11.10400201,42.37200058,12043,Djibouti,DJ,DJI,Dikhil
Tadjoura,Tadjoura,11.78330399,42.9000035,22193,Djibouti,DJ,DJI,Tadjourah
Ali Sabih,Ali Sabih,11.15622988,42.71252437,32165.5,Djibouti,DJ,DJI,Ali Sabieh
Obock,Obock,11.97344098,43.28556433,13142,Djibouti,DJ,DJI,Obock
Djibouti,Djibouti,11.59501446,43.14800167,763506.5,Djibouti,DJ,DJI,Djibouti
Roseau,Roseau,15.30101564,-61.38701298,19953.5,Dominica,DM,DMA,Saint George
Sabaneta,Sabaneta,19.50499807,-71.34498854,16380,Dominican Republic,DO,DOM,Santiago Rodr?guez
Mao,Mao,19.55199609,-71.07499748,48297,Dominican Republic,DO,DOM,Valverde
Cotui,Cotui,19.05900306,-70.1520026,41641,Dominican Republic,DO,DOM,S?nchez Ram?rez
Puerto Plata,Puerto Plata,19.7902171,-70.69024747,119897,Dominican Republic,DO,DOM,Puerto Plata
Dajabon,Dajabon,19.548,-71.70499757,16398,Dominican Republic,DO,DOM,Dajab?n
Moca,Moca,19.39699814,-70.52300059,61834,Dominican Republic,DO,DOM,Espaillat
Salcedo,Salcedo,19.38300302,-70.4167015,45299,Dominican Republic,DO,DOM,Hermanas
Jimani,Jimani,18.49300212,-71.85099553,6567,Dominican Republic,DO,DOM,Independencia
Comendador,Elias Pina,18.875997,-71.70699546,35901,Dominican Republic,DO,DOM,Elias Pina
Pedernales,Pedernales,18.03799801,-71.74099755,11072,Dominican Republic,DO,DOM,Pedernales
Azua,Azua,18.45399613,-70.7290016,59139,Dominican Republic,DO,DOM,Azua
Bonao,Bonao,18.94200314,-70.40899757,73269,Dominican Republic,DO,DOM,Monse?or Nouel
Bani,Bani,18.279999,-70.33100347,66709,Dominican Republic,DO,DOM,Peravia
Hato Mayor,Hato Mayor,18.76400114,-69.25699747,35999,Dominican Republic,DO,DOM,Hato Mayor
Monte Plata,Monte Plata,18.80700306,-69.78400153,15532,Dominican Republic,DO,DOM,Monte Plata
Nagua,Nagua,19.37600108,-69.84700149,33862,Dominican Republic,DO,DOM,Mar?a Trinidad S?nchez
Samana,Samana,19.21200313,-69.3320036,11432,Dominican Republic,DO,DOM,Saman?
San Cristobal,San Cristobal,18.4159981,-70.10900052,154040,Dominican Republic,DO,DOM,San Crist?bal
El Seibo,El Seibo,18.76400114,-69.03500346,23547,Dominican Republic,DO,DOM,El Seybo
Higuey,Higuey,18.61599603,-68.70799749,123787,Dominican Republic,DO,DOM,La Altagracia
Neiba,Neiba,18.46661053,-71.41663334,22200.5,Dominican Republic,DO,DOM,Bahoruco
La Vega,La Vega,19.2165906,-70.51658492,132811.5,Dominican Republic,DO,DOM,La Vega
San Francisco de Macoris,San Francisco de Macoris,19.29999636,-70.25001205,138650.5,Dominican Republic,DO,DOM,Duarte
San Pedro de Macoris,San Pedro de Macoris,18.4503583,-69.29996668,211019.5,Dominican Republic,DO,DOM,San Pedro de Macor?s
Monte Cristi,Monte Cristi,19.86699017,-71.65002995,16852.5,Dominican Republic,DO,DOM,Monte Cristi
Barahona,Barahona,18.20037355,-71.099986,83644,Dominican Republic,DO,DOM,Barahona
Bavaro,Bavaro,18.71700869,-68.44996688,795,Dominican Republic,DO,DOM,La Altagracia
La Romana,La Romana,18.41700116,-68.96660201,202471.5,Dominican Republic,DO,DOM,La Romana
San Juan,San Juan,18.80700306,-71.22899657,72950,Dominican Republic,DO,DOM,San Juan
Santiago,Santiago,19.50000999,-70.67001225,1471007.5,Dominican Republic,DO,DOM,Santiago
Santo Domingo,Santo Domingo,18.47007285,-69.90008508,1078436.5,Dominican Republic,DO,DOM,Distrito Nacional
Dili,Dili,-8.559388409,125.5794559,213947,East Timor,TL,TLS,Dili
Puyo,Puyo,-1.483002014,-77.98699756,24881,Ecuador,EC,ECU,Pastaza
Tulcan,Tulcan,0.821997038,-77.73200048,83000,Ecuador,EC,ECU,Carchi
Pinas,Pinas,-3.670022767,-79.64998092,16981,Ecuador,EC,ECU,El Oro
Puerto Villamil,Puerto Villamil,-0.933342266,-91.01665145,2000,Ecuador,EC,ECU,Gal?pagos
Puerto Baquerizo Moreno,Puerto Baquerizo Moreno,-0.900010967,-89.5999679,5122,Ecuador,EC,ECU,Gal?pagos
Guaranda,Guaranda,-1.60999347,-79.01001998,23933,Ecuador,EC,ECU,Bolivar
Azogues,Azogues,-2.740002015,-78.84003036,51982,Ecuador,EC,ECU,Ca?ar
Salinas,Salinas,-2.200034974,-80.98000309,24616.5,Ecuador,EC,ECU,Guayas
Alausi,Alausi,-2.18995807,-78.84997807,14294,Ecuador,EC,ECU,Chimborazo
Sangolqui,Sangolqui,-0.31002114,-78.4599502,91848,Ecuador,EC,ECU,Pichincha
Muisne,Muisne,0.609974384,-80.02001001,8252.5,Ecuador,EC,ECU,Esmeraldas
San Gabriel,San Gabriel,0.609974384,-77.84003972,15589,Ecuador,EC,ECU,Carchi
Macara,Macara,-4.379591859,-79.94998845,11748,Ecuador,EC,ECU,Loja
Zamora,Zamora,-4.069584942,-78.96999658,11581.5,Ecuador,EC,ECU,Zamora Chinchipe
Latacunga,Latacunga,-0.929569886,-78.60996688,73344.5,Ecuador,EC,ECU,Cotopaxi
Milagro,Milagro,-2.179622784,-79.59998397,55433.5,Ecuador,EC,ECU,Guayas
Babahoyo,Babahoyo,-1.7995943,-79.54001347,59873,Ecuador,EC,ECU,Los Rios
Chone,Chone,-0.689584535,-80.09000574,40379,Ecuador,EC,ECU,Manabi
Jipijapa,Jipijapa,-1.349595928,-80.58000167,28741,Ecuador,EC,ECU,Manabi
Yaupi,Yaupi,-2.854310284,-77.93633875,293,Ecuador,EC,ECU,Morona Santiago
Macas,Macas,-2.309589011,-78.11999679,20644,Ecuador,EC,ECU,Morona Santiago
Cayambe,Cayambe,0.050370299,-78.15999435,27231.5,Ecuador,EC,ECU,Pichincha
Ambato,Ambato,-1.269600811,-78.61999211,217897,Ecuador,EC,ECU,Napo
Tena,Tena,-0.979592673,-77.80998987,24149,Ecuador,EC,ECU,Tungurahua
Valdez,Valdez,1.267103808,-78.98549846,6985.5,Ecuador,EC,ECU,Esmeraldas
San Lorenzo,San Lorenzo,1.270399189,-78.86005497,20209,Ecuador,EC,ECU,Esmeraldas
Esmeraldas,Esmeraldas,0.930419941,-79.6699797,134365.5,Ecuador,EC,ECU,Esmeraldas
Ibarra,Ibarra,0.360377216,-78.12999618,127703.5,Ecuador,EC,ECU,Imbabura
Portoviejo,Portoviejo,-1.060001201,-80.45998316,191963.5,Ecuador,EC,ECU,Manabi
Machala,Machala,-3.260021953,-79.95998784,205578.5,Ecuador,EC,ECU,El Oro
Loja,Loja,-3.990003236,-79.21000777,122082,Ecuador,EC,ECU,Loja
Manta,Manta,-0.980006084,-80.72996668,176941,Ecuador,EC,ECU,Manabi
Riobamba,Riobamba,-1.670041485,-78.65004195,148471,Ecuador,EC,ECU,Chimborazo
Cuenca,Cuenca,-2.89999225,-78.99999475,281921,Ecuador,EC,ECU,Azuay
Santa Cruz,Santa Cruz,-0.533315004,-90.34999964,8147.5,Ecuador,EC,ECU,Gal?pagos
Quito,Quito,-0.214988181,-78.50005111,1550407,Ecuador,EC,ECU,Pichincha
Guayaquil,Guayaquil,-2.220033754,-79.92004195,2233014.5,Ecuador,EC,ECU,Guayas
Shibin el Kom,Shibin el Kom,30.59199913,30.89999749,182900,Egypt,EG,EGY,Al Minufiyah
Benha,Benha,30.46666512,31.18333563,167029,Egypt,EG,EGY,Al Qalyubiyah
Zagazig,Zagazig,30.58333209,31.5166596,285097,Egypt,EG,EGY,Ash Sharqiyah
Kafr el Sheikh,Kafr el Sheikh,31.109004,30.93599763,143970,Egypt,EG,EGY,Kafr ash Shaykh
Tanta,Tanta,30.79043194,31.00000932,404901,Egypt,EG,EGY,Al Gharbiyah
Ismailia,Ismailia,30.5903408,32.25998409,470474,Egypt,EG,EGY,Al Isma`iliyah
El Mansura,El Mansura,31.05044191,31.3800378,540247,Egypt,EG,EGY,Ad Daqahliyah
Dumyat,Dumyat,31.42039349,31.82001094,188149,Egypt,EG,EGY,Dumyat
Matruh,Matruh,31.3504236,27.23000688,82756,Egypt,EG,EGY,Matruh
El Alamein,El Alamein,30.81707115,28.94995357,4938,Egypt,EG,EGY,Matruh
El Daba,El Daba,31.03377626,28.4332926,14212,Egypt,EG,EGY,Matruh
Salum,Salum,31.56697369,25.15003048,7330,Egypt,EG,EGY,Matruh
Damanh?r,Damanhur,31.05044191,30.47001583,371350,Egypt,EG,EGY,Al Buhayrah
Samalut,Samalut,28.30042889,30.71000118,121281,Egypt,EG,EGY,Al Minya
Mallawi,Mallawi,27.73041201,30.83996741,179934.5,Egypt,EG,EGY,Al Minya
Beni Mazar,Beni Mazar,28.49039146,30.80999508,68853,Egypt,EG,EGY,Al Minya
Beni Suef,Beni Suef,29.08038129,31.09002966,339537,Egypt,EG,EGY,Bani Suwayf
Rashid,Rashid,31.46039105,30.39002071,128970.5,Egypt,EG,EGY,Kafr ash Shaykh
Qasr Farafra,Qasr Farafra,27.067145,27.96655106,5000,Egypt,EG,EGY,Al Wadi at Jadid
El Qasr,El Qasr,25.70043256,28.88329097,1716,Egypt,EG,EGY,Al Wadi at Jadid
Isna,Isna,25.2904059,32.54994055,84667.5,Egypt,EG,EGY,Qina
Qena,Qena,26.15045677,32.72000769,268694.5,Egypt,EG,EGY,Qina
Girga,Girga,26.33036826,31.88000728,115475.5,Egypt,EG,EGY,Suhaj
Sohag,Sohag,26.55040651,31.70001827,404709.5,Egypt,EG,EGY,Suhaj
Berenice,Berenice,23.94599184,35.48418005,10,Egypt,EG,EGY,Al Bahr al Ahmar
Bur Safaga,Bur Safaga,26.73372866,33.93331864,21035.5,Egypt,EG,EGY,Al Bahr al Ahmar
El Tur,El Tur,28.239389,33.61479726,21300,Egypt,EG,EGY,Janub Sina'
El Arish,El Arish,31.12488181,33.80056189,153753,Egypt,EG,EGY,Shamal Sina'
El Giza,El Giza,30.00998863,31.19002356,2681863,Egypt,EG,EGY,Al Jizah
Siwa,Siwa,29.20001223,25.51667476,23080,Egypt,EG,EGY,Matruh
El Minya,El Minya,28.09000246,30.74999874,363575,Egypt,EG,EGY,Al Minya
Kom Ombo,Kom Ombo,24.46999086,32.95001949,181874.5,Egypt,EG,EGY,Aswan
El Kharga,El Kharga,25.44000917,30.55001094,49991,Egypt,EG,EGY,Al Wadi at Jadid
Hurghada,Hurghada,27.23000327,33.83001745,157204,Egypt,EG,EGY,Al Bahr al Ahmar
Suez,Suez,30.00497601,32.54994055,498230,Egypt,EG,EGY,As Suways
Bur Said,Bur Said,31.25998985,32.2900081,561932,Egypt,EG,EGY,Bur Sa`id
El Faiyum,El Faiyum,29.31003135,30.83996741,311582.5,Egypt,EG,EGY,Al Fayyum
Aswan,Aswan,24.08750775,32.8989115,277351.5,Egypt,EG,EGY,Aswan
Asyut,Asyut,27.18997988,31.17994665,420585,Egypt,EG,EGY,Asyut
Luxor,Luxor,25.70001914,32.6500378,548572,Egypt,EG,EGY,Qina
Alexandria,Alexandria,31.20001935,29.94999589,3988258,Egypt,EG,EGY,Al Iskandariyah
Cairo,Cairo,30.04996035,31.24996822,9813807,Egypt,EG,EGY,Al Qahirah
Ahuachapan,Ahuachapan,13.91900399,-89.84500155,34102,El Salvador,SV,SLV,Ahuachap?n
Cojutepeque,Cojutepeque,13.71670204,-88.9333016,48411,El Salvador,SV,SLV,Cuscatl?n
Nueva San Salvador,Nueva San Salvador,13.67399699,-89.28999848,124694,El Salvador,SV,SLV,La Libertad
Zacatecoluca,Zacatecoluca,13.508001,-88.86799761,39613,El Salvador,SV,SLV,La Paz
La Union,La Union,13.33199704,-87.83900052,26807,El Salvador,SV,SLV,La Uni?n
San Francisco Gotera,San Francisco Gotera,13.69999812,-88.10000052,16152,El Salvador,SV,SLV,Moraz?n
San Vicente,San Vicente,13.64100303,-88.78499961,37326,El Salvador,SV,SLV,San Vicente
Usulutan,Usulutan,13.3460011,-88.43200162,51910,El Salvador,SV,SLV,Usulut?n
Chalatenango,Chalatenango,14.07200406,-89.09399649,29271,El Salvador,SV,SLV,Chalatenango
Sensuntepeque,Sensuntepeque,13.88004295,-88.63000126,23687.5,El Salvador,SV,SLV,Caba?as
Sonsonate,Sonsonate,13.7199752,-89.7299858,139724,El Salvador,SV,SLV,Sonsonate
San Miguel,San Miguel,13.48334881,-88.18333602,181721.5,El Salvador,SV,SLV,San Miguel
Santa Ana,Santa Ana,13.9946096,-89.55976363,205569.5,El Salvador,SV,SLV,Santa Ana
San Salvador,San Salvador,13.71000165,-89.20304122,717903.5,El Salvador,SV,SLV,San Salvador
Evinayong,Evinayong,1.449999085,10.56670255,8462,Equatorial Guinea,GQ,GNQ,Centro Sur
Luba,Luba,3.449997026,8.550000525,8655,Equatorial Guinea,GQ,GNQ,Bioko Sur
Calatrava,Calatrava,1.116403421,9.418587604,628,Equatorial Guinea,GQ,GNQ,Litoral
Mongomo,Mongomo,1.633684508,11.31655961,6476.5,Equatorial Guinea,GQ,GNQ,Wele-Nz?s
Bata,Bata,1.870000833,9.769987344,135943.5,Equatorial Guinea,GQ,GNQ,Litoral
Malabo,Malabo,3.750015278,8.783277546,155963,Equatorial Guinea,GQ,GNQ,Bioko Norte
Tessenei,Tessenei,15.11038129,36.65749345,9504,Eritrea,ER,ERI,Gash Barka
Agordat,Agordat,15.54903668,37.88666907,18728.5,Eritrea,ER,ERI,Gash Barka
Massawa,Massawa,15.61011822,39.45003617,142564,Eritrea,ER,ERI,Debub
Keren,Keren,15.68039817,38.44999385,148241.5,Eritrea,ER,ERI,Semenawi Keyih Bahri
Mendefera,Adi Ugri,14.88597638,38.81632808,137585.5,Eritrea,ER,ERI,Maekel
Assab,Assab,13.01001853,42.72999101,105496,Eritrea,ER,ERI,Debubawi Keyih Bahri
Asmara,Asmara,15.33333925,38.93332353,592366,Eritrea,ER,ERI,Anseba
Haapsalu,Haapsalu,58.9430556,23.5413889,11805,Estonia,EE,EST,L??ne
Viljandi,Viljandi,58.3638889,25.59,20309,Estonia,EE,EST,Viljandi
Kohtla-Jarve,Kohtla-Jarve,59.39997764,27.28333695,31038,Estonia,EE,EST,Ida-Viru
Narva,Narva,59.37762758,28.16028601,65707,Estonia,EE,EST,Ida-Viru
Tartu,Tartu,58.38394147,26.70988358,90033.5,Estonia,EE,EST,Tartu
Parnu,Parnu,58.37474306,24.51358354,40256,Estonia,EE,EST,P?rnu
Tallinn,Tallinn,59.43387738,24.72804073,367025.5,Estonia,EE,EST,Harju
Awasa,Awasa,7.059996077,38.47699862,133097,Ethiopia,ET,ETH,"Southern Nations, Nationalities and Peoples"
Gore,Gore,8.148996048,35.53700451,9352,Ethiopia,ET,ETH,Addis Ababa
Debre Birhan,Debre Birhan,9.68037681,39.53003129,61509,Ethiopia,ET,ETH,Amhara
Bati,Bati,11.18374758,40.0165649,12826.5,Ethiopia,ET,ETH,Amhara
Adigrat,Adigrat,14.28043194,39.46998328,104021,Ethiopia,ET,ETH,Tigray
Aksum,Aksum,14.13041526,38.72000321,44368,Ethiopia,ET,ETH,Tigray
Yirga Alem,Yirga Alem,6.750426452,38.4099963,36292,Ethiopia,ET,ETH,"Southern Nations, Nationalities and Peoples"
Hosaina,Hosaina,7.550377623,37.85003048,89300,Ethiopia,ET,ETH,"Southern Nations, Nationalities and Peoples"
Dila,Dila,6.410421365,38.3100024,47021,Ethiopia,ET,ETH,"Southern Nations, Nationalities and Peoples"
Giyon,Giyon,8.530421162,37.97002315,76464,Ethiopia,ET,ETH,Addis Ababa
Hagere Hiywet,Hagere Hiywet,8.980393696,37.85003048,39412.5,Ethiopia,ET,ETH,Addis Ababa
Nekemte,Nekemte,9.090464497,36.53000769,73018,Ethiopia,ET,ETH,Addis Ababa
Asela,Asela,7.950404886,39.1399259,82240,Ethiopia,ET,ETH,Addis Ababa
Shashemene,Shashemene,7.200398986,38.59003699,100110.5,Ethiopia,ET,ETH,Addis Ababa
Dembi Dolo,Dembi Dolo,8.533728454,34.79998409,27264,Ethiopia,ET,ETH,Addis Ababa
Gimbi,Gimbi,9.167023131,35.83330603,22423.5,Ethiopia,ET,ETH,Addis Ababa
Asosa,Asosa,10.06699404,34.5333337,24192,Ethiopia,ET,ETH,Benshangul-Gumaz
Jijiga,Jijiga,9.350422789,42.78998734,52507.5,Ethiopia,ET,ETH,Somali
Debre Markos,Debre Markos,10.33997479,37.72001257,65339,Ethiopia,ET,ETH,Amhara
Dese,Dese,11.12997825,39.63002519,159929,Ethiopia,ET,ETH,Amhara
Sodo,Sodo,6.900003885,37.7499849,65737,Ethiopia,ET,ETH,"Southern Nations, Nationalities and Peoples"
Arba Minch,Arba Minch,6.040004699,37.54999711,54343.5,Ethiopia,ET,ETH,"Southern Nations, Nationalities and Peoples"
Harar,Harar,9.319959533,42.15002641,161150,Ethiopia,ET,ETH,Harari
Goba,Goba,7.010023009,39.97000443,33197,Ethiopia,ET,ETH,Addis Ababa
Jima,Jima,7.679982116,36.83004106,128306,Ethiopia,ET,ETH,Addis Ababa
Nazret,Nazret,8.549980691,39.26999548,345443.5,Ethiopia,ET,ETH,Addis Ababa
Nagele,Nagele,5.316612161,39.58330969,11772,Ethiopia,ET,ETH,Addis Ababa
Gode,Gode,5.950010192,43.44999874,71671,Ethiopia,ET,ETH,Somali
Dolo Bay,Dolo Bay,4.183348001,42.08331213,11810,Ethiopia,ET,ETH,Somali
Bahir Dar,Bahir Dar,11.60005292,37.38328894,187823.5,Ethiopia,ET,ETH,Amhara
Mekele,Mekele,13.49998863,39.46998328,95856,Ethiopia,ET,ETH,Tigray
Dire Dawa,Dire Dawa,9.58999473,41.86001827,250325.5,Ethiopia,ET,ETH,Dire Dawa
Gonder,Gonder,12.61004295,37.46002844,155072,Ethiopia,ET,ETH,Amhara
Addis Ababa,Addis Ababa,9.033310363,38.70000443,2928864.5,Ethiopia,ET,ETH,Addis Ababa
Fox Bay,Fox Bay,-51.95058999,-60.08696314,90,Falkland Islands,FK,FLK,
Stanley,Stanley,-51.70001097,-57.8499679,2213,Falkland Islands,FK,FLK,
Klaksvik,Klaksvik,62.2374783,-6.53901149,4664,Faroe Islands,FO,FRO,Eysturoyar
T?rshavn,Torshavn,62.03002382,-6.820033611,14398,Faroe Islands,FO,FRO,Eysturoyar
Palikir,Palikir,6.916643696,158.1499743,4645,Federated States of Micronesia,FM,FSM,
Nandi,Nandi,-17.79959959,177.4166019,27329,Fiji,FJ,FJI,Western
Lautoka,Lautoka,-17.61609658,177.4666247,55894,Fiji,FJ,FJI,Western
Labasa,Labasa,-16.41658323,179.3833036,24187,Fiji,FJ,FJI,Western
Suva,Suva,-18.13301593,178.4417073,131835,Fiji,FJ,FJI,Central
Hameenlinna,Hameenlinna,60.99699611,24.47199954,47261,Finland,FI,FIN,Tavastia Proper
Kouvola,Kouvola,60.87600009,26.70900351,31133,Finland,FI,FIN,Southern Finland
Mikkeli,Mikkeli,61.68999617,27.28500348,46550,Finland,FI,FIN,Southern Savonia
Savonlinna,Savonlinna,61.86662294,28.88334265,20233.5,Finland,FI,FIN,Southern Savonia
Pori,Pori,61.47889467,21.77493933,71526,Finland,FI,FIN,Satakunta
Sodankyl?,Sodankyla,67.41705935,26.60001949,6516.5,Finland,FI,FIN,Lapland
Jyv?skyl?,Jyvaskyla,62.26034568,25.74999385,91581,Finland,FI,FIN,Central Finland
Kuopio,Kuopio,62.89428632,27.69493974,90502,Finland,FI,FIN,Eastern Finland
Lappeenranta,Lappeenranta,61.06705935,28.1833337,54516.5,Finland,FI,FIN,South Karelia
Porvoo,Porvoo,60.40035585,25.66601965,12242,Finland,FI,FIN,Eastern Uusimaa
Kemijarvi,Kemijarvi,66.66666587,27.41666215,8883,Finland,FI,FIN,Lapland
Kokkola,Kokkola,63.83329877,23.11666622,46714,Finland,FI,FIN,Western Finland
Lahti,Lahti,60.99385968,25.66493445,97508,Finland,FI,FIN,P?ij?nne Tavastia
Joensuu,Joensuu,62.59998903,29.76664791,53388,Finland,FI,FIN,North Karelia
Turku,Turku,60.4538668,22.25496171,175442.5,Finland,FI,FIN,Finland Proper
Kemi,Kemi,65.73331199,24.58169307,17060,Finland,FI,FIN,Lapland
Oulu,Oulu,64.99999758,25.47001094,132685,Finland,FI,FIN,Northern Ostrobothnia
Rovaniemi,Rovaniemi,66.50003522,25.71593909,30085,Finland,FI,FIN,Lapland
Vaasa,Vaasa,63.09998435,21.60001461,48930,Finland,FI,FIN,Western Finland
Tampere,Tampere,61.5000045,23.75001257,230983,Finland,FI,FIN,Pirkanmaa
Helsinki,Helsinki,60.17556337,24.93412634,836728.5,Finland,FI,FIN,Southern Finland
Annecy,Annecy,45.89997479,6.116670287,77490.5,France,FR,FRA,Rh?ne-Alpes
Roanne,Roanne,46.03332583,4.066666218,56577.5,France,FR,FRA,Rh?ne-Alpes
Roura,Roura,4.729981302,-52.33002059,2069.5,France,GF,FRA,Guinaa
Sinnamary,Sinnamary,5.380019144,-52.95998214,2781.5,France,GF,FRA,Guinaa
St.-Brieuc,St.-Brieuc,48.51666262,-2.783303265,52998.5,France,FR,FRA,Bretagne
Poitier,Poitier,46.58329226,0.333276529,85383.5,France,FR,FRA,Poitou-Charentes
Angers,Angers,47.48000755,-0.530029949,178329.5,France,FR,FRA,Pays de la Loire
Biarritz,Biarritz,43.47327537,-1.561594891,89268,France,FR,FRA,Aquitaine
Aix-en-Provence,Aix-en-Provence,43.51999086,5.449992634,145309,France,FR,FRA,Provence-Alpes-C?te-d'Azur
Perpignan,Perpignan,42.69998924,2.899967406,128663,France,FR,FRA,Languedoc-Roussillon
Tarbes,Tarbes,43.23329002,0.083343464,53480,France,FR,FRA,Midi-Pyr?n?es
Clermont-Ferrand,Clermont-Ferrand,45.77998212,3.080008096,185865.5,France,FR,FRA,Auvergne
Melun,Melun,48.53330243,2.666648314,144192.5,France,FR,FRA,?le-de-France
Arras,Arras,50.28332481,2.783333698,55608.5,France,FR,FRA,Nord-Pas-de-Calais
Besancon,Besancon,47.22999697,6.03000891,124193,France,FR,FRA,Franche-Comt?
Saint-Georges,Saint-Georges,3.9104706,-51.81000065,1558,France,GF,FRA,Amap?
Saint-Etienne,Saint-Etienne,45.43039105,4.380032103,220982,France,FR,FRA,Rh?ne-Alpes
Grenoble,Grenoble,45.18038047,5.720001992,273563,France,FR,FRA,Rh?ne-Alpes
Fort-de-France,Fort-de-France,14.6104118,-61.08002914,172622,France,MQ,FRA,Martinique
Saint-Laurent-du-Maroni,Saint-Laurent-du-Maroni,5.497624081,-54.03253459,20850.5,France,GF,FRA,Guinaa
Iracoubo,Iracoubo,5.480426452,-53.21999211,881,France,GF,FRA,Guinaa
Cherbourg,Cherbourg,49.65039187,-1.649987428,60991,France,FR,FRA,Basse-Normandie
Caen,Caen,49.18375368,-0.349989259,150361.5,France,FR,FRA,Basse-Normandie
Lorient,Lorient,47.75040448,-3.366575156,71532,France,FR,FRA,Bretagne
Brest,Brest,48.39044293,-4.49500757,142914,France,FR,FRA,Bretagne
Le Mans,Le Mans,48.00041506,0.099983275,143392.5,France,FR,FRA,Pays de la Loire
Nantes,Nantes,47.21038576,-1.590016929,357903,France,FR,FRA,Pays de la Loire
Agen,Agen,44.20041445,0.633335733,46295,France,FR,FRA,Aquitaine
Ajaccio,Ajaccio,41.92706484,8.728293822,46905,France,FR,FRA,Corse
Bastia,Bastia,42.70316734,9.450006875,40558.5,France,FR,FRA,Corse
Toulon,Toulon,43.13418645,5.918821566,263197,France,FR,FRA,Provence-Alpes-C?te-d'Azur
Beziers,Beziers,43.35049217,3.209974323,77759.5,France,FR,FRA,Languedoc-Roussillon
Montpellier,Montpellier,43.61039878,3.869985716,287753,France,FR,FRA,Languedoc-Roussillon
Nimes,Nimes,43.83038535,4.350008096,158891.5,France,FR,FRA,Languedoc-Roussillon
Vichy,Vichy,46.117145,3.416680052,35088.5,France,FR,FRA,Auvergne
Nevers,Nevers,46.98373293,3.166669473,44958.5,France,FR,FRA,Bourgogne
Auxerre,Auxerre,47.80042727,3.566593382,38034,France,FR,FRA,Bourgogne
Dijon,Dijon,47.33040428,5.030018268,159864,France,FR,FRA,Bourgogne
Bourges,Bourges,47.08372683,2.399997923,70163.5,France,FR,FRA,Centre
Tours,Tours,47.38037539,0.699946654,188858.5,France,FR,FRA,Centre
Orleans,Orleans,47.90042116,1.900028441,170725,France,FR,FRA,Centre
Dieppe,Dieppe,49.93373374,1.083334105,39084,France,FR,FRA,Haute-Normandie
Rouen,Rouen,49.43040529,1.079975137,321417.5,France,FR,FRA,Haute-Normandie
Versailles,Versailles,48.80046958,2.133347533,85416,France,FR,FRA,?le-de-France
Brive,Brive,45.15040814,1.533332477,54457,France,FR,FRA,Limousin
Troyes,Troyes,48.34039431,4.083357705,61244,France,FR,FRA,Champagne-Ardenne
Reims,Reims,49.25039044,4.029975951,177939,France,FR,FRA,Champagne-Ardenne
Calais,Calais,50.95041587,1.833314167,83317,France,FR,FRA,Nord-Pas-de-Calais
Amiens,Amiens,49.90037661,2.300004027,118908.5,France,FR,FRA,Picardie
Mulhouse,Mulhouse,47.75040448,7.34998002,163442,France,FR,FRA,Alsace
Nancy,Nancy,48.68368085,6.200024372,187155,France,FR,FRA,Lorraine
Metz,Metz,49.1203467,6.180025593,266550,France,FR,FRA,Lorraine
Pointe-a-Pitre,Pointe-a-Pitre,16.24147504,-61.5329989,81887.5,France,GP,FRA,Guadeloupe
Basse-terre,Basse-terre,16.23039044,-61.43998132,307,France,GP,FRA,Guadeloupe
St.-Benoit,St.-Benoit,-21.03351072,55.71281612,23979,France,RE,FRA,La R?union
Dzaoudzi,Dzaoudzi,-12.78708901,45.27500362,23099,France,YT,FRA,Moyotte
Rennes,Rennes,48.10002138,-1.670012046,204329.5,France,FR,FRA,Bretagne
Nice,Nice,43.71501772,7.265023965,632810,France,FR,FRA,Provence-Alpes-C?te-d'Azur
Toulouse,Toulouse,43.61995892,1.449926716,640027.5,France,FR,FRA,Midi-Pyr?n?es
Limoges,Limoges,45.82997906,1.249990599,146687.5,France,FR,FRA,Limousin
Lille,Lille,50.64996909,3.080008096,636164,France,FR,FRA,Nord-Pas-de-Calais
Strasbourg,Strasbourg,48.57996625,7.750007282,357408.5,France,FR,FRA,Alsace
Kourou,Kourou,5.159980895,-52.64994938,22425.5,France,GF,FRA,Guinaa
La Rochelle,La Rochelle,46.16665102,-1.149992108,76903.5,France,FR,FRA,Poitou-Charentes
Bordeaux,Bordeaux,44.85001304,-0.595013063,517422,France,FR,FRA,Aquitaine
Marseille,Marseille,43.28997906,5.37501013,1097405.5,France,FR,FRA,Provence-Alpes-C?te-d'Azur
Le Havre,Le Havre,49.50497438,0.104970051,214048,France,FR,FRA,Haute-Normandie
St.-Denis,St.-Denis,-20.87889484,55.44807776,163621,France,RE,FRA,La R?union
Lyon,Lyon,45.77000856,4.830030475,947658.5,France,FR,FRA,Rh?ne-Alpes
Cayenne,Cayenne,4.932992166,-52.33002059,57179.5,France,GF,FRA,Guinaa
Paris,Paris,48.86669293,2.333335326,4957588.5,France,FR,FRA,?le-de-France
Papeete,Papeete,-17.53336261,-149.5666694,78856,French Polynesia,PF,PYF,
Ebebiyin,Ebebiyin,2.152997996,11.33000156,24831,Gabon,GA,GAB,Wouleu-Ntem
Tchibanga,Tchibanga,-2.856995957,11.02699849,19365,Gabon,GA,GAB,Nyanga
Mekambo,Mekambo,1.017081318,13.93329911,3170,Gabon,GA,GAB,Ogoou?-Ivindo
Makokou,Makokou,0.567082946,12.8665942,15320.5,Gabon,GA,GAB,Ogoou?-Ivindo
Mitzik,Mitzik,0.78371055,11.56662187,3998.5,Gabon,GA,GAB,Wouleu-Ntem
Bitam,Bitam,2.083657042,11.48337113,13967,Gabon,GA,GAB,Wouleu-Ntem
Lambarene,Lambarene,-0.699609763,10.21662675,23012,Gabon,GA,GAB,Moyen-Ogoou?
Bifoum,Bifoum,-0.332913799,10.38323157,134,Gabon,GA,GAB,Moyen-Ogoou?
Ndende,Ndende,-2.382917868,11.38327388,4101,Gabon,GA,GAB,Ngouni?
Mouila,Mouila,-1.866153545,11.01668127,25234.5,Gabon,GA,GAB,Ngouni?
Omboue,Omboue,-1.566223532,9.249967406,1667,Gabon,GA,GAB,Ogoou?-Maritime
Moanda,Moanda,-1.565500062,13.20001054,28633,Gabon,GA,GAB,Haut-Ogoou?
Okandja,Okandja,-0.682918275,13.78333411,7155,Gabon,GA,GAB,Haut-Ogoou?
Koulamoutou,Koulamoutou,-1.132916647,12.4833101,14343.5,Gabon,GA,GAB,Ogoou?-Lolo
Oyem,Oyem,1.616631286,11.58331335,37146.5,Gabon,GA,GAB,Wouleu-Ntem
Mayumba,Mayumba,-3.416601543,10.65003699,3996,Gabon,GA,GAB,Nyanga
Gamba,Gamba,-2.650033347,9.999999144,7230.5,Gabon,GA,GAB,Ogoou?-Maritime
Franceville,Franceville,-1.633299541,13.58329464,41056,Gabon,GA,GAB,Haut-Ogoou?
Libreville,Libreville,0.38538861,9.457965046,530755.5,Gabon,GA,GAB,Estuaire
Port-Gentil,Port-Gentil,-0.720021953,8.780021931,112999.5,Gabon,GA,GAB,Ogoou?-Maritime
Kutaisi,Kutaisi,42.24999086,42.72999101,181141.5,Georgia,GE,GEO,Imereti
Tskhinvali,Tskhinvali,42.23249839,43.97503129,26751,Georgia,GE,GEO,Shida Kartli
Poti,Poti,42.15565554,41.671606,46001,Georgia,GE,GEO,Samegrelo-Zemo Svaneti
Rustavi,Rustavi,41.57036826,45.05000443,156770,Georgia,GE,GEO,Kvemo Kartli
Batumi,Batumi,41.6000047,41.63000647,138674,Georgia,GE,GEO,Ajaria
Sukhumi,Sukhumi,43.02002138,41.02001786,76219,Georgia,GE,GEO,Abkhazia
Tbilisi,Tbilisi,41.72500999,44.79079545,1052628.5,Georgia,GE,GEO,Tbilisi
Mainz,Mainz,49.98247246,8.273219156,184997,Germany,DE,DEU,Rheinland-Pfalz
Schwerin,Schwerin,53.63330408,11.41669861,96641,Germany,DE,DEU,Mecklenburg-Vorpommern
Bielefeld,Bielefeld,52.02998822,8.530011351,311739.5,Germany,DE,DEU,Nordrhein-Westfalen
Dortmund,Dortmund,51.52996706,7.450025593,588462,Germany,DE,DEU,Nordrhein-Westfalen
Duisburg,Duisburg,51.42997316,6.750016641,882381,Germany,DE,DEU,Nordrhein-Westfalen
Wuppertal,Wuppertal,51.25000999,7.169991006,562997.5,Germany,DE,DEU,Nordrhein-Westfalen
Essen,Essen,51.44999778,7.016615355,1157801.5,Germany,DE,DEU,Nordrhein-Westfalen
Karlsruhe,Karlsruhe,48.99999229,8.399993448,330643,Germany,DE,DEU,Baden-W?rttemberg
Heidelberg,Heidelberg,49.41999249,8.699975137,284967.5,Germany,DE,DEU,Baden-W?rttemberg
Kassel,Kassel,51.30000694,9.500029662,242212.5,Germany,DE,DEU,Hessen
Oldenburg,Oldenburg,53.1299986,8.220004434,163338,Germany,DE,DEU,Niedersachsen
Emden,Emden,53.36667666,7.216654824,49786,Germany,DE,DEU,Niedersachsen
Braunschweig,Braunschweig,52.24997479,10.5000203,239884.5,Germany,DE,DEU,Niedersachsen
Erfurt,Erfurt,50.97005292,11.02996212,189365,Germany,DE,DEU,Th?ringen
Coburg,Coburg,50.26660748,10.96660681,51477.5,Germany,DE,DEU,Bayern
Augsburg,Augsburg,48.35000612,10.89999589,309092.5,Germany,DE,DEU,Bayern
Furth,Furth,49.47001528,10.99998979,174934.5,Germany,DE,DEU,Bayern
Chemnitz,Chemnitz,50.82998395,12.91997595,274931.5,Germany,DE,DEU,Sachsen
Bonn,Bonn,50.72045575,7.080022337,496834,Germany,DE,DEU,Nordrhein-Westfalen
M?nster,Munster,51.97040529,7.620041055,253612.5,Germany,DE,DEU,Nordrhein-Westfalen
D?sseldorf,Dusseldorf,51.22037355,6.779988972,906196.5,Germany,DE,DEU,Nordrhein-Westfalen
Ulm,Ulm,48.40039064,9.999999144,146703,Germany,DE,DEU,Baden-W?rttemberg
Mannheim,Mannheim,49.50037518,8.470015013,1337587,Germany,DE,DEU,Baden-W?rttemberg
Freiburg,Freiburg,48.00041506,7.869948281,235427.5,Germany,DE,DEU,Baden-W?rttemberg
Giessen,Giessen,50.58371991,8.650004027,78384.5,Germany,DE,DEU,Hessen
Wiesbaden,Wiesbaden,50.08039146,8.250028441,444779,Germany,DE,DEU,Hessen
Bremerhaven,Bremerhaven,53.55043805,8.579982461,127598.5,Germany,DE,DEU,Bremen
Osnabr?ck,Osnabruck,52.28043805,8.049988972,198865,Germany,DE,DEU,Niedersachsen
Hannover,Hannover,52.36697023,9.716657266,618815,Germany,DE,DEU,Niedersachsen
Gottingen,Gottingen,51.52043276,9.920004027,130784,Germany,DE,DEU,Niedersachsen
Gera,Gera,50.87036908,12.07000199,103857,Germany,DE,DEU,Th?ringen
Jena,Jena,50.93044293,11.58000606,99941.5,Germany,DE,DEU,Th?ringen
Flensburg,Flensburg,54.78374778,9.433315388,91884,Germany,DE,DEU,Schleswig-Holstein
Lubeck,Lubeck,53.87039268,10.66998409,223798.5,Germany,DE,DEU,Schleswig-Holstein
Kiel,Kiel,54.33039044,10.13001705,251092.5,Germany,DE,DEU,Schleswig-Holstein
Koblenz,Koblenz,50.35047833,7.599990599,209976,Germany,DE,DEU,Rheinland-Pfalz
Saarbrucken,Saarbrucken,49.25039044,6.970003213,472871,Germany,DE,DEU,Saarland
Regensburg,Regensburg,49.02040448,12.12002478,146755,Germany,DE,DEU,Bayern
Rosenheim,Rosenheim,47.8503467,12.13330562,76488,Germany,DE,DEU,Bayern
Hof,Hof,50.31704368,11.91667802,52696,Germany,DE,DEU,Bayern
Wurzburg,Wurzburg,49.80043439,9.950028034,151146,Germany,DE,DEU,Bayern
Ingolstadt,Ingolstadt,48.77041974,11.44998816,141991.5,Germany,DE,DEU,Bayern
Cottbus,Cottbus,51.7704175,14.32996741,94910.5,Germany,DE,DEU,Brandenburg
Potsdam,Potsdam,52.40040489,13.06999263,181693.5,Germany,DE,DEU,Brandenburg
Magdeburg,Magdeburg,52.13042137,11.62000362,227378.5,Germany,DE,DEU,Sachsen-Anhalt
Leipzig,Leipzig,51.33540529,12.40998124,523750,Germany,DE,DEU,Sachsen
Stralsund,Stralsund,54.30041811,13.10001664,60172,Germany,DE,DEU,Mecklenburg-Vorpommern
Rostock,Rostock,54.07038047,12.14999711,200686.5,Germany,DE,DEU,Mecklenburg-Vorpommern
Stuttgart,Stuttgart,48.77997988,9.199996296,1775644,Germany,DE,DEU,Baden-W?rttemberg
Bremen,Bremen,53.08000165,8.80002071,635705,Germany,DE,DEU,Bremen
N?rnberg,Nurnberg,49.44999066,11.0799849,618270.5,Germany,DE,DEU,Bayern
Cologne,Cologne,50.93000368,6.950004434,983697.5,Germany,DE,DEU,Nordrhein-Westfalen
Dresden,Dresden,51.04997052,13.75000281,552184.5,Germany,DE,DEU,Sachsen
Frankfurt,Frankfurt,50.09997683,8.67501542,1787332,Germany,DE,DEU,Hessen
Hamburg,Hamburg,53.55002464,9.999999144,1748058.5,Germany,DE,DEU,Hamburg
Munich,Munich,48.12994204,11.57499345,1267695.5,Germany,DE,DEU,Bayern
Berlin,Berlin,52.52181866,13.40154862,3250007,Germany,DE,DEU,Berlin
Sunyani,Sunyani,7.335998991,-2.336003416,70299,Ghana,GH,GHA,Brong Ahafo
Tamale,Tamale,9.400419738,-0.83998519,342871,Ghana,GH,GHA,Northern
Yendi,Yendi,9.433725198,-0.016650433,30841.5,Ghana,GH,GHA,Northern
Bolgatanga,Bolgatanga,10.79038658,-0.84998458,68303.5,Ghana,GH,GHA,Upper East
Bawku,Bawku,11.06039593,-0.239995973,65212,Ghana,GH,GHA,Upper East
Wa,Wa,10.06040529,-2.500013063,76891.5,Ghana,GH,GHA,Upper West
Obuasi,Obuasi,6.190408955,-1.659986818,158986.5,Ghana,GH,GHA,Ashanti
Berekum,Berekum,7.450383727,-2.59000757,36484.5,Ghana,GH,GHA,Brong Ahafo
Winneba,Winneba,5.350434386,-0.630049684,41911,Ghana,GH,GHA,Central
Cape Coast,Cape Coast,5.11037152,-1.249986004,139265.5,Ghana,GH,GHA,Central
Nkawkaw,Nkawkaw,6.550464497,-0.780014691,54914.5,Ghana,GH,GHA,Eastern
Koforidua,Koforidua,6.090415058,-0.260020591,126459.5,Ghana,GH,GHA,Eastern
Tema,Tema,5.640365009,0.010014606,184969.5,Ghana,GH,GHA,Greater Accra
Ho,Ho,6.600409769,0.46998653,81521,Ghana,GH,GHA,Volta
Kumasi,Kumasi,6.689990864,-1.630014487,1468575.5,Ghana,GH,GHA,Ashanti
Sekondi,Sekondi,4.943275776,-1.704015138,212560,Ghana,GH,GHA,Western
Accra,Accra,5.550034606,-0.21671574,2042132,Ghana,GH,GHA,Greater Accra
Gibraltar,Gibraltar,36.13243495,-5.37807483,106813.5,Gibraltar,GI,GIB,Gibraltar
Lamia,Lamia,38.89899915,22.43400358,47246,Greece,GR,GRC,Stere? Ell?da
Polygyros,Polygyros,40.38100213,23.45300148,5258,Greece,GR,GRC,Kentriki Makedonia
Komatini,Komatini,41.13330309,25.41670256,45631,Greece,GR,GRC,Anatoliki Makedonia kai Thraki
Pirai?vs,Piraievs,37.95002077,23.69998979,320881,Greece,GR,GRC,Attiki
Volos,Volos,39.36995994,22.95000972,97528.5,Greece,GR,GRC,Thessalia
Hania,Hania,35.51221092,24.01557776,66646.5,Greece,GR,GRC,Kriti
Kavala,Kavala,40.94121113,24.40176036,56095,Greece,GR,GRC,Anatoliki Makedonia kai Thraki
Alexandroupoli,Alexandroupoli,40.84861937,25.87440978,48711.5,Greece,GR,GRC,Anatoliki Makedonia kai Thraki
Kerkira,Kerkira,39.61542299,19.9147428,32760,Greece,GR,GRC,Ionioi Nisoi
Tripoli,Tripoli,37.50914329,22.37939856,27765.5,Greece,GR,GRC,Peloponnisos
Sparti,Sparti,37.07371767,22.42967973,15842,Greece,GR,GRC,Peloponnisos
Agrinio,Agrinio,38.62176271,21.4077266,59379,Greece,GR,GRC,Dytiki Ellada
Pirgos,Pirgos,37.68373212,21.44999792,22311,Greece,GR,GRC,Dytiki Ellada
Larissa,Larissa,39.63040916,22.42001623,120122.5,Greece,GR,GRC,Thessalia
Ioanina,Ioanina,39.66790041,20.85086137,75158,Greece,GR,GRC,Ipeiros
Mitilini,Mitilini,39.11041506,26.55464758,28825,Greece,GR,GRC,Voreio Aigaio
Hios,Hios,38.36810895,26.1358101,25422,Greece,GR,GRC,Voreio Aigaio
Chalkida,Chalkida,38.46399457,23.61239823,63200,Greece,GR,GRC,Stere? Ell?da
Sitia,Sitia,35.20042116,26.09855139,8770,Greece,GR,GRC,Kriti
Katerini,Katerini,40.2723338,22.50249182,50850.5,Greece,GR,GRC,Kentriki Makedonia
Seres,Seres,41.08597923,23.54971472,50910.5,Greece,GR,GRC,Kentriki Makedonia
Xanthi,Xanthi,41.14178977,24.88358679,49395.5,Greece,GR,GRC,Anatoliki Makedonia kai Thraki
Ermoupoli,Ermoupoli,37.45041302,24.93329952,12260,Greece,GR,GRC,Notio Aigaio
Kos,Kos,36.89372866,27.28881466,18967.5,Greece,GR,GRC,Notio Aigaio
Rodos,Rodos,36.44122398,28.22250443,56548.5,Greece,GR,GRC,Notio Aigaio
Patra,Patra,38.23000368,21.72998083,159579.5,Greece,GR,GRC,Dytiki Ellada
Kalamata,Kalamata,37.03891359,22.11419511,61465.5,Greece,GR,GRC,Peloponnisos
Iraklio,Iraklio,35.32501304,25.13049678,134404,Greece,GR,GRC,Kriti
Thessaloniki,Thessaloniki,40.69610638,22.88500077,591145,Greece,GR,GRC,Kentriki Makedonia
Athens,Athens,37.98332623,23.73332108,1985568.5,Greece,GR,GRC,Attiki
Qasigiannguit,Qasigiannguit,68.81927014,-51.17851854,1341,Greenland,GL,GRL,Qaasuitsup Kommunia
Kullorsuaq,Kullorsuaq,74.57806289,-57.22498603,443,Greenland,GL,GRL,
Tasiusaq,Tasiusaq,73.36900226,-56.05981366,249,Greenland,GL,GRL,
Kulusuk,Kulusuk,65.56657798,-37.18332239,286,Greenland,GL,GRL,Kommuneqarfik Sermersooq
Paamiut,Paamiut,62.00410237,-49.63507012,1862,Greenland,GL,GRL,Kommuneqarfik Sermersooq
Ittoqqortoormiit,Ittoqqortoormiit,70.48335797,-21.9666543,469,Greenland,GL,GRL,Kommuneqarfik Sermersooq
Timmiarmiut,Timmiarmiut,62.53327476,-42.21671025,10,Greenland,GL,GRL,Kommune Kujalleq
Qaqortoq,Qaqortoq,60.72890973,-46.03641168,3224,Greenland,GL,GRL,Kommune Kujalleq
Kangerlussuaq,Kangerlussuaq,67.01412249,-50.70990925,556,Greenland,GL,GRL,Qeqqata Kommunia
Nord,Nord,81.71662579,-17.80003524,10,Greenland,GL,GRL,Nationalparken
Qeqertasuaq,Qeqertasuaq,69.24416391,-53.56523854,7.5,Greenland,GL,GRL,Qaasuitsup Kommunia
Nuussuaq,Nuussuaq,74.12096872,-57.06736051,204,Greenland,GL,GRL,Qaasuitsup Kommunia
Ilulissat,Ilulissat,69.21666526,-51.09996647,4413,Greenland,GL,GRL,Qaasuitsup Kommunia
Tasiilaq,Tasiilaq,65.60186934,-37.6337371,1829,Greenland,GL,GRL,
Savissivik,Savissivik,76.01947624,-65.11248065,66,Greenland,GL,GRL,
Kangersuatsiaq,Kangersuatsiaq,72.37963955,-55.54911893,193,Greenland,GL,GRL,
Uummannaq,Uummannaq,70.67502343,-52.12293443,1299,Greenland,GL,GRL,
Narsarsuaq,Narsarsuaq,61.16658815,-45.41661829,145,Greenland,GL,GRL,Kommune Kujalleq
Sisimiut,Sisimiut,66.95000775,-53.66660567,5227,Greenland,GL,GRL,Qeqqata Kommunia
Upernavik,Upernavik,72.70936669,-56.14167532,1129,Greenland,GL,GRL,Qaasuitsup Kommunia
Qaanaaq,Qaanaaq,77.48347333,-69.33223861,437,Greenland,GL,GRL,Qaasuitsup Kommunia
Nuuk,Nuuk,64.19828147,-51.73265879,14798,Greenland,GL,GRL,Kommuneqarfik Sermersooq
Saint George's,Saint George's,12.0526334,-61.74164323,30538.5,Grenada,GD,GRD,
Agana,Agana,13.4700163,144.750017,61755.5,Guam,GU,GUM,
Salama,Salama,15.10299903,-90.31400061,40000,Guatemala,GT,GTM,Baja Verapaz
Retalhuleu,Retalhuleu,14.53709704,-91.67701454,36656,Guatemala,GT,GTM,Retalhuleu
San Marcos,San Marcos,14.96600106,-91.79999952,25088,Guatemala,GT,GTM,San Marcos
Chimaltenango,Chimaltenango,14.66199914,-90.8199985,82370,Guatemala,GT,GTM,Chimaltenango
Antigua Guatemala,Antigua Guatemala,14.5666981,-90.73330161,39368,Guatemala,GT,GTM,Sacatep?quez
Solola,Solola,14.77299598,-91.18299551,45373,Guatemala,GT,GTM,Solol?
Totonicapan,Totonicapan,14.91399898,-91.35800061,69734,Guatemala,GT,GTM,Totonicap?n
El Progreso,El Progreso,14.85,-90.01670359,147197,Guatemala,GT,GTM,El Progreso
Cuilapa,Cuilapa,14.27900409,-90.2979985,16484,Guatemala,GT,GTM,Santa Rosa
Chiquimula,Chiquimula,14.79699906,-89.54399653,41521,Guatemala,GT,GTM,Chiquimula
Jalapa,Jalapa,14.63300111,-89.98900162,45834,Guatemala,GT,GTM,Jalapa
Zacapa,Zacapa,14.97200398,-89.52900256,36088,Guatemala,GT,GTM,Zacapa
Santa Cruz Del Quiche,Santa Cruz Del Quiche,15.0333031,-91.13329763,23618,Guatemala,GT,GTM,Quich?
San Luis,San Luis,16.2000047,-89.4400035,69623,Guatemala,GT,GTM,Pet?n
Coban,Coban,15.46999758,-90.3799978,59284.5,Guatemala,GT,GTM,Alta Verapaz
Livingston,Livingston,15.83065388,-88.75623452,12302.5,Guatemala,GT,GTM,Izabal
Jutiapa,Jutiapa,14.28999208,-89.90000126,42506.5,Guatemala,GT,GTM,Jutiapa
Huehuetenango,Huehuetenango,15.32039431,-91.46998295,82709,Guatemala,GT,GTM,Huehuetenango
Flores,Flores,16.93368085,-89.88328394,29249.5,Guatemala,GT,GTM,Pet?n
La Libertad,La Libertad,16.78043439,-90.11998784,8584.5,Guatemala,GT,GTM,Pet?n
San Jose,San Jose,13.93972958,-90.82003203,14248,Guatemala,GT,GTM,Escuintla
Escuintla,Escuintla,14.30040489,-90.77999923,105401.5,Guatemala,GT,GTM,Escuintla
Mazatenango,Mazatenango,14.53036501,-91.50998051,54392,Guatemala,GT,GTM,Suchitep?quez
Puerto Barrios,Puerto Barrios,15.71749529,-88.59265184,54877.5,Guatemala,GT,GTM,Izabal
Quetzaltenango,Quetzaltenango,14.82995913,-91.52000574,399983,Guatemala,GT,GTM,Quezaltenango
Guatemala,Guatemala,14.62113466,-90.52696558,1009469,Guatemala,GT,GTM,Guatemala
Mali,Mali,12.08400302,-12.30100143,5479,Guinea,GN,GIN,Labe
Tongue,Tongue,11.43999904,-11.67000248,25531,Guinea,GN,GIN,Labe
Kouroussa,Kouroussa,10.6530031,-9.891998549,14223,Guinea,GN,GIN,Kankan
Pita,Pita,11.0799991,-12.40100056,20052,Guinea,GN,GIN,Mamou
Dalaba,Dalaba,10.65600001,-12.27200357,6349,Guinea,GN,GIN,Mamou
Boffa,Boffa,10.18500307,-14.04299645,2332,Guinea,GN,GIN,Boke
Koundara,Koundara,12.4800031,-13.29599643,13990,Guinea,GN,GIN,Boke
Gaoual,Gaoual,11.75400014,-13.21299843,7461,Guinea,GN,GIN,Boke
Telimele,Telimele,10.90500311,-13.04299756,30311,Guinea,GN,GIN,Kindia
Forecariah,Forecariah,9.430002076,-13.09799655,12358,Guinea,GN,GIN,Kindia
Beyla,Beyla,8.686997987,-8.657000454,13204,Guinea,GN,GIN,Nzerekore
Gueckedou,Gueckedou,8.553996122,-10.1510005,221715,Guinea,GN,GIN,Nzerekore
Dinguiraye,Dinguiraye,11.29899604,-10.72600144,6062,Guinea,GN,GIN,Faranah
Dabola,Dabola,10.747998,-11.10899649,13057,Guinea,GN,GIN,Faranah
Kerouane,Kerouane,9.270375996,-9.019976849,11317,Guinea,GN,GIN,Kankan
Siguiri,Siguiri,11.41709251,-9.166634564,46880,Guinea,GN,GIN,Kankan
Mamou,Mamou,10.38038576,-12.1000214,56386,Guinea,GN,GIN,Mamou
Kamsar,Kamsar,10.6854059,-14.60501062,34973,Guinea,GN,GIN,Boke
Fria,Fria,10.38038576,-13.54998458,23729,Guinea,GN,GIN,Boke
Macenta,Macenta,8.550368265,-9.480000449,42167.5,Guinea,GN,GIN,Nzerekore
Yomou,Yomou,7.570428079,-9.269987428,2607.5,Guinea,GN,GIN,Nzerekore
Faranah,Faranah,10.04040651,-10.75000045,14409.5,Guinea,GN,GIN,Faranah
Kissidougou,Kissidougou,9.190458393,-10.12001306,56957,Guinea,GN,GIN,Faranah
Labe,Labe,11.31999249,-12.3000092,99612,Guinea,GN,GIN,Labe
Boke,Boke,10.93998985,-14.29999048,116270,Guinea,GN,GIN,Boke
Kindia,Kindia,10.06001772,-12.86997441,93511,Guinea,GN,GIN,Kindia
Kankan,Kankan,10.38999758,-9.310010825,110457.5,Guinea,GN,GIN,Kankan
Nzerekore,Nzerekore,7.760003071,-8.829988445,150424.5,Guinea,GN,GIN,Nzerekore
Conakry,Conakry,9.531522846,-13.68023503,1494000,Guinea,GN,GIN,Conakry
Cacheu,Cacheu,12.26899803,-16.16499854,10490,Guinea Bissau,GW,GNB,Cacheu
Farim,Farim,12.49299903,-15.22700042,6792,Guinea Bissau,GW,GNB,Oio
Fulacunda,Fulacunda,11.77299899,-15.19499654,1311,Guinea Bissau,GW,GNB,Quinara
Gabu,Gabu,12.27999608,-14.23400348,14430,Guinea Bissau,GW,GNB,Gab?
Catio,Catio,11.21670002,-15.16670049,9898,Guinea Bissau,GW,GNB,Tombali
Bolama,Bolama,11.58295303,-15.48280399,9179,Guinea Bissau,GW,GNB,Bolama
Bafata,Bafata,12.16699506,-14.66601465,26112.5,Guinea Bissau,GW,GNB,Bafat?
Bissau,Bissau,11.86502382,-15.59836084,395683.5,Guinea Bissau,GW,GNB,Bissau
Corriverton,Corriverton,5.900039082,-57.16998356,11787,Guyana,GY,GUY,Mahaica-Berbice
Ituni,Ituni,5.430016092,-58.24999516,75,Guyana,GY,GUY,Upper Takutu-Upper Essequibo
Lethem,Lethem,3.389959736,-59.80002975,352,Guyana,GY,GUY,Upper Demerara-Berbice
Kumaka,Kumaka,3.900393696,-58.38001306,1467.5,Guyana,GY,GUY,Upper Demerara-Berbice
Bartica,Bartica,6.410421365,-58.63002364,11340.5,Guyana,GY,GUY,Pomeroon-Supenaam
Anna Regina,Anna Regina,7.270420551,-58.50005742,3113,Guyana,GY,GUY,Cuyuni-Mazaruni
Linden,Linden,5.99000775,-58.2699681,28041.5,Guyana,GY,GUY,Upper Takutu-Upper Essequibo
Mabaruma,Mabaruma,8.199976216,-59.77997929,2972,Guyana,GY,GUY,Barima-Waini
New Amsterdam,New Amsterdam,6.250017719,-57.52998743,40956.5,Guyana,GY,GUY,Essequibo Islands-West Demerara
Georgetown,Georgetown,6.801973693,-58.16702865,249683.5,Guyana,GY,GUY,East Berbice-Corentyne
Jeremie,Jeremie,18.63393473,-74.11842526,30917,Haiti,HT,HTI,Grand'Anse
Port-De-Paix,Port-De-Paix,19.93176008,-72.82948452,34657,Haiti,HT,HTI,Nord-Ouest
Hinche,Hinche,19.14300009,-72.0039956,18590,Haiti,HT,HTI,Centre
Fort-Liberte,Fort-Liberte,19.66556703,-71.84483954,11465,Haiti,HT,HTI,Nord-Est
Jacmel,Jacmel,18.23499903,-72.53700258,33563,Haiti,HT,HTI,Sud-Est
Les Cayes,Les Cayes,18.20037355,-73.74997929,122728.5,Haiti,HT,HTI,Sud
Gonaives,Gonaives,19.45042645,-72.68324854,125819.5,Haiti,HT,HTI,L'Artibonite
Cap-Haitien,Cap-Haitien,19.7592224,-72.21251602,208151,Haiti,HT,HTI,Nord
Port-au-Prince,Port-au-Prince,18.5410246,-72.33603459,1616371,Haiti,HT,HTI,Ouest
Yoro,Yoro,15.05999711,-87.29000054,15774,Honduras,HN,HND,Yoro
La Esperanza,La Esperanza,14.33300406,-88.16669954,5318,Honduras,HN,HND,Intibuc?
La Paz,La Paz,14.31999903,-87.68400257,17555,Honduras,HN,HND,La Paz
Santa Barbara,Santa Barbara,14.91900304,-88.23599963,15119,Honduras,HN,HND,Santa B?rbara
Gracias,Gracias,14.58330306,-88.58330051,7909,Honduras,HN,HND,Lempira
Nueva Ocotepeque,Nueva Ocotepeque,14.43699912,-89.18199855,8780,Honduras,HN,HND,Ocotepeque
Yuscaran,Yuscaran,13.94399699,-86.85099854,2371,Honduras,HN,HND,El Para?so
Roatan,Roatan,16.32999599,-86.51899761,7514,Honduras,HN,HND,Islas de la Bah?a
Nacaome,Nacaome,13.5299868,-87.48996749,30464.5,Honduras,HN,HND,Valle
Santa Rosa de Copan,Santa Rosa de Copan,14.76998863,-88.77999211,31641,Honduras,HN,HND,Cop?n
Trujillo,Trujillo,15.9103583,-85.9600092,7366.5,Honduras,HN,HND,Col?n
Brus Laguna,Brus Laguna,15.75041974,-84.47999618,4067,Honduras,HN,HND,Gracias a Dios
Puerto Lempira,Puerto Lempira,15.26202578,-83.77164148,4760,Honduras,HN,HND,Gracias a Dios
Juticalpa,Juticalpa,14.67040814,-86.22996688,35564,Honduras,HN,HND,Olancho
Comayagua,Comayagua,14.46039512,-87.64998356,64963,Honduras,HN,HND,Comayagua
Choluteca,Choluteca,13.30067263,-87.19081262,87650.5,Honduras,HN,HND,Choluteca
La Ceiba,La Ceiba,15.7631063,-86.79698653,138072,Honduras,HN,HND,Atl?ntida
San Pedro Sula,San Pedro Sula,15.50002159,-88.02998621,584778.5,Honduras,HN,HND,Cort?s
Tegucigalpa,Tegucigalpa,14.1020449,-87.21752934,898424,Honduras,HN,HND,Francisco Moraz?n
Hong Kong,Hong Kong,22.3049809,114.1850093,5878789.5,Hong Kong S.A.R.,HK,HKG,
Veszprem,Veszprem,47.09099714,17.91099957,62023,Hungary,HU,HUN,Veszpr?m
Zalaegerszeg,Zalaegerszeg,46.84400103,16.83999959,61898,Hungary,HU,HUN,Zala
Tatabanya,Tatabanya,47.54999718,18.43299957,70541,Hungary,HU,HUN,Kom?rom-Esztergom
Szekszard,Szekszard,46.34399711,18.71299858,34174,Hungary,HU,HUN,Tolna
Salgotarjan,Salgotarjan,48.10500008,19.82600163,39640,Hungary,HU,HUN,N?gr?d
Bekescsaba,Bekescsaba,46.67200211,21.10100457,65206,Hungary,HU,HUN,B?k?s
Eger,Eger,47.89500314,20.38300258,56647,Hungary,HU,HUN,Heves
Szombathely,Szombathely,47.22534609,16.62874182,94526,Hungary,HU,HUN,Vas
Kecskemet,Kecskemet,46.90004295,19.70002722,111871,Hungary,HU,HUN,B?cs-Kiskun
Szekesfehervar,Szekesfehervar,47.19467613,18.40806474,122959.5,Hungary,HU,HUN,Fej?r
Nyiregyhaza,Nyiregyhaza,47.96532676,21.71871537,146589,Hungary,HU,HUN,Szabolcs-Szatm?r-Bereg
Pecs,Pecs,46.08042889,18.2200142,171455.5,Hungary,HU,HUN,Baranya
Gyor,Gyor,47.70035585,17.63002437,132173,Hungary,HU,HUN,Gyor-Moson-Sopron
Kaposvar,Kaposvar,46.36702639,17.79998816,88137,Hungary,HU,HUN,Somogy
Vac,Vac,47.78365826,19.13324011,35200.5,Hungary,HU,HUN,Pest
Miskolc,Miskolc,48.10040896,20.78001298,210197,Hungary,HU,HUN,Borsod-Aba?j-Zempl?n
Szeged,Szeged,46.25039268,20.15002559,176324,Hungary,HU,HUN,Csongr?d
Debrecen,Debrecen,47.53046958,21.63003861,217705,Hungary,HU,HUN,Hajd?-Bihar
Szolnok,Szolnok,47.18635622,20.17937781,92367.5,Hungary,HU,HUN,J?sz-Nagykun-Szolnok
Budapest,Budapest,47.50000633,19.08332068,1679000,Hungary,HU,HUN,Budapest
Borgarnes,Borgarnes,64.56950277,-21.86232219,1783,Iceland,IS,ISL,Vesturland
Egilssta?ir,Egilsstadir,65.26742312,-14.3949976,1822.5,Iceland,IS,ISL,Austur-H?ra?
Sau??rkr?kur,Saudarkrokur,65.74641197,-19.63899276,2191,Iceland,IS,ISL,Akrahreppur
Selfoss,Selfoss,63.93342185,-20.99694605,5030.5,Iceland,IS,ISL,Biskupstungnahreppur
Hofn,Hofn,64.2723151,-15.21385946,1695,Iceland,IS,ISL,Sveitarf?lagi? Hornafj?r?ur
?safj?r?ur,Isafjordur,66.08331647,-23.14996708,1949.5,Iceland,IS,ISL,Vestfir?ir
Akureyi,Akureyi,65.66657188,-18.10001693,14754,Iceland,IS,ISL,Akureyri
Keflav?k,Keflavik,64.01664675,-22.56659184,7377,Iceland,IS,ISL,Su?urnes
Reykjav?k,Reykjavik,64.15002362,-21.95001449,140059,Iceland,IS,ISL,Su?urnes
Panaji,Panaji,15.491997,73.81800065,65586,India,IN,IND,Goa
Simla,Simla,31.10002545,77.16659704,173503,India,IN,IND,Himachal Pradesh
Gurgaon,Gurgaon,28.45000633,77.01999101,197340,India,IN,IND,Haryana
Sonipat,Sonipat,28.9999986,77.01999101,250521,India,IN,IND,Haryana
Rohtak,Rohtak,28.9000047,76.58001786,317245,India,IN,IND,Haryana
Hisar,Hisar,29.16998822,75.72503129,423039,India,IN,IND,Haryana
Bhiwani,Bhiwani,28.81001019,76.12500688,190855,India,IN,IND,Haryana
Ambala,Ambala,30.32002138,76.82000321,146787,India,IN,IND,Haryana
Sopore,Sopur,34.29995933,74.46665849,60725.5,India,IN,IND,Jammu and Kashmir
Silvassa,Silvassa,20.26657819,73.0166178,27359,India,IN,IND,Dadra and Nagar Haveli
Kalyan,Kalyan,19.25023195,73.16017493,1576614,India,IN,IND,Maharashtra
Bhusawal,Bhusawal,21.01999473,75.8300378,177683.5,India,IN,IND,Maharashtra
Jorhat,Jorhat,26.7499809,94.21666744,69033,India,IN,IND,Assam
Hoshiarpur,Hoshiarpur,31.51997398,75.98000281,158142,India,IN,IND,Punjab
Ajmer,Ajmer,26.44999921,74.63998124,553948,India,IN,IND,Rajasthan
Hathras,Hathras,27.59998069,78.05000565,126882,India,IN,IND,Uttar Pradesh
Sitapur,Sitapur,27.6300047,80.74999589,164435,India,IN,IND,Uttar Pradesh
Pilibhit,Pilibhit,28.63999473,79.81000159,131008,India,IN,IND,Uttar Pradesh
Budaun,Budaun,28.03000612,79.08999385,161555,India,IN,IND,Uttar Pradesh
Firozabad,Firozabad,27.14998232,78.39494584,306409,India,IN,IND,Uttar Pradesh
Mathura,Mathura,27.4999868,77.67002885,330511,India,IN,IND,Uttar Pradesh
Bulandshahr,Bulandshahr,28.4103705,77.84841589,198612,India,IN,IND,Uttar Pradesh
Hapur,Hapur,28.74365765,77.76278804,242920,India,IN,IND,Uttar Pradesh
Muzaffarnagar,Muzaffarnagar,29.48500775,77.69504024,349706,India,IN,IND,Uttar Pradesh
Gangtok,Gangtok,27.3333303,88.6166475,54300,India,IN,IND,Sikkim
Diu,Diu,20.71967334,70.99039497,23779,India,IN,IND,Dadra and Nagar Haveli
Pathankot,Pathankot,32.27034161,75.72001868,214146.5,India,IN,IND,Himachal Pradesh
Sirsa,Sirsa,29.4903821,75.02998328,170884,India,IN,IND,Haryana
Panipat,Panipat,29.40041343,76.96996822,292808,India,IN,IND,Haryana
Karnal,Karnal,29.68044802,76.96996822,225049,India,IN,IND,Haryana
Baramula,Baramula,34.20043052,74.35002478,122631,India,IN,IND,Jammu and Kashmir
Proddatur,Proddatur,14.7504291,78.57002559,187624,India,IN,IND,Andhra Pradesh
Nandyal,Nandyal,15.5203821,78.47995357,176995.5,India,IN,IND,Andhra Pradesh
Hindupur,Hindupur,13.78035911,77.48998816,150805,India,IN,IND,Andhra Pradesh
Tirupati,Tirupati,13.65041872,79.41999955,268928,India,IN,IND,Andhra Pradesh
Ongole,Ongole,15.56037966,80.05003861,187866,India,IN,IND,Andhra Pradesh
Vizianagaram,Vizianagaram,18.12040428,83.50000891,90276,India,IN,IND,Andhra Pradesh
Rajahmundry,Rajahmundry,17.03034161,81.78998409,304804,India,IN,IND,Andhra Pradesh
Machilipatnam,Machilipatnam,16.20041811,81.17999548,192827,India,IN,IND,Andhra Pradesh
Khammam,Khammam,17.28042971,80.16005774,230671,India,IN,IND,Andhra Pradesh
Chirala,Chirala,15.86041302,80.33999508,170000.5,India,IN,IND,Andhra Pradesh
Karimnagar,Karimnagar,18.4604352,79.10999263,258498,India,IN,IND,Andhra Pradesh
Nizamabad,Nizamabad,18.67039654,78.10002844,346971.5,India,IN,IND,Andhra Pradesh
Kollam,Kollam,8.900372741,76.56999263,394163,India,IN,IND,Kerala
Alappuzha,Alappuzha,9.500413634,76.37000484,176783,India,IN,IND,Kerala
Puri,Puri,19.82042971,85.90001746,201026,India,IN,IND,Orissa
Sambalpur,Sambalpur,21.47040651,83.97005774,236869.5,India,IN,IND,Orissa
Raurkela,Raurkela,22.2304118,84.82995357,554730,India,IN,IND,Orissa
Kavaratti,Kavaratti,10.56257331,72.63686717,10688,India,IN,IND,Lakshadweep
Mandya,Mandya,12.57038129,76.91999711,209939.5,India,IN,IND,Karnataka
Kolar,Kolar,13.13370607,78.13335974,135533,India,IN,IND,Karnataka
Shimoga,Shimoga,13.93037579,75.56002844,486802.5,India,IN,IND,Karnataka
Raichur,Raichur,16.21036582,77.35500932,240601,India,IN,IND,Karnataka
Hospet,Hospet,15.28039675,76.37501745,241926.5,India,IN,IND,Karnataka
Bidar,Bidar,17.92292279,77.5175317,252103.5,India,IN,IND,Karnataka
Sangli,Sangli,16.86040367,74.57502397,601214,India,IN,IND,Maharashtra
Parbhani,Parbhani,19.27038576,76.76000688,333977.5,India,IN,IND,Maharashtra
Malegaon,Malegaon,20.5603587,74.52500118,563103,India,IN,IND,Maharashtra
Port Blair,Port Blair,11.66702557,92.73598262,119806,India,IN,IND,Andaman and Nicobar
Tezpur,Tezpur,26.6337606,92.80000972,58851,India,IN,IND,Assam
Silchar,Silchar,24.79041058,92.79003617,152393,India,IN,IND,Assam
Kohima,Kohima,25.6669979,94.11657019,92113,India,IN,IND,Nagaland
Shillong,Shillong,25.57049217,91.8800142,364926,India,IN,IND,Meghalaya
Abohar,Abohar,30.12042116,74.29002844,130603,India,IN,IND,Punjab
Patiala,Patiala,30.32040895,76.38499101,329224,India,IN,IND,Punjab
Bhilwara,Bhilwara,25.35042808,74.6350203,358171,India,IN,IND,Rajasthan
Pali,Pali,25.79037539,73.32993201,208748.5,India,IN,IND,Rajasthan
Tonk,Tonk,26.15045677,75.79004024,166532.5,India,IN,IND,Rajasthan
Sikar,Sikar,27.61039349,75.1400024,318789.5,India,IN,IND,Rajasthan
Bikaner,Bikaner,28.0303937,73.32993201,485961.5,India,IN,IND,Rajasthan
Bharatpur,Bharatpur,27.25036379,77.50001339,229384,India,IN,IND,Rajasthan
Alwar,Alwar,27.5453587,76.6049259,283228,India,IN,IND,Rajasthan
Fatehpur,Fatehpur,25.88036989,80.80001868,166480,India,IN,IND,Uttar Pradesh
Faizabad,Faizabad,26.75039431,82.17001257,153047,India,IN,IND,Uttar Pradesh
Bahraich,Bahraich,27.62041872,81.66993974,182218,India,IN,IND,Uttar Pradesh
Mirzapur,Mirzapur,25.145376,82.56998816,239754,India,IN,IND,Uttar Pradesh
Jhansi,Jhansi,25.45295412,78.55746822,619710.5,India,IN,IND,Uttar Pradesh
Shahjahanpur,Shahjahanpur,27.88037701,79.90503454,320434,India,IN,IND,Uttar Pradesh
Rampur,Rampur,28.8153587,79.0249849,296418,India,IN,IND,Uttar Pradesh
Bareilly,Bareilly,28.34538739,79.41999955,781217.5,India,IN,IND,Uttar Pradesh
Etawah,Etawah,26.78545677,79.01495968,257448,India,IN,IND,Uttar Pradesh
Dehra Dun,Dehra Dun,30.32040895,78.05000565,646321.5,India,IN,IND,Uttaranchal
Haora,Haora,22.58039044,88.32994665,2934655,India,IN,IND,West Bengal
Alipur Duar,Alipur Duar,26.48374392,89.56666703,127342,India,IN,IND,West Bengal
Haldia,Haldia,22.02566978,88.05833533,200762,India,IN,IND,West Bengal
Bhatpara,Bhatpara,22.85042564,88.52001257,483129,India,IN,IND,West Bengal
Medinipur,Medinipur,22.3304057,87.15001868,169127,India,IN,IND,West Bengal
Siliguri,Siliguri,26.72042198,88.45500362,515574,India,IN,IND,West Bengal
Purnia,Purnia,25.78541445,87.4799727,198453,India,IN,IND,Bihar
Muzaffarpur,Muzaffarpur,26.12043276,85.37994584,333200,India,IN,IND,Bihar
Aurangabad,Aurangabad,24.7704118,84.38000688,95929,India,IN,IND,Bihar
Bilaspur,Bilaspur,22.09042035,82.15998734,436780,India,IN,IND,Chhattisgarh
Burhanpur,Burhanpur,21.30039105,76.13001949,197233,India,IN,IND,Madhya Pradesh
Ujjain,Ujjain,23.19040489,75.79004024,485348,India,IN,IND,Madhya Pradesh
Ratlam,Ratlam,23.35039512,75.02998328,272036,India,IN,IND,Madhya Pradesh
Sagar,Sagar,23.85039044,78.75001461,287786.5,India,IN,IND,Madhya Pradesh
Vellore,Vellore,12.92038576,79.15004187,177081,India,IN,IND,Tamil Nadu
Tiruvannamalai,Tiruvannamalai,12.26037437,79.09996741,138243,India,IN,IND,Tamil Nadu
Rajapalaiyam,Rajapalaiyam,9.420392679,77.5800085,338975,India,IN,IND,Tamil Nadu
Cuddalore,Cuddalore,11.72040733,79.77000403,158569,India,IN,IND,Tamil Nadu
Karur,Karur,10.95037681,78.08333695,76915,India,IN,IND,Tamil Nadu
Kanchipuram,Kanchipuram,12.83372438,79.71667395,155029,India,IN,IND,Tamil Nadu
Tirunelveli,Tirunelveli,8.730408955,77.68997595,489022,India,IN,IND,Tamil Nadu
Nagercoil,Nagercoil,8.180365009,77.42999182,219093.5,India,IN,IND,Tamil Nadu
Thanjavur,Thanjavur,10.77041363,79.15004187,219571,India,IN,IND,Tamil Nadu
Kumbakonam,Kumbakonam,10.98047833,79.40000077,139264,India,IN,IND,Tamil Nadu
Valparai,Valparai,10.32041526,76.96996822,102330.5,India,IN,IND,Tamil Nadu
Tiruppur,Tiruppur,11.08042055,77.32999792,547271.5,India,IN,IND,Tamil Nadu
Daman,Daman,20.41700828,72.85001298,39737,India,IN,IND,Dadra and Nagar Haveli
Navsari,Navsari,20.85039268,72.92003454,163000,India,IN,IND,Dadra and Nagar Haveli
Bhuj,Bhuj,23.25037539,69.80999182,289429,India,IN,IND,Dadra and Nagar Haveli
Bhavnagar,Bhavnagar,21.77842389,72.12995357,509790,India,IN,IND,Dadra and Nagar Haveli
Gandhinagar,Gandhinagar,23.30039817,72.63994828,195891,India,IN,IND,Dadra and Nagar Haveli
Itanagar,Itanagar,27.10039878,93.61660071,44971,India,IN,IND,Arunachal Pradesh
Aizawl,Aizawl,23.71039899,92.72001461,274176,India,IN,IND,Mizoram
Agartala,Agartala,23.83540428,91.27999914,203264,India,IN,IND,Tripura
Kakinada,Kakinada,16.96747723,82.23750199,292923,India,IN,IND,Andhra Pradesh
Warangal,Warangal,18.00999758,79.57998979,1034690,India,IN,IND,Andhra Pradesh
Brahmapur,Brahmapur,19.31999514,84.79998124,324726,India,IN,IND,Orissa
Bijapur,Bijapur,16.83541811,75.70999345,270967,India,IN,IND,Karnataka
Bhiwandi,Bhiwandi,19.35001914,73.12999589,751017.5,India,IN,IND,Maharashtra
Latur,Latur,18.40041302,76.56999263,361680.5,India,IN,IND,Maharashtra
Ahmednagar,Ahmednagar,19.11042137,74.75000037,379450,India,IN,IND,Maharashtra
Chandrapur,Chandrapur,19.9699813,79.30000688,461734.5,India,IN,IND,Maharashtra
Amravati,Amravati,20.94997316,77.77002274,669144,India,IN,IND,Maharashtra
Dhule,Dhule,20.89997622,74.76999914,423026.5,India,IN,IND,Maharashtra
Dibrugarh,Dibrugarh,27.48332115,94.8999849,144260.5,India,IN,IND,Assam
Imphal,Imphal,24.79997072,93.95001705,244254.5,India,IN,IND,Manipur
Udaipur,Udaipur,24.59998293,73.73001094,446260.5,India,IN,IND,Rajasthan
Gorakhpur,Gorakhpur,26.75039431,83.38001623,674246,India,IN,IND,Uttar Pradesh
Barddhaman,Barddhaman,23.25037539,87.86496212,301725,India,IN,IND,West Bengal
Krishnanagar,Krishnanagar,23.38034161,88.5300378,145926,India,IN,IND,West Bengal
Gaya,Gaya,24.79997072,85.00002071,423692,India,IN,IND,Bihar
Porbandar,Porbandar,21.6699809,69.67000037,186778,India,IN,IND,Dadra and Nagar Haveli
Nellore,Nellore,14.43998293,79.98993892,541081,India,IN,IND,Andhra Pradesh
Kurnool,Kurnool,15.83000144,78.03000688,351522,India,IN,IND,Andhra Pradesh
Guntur,Guntur,16.32999676,80.4500142,530577,India,IN,IND,Andhra Pradesh
Tumkur,Tumkur,13.32997316,77.1000378,353482.5,India,IN,IND,Karnataka
Davangere,Davangere,14.47000694,75.92000647,469344.5,India,IN,IND,Karnataka
Bellary,Bellary,15.15004295,76.91503617,391034.5,India,IN,IND,Karnataka
Belgaum,Belgaum,15.86501223,74.5050024,609472.5,India,IN,IND,Karnataka
Tuticorin,Tuticorin,8.81999005,78.13000077,436094,India,IN,IND,Tamil Nadu
Dindigul,Dindigul,10.37997235,78.00003454,200797,India,IN,IND,Tamil Nadu
Chandigarh,Chandigarh,30.71999697,76.78000565,946685.5,India,IN,IND,Chandigarh
Jammu,Jammu,32.71178754,74.84673865,628283.5,India,IN,IND,Jammu and Kashmir
Sholapur,Sholapur,17.6704059,75.90000769,1009056,India,IN,IND,Maharashtra
Aurangabad,Aurangabad,19.89569643,75.32030147,1064720.5,India,IN,IND,Maharashtra
Nasik,Nasik,20.00041872,73.77998205,1381248.5,India,IN,IND,Maharashtra
Dispur,Dispur,26.14402305,91.76663611,16140,India,IN,IND,Assam
Jullundur,Jullundur,31.33492067,75.56902014,820089,India,IN,IND,Punjab
Allahabad,Allahabad,25.45499534,81.84000688,1137219,India,IN,IND,Uttar Pradesh
Moradabad,Moradabad,28.8417912,78.75678422,754069.5,India,IN,IND,Uttar Pradesh
Ghaziabad,Ghaziabad,28.66038108,77.40839107,1270095.5,India,IN,IND,Uttar Pradesh
Agra,Agra,27.17042035,78.01502071,1511027.5,India,IN,IND,Uttar Pradesh
Aligarh,Aligarh,27.89221092,78.06178788,779103.5,India,IN,IND,Uttar Pradesh
Meerut,Meerut,29.00041201,77.70000118,1310592,India,IN,IND,Uttar Pradesh
Dhanbad,Dhanbad,23.80039349,86.41998572,732818,India,IN,IND,Jharkhand
Gwalior,Gwalior,26.2299868,78.18007523,930229,India,IN,IND,Madhya Pradesh
Vadodara,Vadodara,22.31001935,73.18001868,1582738,India,IN,IND,Dadra and Nagar Haveli
Rajkot,Rajkot,22.31001935,70.80000891,1179941,India,IN,IND,Dadra and Nagar Haveli
Faridabad,Faridabad,28.4333333,77.3166667,1394000,India,IN,IND,Haryana
Srinagar,Srinagar,34.09997154,74.81500932,1057928.5,India,IN,IND,Jammu and Kashmir
Vijayawada,Vijayawada,16.51995933,80.63000321,1005793.5,India,IN,IND,Andhra Pradesh
Thiruvananthapuram,Thiruvananthapuram,8.499983743,76.95002112,869076.5,India,IN,IND,Kerala
Kochi,Kochi,10.01500755,76.22391557,1061848,India,IN,IND,Kerala
Cuttack,Cuttack,20.47000246,85.88994055,580000,India,IN,IND,Orissa
Hubli,Hubli,15.35997845,75.12501623,841402,India,IN,IND,Karnataka
Mangalore,Mangalore,12.90002525,74.84999426,597009.5,India,IN,IND,Karnataka
Mysore,Mysore,12.30998374,76.66001298,877656.5,India,IN,IND,Karnataka
Gulbarga,Gulbarga,17.34996035,76.82000321,482546.5,India,IN,IND,Karnataka
Kolhapur,Kolhapur,16.70000002,74.22000688,655920.5,India,IN,IND,Maharashtra
Nanded,Nanded,19.16997845,77.30002559,587136,India,IN,IND,Maharashtra
Akola,Akola,20.70998781,77.01001745,466179.5,India,IN,IND,Maharashtra
Guwahati,Guwahati,26.16001691,91.76999508,500258,India,IN,IND,Assam
Ludhiana,Ludhiana,30.92776206,75.87225745,1597184,India,IN,IND,Punjab
Kota,Kota,25.17999921,75.83499874,795044,India,IN,IND,Rajasthan
Jodhpur,Jodhpur,26.29176597,73.01677283,958238,India,IN,IND,Rajasthan
Lucknow,Lucknow,26.85503908,80.91499874,2583505.5,India,IN,IND,Uttar Pradesh
Saharanpur,Saharanpur,29.97001691,77.55003617,484873,India,IN,IND,Uttar Pradesh
Ranchi,Ranchi,23.37000633,85.33002641,945227,India,IN,IND,Jharkhand
Bhagalpur,Bhagalpur,25.22999615,86.98000321,361548,India,IN,IND,Bihar
Raipur,Raipur,21.23499453,81.63500647,777497.5,India,IN,IND,Chhattisgarh
Jabalpur,Jabalpur,23.17505699,79.95505733,1157584,India,IN,IND,Madhya Pradesh
Indore,Indore,22.71505922,75.86502274,1931520.5,India,IN,IND,Madhya Pradesh
Pondicherry,Pondicherry,11.93499371,79.83000037,227411,India,IN,IND,Puducherry
Salem,Salem,11.66999697,78.18007523,825698,India,IN,IND,Tamil Nadu
Tiruchirappalli,Tiruchirappalli,10.80999778,78.68996659,863242,India,IN,IND,Tamil Nadu
Kozhikode,Kozhikode,11.25043601,75.76998979,696461,India,IN,IND,Kerala
Bhubaneshwar,Bhubaneshwar,20.27042808,85.82736039,803121.5,India,IN,IND,Orissa
Jamshedpur,Jamshedpur,22.78753542,86.19751868,958169,India,IN,IND,Jharkhand
Vishakhapatnam,Vishakhapatnam,17.73001467,83.30498205,1296089,India,IN,IND,Andhra Pradesh
Amritsar,Amritsar,31.63999249,74.86999304,1152225,India,IN,IND,Punjab
Varanasi,Varanasi,25.32999005,83.00003943,1258202,India,IN,IND,Uttar Pradesh
Asansol,Asansol,23.6833333,86.9833333,1328000,India,IN,IND,West Bengal
Bhilai,Bhilai,21.2166667,81.4333333,1097000,India,IN,IND,Chhattisgarh
Bhopal,Bhopal,23.24998781,77.40999304,1663457,India,IN,IND,Madhya Pradesh
Madurai,Madurai,9.920026264,78.12002722,1101954,India,IN,IND,Tamil Nadu
Coimbatore,Coimbatore,10.99996035,76.95002112,1327911.5,India,IN,IND,Tamil Nadu
Delhi,Delhi,28.6699929,77.23000403,11779606.5,India,IN,IND,Delhi
Hyderabad,Hyderabad,17.39998313,78.47995357,4986908,India,IN,IND,Andhra Pradesh
Pune,Pune,18.53001752,73.85000362,3803872,India,IN,IND,Maharashtra
Nagpur,Nagpur,21.16995974,79.08999385,2341009,India,IN,IND,Maharashtra
Jaipur,Jaipur,26.92113324,75.80998734,2814379,India,IN,IND,Rajasthan
Kanpur,Kanpur,26.4599986,80.3199963,2992624.5,India,IN,IND,Uttar Pradesh
Patna,Patna,25.62495913,85.13003861,1878960,India,IN,IND,Bihar
Chennai,Chennai,13.08998781,80.27999874,5745531.5,India,IN,IND,Tamil Nadu
Ahmedabad,Ahmedabad,23.03005292,72.58000362,4547355,India,IN,IND,Dadra and Nagar Haveli
Surat,Surat,21.19998374,72.84003943,3368252,India,IN,IND,Dadra and Nagar Haveli
New Delhi,New Delhi,28.60002301,77.19998002,317797,India,IN,IND,Delhi
Bangalore,Bangalore,12.96999514,77.56000972,5945523.5,India,IN,IND,Karnataka
Mumbai,Mumbai,19.01699038,72.8569893,15834918,India,IN,IND,Maharashtra
Kolkata,Kolkata,22.4949693,88.32467566,9709196,India,IN,IND,West Bengal
Binjai,Binjai,3.620359109,98.50007524,405494.5,Indonesia,ID,IDN,Sumatera Utara
Padangsidempuan,Padangsidempuan,1.388738219,99.27336137,183721.5,Indonesia,ID,IDN,Sumatera Utara
Tarutung,Tarutung,2.017071959,98.96666174,1305,Indonesia,ID,IDN,Sumatera Utara
Tebingtinggi,Tebingtinggi,3.33037681,99.13001094,192786.5,Indonesia,ID,IDN,Sumatera Utara
Tidore,Tidore,0.696377379,127.4359834,60611,Indonesia,ID,IDN,Maluku Utara
Bukittinggi,Bukittinggi,-0.303148174,100.3614603,302855,Indonesia,ID,IDN,Sumatera Barat
Sawahlunto,Sawahlunto,-0.666278464,100.7833467,50354,Indonesia,ID,IDN,Sumatera Barat
Padangpanjang,Padangpanjang,-0.449599183,100.4166508,44096,Indonesia,ID,IDN,Sumatera Barat
Amahai,Amahai,-3.328131491,128.9404911,26172.5,Indonesia,ID,IDN,Maluku
Mataram,Mataram,-8.579542217,116.1350195,409041.5,Indonesia,ID,IDN,Nusa Tenggara Barat
Praya,Praya,-8.7223242,116.2923226,35183,Indonesia,ID,IDN,Nusa Tenggara Barat
Baubau,Baubau,-5.469861228,122.6163293,24412,Indonesia,ID,IDN,Sulawesi Tenggara
Luwuk,Luwuk,-0.939595114,122.7900138,43550.5,Indonesia,ID,IDN,Sulawesi Tengah
Poso,Poso,-1.389593487,120.7600085,41507,Indonesia,ID,IDN,Sulawesi Tengah
Biak,Biak,-1.161493715,136.048481,103610,Indonesia,ID,IDN,Papua
Timika,Timika,-4.549607321,136.88998,26021,Indonesia,ID,IDN,Papua
Langsa,Langsa,4.673576476,97.96636104,117256,Indonesia,ID,IDN,Aceh
Indramayu,Indramayu,-6.335648174,108.3190108,123263,Indonesia,ID,IDN,Jawa Barat
Sukabumi,Sukabumi,-6.909618308,106.899976,276414,Indonesia,ID,IDN,Jawa Barat
Cilacap,Cilacap,-7.718819561,109.0154024,1174964,Indonesia,ID,IDN,Jawa Tengah
Pati,Pati,-6.741514873,111.034659,122785,Indonesia,ID,IDN,Jawa Tengah
Pakalongan,Pakalongan,-6.8795943,109.6700394,264972.5,Indonesia,ID,IDN,Jawa Tengah
Tegal,Tegal,-6.869569073,109.1199955,237084,Indonesia,ID,IDN,Jawa Tengah
Salatiga,Salatiga,-7.309542217,110.4900927,174322.5,Indonesia,ID,IDN,Jawa Tengah
Magelang,Magelang,-7.469584128,110.1799825,111461,Indonesia,ID,IDN,Jawa Tengah
Serang,Serang,-6.109977194,106.1496342,164767,Indonesia,ID,IDN,Banten
Bekasi,Bekasi,-6.217257468,106.972323,1949165,Indonesia,ID,IDN,Jakarta Raya
Singkawang,Singkawang,0.911980927,108.9654697,174925,Indonesia,ID,IDN,Kalimantan Barat
Bandar Lampung,Tanjungkarang-Telubketung,-5.449604066,105.3000219,881801,Indonesia,ID,IDN,Lampung
Perabumulih,Perabumulih,-3.443163229,104.2314567,83754,Indonesia,ID,IDN,Sumatera Selatan
Kuta,Kuta,-8.715112509,115.1841208,22879.5,Indonesia,ID,IDN,Bali
Singaraja,Singaraja,-8.115199274,115.094398,184126,Indonesia,ID,IDN,Bali
Sumenep,Sumenep,-7.004909649,113.8496293,84656,Indonesia,ID,IDN,Jawa Timur
Banyuwangi,Banyuwangi,-8.195017884,114.3695975,140295,Indonesia,ID,IDN,Jawa Timur
Tuban,Tuban,-6.899541403,112.0499975,76242,Indonesia,ID,IDN,Jawa Timur
Probolinggo,Probolinggo,-7.749618715,113.1500337,181656,Indonesia,ID,IDN,Jawa Timur
Pasuruan,Pasuruan,-7.629574362,112.9000232,343161,Indonesia,ID,IDN,Jawa Timur
Mojokerto,Mojokerto,-7.469584128,112.4299743,112557,Indonesia,ID,IDN,Jawa Timur
Madiun,Madiun,-7.634586976,111.5149914,186099,Indonesia,ID,IDN,Jawa Timur
Kediri,Kediri,-7.789616273,112.0000264,235143,Indonesia,ID,IDN,Jawa Timur
Blitar,Blitar,-8.069599183,112.1499914,132416,Indonesia,ID,IDN,Jawa Timur
Waingapu,Waingapu,-9.658236065,120.253011,35990.5,Indonesia,ID,IDN,Nusa Tenggara Timur
Maumere,Maumere,-8.618867982,122.212323,75941.5,Indonesia,ID,IDN,Nusa Tenggara Timur
Ende,Ende,-8.862315655,121.6489465,60930,Indonesia,ID,IDN,Nusa Tenggara Timur
Makale,Makale,-3.09682778,119.8530871,9960,Indonesia,ID,IDN,Sulawesi Selatan
Palopo,Palopo,-3.099928366,120.2363195,2444,Indonesia,ID,IDN,Sulawesi Selatan
Watampone,Watampone,-4.532812481,120.3333679,58953,Indonesia,ID,IDN,Sulawesi Selatan
Pinrang,Pinrang,-3.785726299,119.6522208,182731,Indonesia,ID,IDN,Sulawesi Selatan
Majene,Majene,-3.533596986,118.9660095,155046,Indonesia,ID,IDN,Sulawesi Barat
Tanjungpinang,Tanjungpinang,0.916829039,104.471442,176069,Indonesia,ID,IDN,Kepulauan Riau
Telukbutun,Telukbutun,4.216989358,108.2,140,Indonesia,ID,IDN,Kepulauan Riau
Sungaipenuh,Sungaipenuh,-2.063144105,101.3964359,56773,Indonesia,ID,IDN,Jambi
Sampit,Sampit,-2.532934551,112.9500459,79381.5,Indonesia,ID,IDN,Kalimantan Tengah
Kualakapuas,Kualakapuas,-3.099618308,114.3500122,18512.5,Indonesia,ID,IDN,Kalimantan Tengah
Palangkaraya,Palangkaraya,-2.209595114,113.9099873,148289,Indonesia,ID,IDN,Kalimantan Tengah
Bontang,Bontang,0.133259297,117.5000008,101691,Indonesia,ID,IDN,Kalimantan Timur
Denpasar,Denpasar,-8.650028871,115.2199849,569133.5,Indonesia,ID,IDN,Bali
Sorong,Sorong,-0.855414206,131.2849991,125535,Indonesia,ID,IDN,Irian Jaya Barat
Sibolga,Sibolga,1.749982319,98.80000525,148513,Indonesia,ID,IDN,Sumatera Utara
Pematangsiantar,Pematangsiantar,2.961432921,99.061488,275407,Indonesia,ID,IDN,Sumatera Utara
Pekanbaru,Pekanbaru,0.564964212,101.425013,705218,Indonesia,ID,IDN,Riau
Manado,Manado,1.480024637,124.8499914,449497.5,Indonesia,ID,IDN,Sulawesi Utara
Yogyakarta,Yogyakarta,-7.77995278,110.3750093,636660,Indonesia,ID,IDN,Yogyakarta
Kendari,Kendari,-3.95532835,122.5973124,165377,Indonesia,ID,IDN,Sulawesi Tenggara
Palu,Palu,-0.907038962,119.8330367,473871,Indonesia,ID,IDN,Sulawesi Tengah
Nabire,Nabire,-3.351540915,135.5134232,28834.5,Indonesia,ID,IDN,Papua
Merauke,Merauke,-8.493190899,140.401807,34412,Indonesia,ID,IDN,Papua
Lhokseumawe,Lhokseumawe,5.191400166,97.14145015,114648,Indonesia,ID,IDN,Aceh
Samarinda,Samarinda,-0.500035381,117.1499963,473694,Indonesia,ID,IDN,Kalimantan Timur
Cirebon,Cirebon,-6.733298321,108.5666442,254298,Indonesia,ID,IDN,Jawa Barat
Tasikmalaya,Tasikmalaya,-7.325406882,108.2146761,271143,Indonesia,ID,IDN,Jawa Barat
Bogor,Bogor,-6.570000795,106.7500109,859000,Indonesia,ID,IDN,Jawa Barat
Bengkulu,Bengkulu,-3.800040671,102.2699743,368192.5,Indonesia,ID,IDN,Bengkulu
Pontianak,Pontianak,-0.029986553,109.3199833,578807.5,Indonesia,ID,IDN,Kalimantan Barat
Kotabumi,Kotabumi,-4.833310935,104.8999947,42366,Indonesia,ID,IDN,Lampung
Lahat,Lahat,-3.800040671,103.5333081,50469.5,Indonesia,ID,IDN,Sumatera Selatan
Pangkalpinang,Pangkalpinang,-2.080042298,106.1500476,99785.5,Indonesia,ID,IDN,Bangka-Belitung
Jember,Jember,-8.172693666,113.6873136,298585,Indonesia,ID,IDN,Jawa Timur
Martapura,Martapura,-3.413500957,114.8364941,164844,Indonesia,ID,IDN,Kalimantan Selatan
Ruteng,Ruteng,-8.611839987,120.4698453,44272.5,Indonesia,ID,IDN,Nusa Tenggara Timur
Jambi,Jambi,-1.589994691,103.6100476,438706.5,Indonesia,ID,IDN,Jambi
Manokwari,Manokwari,-0.871123841,134.0692736,63847,Indonesia,ID,IDN,Irian Jaya Barat
Ternate,Ternate,0.792960631,127.3630163,144626,Indonesia,ID,IDN,Maluku Utara
Ambon,Ambon,-3.716686586,128.2000195,227561,Indonesia,ID,IDN,Maluku
Raba,Raba,-8.449989401,118.7666418,106101,Indonesia,ID,IDN,Nusa Tenggara Barat
Jayapura,Jayapura,-2.532986228,140.69998,152118,Indonesia,ID,IDN,Papua
Banda Aceh,Banda Aceh,5.549982929,95.32001094,344065.5,Indonesia,ID,IDN,Aceh
Balikpapan,Balikpapan,-1.250015443,116.8300158,439885.5,Indonesia,ID,IDN,Kalimantan Timur
Surakarta,Surakarta,-7.564978822,110.8250077,555308,Indonesia,ID,IDN,Jawa Tengah
Bandar Lampung,Bandar Lampung,-5.430018698,105.2699979,795757,Indonesia,ID,IDN,Lampung
Tanjungpandan,Tanjungpandan,-2.750027243,107.6500077,61591,Indonesia,ID,IDN,Bangka-Belitung
Malang,Malang,-7.97999225,112.610015,775858,Indonesia,ID,IDN,Jawa Timur
Kupang,Kupang,-10.17866941,123.5829886,270798,Indonesia,ID,IDN,Nusa Tenggara Timur
Parepare,Parepare,-4.016668275,119.6333073,87776,Indonesia,ID,IDN,Sulawesi Selatan
Gorontalo,Gorontalo,0.549978047,123.0700484,254846,Indonesia,ID,IDN,Gorontalo
Padang,Padang,-0.960007305,100.3600134,847676,Indonesia,ID,IDN,Sumatera Barat
Tarakan,Tarakan,3.300016906,117.6330159,145273.5,Indonesia,ID,IDN,Kalimantan Timur
Semarang,Semarang,-6.966617412,110.4200195,1342042,Indonesia,ID,IDN,Jawa Tengah
Palembang,Palembang,-2.980039043,104.7500297,1595250,Indonesia,ID,IDN,Sumatera Selatan
Bandjarmasin,Bandjarmasin,-3.329991843,114.5800756,588206.5,Indonesia,ID,IDN,Kalimantan Selatan
Ujungpandang,Ujungpandang,-5.139958884,119.4320275,1262000,Indonesia,ID,IDN,Sulawesi Selatan
Medan,Medan,3.579973978,98.65004024,1932985.5,Indonesia,ID,IDN,Sumatera Utara
Bandung,Bandung,-6.950029278,107.5700126,2046859.5,Indonesia,ID,IDN,Jawa Barat
Surabaya,Surabaya,-7.249235821,112.7508333,2609829,Indonesia,ID,IDN,Jawa Timur
Jakarta,Jakarta,-6.174417705,106.8294376,8832560.5,Indonesia,ID,IDN,Jakarta Raya
Yasuj,Yasuj,30.65900412,51.59400361,96786,Iran,IR,IRN,Kohgiluyeh and Buyer Ahmad
Shar e Kord,Shar e Kord,32.32099805,50.85399659,129153,Iran,IR,IRN,Chahar Mahall and Bakhtiari
Marv Dasht,Marv Dasht,29.80144838,52.82146806,124429,Iran,IR,IRN,Fars
Shahrud,Shahrud,36.42287884,54.96288773,125304,Iran,IR,IRN,Semnan
Varamin,Varamin,35.31658978,51.64660437,172215,Iran,IR,IRN,Tehran
Masjed Soleyman,Masjed Soleyman,31.97999758,49.2999259,132586.5,Iran,IR,IRN,Khuzestan
Borujerd,Borujerd,33.91995668,48.8000081,251958,Iran,IR,IRN,Lorestan
Malayer,Malayer,34.31998395,48.84997921,176573,Iran,IR,IRN,Hamadan
Zanjan,Zanjan,36.67002138,48.50002641,355012.5,Iran,IR,IRN,Zanjan
Urmia,Orumiyeh,37.52999473,44.99998165,577307,Iran,IR,IRN,West Azarbaijan
Ahar,Ahar,38.48290814,47.06290482,98993.5,Iran,IR,IRN,East Azarbaijan
Sanandaj,Sanandaj,35.30000165,47.02001339,331798,Iran,IR,IRN,Kordestan
Neyshabur,Neyshabur,36.22002301,58.82001664,221314.5,Iran,IR,IRN,Razavi Khorasan
Bojnurd,Bojnurd,37.46999839,57.32000484,200311.5,Iran,IR,IRN,North Khorasan
Sirjan,Sirjan,29.46996991,55.73002437,171007,Iran,IR,IRN,Kerman
Qomsheh,Qomsheh,32.01149436,51.85971798,118301,Iran,IR,IRN,Esfahan
Kashan,Kashan,33.98041811,51.57999345,249394.5,Iran,IR,IRN,Esfahan
Khomeini Shahr,Khomeini Shahr,32.70041872,51.46997432,437138,Iran,IR,IRN,Esfahan
Fasa,Fasa,28.97183494,53.67149369,111259.5,Iran,IR,IRN,Fars
Gonbad-e Kavus,Gonbad-e Kavus,37.25182049,55.17145382,145699,Iran,IR,IRN,Golestan
Gorgan,Gorgan,36.83034751,54.48002315,262980,Iran,IR,IRN,Golestan
Amol,Amol,36.4713255,52.36330481,210516,Iran,IR,IRN,Mazandaran
Sari,Sari,36.55039044,53.10000403,263431.5,Iran,IR,IRN,Mazandaran
Semnan,Semnan,35.5547923,53.37430253,117888,Iran,IR,IRN,Semnan
Karaj,Karaj,35.8003587,50.97000484,1423000,Iran,IR,IRN,Tehran
Behbehan,Behbehan,30.58181419,50.26146928,82517,Iran,IR,IRN,Khuzestan
Dezful,Dezful,32.38038658,48.4700024,315482,Iran,IR,IRN,Khuzestan
Khorramabad,Khorramabad,33.48042279,48.35000972,352511.5,Iran,IR,IRN,Lorestan
Ilam,Ilam,33.63041363,46.43002356,146917,Iran,IR,IRN,Ilam
Saveh,Saveh,35.02182741,50.33143917,145384.5,Iran,IR,IRN,Markazi
Arak,Arak,34.08041201,49.70000484,463449,Iran,IR,IRN,Markazi
Mahabad,Mahabad,36.77037701,45.72004106,153428.5,Iran,IR,IRN,West Azarbaijan
Khvoy,Khvoy,38.53039878,44.97000932,189049,Iran,IR,IRN,West Azarbaijan
Maragheh,Maragheh,37.42038902,46.22001054,151385,Iran,IR,IRN,East Azarbaijan
Qasr-e Shirin,Qasr-e Shirin,34.5123753,45.5772074,11202,Iran,IR,IRN,Kermanshah
Bijar,Bijar,35.87407513,47.59367346,48806,Iran,IR,IRN,Kordestan
Yazdan,Yazdan,33.50649355,60.89379187,1894,Iran,IR,IRN,South Khorasan
Torbat-e Jam,Torbat-e Jam,35.22333966,60.61287878,81753,Iran,IR,IRN,Razavi Khorasan
Quchan,Quchan,37.11182904,58.50148311,128641.5,Iran,IR,IRN,Razavi Khorasan
Chabahar,Chabahar,25.30040529,60.62993201,56544,Iran,IR,IRN,Sistan and Baluchestan
Kashmar,Kashmar,35.18143007,58.45146033,126643,Iran,IR,IRN,Razavi Khorasan
Bam,Bam,29.10769228,58.36195675,99268,Iran,IR,IRN,Kerman
Kerman,Kerman,30.29999676,57.08001949,556518,Iran,IR,IRN,Kerman
Bandar-e Bushehr,Bandar-e Bushehr,28.91997764,50.83001339,167218.5,Iran,IR,IRN,Bushehr
Abadan,Abadan,30.33074424,48.2796781,315129,Iran,IR,IRN,Khuzestan
Ardabil,Ardabil,38.25000246,48.30003861,412678,Iran,IR,IRN,Ardebil
Qom,Qom,34.65001548,50.95000606,933478,Iran,IR,IRN,Qom
Qazvin,Qazvin,36.27001996,49.99998653,399093,Iran,IR,IRN,Qazvin
Kermanshah,Kermanshah,34.38000612,47.06001094,828313,Iran,IR,IRN,Kermanshah
Rasht,Rasht,37.29998293,49.62998328,544737.5,Iran,IR,IRN,Gilan
Birjand,Birjand,32.88002016,59.21994055,260842.5,Iran,IR,IRN,South Khorasan
Sabzewar,Sabzewar,36.22002301,57.63001176,215910.5,Iran,IR,IRN,Razavi Khorasan
Zabol,Zabol,31.02145144,61.48145626,177978.5,Iran,IR,IRN,Sistan and Baluchestan
Zahedan,Zahedan,29.49999392,60.83002315,575433.5,Iran,IR,IRN,Sistan and Baluchestan
Yazd,Yazd,31.92005292,54.37000403,451923.5,Iran,IR,IRN,Yazd
Ahvaz,Ahvaz,31.27998863,48.72001298,918572.5,Iran,IR,IRN,Khuzestan
Bandar-e-Abbas,Bandar-e-Abbas,27.20405978,56.27213554,414503.5,Iran,IR,IRN,Hormozgan
Hamadan,Hamadan,34.79602724,48.51501257,264293,Iran,IR,IRN,Hamadan
Tabriz,Tabriz,38.08629152,46.30124589,1304713,Iran,IR,IRN,East Azarbaijan
Isfahan,Isfahan,32.70000531,51.7000378,1572883,Iran,IR,IRN,Esfahan
Shiraz,Shiraz,29.62996014,52.57001054,1240000,Iran,IR,IRN,Fars
Mashhad,Mashhad,36.27001996,59.5699967,2318126.5,Iran,IR,IRN,Razavi Khorasan
Tehran,Tehran,35.67194277,51.42434403,7513154.5,Iran,IR,IRN,Tehran
Dahuk,Dahuk,36.86670013,43.00000263,620500,Iraq,IQ,IRQ,Dihok
Samarra,Samarra,34.19399705,43.87500062,158508,Iraq,IQ,IRQ,Sala ad-Din
Az Aubayr,Az Aubayr,30.38916445,47.70798173,192447.5,Iraq,IQ,IRQ,Al-Basrah
Ad Diwaniyah,Ad Diwaniyah,31.9889376,44.92396562,338604.5,Iraq,IQ,IRQ,Al-Qadisiyah
Ash Shatrah,Ash Shatrah,31.41752545,46.17722245,122340.5,Iraq,IQ,IRQ,Dhi-Qar
Mandali,Mandali,33.74361086,45.54635657,16420.5,Iraq,IQ,IRQ,Diyala
Ar Ramadi,Ar Ramadi,33.42001304,43.29998205,284830,Iraq,IQ,IRQ,Al-Anbar
Al Musayyib,Al Musayyib,32.778631,44.28999914,59677.5,Iraq,IQ,IRQ,Babil
Zakho,Zakho,37.14454022,42.68720292,114957.5,Iraq,IQ,IRQ,Dihok
Tall Afar,Tall Afar,36.37598248,42.44974971,144465,Iraq,IQ,IRQ,Ninawa
Tikrit,Tikrit,34.59704714,43.67696163,49534,Iraq,IQ,IRQ,Sala ad-Din
Karbala,Karbala,32.61492006,44.02448564,472571,Iraq,IQ,IRQ,Karbala'
As Samawah,As Samawah,31.3098576,45.28027462,163934,Iraq,IQ,IRQ,Al-Muthannia
An Nasiriyah,An Nasiriyah,31.04294883,46.26755286,425898,Iraq,IQ,IRQ,Dhi-Qar
Al Amarah,Al Amarah,31.84160809,47.15116817,334154.5,Iraq,IQ,IRQ,Maysan
Al Kut,Al Kut,32.49071576,45.83037024,318341.5,Iraq,IQ,IRQ,Wasit
As Sulaymaniyah,As Sulaymaniyah,35.56127769,45.43085974,654318,Iraq,IQ,IRQ,As-Sulaymaniyah
Baqubah,Baqubah,33.74764162,44.65726355,226014.5,Iraq,IQ,IRQ,Diyala
Ar Rutbah,Ar Rutbah,33.0384601,40.28445552,17199.5,Iraq,IQ,IRQ,Al-Anbar
Al Fallujah,Al Fallujah,33.34766604,43.77726558,210989,Iraq,IQ,IRQ,Al-Anbar
Al Hillah,Al Hillah,32.47213808,44.42172237,479652.5,Iraq,IQ,IRQ,Babil
Irbil,Irbil,36.1790436,44.00862097,795870,Iraq,IQ,IRQ,Arbil
Kirkuk,Kirkuk,35.4722392,44.3922668,555052.5,Iraq,IQ,IRQ,At-Ta'mim
Mosul,Mosul,36.34500246,43.14500443,1228467,Iraq,IQ,IRQ,Ninawa
An Najaf,An Najaf,32.00033225,44.33537105,612776,Iraq,IQ,IRQ,An-Najaf
Basra,Basra,30.51352378,47.81355668,870000,Iraq,IQ,IRQ,Al-Basrah
Baghdad,Baghdad,33.3386485,44.39386877,5054000,Iraq,IQ,IRQ,Baghdad
Ros Comain,Ros Comain,53.6333333,-8.1833333,4860,Ireland,IE,IRL,Roscommon
Muineachan,Muineachan,54.25,-6.9666667,5937,Ireland,IE,IRL,Monaghan
Shannon,Shannon,52.7038489,-8.864146567,8143.5,Ireland,IE,IRL,Clare
Waterford,Waterford,52.2582947,-7.111927939,49275,Ireland,IE,IRL,Kilkenny
Tralee,Tralee,52.26669212,-9.716652671,24662.5,Ireland,IE,IRL,Kerry
Donegal,Donegal,54.65000917,-8.116672812,2229,Ireland,IE,IRL,Donegal
Drogheda,Drogheda,53.71926495,-6.347762697,34987,Ireland,IE,IRL,Louth
Dundalk,Dundalk,54.00041058,-6.416673219,38884,Ireland,IE,IRL,Louth
Galway,Galway,53.272393,-9.048812298,73140,Ireland,IE,IRL,Galway
Kilkenny,Kilkenny,52.65454958,-7.252255291,21401,Ireland,IE,IRL,Kilkenny
Killarney,Killarney,52.05040041,-9.516664878,9601,Ireland,IE,IRL,Kerry
Sligo,Sligo,54.26706097,-8.483317099,17214,Ireland,IE,IRL,Sligo
Cork,Cork,51.89860089,-8.49577112,162852,Ireland,IE,IRL,Cork
Limerick,Limerick,52.664704,-8.623050172,84066,Ireland,IE,IRL,Limerick
Dublin,Dublin,53.33306114,-6.248905682,1013988,Ireland,IE,IRL,Dublin
Douglas,Douglas,54.15042727,-4.480021404,31036,Isle of Man,IM,IMN,
Ramla,Ramla,31.91670012,34.86670252,63860,Israel,IL,ISR,HaMerkaz
Beer Sheva,Beer Sheva,31.2500163,34.8300081,196504,Israel,IL,ISR,HaDarom
Haifa,Haifa,32.8204114,34.98002478,639150,Israel,IL,ISR,Haifa
Nazareth,Nazareth,32.70398439,35.2955094,108129.5,Israel,IL,ISR,HaZafon
Jerusalem,Jerusalem,31.77840782,35.20662593,915150,Israel,IL,ISR,Jerusalem
Tel Aviv-Yafo,Tel Aviv-Yafo,32.07999147,34.77001176,1745179,Israel,IL,ISR,Tel Aviv
Potenza,Potenza,40.64200213,15.7989965,69060,Italy,IT,ITA,Basilicata
Campobasso,Campobasso,41.56299912,14.65599656,50762,Italy,IT,ITA,Molise
Aosta,Aosta,45.73700107,7.315002596,34062,Italy,IT,ITA,Valle d'Aosta
Modena,Modena,44.65002525,10.91999467,175034.5,Italy,IT,ITA,Emilia-Romagna
Crotone,Crotone,39.08333661,17.12333695,59313.5,Italy,IT,ITA,Calabria
Vibo Valentia,Vibo Valentia,38.66659202,16.10004024,32168,Italy,IT,ITA,Calabria
Reggio di Calabria,Reggio di Calabria,38.11499778,15.64136023,179034.5,Italy,IT,ITA,Calabria
Caserta,Caserta,41.05996014,14.33735714,164744,Italy,IT,ITA,Campania
Barletta,Barletta,41.31999595,16.27000403,99962,Italy,IT,ITA,Apulia
Ragusa,Ragusa,36.93003135,14.72999467,67361,Italy,IT,ITA,Sicily
Asti,Asti,44.92998232,8.209979206,63410.5,Italy,IT,ITA,Piemonte
Novara,Novara,45.45000226,8.61998002,88966,Italy,IT,ITA,Piemonte
Como,Como,45.81000612,9.08000362,167438,Italy,IT,ITA,Lombardia
Udine,Udine,46.07001609,13.2400081,107019.5,Italy,IT,ITA,Friuli-Venezia Giulia
Treviso,Treviso,45.67001467,12.24001745,128726.5,Italy,IT,ITA,Veneto
Parma,Parma,44.81042889,10.32003129,164734,Italy,IT,ITA,Emilia-Romagna
Ravenna,Ravenna,44.42037518,12.22001868,124302.5,Italy,IT,ITA,Emilia-Romagna
Ferrara,Ferrara,44.85042645,11.60992672,121754,Italy,IT,ITA,Emilia-Romagna
Bologna,Bologna,44.50042198,11.34002071,429694.5,Italy,IT,ITA,Emilia-Romagna
Olbia,Olbia,40.9142849,9.515071858,44341,Italy,IT,ITA,Sardegna
Cagliari,Cagliari,39.22239789,9.103981485,227880,Italy,IT,ITA,Sardegna
Pisa,Pisa,43.72046958,10.40002641,146515,Italy,IT,ITA,Toscana
Livorno,Livorno,43.55113366,10.3022747,145016.5,Italy,IT,ITA,Toscana
Siena,Siena,43.31703168,11.34999426,48731,Italy,IT,ITA,Toscana
Arezzo,Arezzo,43.46172569,11.87497514,82613,Italy,IT,ITA,Toscana
Catanzaro,Catanzaro,38.9003762,16.60000972,90541,Italy,IT,ITA,Calabria
Salerno,Salerno,40.68039675,14.76994055,546922,Italy,IT,ITA,Campania
Benevento,Benevento,41.13370241,14.74999345,59280,Italy,IT,ITA,Campania
Bari,Bari,41.1142204,16.87275793,408554.5,Italy,IT,ITA,Apulia
Foggia,Foggia,41.46047833,15.55996985,147028,Italy,IT,ITA,Apulia
Lecce,Lecce,40.36039044,18.14999263,122942.5,Italy,IT,ITA,Apulia
Brindisi,Brindisi,40.64034751,17.93000606,96759,Italy,IT,ITA,Apulia
Taranto,Taranto,40.50839174,17.22999711,148807,Italy,IT,ITA,Apulia
Messina,Messina,38.2004706,15.5499963,224047.5,Italy,IT,ITA,Sicily
Marsala,Marsala,37.80540428,12.43866166,60481.5,Italy,IT,ITA,Sicily
Siracusa,Siracusa,37.0703587,15.28996049,123110,Italy,IT,ITA,Sicily
Pescara,Pescara,42.45543052,14.21865637,215537.5,Italy,IT,ITA,Abruzzo
L'Aquila,L'Aquila,42.35039817,13.39002478,62201.5,Italy,IT,ITA,Abruzzo
Civitavecchia,Civitavecchia,42.10041343,11.79999263,55674,Italy,IT,ITA,Lazio
Ancona,Ancona,43.60037355,13.49994055,95599,Italy,IT,ITA,Marche
Perugia,Perugia,43.11037762,12.38998246,141998,Italy,IT,ITA,Umbria
Bergamo,Bergamo,45.70040041,9.669993448,160658,Italy,IT,ITA,Lombardia
Trieste,Trieste,45.65037762,13.80002559,213609.5,Italy,IT,ITA,Friuli-Venezia Giulia
Bolzano,Bolzano,46.5004291,11.36001949,95442,Italy,IT,ITA,Trentino-Alto Adige
Trento,Trento,46.08042889,11.11998246,106377,Italy,IT,ITA,Trentino-Alto Adige
Verona,Verona,45.44039044,10.99001623,300333.5,Italy,IT,ITA,Veneto
Sassari,Sassari,40.73000612,8.57000891,102822.5,Italy,IT,ITA,Sardegna
Turin,Turin,45.07038719,7.669960489,1258631.5,Italy,IT,ITA,Piemonte
Genoa,Genoa,44.40998822,8.930038614,624724,Italy,IT,ITA,Liguria
Florence,Florence,43.78000083,11.25000036,935758.5,Italy,IT,ITA,Toscana
Catania,Catania,37.49997072,15.07999914,482908,Italy,IT,ITA,Sicily
Venice,Venice,45.43865928,12.33499874,270816,Italy,IT,ITA,Veneto
Palermo,Palermo,38.12502301,13.35002722,767587.5,Italy,IT,ITA,Sicily
Naples,Naples,40.84002525,14.24501135,1619486,Italy,IT,ITA,Campania
Milan,Milan,45.4699752,9.20500891,2125830.5,Italy,IT,ITA,Lombardia
Rome,Rome,41.89595563,12.48325842,1687226,Italy,IT,ITA,Lazio
Touba,Touba,8.280000029,-7.684001549,27504,Ivory Coast,CI,CIV,Bafing
Bouafle,Bouafle,6.977997104,-5.748002428,60962,Ivory Coast,CI,CIV,Marahou?
Divo,Divo,5.839002037,-5.360003483,127867,Ivory Coast,CI,CIV,Sud-Bandama
Toumodi,Toumodi,6.552000132,-5.019002394,39005,Ivory Coast,CI,CIV,Lacs
Aboisso,Aboisso,5.466699052,-3.20000353,37654,Ivory Coast,CI,CIV,Sud-Como?
Ferkessedougou,Ferkessedougou,9.600407531,-5.200029136,57410,Ivory Coast,CI,CIV,Savanes
Odienne,Odienne,9.510413024,-7.580013063,34488,Ivory Coast,CI,CIV,Dengu?l?
Man,Man,7.400412617,-7.549989056,143157.5,Ivory Coast,CI,CIV,Dix-Huit Montagnes
Seguela,Seguela,7.950404886,-6.670016929,31880,Ivory Coast,CI,CIV,Worodougou
Gagnoa,Gagnoa,6.150411396,-5.879987632,111188,Ivory Coast,CI,CIV,Fromager
Soubre,Soubre,5.790407531,-6.610020591,83712.5,Ivory Coast,CI,CIV,Bas-Sassandra
San-Pedro,San-Pedro,4.77041811,-6.639967083,203512,Ivory Coast,CI,CIV,Bas-Sassandra
Sassandra,Sassandra,4.950381286,-6.083282716,30842.5,Ivory Coast,CI,CIV,Bas-Sassandra
Bondoukou,Bondoukou,8.030425841,-2.800020591,38501.5,Ivory Coast,CI,CIV,Zanzan
Agboville,Agboville,5.940346699,-4.280033611,73027.5,Ivory Coast,CI,CIV,Agn?by
Dimbokro,Dimbokro,6.650458393,-4.710007366,46467.5,Ivory Coast,CI,CIV,N'zi-Como?
Grand Bassam,Grand Bassam,5.200391865,-3.749988445,61226.5,Ivory Coast,CI,CIV,Lagunes
Dabou,Dabou,5.320358703,-4.389949383,71287,Ivory Coast,CI,CIV,Lagunes
Guiglo,Guiglo,6.550464497,-7.48996688,37490,Ivory Coast,CI,CIV,Moyen-Cavally
Abengourou,Abengourou,6.730375996,-3.490004315,87809,Ivory Coast,CI,CIV,Moyen-Comoe
Korhogo,Korhogo,9.459976826,-5.639950604,172535,Ivory Coast,CI,CIV,Savanes
Daloa,Daloa,6.889978657,-6.450004518,235410,Ivory Coast,CI,CIV,Haut-Sassandra
Bouake,Bouake,7.689981505,-5.030013673,511151,Ivory Coast,CI,CIV,Vall?e du Bandama
Yamoussoukro,Yamoussoukro,6.81838096,-5.275502565,200514.5,Ivory Coast,CI,CIV,Lacs
Abidjan,Abidjan,5.319996967,-4.04004826,3496197.5,Ivory Coast,CI,CIV,Lagunes
Lucea,Lucea,18.44299809,-78.17900362,6289,Jamaica,JM,JAM,Hanover
Mandeville,Mandeville,18.03300305,-77.49999851,47115,Jamaica,JM,JAM,Manchester
Black River,Black River,18.03099607,-77.85199748,4229,Jamaica,JM,JAM,Saint Elizabeth
Falmouth,Falmouth,18.47958305,-77.6560496,7779,Jamaica,JM,JAM,Trelawny
Savanna-la-Mar,Savanna La Mar,18.1639981,-77.94800051,25260.5,Jamaica,JM,JAM,Westmoreland
Port Antonio,Port Antonio,18.15900314,-76.38000262,14400,Jamaica,JM,JAM,Portland
St. Ann's Bay,St. Anns Bay,18.43263914,-77.19952454,13671,Jamaica,JM,JAM,Saint Ann
Port Maria,Port Maria,18.37700105,-76.89999547,7906,Jamaica,JM,JAM,Saint Mary
Half Way Tree,Halfway Tree,18.0333001,-76.79999651,96494,Jamaica,JM,JAM,Saint Andrew
Port Morant,Port Morant,17.89100103,-76.32899957,11536,Jamaica,JM,JAM,Saint Thomas
May Pen,May Pen,17.96661521,-77.23328089,89948.5,Jamaica,JM,JAM,Clarendon
Spanish Town,Spanish Town,17.98333254,-76.94999068,297531.5,Jamaica,JM,JAM,Saint Catherine
Montego Bay,Montego Bay,18.46668805,-77.91667586,104437.5,Jamaica,JM,JAM,Saint James
Kingston,Kingston,17.97707662,-76.76743371,801336.5,Jamaica,JM,JAM,Kingston
Okayama,Okayama,34.67202964,133.9170865,752872,Japan,JP,JPN,Okayama
Shimonoseki,Shimonoseki,33.96543194,130.9454333,236198.5,Japan,JP,JPN,Yamaguchi
Kanoya,Kanoya,31.38331565,130.8500386,68513.5,Japan,JP,JPN,Kagoshima
Takamatsu,Takamatsu,34.34473696,134.044779,329861.5,Japan,JP,JPN,Kagawa
Tokushima,Tokushima,34.06738955,134.5525,355552.5,Japan,JP,JPN,Tokushima
Toyama,Toyama,36.69999371,137.2300109,329172,Japan,JP,JPN,Toyama
Takaoka,Takaoka,36.67002138,136.9999991,124437,Japan,JP,JPN,Toyama
Otsu,Otsu,35.006402,135.8674068,437802.5,Japan,JP,JPN,Shiga
Maebashi,Maebashi,36.39269981,139.0726892,313791,Japan,JP,JPN,Gunma
Kawasaki,Kawasaki,35.52998761,139.705002,1372025.5,Japan,JP,JPN,Kanagawa
Kawagoe,Kawagoe,35.91769004,139.4910616,337931,Japan,JP,JPN,Saitama
Utsunomiya,Utsunomiya,36.54997703,139.8700048,558808.5,Japan,JP,JPN,Tochigi
Hachioji,Hachioji,35.65770591,139.3260587,579399,Japan,JP,JPN,Tokyo
Koriyama,Koriyama,37.40997622,140.3799996,302581,Japan,JP,JPN,Fukushima
Kure,Kure,34.25097007,132.5655928,196807.5,Japan,JP,JPN,Hiroshima
Matsue,Matsue,35.46699404,133.0666475,150527,Japan,JP,JPN,Shimane
Tottori,Tottori,35.50037701,134.2332946,142635.5,Japan,JP,JPN,Tottori
Sasebo,Sasebo,33.1631295,129.7177046,224347.5,Japan,JP,JPN,Nagasaki
Kitakyushu,Kitakyushu,33.87039899,130.8200146,990286.5,Japan,JP,JPN,Fukuoka
Kumamoto,Kumamoto,32.80092938,130.700642,699327.5,Japan,JP,JPN,Kumamoto
Oita,Oita,33.24322797,131.5978999,412100.5,Japan,JP,JPN,Oita
Gifu,Gifu,35.42309491,136.7627526,405304.5,Japan,JP,JPN,Gifu
Tsu,Tsu,34.71706565,136.5166695,392484.5,Japan,JP,JPN,Mie
Matsumoto,Matsumoto,36.2404352,137.9700175,217796.5,Japan,JP,JPN,Nagano
Shizuoka,Shizuoka,34.98583478,138.3853926,686446.5,Japan,JP,JPN,Shizuoka
Hamamatsu,Hamamatsu,34.71807334,137.7327193,887242.5,Japan,JP,JPN,Shizuoka
Obihiro,Obihiro,42.93041445,143.1700101,169614,Japan,JP,JPN,Hokkaido
Tomakomai,Tomakomai,42.6504057,141.5500057,161355.5,Japan,JP,JPN,Hokkaido
Kitami,Kitami,43.8503583,143.8999914,103971.5,Japan,JP,JPN,Hokkaido
Otaru,Otaru,43.18871909,140.9783093,139260.5,Japan,JP,JPN,Hokkaido
Fukui,Fukui,36.07041974,136.2200468,241288.5,Japan,JP,JPN,Fukui
Maizuru,Maizuru,35.4504059,135.3333309,62531.5,Japan,JP,JPN,Kyoto
Wakayama,Wakayama,34.22311647,135.1677079,395503,Japan,JP,JPN,Wakayama
Mito,Mito,36.37042727,140.4800451,300215,Japan,JP,JPN,Ibaraki
Kofu,Kofu,35.6503937,138.5833134,193770,Japan,JP,JPN,Yamanashi
Iwaki,Iwaki,37.0553467,140.8900459,324677,Japan,JP,JPN,Fukushima
Nagaoka,Nagaoka,37.45041302,138.8600406,187560,Japan,JP,JPN,Niigata
Yamagata,Yamagata,38.27049217,140.3200032,263373.5,Japan,JP,JPN,Yamagata
Tsuruoka,Tsuruoka,38.70041424,139.830214,88052.5,Japan,JP,JPN,Yamagata
Kagoshima,Kagoshima,31.58596478,130.561064,536092.5,Japan,JP,JPN,Kagoshima
Matsuyama,Matsuyama,33.84554262,132.765839,525089,Japan,JP,JPN,Ehime
Kanazawa,Kanazawa,36.56000226,136.6400211,505093,Japan,JP,JPN,Ishikawa
Muroran,Muroran,42.34995892,140.9800146,125936.5,Japan,JP,JPN,Hokkaido
Asahikawa,Asahikawa,43.75501528,142.3799808,341079.5,Japan,JP,JPN,Hokkaido
Kobe,Kobe,34.67998781,135.1699816,1528478,Japan,JP,JPN,Hyogo
Yokohama,Yokohama,35.32002626,139.5800484,3697894,Japan,JP,JPN,Kanagawa
Akita,Akita,39.70999086,140.0899914,300962.5,Japan,JP,JPN,Akita
Aomori,Aomori,40.82503908,140.7100052,281571.5,Japan,JP,JPN,Aomori
Hirosaki,Hirosaki,40.56999005,140.4700199,171700.5,Japan,JP,JPN,Aomori
Hachinohe,Hachinohe,40.50999371,141.5400321,225575,Japan,JP,JPN,Aomori
Fukushima,Fukushima,37.74000775,140.4700199,278961.5,Japan,JP,JPN,Fukushima
Morioka,Morioka,39.72001609,141.1300313,294782.5,Japan,JP,JPN,Iwate
Niigata,Niigata,37.91999676,139.0400297,537534.5,Japan,JP,JPN,Niigata
Fukuoka,Fukuoka,33.59501528,130.4100138,2092144.5,Japan,JP,JPN,Fukuoka
Miyazaki,Miyazaki,31.91824424,131.418376,317793.5,Japan,JP,JPN,Miyazaki
Naha,Naha,26.20717165,127.6729716,611572,Japan,JP,JPN,Okinawa
Kochi,Kochi,33.56243329,133.5375232,323095,Japan,JP,JPN,Kochi
Nagoya,Nagoya,35.15499758,136.9149914,2710639.5,Japan,JP,JPN,Aichi
Nagano,Nagano,36.64999676,138.1700052,477243.5,Japan,JP,JPN,Nagano
Kushiro,Kushiro,42.97495953,144.3746911,191089,Japan,JP,JPN,Hokkaido
Hakodate,Hakodate,41.79497988,140.7399776,289357,Japan,JP,JPN,Hokkaido
Kyoto,Kyoto,35.02999229,135.7499979,1632320,Japan,JP,JPN,Kyoto
Sendai,Sendai,38.28710614,141.0217175,1643781,Japan,JP,JPN,Miyagi
Sakata,Sakata,38.92003908,139.8500577,86507.5,Japan,JP,JPN,Yamagata
Nagasaki,Nagasaki,32.76498842,129.8850329,422829.5,Japan,JP,JPN,Nagasaki
Hiroshima,Hiroshima,34.3878351,132.442913,1594420.5,Japan,JP,JPN,Hiroshima
Sapporo,Sapporo,43.07497927,141.3400443,2202893,Japan,JP,JPN,Hokkaido
Osaka,Osaka,34.75003522,135.4601448,6943206.5,Japan,JP,JPN,Osaka
Tokyo,Tokyo,35.68501691,139.7514074,22006299.5,Japan,JP,JPN,Tokyo
Al Mafraq,Al Mafraq,32.28329707,36.23329852,57118,Jordan,JO,JOR,Mafraq
At Tafilah,At Tafilah,30.83333404,35.60000464,25429,Jordan,JO,JOR,Tafilah
Ma'an,Ma'an,30.19200312,35.73600358,50350,Jordan,JO,JOR,Ma`an
Irbid,Irbid,32.54998863,35.84999752,471020,Jordan,JO,JOR,Irbid
As Salt,As Salt,32.03919293,35.72721431,110439,Jordan,JO,JOR,Balqa
Az Zarqa,Az Zarqa,32.06999208,36.1000081,843678,Jordan,JO,JOR,Zarqa
Al Aqabah,Al Aqabah,29.52699485,35.07769324,95048,Jordan,JO,JOR,Aqaba
Al Karak,Al Karak,31.1851107,35.70473507,50870,Jordan,JO,JOR,Karak
Amman,Amman,31.95002525,35.93329993,1060000,Jordan,JO,JOR,Amman
Turgay,Turgay,49.62600011,63.49899651,5277,Kazakhstan,KZ,KAZ,Qostanay
Mangyshlak,Mangyshlak,43.69045506,51.14173561,147443,Kazakhstan,KZ,KAZ,Mangghystau
Maqat,Maqat,47.64824017,53.32650183,12169,Kazakhstan,KZ,KAZ,Atyrau
Bestobe,Bestobe,52.49967531,73.0997135,7189,Kazakhstan,KZ,KAZ,Aqmola
Osakarovka,Osakarovka,50.57994753,72.56992672,4196,Kazakhstan,KZ,KAZ,Qaraghandy
Aqadyr,Aqadyr,48.27486859,72.85988318,5359.5,Kazakhstan,KZ,KAZ,Qaraghandy
Sharbaqty,Sharbaqty,52.49990786,78.14994787,107,Kazakhstan,KZ,KAZ,Pavlodar
Shemonaikha,Shemonaikha,50.63159812,81.90496415,23631.5,Kazakhstan,KZ,KAZ,East Kazakhstan
Serebryansk,Serebryansk,49.69989789,83.42487138,701,Kazakhstan,KZ,KAZ,East Kazakhstan
Boralday,Boralday,43.33413658,76.82883988,20996,Kazakhstan,KZ,KAZ,Almaty
Zharkent,Zharkent,44.16155377,79.9801204,35459,Kazakhstan,KZ,KAZ,Almaty
Esik,Esik,43.36906984,77.44378943,30883,Kazakhstan,KZ,KAZ,Almaty
Lenger,Lenger,42.18991701,69.87991003,22148,Kazakhstan,KZ,KAZ,South Kazakhstan
Kentau,Kentau,43.5165027,68.51988969,55864.5,Kazakhstan,KZ,KAZ,South Kazakhstan
Zhosaly,Zhosaly,45.48772605,64.07804195,19023.5,Kazakhstan,KZ,KAZ,Qyzylorda
Oktyabrsk,Oktyabrsk,49.47306419,57.44490678,27284.5,Kazakhstan,KZ,KAZ,Aqt?be
Algha,Algha,49.90316713,57.33499101,28267,Kazakhstan,KZ,KAZ,Aqt?be
Bayghanin,Bayghanin,48.69169069,55.87399491,4271,Kazakhstan,KZ,KAZ,Aqt?be
Embi,Embi,48.82677289,58.14419226,10009.5,Kazakhstan,KZ,KAZ,Aqt?be
Zhetiqara,Zhetiqara,52.19297569,61.23992061,44922,Kazakhstan,KZ,KAZ,Qostanay
Komsomolets,Komsomolets,53.75055503,62.05020707,5693.5,Kazakhstan,KZ,KAZ,Qostanay
Tobol,Tobol,52.69800946,62.57492956,3913.5,Kazakhstan,KZ,KAZ,Qostanay
Qusmuryn,Qusmuryn,52.45799827,64.59997392,4345.5,Kazakhstan,KZ,KAZ,Qostanay
Shieli,Shieli,44.16700563,66.75002356,25871,Kazakhstan,KZ,KAZ,Qyzylorda
Makhambet,Makhambet,47.67136538,51.57978674,4761.5,Kazakhstan,KZ,KAZ,Atyrau
Chapaev,Chapaev,50.19149579,51.14492956,3515.5,Kazakhstan,KZ,KAZ,West Kazakhstan
Zhanibek,Zhanibek,49.4276406,46.8772314,6824,Kazakhstan,KZ,KAZ,West Kazakhstan
Aqsay,Aqsay,51.17143597,53.03489172,30404.5,Kazakhstan,KZ,KAZ,West Kazakhstan
Esil,Esil,51.95696942,66.37748816,7065.5,Kazakhstan,KZ,KAZ,Aqmola
Derzhavinsk,Derzhavinsk,51.10206036,66.30746659,14852,Kazakhstan,KZ,KAZ,Aqmola
Zhaltyr,Zhaltyr,51.63241559,69.83278113,694,Kazakhstan,KZ,KAZ,Aqmola
Makinsk,Makinsk,52.6403644,70.4099552,20365.5,Kazakhstan,KZ,KAZ,Aqmola
Aqsu,Aqsu,52.45019513,71.9597314,8543,Kazakhstan,KZ,KAZ,Aqmola
Zholymbet,Zholymbet,51.75023785,71.70987585,3969,Kazakhstan,KZ,KAZ,Aqmola
Erymentau,Erymentau,51.63032269,73.10493282,19655,Kazakhstan,KZ,KAZ,Aqmola
Saryshaghan,Saryshaghan,46.11954795,73.61911332,2331,Kazakhstan,KZ,KAZ,Qaraghandy
Qarazhal,Qarazhal,48.02527142,70.79990556,17988.5,Kazakhstan,KZ,KAZ,Qaraghandy
Atasu,Atasu,48.69032127,71.64993119,16400,Kazakhstan,KZ,KAZ,Qaraghandy
Kishkenekol,Kishkenekol,53.63676353,72.34141353,6779,Kazakhstan,KZ,KAZ,North Kazakhstan
Tayynsha,Tayynsha,53.84812014,69.76379309,7128.5,Kazakhstan,KZ,KAZ,North Kazakhstan
Bulaevo,Bulaevo,54.90531659,70.43997921,5383,Kazakhstan,KZ,KAZ,North Kazakhstan
Ertis,Ertis,53.34530845,75.44990596,6311,Kazakhstan,KZ,KAZ,Pavlodar
Kachiry,Kachiry,53.08036338,76.08997025,5130.5,Kazakhstan,KZ,KAZ,Pavlodar
Zaysan,Zaysan,47.47522748,84.85982255,14199,Kazakhstan,KZ,KAZ,East Kazakhstan
Zyryanovsk,Zyryanovsk,49.74526979,84.25484656,47293.5,Kazakhstan,KZ,KAZ,East Kazakhstan
Ridder,Ridder,50.35538759,83.5149434,54710,Kazakhstan,KZ,KAZ,East Kazakhstan
Shar,Shar,49.6003174,81.05493852,5124.5,Kazakhstan,KZ,KAZ,East Kazakhstan
Urzhar,Urzhar,47.10018577,81.60482743,13854,Kazakhstan,KZ,KAZ,East Kazakhstan
Sarqan,Sarqan,45.42033999,79.91490474,61329,Kazakhstan,KZ,KAZ,Almaty
Ushtobe,Ushtobe,45.26533653,77.96995886,19116.5,Kazakhstan,KZ,KAZ,Almaty
Shonzhy,Shonzhy,43.54208254,79.47028072,3902,Kazakhstan,KZ,KAZ,Almaty
Qapshaghay,Qapshaghay,43.88438723,77.06872188,40319.5,Kazakhstan,KZ,KAZ,Almaty
Otar,Otar,43.53458946,75.2138997,11238,Kazakhstan,KZ,KAZ,Almaty
Fort Shevchenko,Fort Shevchenko,44.51706179,50.26663692,3236,Kazakhstan,KZ,KAZ,Mangghystau
Zhangaozen,Zhangaozen,43.30039187,52.80002234,8895,Kazakhstan,KZ,KAZ,Mangghystau
Arys,Arys,42.43687868,68.80483354,39466.5,Kazakhstan,KZ,KAZ,South Kazakhstan
Burylbaytal,Burylbaytal,44.93874147,74.03025102,92.5,Kazakhstan,KZ,KAZ,Zhambyl
Shu,Shu,43.59525759,73.74484208,41112,Kazakhstan,KZ,KAZ,Zhambyl
Qulan,Qulan,42.92036338,72.70495723,10200,Kazakhstan,KZ,KAZ,Zhambyl
Oytal,Oytal,42.91529909,73.25489783,16247,Kazakhstan,KZ,KAZ,Zhambyl
Qaratau,Qaratau,43.18538597,70.45997799,35743,Kazakhstan,KZ,KAZ,Zhambyl
Khromtau,Khromtau,50.26994061,58.44996171,21614,Kazakhstan,KZ,KAZ,Aqt?be
Arqalyq,Arqalyq,50.24180279,66.89761145,48760.5,Kazakhstan,KZ,KAZ,Qostanay
Oostanay,Oostanay,53.22089744,63.62830196,223450.5,Kazakhstan,KZ,KAZ,Qostanay
Baykonur,Baykonur,45.69135703,63.24134884,36175,Kazakhstan,KZ,KAZ,Qyzylorda
Balyqshy,Balyqshy,47.06659609,51.86659094,25442,Kazakhstan,KZ,KAZ,Atyrau
Atbasar,Atbasar,51.82188723,68.34770382,35308,Kazakhstan,KZ,KAZ,Aqmola
Kokshetau,Kokshetau,53.29998822,69.41998979,126658.5,Kazakhstan,KZ,KAZ,Aqmola
Temirtau,Temirtau,50.06501772,72.96499304,167193.5,Kazakhstan,KZ,KAZ,Qaraghandy
Zhezqazghan,Zhezqazghan,47.77998924,67.77001298,104357,Kazakhstan,KZ,KAZ,Qaraghandy
Qarqaraly,Qarqaraly,49.42490175,75.46489213,4899,Kazakhstan,KZ,KAZ,Qaraghandy
Balqash,Balqash,46.8532241,74.95024654,80586,Kazakhstan,KZ,KAZ,Qaraghandy
Petropavlovsk,Petropavlovsk,54.87999514,69.22000199,214579,Kazakhstan,KZ,KAZ,North Kazakhstan
Ayakoz,Ayakoz,47.96473248,80.42970536,39670,Kazakhstan,KZ,KAZ,East Kazakhstan
Taldyqorghan,Taldyqorghan,45.00000389,78.40001013,88380,Kazakhstan,KZ,KAZ,Almaty
Turkistan,Turkistan,43.30155458,68.25489294,86743.5,Kazakhstan,KZ,KAZ,South Kazakhstan
Shalqar,Shalqar,47.83629071,59.6140767,27256,Kazakhstan,KZ,KAZ,Aqt?be
Qazaly,Qazaly,45.7627997,62.10751623,3436,Kazakhstan,KZ,KAZ,Qyzylorda
Aral,Aral,46.79997154,61.66661291,30185,Kazakhstan,KZ,KAZ,Qyzylorda
Qulsary,Qulsary,46.98326784,54.01653723,37103,Kazakhstan,KZ,KAZ,Atyrau
Oral,Oral,51.27111981,51.33499548,204894,Kazakhstan,KZ,KAZ,West Kazakhstan
Beyneu,Beyneu,45.18335187,55.10003699,32452,Kazakhstan,KZ,KAZ,Mangghystau
Aqtau,Aqtau,43.6231887,51.2365002,4479,Kazakhstan,KZ,KAZ,Mangghystau
Aqtobe,Aqtobe,50.28001752,57.16998816,260493,Kazakhstan,KZ,KAZ,Aqt?be
Rudny,Rudny,52.95269676,63.1300378,104235.5,Kazakhstan,KZ,KAZ,Qostanay
Qyzylorda,Qyzylorda,44.80001609,65.46498572,213259.5,Kazakhstan,KZ,KAZ,Qyzylorda
Atyrau,Atyrau,47.11269147,51.92002437,170583,Kazakhstan,KZ,KAZ,Atyrau
Ekibastuz,Ekibastuz,51.72998069,75.31993974,124669,Kazakhstan,KZ,KAZ,Pavlodar
Pavlodar,Pavlodar,52.29999758,76.95002112,316254,Kazakhstan,KZ,KAZ,Pavlodar
Semey,Semey,50.43499514,80.2750378,302066.5,Kazakhstan,KZ,KAZ,East Kazakhstan
Oskemen,Oskemen,49.99003522,82.61494665,284350.5,Kazakhstan,KZ,KAZ,East Kazakhstan
Shymkent,Shymkent,42.32001243,69.59501786,439712,Kazakhstan,KZ,KAZ,South Kazakhstan
Taraz,Taraz,42.89997703,71.36498734,332723.5,Kazakhstan,KZ,KAZ,Zhambyl
Astana,Astana,51.1811253,71.42777421,335312.5,Kazakhstan,KZ,KAZ,Aqmola
Qaraghandy,Qaraghandy,49.88497703,73.11500972,378273.5,Kazakhstan,KZ,KAZ,Qaraghandy
Almaty,Almaty,43.32498985,76.91503617,1096256,Kazakhstan,KZ,KAZ,Almaty
Nyeri,Nyeri,-0.41699699,36.95100363,51084,Kenya,KE,KEN,Central
Mwingi,Mwingi,-0.929569886,38.07001705,9546.5,Kenya,KE,KEN,Eastern
Embu,Embu,-0.519569073,37.45000321,46771,Kenya,KE,KEN,Eastern
Machakos,Machakos,-1.509534486,37.25998897,88448,Kenya,KE,KEN,Eastern
Nanyuki,Nanyuki,0.020397968,37.06000118,34342,Kenya,KE,KEN,Rift Valley
Maralal,Maralal,1.110460631,36.68002437,20841,Kenya,KE,KEN,Rift Valley
Konza,Konza,-1.74962319,37.11999752,2004,Kenya,KE,KEN,Rift Valley
Lodwar,Lodwar,3.130389017,35.57001461,17089.5,Kenya,KE,KEN,Rift Valley
Eldama Ravine,Eldama Ravine,0.050370299,35.72003129,15052.5,Kenya,KE,KEN,Rift Valley
Sotik,Sotik,-0.679559307,35.12001623,36942.5,Kenya,KE,KEN,Rift Valley
Namanga,Namanga,-2.539600811,36.80001705,7664.5,Kenya,KE,KEN,Rift Valley
Naivasha,Naivasha,-0.709583314,36.42996212,41174.5,Kenya,KE,KEN,Rift Valley
Kericho,Kericho,-0.359578838,35.28000647,67300,Kenya,KE,KEN,Rift Valley
Kitale,Kitale,1.030465514,34.98994665,112809,Kenya,KE,KEN,Rift Valley
Bungoma,Bungoma,0.570390237,34.55999874,55962,Kenya,KE,KEN,Western
Kakamega,Kakamega,0.290407327,34.7300142,63426,Kenya,KE,KEN,Western
Wajir,Wajir,1.750369892,40.04999955,40240,Kenya,KE,KEN,North-Eastern
Garissa,Garissa,-0.439625632,39.67002274,65948,Kenya,KE,KEN,North-Eastern
Witu,Witu,-2.379610576,40.43002803,3945,Kenya,KE,KEN,Coast
Tsavo,Tsavo,-2.982777894,38.46663367,414,Kenya,KE,KEN,Coast
Voi,Voi,-3.36957599,38.56998653,28055.5,Kenya,KE,KEN,Coast
Kilifi,Kilifi,-3.609613018,39.85001176,63228.5,Kenya,KE,KEN,Coast
Thika,Thika,-1.039589011,37.09002519,93571.5,Kenya,KE,KEN,Central
Kendu Bay,Kendu Bay,-0.359578838,34.63999385,91248,Kenya,KE,KEN,Nyanza
Karungu,Karungu,-0.849626446,34.14999792,2376,Kenya,KE,KEN,Nyanza
Kisii,Kisii,-0.669585756,34.75998653,28547,Kenya,KE,KEN,Nyanza
Marsabit,Marsabit,2.329998595,37.9799967,15910.5,Kenya,KE,KEN,Eastern
Moyale,Moyale,3.51997764,39.05000891,20540,Kenya,KE,KEN,Eastern
Nakuru,Nakuru,-0.279997132,36.06998409,312315,Kenya,KE,KEN,Rift Valley
Lamu,Lamu,-2.26204362,40.91966643,17435,Kenya,KE,KEN,Coast
Malindi,Malindi,-3.209999167,40.10002234,81160,Kenya,KE,KEN,Coast
Kisumu,Kisumu,-0.090034567,34.75001298,306047,Kenya,KE,KEN,Nyanza
Meru,Meru,0.059982116,37.64001745,47226,Kenya,KE,KEN,Eastern
Eldoret,Eldoret,0.520005716,35.26998124,285913.5,Kenya,KE,KEN,Rift Valley
Mombasa,Mombasa,-4.040026022,39.68991817,840834,Kenya,KE,KEN,Coast
Nairobi,Nairobi,-1.283346742,36.81665686,2880273.5,Kenya,KE,KEN,Nairobi
Tarawa,Tarawa,1.338187506,173.0175708,25668,Kiribati,KI,KIR,
Prizren,Prizren,42.22932029,20.75009232,157574.5,Kosovo,,KOS,Prizren
Pec,Pec,42.66032757,20.3107393,93481.5,Kosovo,-99,KOS,?akovica
Pristina,Pristina,42.66670961,21.16598425,331700,Kosovo,-99,KOS,Pristina
Hawalli,Hawalli,29.33334002,47.99999756,164212,Kuwait,KW,KWT,Hawalli
Al Ahmadi,Al Ahmadi,29.0769448,48.08377274,68763,Kuwait,KW,KWT,Al Ahmadi
Al Jahra,Al Jahra,29.33747154,47.6580623,194193,Kuwait,KW,KWT,Al Jahrah
Kuwait,Kuwait,29.36971763,47.97830115,1061532,Kuwait,KW,KWT,Al Kuwayt
Tokmak,Tokmak,42.82987795,75.28459306,87953.5,Kyrgyzstan,KG,KGZ,Bishkek
Kara Balta,Kara Balta,42.83062726,73.88566036,68464.5,Kyrgyzstan,KG,KGZ,Bishkek
Cholpon Ata,Cholpon Ata,42.65133588,77.08107255,14086.5,Kyrgyzstan,KG,KGZ,Ysyk-K?l
Naryn,Naryn,41.42634605,75.99106156,44003.5,Kyrgyzstan,KG,KGZ,Naryn
Kok Yangak,Kok Yangak,41.03071128,73.20575354,14523,Kyrgyzstan,KG,KGZ,Jalal-Abad
Balykchy,Balykchy,42.4560248,76.18536495,40263.5,Kyrgyzstan,KG,KGZ,Ysyk-K?l
At Bashy,At Bashy,41.17248557,75.79680985,15413.5,Kyrgyzstan,KG,KGZ,Naryn
Jalal Abad,Jalal Abad,40.94288719,73.00251013,162299.5,Kyrgyzstan,KG,KGZ,Jalal-Abad
Toktogul,Toktogul,41.88257143,72.93719112,22725.5,Kyrgyzstan,KG,KGZ,Jalal-Abad
Tash Komur,Tash Komur,41.34185508,72.23144608,19974.5,Kyrgyzstan,KG,KGZ,Jalal-Abad
Talas,Talas,42.51837242,72.24291825,28646,Kyrgyzstan,KG,KGZ,Talas
Osh,Osh,40.54040529,72.79001664,295638.5,Kyrgyzstan,KG,KGZ,Osh
Karakol,Karakol,42.49204327,78.38182003,63411.5,Kyrgyzstan,KG,KGZ,Ysyk-K?l
Bishkek,Bishkek,42.87307945,74.58520422,820606,Kyrgyzstan,KG,KGZ,Bishkek
Ban Houayxay,Ban Houayxay,20.2775,100.4127778,6347,Laos,LA,LAO,Bokeo
Louang Namtha,Louang Namtha,20.95000205,101.4166986,3225,Laos,LA,LAO,Louang Namtha
Champasak,Champasak,14.88330011,105.8667036,12994,Laos,LA,LAO,Champasak
Saravan,Saravan,15.715998,106.4269987,5521,Laos,LA,LAO,Saravan
Xam Nua,Xam Nua,20.41669802,104.0333047,38992,Laos,LA,LAO,Houaphan
Phongsali,Phongsali,21.68330399,102.0999967,6000,Laos,LA,LAO,Ph?ngsali
Attapu,Attapu,14.8079971,106.8390005,4297,Laos,LA,LAO,Attapu
Xaignabouri,Xaignabouri,19.2504645,101.7500577,16200,Laos,LA,LAO,Xaignabouri
Pakxe,Pakxe,15.12206016,105.8183365,95553.5,Laos,LA,LAO,Champasak
Xiangkhoang,Xiangkhoang,19.33368939,103.3665999,5189,Laos,LA,LAO,Xiangkhoang
Louangphrabang,Louangphrabang,19.88453432,102.1416101,77260,Laos,LA,LAO,Louangphrabang
Thakhek,Thakhek,17.41119692,104.8361226,51564,Laos,LA,LAO,Khammouan
Savannakhet,Savannakhet,16.53758099,104.772974,75725.5,Laos,LA,LAO,Savannakh?t
Vientiane,Vientiane,17.96669273,102.59998,662174,Laos,LA,LAO,Vientiane [prefecture]
Rezekne,Rezekne,56.50002545,27.3165649,38219,Latvia,LV,LVA,Latgale
Ventspils,Ventspils,57.38986778,21.56058549,42764,Latvia,LV,LVA,Ventspils
Jelgava,Jelgava,56.65270347,23.71280554,64499,Latvia,LV,LVA,Jelgava
Liepaga,Liepaga,56.50997316,21.01002478,83969.5,Latvia,LV,LVA,Liepaja
Daugavpils,Daugavpils,55.87995994,26.50999914,109969.5,Latvia,LV,LVA,Daugavpils
Riga,Riga,56.95002382,24.09996537,723802.5,Latvia,LV,LVA,Riga
B'abda,B'abda,33.83330406,35.53329652,9000,Lebanon,LB,LBN,Mount Lebanon
Nabatiye et Tahta,Nabatiye et Tahta,33.38330402,35.45000164,60000,Lebanon,LB,LBN,An Nabatiyah
Saida,Saida,33.56302757,35.36878658,173894,Lebanon,LB,LBN,South Lebanon
Zahle,Zahle,33.85011599,35.90415442,61192,Lebanon,LB,LBN,Mount Lebanon
Trablous,Trablous,34.42000368,35.8699963,361286,Lebanon,LB,LBN,North Lebanon
Beirut,Beirut,33.87197512,35.50970821,1779062.5,Lebanon,LB,LBN,Beirut
Teyateyaneng,Teyateyaneng,-29.15299794,27.75300351,5115,Lesotho,LS,LSO,Berea
Mohales Hoek,Mohales Hoek,-30.15899991,27.47999751,24992,Lesotho,LS,LSO,Mohale's Hoek
Moyeni,Moyeni,-30.41099991,27.71600451,24130,Lesotho,LS,LSO,Quthing
Hlotse,Hlotse,-28.87800298,28.05599764,47675,Lesotho,LS,LSO,Leribe
Butha-Buthe,Butha-Buthe,-28.74999591,28.25000158,16330,Lesotho,LS,LSO,Leribe
Mokhotlong,Mokhotlong,-29.29100403,29.07800155,8809,Lesotho,LS,LSO,Mokhotlong
Mafetang,Mafetang,-29.81664386,27.25000565,54708.5,Lesotho,LS,LSO,Mafeteng
Maseru,Maseru,-29.31667438,27.48327307,239839.5,Lesotho,LS,LSO,Maseru
Barclayville,Barclayville,4.799996997,-8.166698518,2733,Liberia,LR,LBR,GrandKru
Voinjama,Voinjama,8.416701115,-9.749996524,26594,Liberia,LR,LBR,Lofa
Bensonville,Bentol,6.433299035,-10.60000152,4089,Liberia,LR,LBR,Montserrado
Kakata,Kakata,6.525999009,-10.34900054,33945,Liberia,LR,LBR,Margibi
Sanniquellie,Sanniquellie,7.371000109,-8.684999462,11415,Liberia,LR,LBR,Nimba
Rivercess,Rivercess,5.464998046,-9.577997442,2578,Liberia,LR,LBR,River Cess
Harper,Harper,4.375377623,-7.716981447,25249,Liberia,LR,LBR,Maryland
Gbarnga,Gbarnga,7.010410582,-9.489999839,31856.5,Liberia,LR,LBR,Bong
Zwedru,Zwedru,6.070390441,-8.130005332,19459.5,Liberia,LR,LBR,GrandGedeh
Greenville,Greenville,5.011126932,-9.038812908,10374,Liberia,LR,LBR,Sinoe
Buchanan,Buchanan,5.916084614,-10.05247197,37023,Liberia,LR,LBR,Grand Bassa
Robertsport,Robertsport,6.753320332,-11.36859318,7951,Liberia,LR,LBR,Grand Cape Mount
Monrovia,Monrovia,6.31055666,-10.80475163,913331,Liberia,LR,LBR,Montserrado
Dirj,Dirj,30.1679118,10.45666378,931,Libya,LY,LBY,Ghadamis
Nalut,Nalut,31.88044293,10.97001745,66418.5,Libya,LY,LBY,Ghadamis
Zillah,Zillah,28.55041363,17.58336055,10,Libya,LY,LBY,Al Jufrah
Al Khums,Al Khums,32.66042116,14.25999752,192502,Libya,LY,LBY,Al Marqab
Tajarhi,Tajarhi,24.3703587,14.47083736,1498,Libya,LY,LBY,Murzuq
Umm al Abid,Umm al Abid,27.51701418,15.03333533,299,Libya,LY,LBY,Sabha
Az Zawiyah,Az Zawiyah,32.76041506,12.71998816,193061.5,Libya,LY,LBY,Az Zawiyah
Gharyan,Gharyan,32.17037355,13.01996985,116014.5,Libya,LY,LBY,Mizdah
Mizdah,Mizdah,31.43372601,12.98333126,16379.5,Libya,LY,LBY,Mizdah
Bani Walid,Bani Walid,31.77039797,13.98998816,55871,Libya,LY,LBY,Bani Walid
Al Marj,Al Marj,32.50045677,20.82998409,127427.5,Libya,LY,LBY,Al Hizam Al Akhdar
Al Bayda,Al Bayda,32.76041506,21.62001339,1794,Libya,LY,LBY,Al Jabal al Akhdar
Shahhat,Shahhat,32.82813702,21.86216915,44188,Libya,LY,LBY,Al Jabal al Akhdar
El Agheila,El Agheila,30.25702781,19.20000606,100,Libya,LY,LBY,Ajdabiya
Maradah,Maradah,29.23370526,19.21664587,2364.5,Libya,LY,LBY,Ajdabiya
Qaminis,Qaminis,31.66063723,20.01546016,5348,Libya,LY,LBY,Benghazi
As Sidr,As Sidr,30.67041343,18.26662634,50,Libya,LY,LBY,Surt
Al Jaghbub,Al Jaghbub,29.75039207,24.51658077,1744,Libya,LY,LBY,Al Butnan
Ghadamis,Ghadamis,30.13328859,9.500029662,6623,Libya,LY,LBY,Ghadamis
Hun,Hun,29.11665814,15.93333207,17352,Libya,LY,LBY,Al Jufrah
Birak,Birak,27.53331809,14.28335526,42432.5,Libya,LY,LBY,Ash Shati'
Ghat,Ghat,24.96474103,10.17275346,22006,Libya,LY,LBY,Ghat
Marzuq,Marzuq,25.90439943,13.89722896,49401.5,Libya,LY,LBY,Murzuq
Ajdabiya,Ajdabiya,30.76999392,20.21999548,139095.5,Libya,LY,LBY,Ajdabiya
Awjilah,Awjilah,29.10802818,21.2869071,6610,Libya,LY,LBY,Ajdabiya
Surt,Surt,31.2099929,16.59003617,110756.5,Libya,LY,LBY,Surt
Darnah,Darnah,32.76481113,22.63913928,103378,Libya,LY,LBY,Al Qubbah
Tubruq,Tubruq,32.07999147,23.96002559,192289.5,Libya,LY,LBY,Al Butnan
Al Jawf,Al Jawf,24.19998151,23.28998897,24132,Libya,LY,LBY,Al Kufrah
Tmassah,Tmassah,26.36664512,15.80000688,350,Libya,LY,LBY,Murzuq
Misratah,Misratah,32.37997316,15.09999792,301160,Libya,LY,LBY,Misratah
Zuwarah,Zuwarah,32.93440961,12.07914872,123848,Libya,LY,LBY,An Nuqat al Khams
Sabha,Sabha,27.0332711,14.43332027,100249,Libya,LY,LBY,Sabha
Banghazi,Banghazi,32.11673342,20.06672318,881187,Libya,LY,LBY,Benghazi
Tripoli,Tripoli,32.89250002,13.18001176,1209199,Libya,LY,LBY,Tajura' wa an Nawahi al Arba
Vaduz,Vaduz,47.13372377,9.516669473,20811.5,Liechtenstein,LI,LIE,
Paneve?ys,Panevezys,55.74002016,24.37002641,122400,Lithuania,LT,LTU,Panevezio
Siauliai,Siauliai,55.93863853,23.32502559,132057.5,Lithuania,LT,LTU,?iauliai
Klaipeda,Klaipeda,55.72040896,21.11994055,191334,Lithuania,LT,LTU,Klaipedos
Kaunas,Kaunas,54.95040428,23.88003048,363844.5,Lithuania,LT,LTU,Kauno
Vilnius,Vilnius,54.68336631,25.31663529,524697.5,Lithuania,LT,LTU,Vilniaus
Diekirch,Diekirch,49.88330105,6.166701555,6242,Luxembourg,LU,LUX,Diekirch
Grevenmacher,Grevenmacher,49.69999811,6.333300575,3958,Luxembourg,LU,LUX,Grevenmacher
Luxembourg,Luxembourg,49.61166038,6.130002806,91972,Luxembourg,LU,LUX,Luxembourg
Macau,Macau,22.20299746,113.5450484,568700,Macau S.A.R,MO,MAC,
Tetovo,Tetovo,42.00923037,20.9700789,96038,Macedonia,MK,MKD,Tetovo
Bitola,Bitola,41.03905703,21.33951371,75551,Macedonia,MK,MKD,Bitola
Skopje,Skopje,42.00000612,21.43346147,484488,Macedonia,MK,MKD,Centar
Sambava,Sambava,-14.26617186,50.16659135,37493.5,Madagascar,MG,MDG,Antsiranana
Ambanja,Ambanja,-13.68289996,48.45000362,26231.5,Madagascar,MG,MDG,Antsiranana
Ihosy,Ihosy,-22.39962889,46.11665767,13902,Madagascar,MG,MDG,Fianarantsoa
Mandritsara,Mandritsara,-15.83284625,48.81664791,9705,Madagascar,MG,MDG,Mahajanga
Besalampy,Besalampy,-16.74953449,44.48332068,1022,Madagascar,MG,MDG,Mahajanga
Marovoay,Marovoay,-16.09954832,46.63331864,16513,Madagascar,MG,MDG,Mahajanga
Antsohihy,Antsohihy,-14.86608356,47.98336544,15258.5,Madagascar,MG,MDG,Mahajanga
Ambatondrazaka,Ambatondrazaka,-17.83287921,48.41667232,41843,Madagascar,MG,MDG,Toamasina
Bekiy,Bekiy,-24.21615884,45.31660315,4286,Madagascar,MG,MDG,Toliary
Manja,Manja,-21.43291787,44.33325232,1536,Madagascar,MG,MDG,Toliary
Miandrivazo,Miandrivazo,-19.51618732,45.46661983,11893.5,Madagascar,MG,MDG,Toliary
Antsirabe,Antsirabe,-19.85001707,47.03329423,307921,Madagascar,MG,MDG,Antananarivo
Antalaha,Antalaha,-14.88334349,50.28332841,40668,Madagascar,MG,MDG,Antsiranana
Andoany,Andoany,-13.40002317,48.26660396,20535.5,Madagascar,MG,MDG,Antsiranana
Farafangana,Farafangana,-22.81660602,47.8332454,14992.5,Madagascar,MG,MDG,Fianarantsoa
Mananjary,Mananjary,-21.216652,48.33331824,19841,Madagascar,MG,MDG,Fianarantsoa
Maintirano,Maintirano,-18.06661172,44.01668249,5925,Madagascar,MG,MDG,Mahajanga
Toamasina,Toamasina,-18.18179848,49.40498409,208299.5,Madagascar,MG,MDG,Toamasina
Maroantsetra,Maroantsetra,-15.43333576,49.73333614,30952.5,Madagascar,MG,MDG,Toamasina
Tolanaro,Tolanaro,-25.02680703,46.99004106,16818,Madagascar,MG,MDG,Toliary
Morombe,Morombe,-21.73913848,43.36567763,16727,Madagascar,MG,MDG,Toliary
Androka,Androka,-25.02194623,44.07494694,174,Madagascar,MG,MDG,Toliary
Morondava,Morondava,-20.28327228,44.28333288,20018.5,Madagascar,MG,MDG,Toliary
Antsiranana,Antsiranana,-12.27650152,49.3115261,76312,Madagascar,MG,MDG,Antsiranana
Fianarantsoa,Fianarantsoa,-21.43333128,47.08326534,175705.5,Madagascar,MG,MDG,Fianarantsoa
Mahajanga,Mahajanga,-15.67001382,46.34501583,145158.5,Madagascar,MG,MDG,Mahajanga
Toliara,Toliara,-23.35683144,43.68998409,106278,Madagascar,MG,MDG,Toliary
Antananarivo,Antananarivo,-18.91663735,47.5166239,1544216.5,Madagascar,MG,MDG,Antananarivo
Mzimba,Mzimba,-11.9,33.6,19308,Malawi,MW,MWI,Mzimba
Machinga,Machinga,-14.9666667,35.5166667,1418,Malawi,MW,MWI,Machinga
Dedza,Dedza,-14.3666667,34.3333333,15608,Malawi,MW,MWI,Dedza
Mchinji,Mchinji,-13.8,32.9,18305,Malawi,MW,MWI,Mchinji
Ntcheu,Ntcheu,-14.8166667,34.6333333,10445,Malawi,MW,MWI,Ntcheu
Chiradzulu,Chiradzulu,-15.7,35.1833333,1580,Malawi,MW,MWI,Chiradzulu
Nsanje,Nsanje,-16.9166667,35.2666667,21774,Malawi,MW,MWI,Nsanje
Mwanza,Mwanza,-15.6166667,34.5166667,11379,Malawi,MW,MWI,Mwanza
Mulanje,Mulanje,-16.0333333,35.5,16483,Malawi,MW,MWI,Mulanje
Karonga,Karonga,-9.932896302,33.93331864,33325.5,Malawi,MW,MWI,Chitipa
Chitipa,Chitipa,-9.716217022,33.26664099,11118,Malawi,MW,MWI,Chitipa
Nkhata Bay,Nkhata Bay,-11.59961627,34.30001461,16914.5,Malawi,MW,MWI,Nkhata Bay
Nkhotakota,Nkhotakota,-12.91628009,34.30001461,42359.5,Malawi,MW,MWI,Nkhotakota
Mangochi,Mangochi,-14.45959674,35.26998124,68973.5,Malawi,MW,MWI,Mangochi
Salima,Salima,-13.78294554,34.43328813,50616.5,Malawi,MW,MWI,Salima
Chiromo,Chiromo,-16.55001178,35.1332454,25235,Malawi,MW,MWI,Nsanje
Zomba,Zomba,-15.39003091,35.31003048,80932,Malawi,MW,MWI,Zomba
Mzuzu,Mzuzu,-11.45998655,34.01998002,110201,Malawi,MW,MWI,Mzimba
Blantyre,Blantyre,-15.79000649,34.98994665,584877,Malawi,MW,MWI,Blantyre
Lilongwe,Lilongwe,-13.98329507,33.78330196,646750,Malawi,MW,MWI,Lilongwe
Kangar,Kangar,6.433001991,100.1899987,63869,Malaysia,MY,MYS,Perlis
Kuala Lipis,Kuala Lipis,4.18400112,102.0420006,15448,Malaysia,MY,MYS,Pahang
Shah Alam,Shah Alam,3.066695996,101.5499977,481654,Malaysia,MY,MYS,Selangor
Teluk Intan,Teluk Intan,4.01185976,101.0314453,82506,Malaysia,MY,MYS,Perak
Butterworth,Butterworth,5.417071146,100.4000109,464621.5,Malaysia,MY,MYS,Pulau Pinang
Sungai Petani,Sungai Petani,5.649718444,100.4793343,293671,Malaysia,MY,MYS,Kedah
Alor Setar,Alor Setar,6.113307718,100.3729325,276921.5,Malaysia,MY,MYS,Kedah
Muar,Muar,2.033737609,102.566597,159621.5,Malaysia,MY,MYS,Johor
Batu Pahat,Batu Pahat,1.850363789,102.9333447,177927.5,Malaysia,MY,MYS,Johor
Keluang,Keluang,2.038310973,103.317869,163264,Malaysia,MY,MYS,Johor
Seremban,Seremban,2.710492166,101.9400203,336824,Malaysia,MY,MYS,Negeri Sembilan
Raub,Raub,3.792700011,101.8423002,36772.5,Malaysia,MY,MYS,Pahang
Chukai,Chukai,4.233241596,103.4478869,63535.5,Malaysia,MY,MYS,Trengganu
Kuala Terengganu,Kuala Terengganu,5.330409769,103.12,317637.5,Malaysia,MY,MYS,Trengganu
Lahad Datu,Lahad Datu,5.046396097,118.3359704,82966,Malaysia,MY,MYS,Sabah
Bintulu,Bintulu,3.16640749,113.0359838,117643.5,Malaysia,MY,MYS,Sarawak
Miri,Miri,4.399923929,113.9845048,219957.5,Malaysia,MY,MYS,Sarawak
Johor Bahru,Johor Bahru,1.480024637,103.7300402,838744.5,Malaysia,MY,MYS,Johor
Kelang,Kelang,3.020369892,101.5500183,917933.5,Malaysia,MY,MYS,Selangor
Taiping,Taiping,4.864960143,100.7199914,227371,Malaysia,MY,MYS,Perak
Ipoh,Ipoh,4.599989236,101.0649833,656227,Malaysia,MY,MYS,Perak
Kota Baharu,Kota Baharu,6.119973978,102.2299768,392449.5,Malaysia,MY,MYS,Kelantan
Malacca,Malacca,2.206414407,102.2464615,645916.5,Malaysia,MY,MYS,Melaka
Kuantan,Kuantan,3.829958719,103.3200394,320462,Malaysia,MY,MYS,Pahang
Tawau,Tawau,4.270965392,117.8959973,297996.5,Malaysia,MY,MYS,Sabah
Sandakan,Sandakan,5.842962462,118.107974,341788.5,Malaysia,MY,MYS,Sabah
Kota Kinabalu,Kota Kinabalu,5.979982523,116.1100081,492498.5,Malaysia,MY,MYS,Sabah
Sibu,Sibu,2.302971821,111.8430334,201035.5,Malaysia,MY,MYS,Sarawak
George Town,George Town,5.413613156,100.3293679,1610101,Malaysia,MY,MYS,Pulau Pinang
Kuching,Kuching,1.529969909,110.3299991,537685,Malaysia,MY,MYS,Sarawak
Putrajaya,Putrajaya,2.914019795,101.701947,58982,Malaysia,MY,MYS,Selangor
Kuala Lumpur,Kuala Lumpur,3.166665872,101.6999833,1448000,Malaysia,MY,MYS,Selangor
Male,Male,4.16670819,73.49994747,108310,Maldives,MV,MDV,
Goundam,Goundam,16.41699404,-3.666582684,6217.5,Mali,ML,MLI,Timbuktu
Aguelhok,Aguelhok,19.45487062,0.856371214,8540,Mali,ML,MLI,Kidal
Bourem,Bourem,16.90037539,-0.349989259,28743,Mali,ML,MLI,Gao
Kati,Kati,12.75042198,-8.080008384,54908.5,Mali,ML,MLI,Bamako
Banamba,Banamba,13.55039899,-7.449995159,18312,Mali,ML,MLI,Bamako
Kangaba,Kangaba,11.94041974,-8.440012249,17232,Mali,ML,MLI,Bamako
Nioro du Sahel,Nioro du Sahel,15.23042564,-9.589967897,14421,Mali,ML,MLI,Kayes
Bafoulabe,Bafoulabe,13.80038373,-10.82002201,26823,Mali,ML,MLI,Kayes
Satadougou,Satadougou,12.61699343,-11.4066012,706,Mali,ML,MLI,Kayes
Yelimane,Yelimane,15.13371319,-10.56662663,988,Mali,ML,MLI,Kayes
Kita,Kita,13.05040367,-9.483307741,26102,Mali,ML,MLI,Kayes
Koutiala,Koutiala,12.39041811,-5.469986818,102140,Mali,ML,MLI,Sikasso
Sikasso,Sikasso,11.3204059,-5.679999839,185269.5,Mali,ML,MLI,Sikasso
Bougouni,Bougouni,11.42042564,-7.48996688,30547,Mali,ML,MLI,Sikasso
Markala,Markala,13.67036582,-6.069950197,46161.5,Mali,ML,MLI,S?gou
Sokolo,Sokolo,14.73373761,-6.133305503,4251,Mali,ML,MLI,S?gou
San,San,13.30041424,-4.900047446,33098.5,Mali,ML,MLI,S?gou
Taoudenni,Taoudenni,22.66658673,-3.983359214,3019,Mali,ML,MLI,Timbuktu
Araouane,Araouane,18.90002077,-3.529950197,4026,Mali,ML,MLI,Timbuktu
Tessalit,Tessalit,20.20138837,1.088811807,5869.5,Mali,ML,MLI,Kidal
Menaka,Menaka,15.91666282,2.399997923,9110,Mali,ML,MLI,Gao
Nara,Nara,15.18001528,-7.279979697,18459,Mali,ML,MLI,Bamako
Koulikoro,Koulikoro,12.88330792,-7.549989056,13408.5,Mali,ML,MLI,Bamako
Mopti,Mopti,14.48997988,-4.180039715,93269.5,Mali,ML,MLI,Mopti
Gao,Gao,16.26658978,-0.05000757,87472.5,Mali,ML,MLI,Gao
Kayes,Kayes,14.44998232,-11.44001001,77207,Mali,ML,MLI,Kayes
Segou,Segou,13.43999229,-6.260016115,107752,Mali,ML,MLI,S?gou
Timbuktu,Timbuktu,16.7665851,-3.016596518,68872,Mali,ML,MLI,Timbuktu
Bamako,Bamako,12.65001467,-8.000039105,1395640.5,Mali,ML,MLI,Bamako
Djenne,Djenne,13.89999005,-4.549991294,27663,Mali,ML,MLI,Mopti
Valletta,Valletta,35.89973248,14.51471065,187608,Malta,MT,MLT,
Majuro,Majuro,7.103004311,171.3800002,22950,Marshall Islands,MH,MHL,
Fderik,Fderik,22.67900113,-12.70700053,5760,Mauritania,MR,MRT,Tiris Zemmour
Aleg,Aleg,17.057997,-13.90899556,8388,Mauritania,MR,MRT,Brakna
Akjoujt,Akjoujt,19.74699906,-14.39099948,370,Mauritania,MR,MRT,Inchiri
Zouirat,Zouirat,22.73038129,-12.4833055,56345,Mauritania,MR,MRT,Tiris Zemmour
Chegga,Chegga,25.38040041,-5.779967897,10,Mauritania,MR,MRT,Tiris Zemmour
Magta Lajar,Magta Lajar,17.00039512,-13.49998763,10,Mauritania,MR,MRT,Brakna
Bogue,Bogue,16.59039431,-14.26996647,10415,Mauritania,MR,MRT,Brakna
Boutilimit,Boutilimit,17.55038739,-14.70004358,14142,Mauritania,MR,MRT,Trarza
Selibaby,Selibaby,15.16701866,-12.18332381,460,Mauritania,MR,MRT,Guidimaka
Timbedra,Timbedra,16.25041506,-8.166618084,245,Mauritania,MR,MRT,Hodh ech Chargui
Nema,Nema,16.61705935,-7.250007366,127500,Mauritania,MR,MRT,Hodh ech Chargui
Saint-Louis,Saint-Louis,16.01998985,-16.51001062,198396,Mauritania,MR,MRT,Trarza
Tidjikdja,Tidjikdja,18.5500163,-11.41660059,19981,Mauritania,MR,MRT,Tagant
Bir Mogrein,Bir Mogrein,25.23330345,-11.58330876,10,Mauritania,MR,MRT,Tiris Zemmour
Rosso,Rosso,16.52401593,-15.81266301,47203,Mauritania,MR,MRT,Trarza
Kiffa,Kiffa,16.61997906,-11.39998661,73930,Mauritania,MR,MRT,Assaba
Nouadhibou,Nouadhibou,20.90000205,-17.05602381,86738,Mauritania,MR,MRT,Dakhlet Nouadhibou
Ayoun el Atrous,Ayoun el Atrous,16.66659121,-9.616658774,1423,Mauritania,MR,MRT,Hodh el Gharbi
Nouakchott,Nouakchott,18.08642702,-15.97534041,701772,Mauritania,MR,MRT,Nouakchott
Atar,Atar,20.51664044,-13.04998926,44265,Mauritania,MR,MRT,Adrar
Curepipe,Curepipe,-20.31619017,57.51663367,192087.5,Mauritius,MU,MUS,
Port Louis,Port Louis,-20.16663857,57.49999385,371953.5,Mauritius,MU,MUS,
Vicente Guerrero,Vicente Guerrero,30.76405113,-116.0092603,7294.5,Mexico,MX,MEX,Baja California
Loreto,Loreto,26.01333335,-111.3516635,10760.5,Mexico,MX,MEX,Baja California Sur
Ciudad Constitucion,Ciudad Constitucion,25.04000775,-111.6599909,37605.5,Mexico,MX,MEX,Baja California Sur
Allende,Allende,28.32998781,-100.8499789,18268.5,Mexico,MX,MEX,Coahuila
Nueva Rosita,Nueva Rosita,27.94995933,-101.2199821,35746.5,Mexico,MX,MEX,Coahuila
Hidalgo del Parral,Hidalgo del Parral,26.93335472,-105.6666358,102573,Mexico,MX,MEX,Chihuahua
Ascension,Ascension,31.10002545,-107.979983,10761,Mexico,MX,MEX,Chihuahua
Gomez Palacio,Gomez Palacio,25.57005292,-103.5000238,313952.5,Mexico,MX,MEX,Durango
Canatlan,Canatlan,24.51998781,-104.7799974,7806.5,Mexico,MX,MEX,Durango
Villa Union,Villa Union,23.19999086,-106.2300381,14563,Mexico,MX,MEX,Sinaloa
Altata,Altata,24.63604509,-107.9162153,750,Mexico,MX,MEX,Sinaloa
Esperanza,Esperanza,27.58000775,-109.9299931,3836,Mexico,MX,MEX,Sonora
Magdalena,Magdalena,30.61661826,-111.0499506,13402,Mexico,MX,MEX,Sonora
Nacozari Viejo,Nacozari Viejo,30.42001528,-109.6499844,11872,Mexico,MX,MEX,Sonora
Villanueva,Villanueva,22.35001691,-102.88001,9093.5,Mexico,MX,MEX,Zacatecas
Montemorelos,Montemorelos,25.1899986,-99.83998885,40167,Mexico,MX,MEX,Nuevo Le?n
Sabinas Hidalgo,Sabinas Hidalgo,26.51002138,-100.1799681,26122.5,Mexico,MX,MEX,Nuevo Le?n
Cardenas,Cardenas,22.00001243,-99.66999923,15331,Mexico,MX,MEX,San Luis Potos?
Ciudad Valles,Ciudad Valles,21.97998781,-99.02001306,112234,Mexico,MX,MEX,San Luis Potos?
Rio Verde,Rio Verde,21.92999086,-99.98000615,59233.5,Mexico,MX,MEX,San Luis Potos?
Ciudad Mante,Ciudad Mante,22.73335268,-98.95001734,78299.5,Mexico,MX,MEX,Tamaulipas
Reynosa,Reynosa,26.07999595,-98.30003117,458997,Mexico,MX,MEX,Tamaulipas
Ciudad Madero,Ciudad Madero,22.31890769,-97.836106,165411.5,Mexico,MX,MEX,Tamaulipas
Autlan,Autlan,19.77001935,-104.3699966,44912,Mexico,MX,MEX,Jalisco
Ciudad Hidalgo,Ciudad Hidalgo,19.67997316,-100.569996,59573.5,Mexico,MX,MEX,Michoac?n
Apatzingan,Apatzingan,19.07998395,-102.3500165,92616.5,Mexico,MX,MEX,Michoac?n
Santiago Ixcuintla,Santiago Ixcuintla,21.81999758,-105.2200481,17077.5,Mexico,MX,MEX,Nayarit
Juchitan,Juchitan,16.42999066,-95.01999882,62254.5,Mexico,MX,MEX,Oaxaca
Miahuatlan,Miahuatlan,16.32999676,-96.60000574,16661.5,Mexico,MX,MEX,Oaxaca
Atlixco,Atlixco,18.90002077,-98.44999618,91866.5,Mexico,MX,MEX,Puebla
Acatlan,Acatlan,18.19996014,-98.04999475,17585.5,Mexico,MX,MEX,Puebla
Paraiso,Paraiso,18.40002545,-93.22997888,14167.5,Mexico,MX,MEX,Tabasco
Balancan,Balancan,17.79995872,-91.52997929,7666.5,Mexico,MX,MEX,Tabasco
Tlaxcala,Tlaxcala,19.31999514,-98.2300096,296836.5,Mexico,MX,MEX,Tlaxcala
Irapuato,Irapuato,20.67001609,-101.4999909,339554,Mexico,MX,MEX,Guanajuato
Celaya,Celaya,20.53002464,-100.8000078,344799,Mexico,MX,MEX,Guanajuato
Chilpancingo,Chilpancingo,17.54997398,-99.5000096,173818.5,Mexico,MX,MEX,Guerrero
Iguala,Iguala,18.37000144,-99.53998133,110641.5,Mexico,MX,MEX,Guerrero
Tecpan,Tecpan,17.24999229,-100.6799893,14638,Mexico,MX,MEX,Guerrero
Atoyac,Atoyac,17.19999534,-100.4300304,19798,Mexico,MX,MEX,Guerrero
Nezahualcoyotl,Nezahualcoyotl,19.41001548,-99.02998661,929681.5,Mexico,MX,MEX,M?xico
San Juan del Rio,San Juan del Rio,20.37998212,-100.0000308,132866,Mexico,MX,MEX,Quer?taro
Jaltipan,Jaltipan,17.93997601,-94.73999007,66998,Mexico,MX,MEX,Veracruz
Orizaba,Orizaba,18.85002382,-97.12999923,238340.5,Mexico,MX,MEX,Veracruz
Xalapa,Xalapa,19.52998232,-96.91998621,438667,Mexico,MX,MEX,Veracruz
Nautla,Nautla,20.21658124,-96.78335372,2653.5,Mexico,MX,MEX,Veracruz
San Cristobal de Las Casas,San Cristobal de Las Casas,16.74999697,-92.63337447,157828.5,Mexico,MX,MEX,Chiapas
Escuintla,Escuintla,15.33000612,-92.62998967,58313.5,Mexico,MX,MEX,Chiapas
Motul,Motul,21.09998985,-89.27998743,21181,Mexico,MX,MEX,Yucat?n
Tekax,Tekax,20.1999931,-89.27998743,20577,Mexico,MX,MEX,Yucat?n
Peto,Peto,20.12997154,-88.91998356,12924,Mexico,MX,MEX,Yucat?n
Halacho,Halacho,20.47997601,-90.08001612,8116,Mexico,MX,MEX,Yucat?n
San Quintin,San Quintin,30.48373232,-115.9499874,5433,Mexico,MX,MEX,Baja California
Punta Prieta,Punta Prieta,28.93369773,-114.1665821,527,Mexico,MX,MEX,Baja California
San Felipe,San Felipe,31.02411277,-114.8496153,18068,Mexico,MX,MEX,Baja California
Santa Rosalia,Santa Rosalia,27.31707806,-112.2833637,11110,Mexico,MX,MEX,Baja California Sur
Guerrero Negro,Guerrero Negro,27.99042198,-114.1699669,13054,Mexico,MX,MEX,Baja California Sur
Piedras Negras,Piedras Negras,28.70763918,-100.5316521,137295,Mexico,MX,MEX,Coahuila
San Pedro de las Colonias,San Pedro de las Colonias,25.7592145,-102.9826911,53688,Mexico,MX,MEX,Coahuila
Sierra Mojada,Sierra Mojada,27.28757082,-103.2871945,10,Mexico,MX,MEX,Coahuila
Parras,Parras,25.42039797,-102.1799494,23714,Mexico,MX,MEX,Coahuila
Cuauhtemoc,Cuauhtemoc,28.42574424,-106.8695856,84967.5,Mexico,MX,MEX,Chihuahua
Nuevo Casas Grandes,Nuevo Casas Grandes,30.41849082,-107.9118993,53091,Mexico,MX,MEX,Chihuahua
Ojinaga,Ojinaga,29.54040489,-104.41002,19804.5,Mexico,MX,MEX,Chihuahua
Villa Ahumada,Villa Ahumada,30.61044293,-106.5099952,8213.5,Mexico,MX,MEX,Chihuahua
Santa Barbara,Santa Barbara,26.80044293,-105.8200373,8413.5,Mexico,MX,MEX,Chihuahua
Ciudad Camargo,Ciudad Camargo,27.69041445,-105.1700511,35904.5,Mexico,MX,MEX,Chihuahua
Cuencame,Cuencame,24.8704057,-103.6999858,5416,Mexico,MX,MEX,Durango
Papasquiaro,Papasquiaro,24.83040814,-105.3399891,11635.5,Mexico,MX,MEX,Durango
Escuinapa,Escuinapa,22.85042564,-105.7999868,28248,Mexico,MX,MEX,Sinaloa
Guamuchil,Guamuchil,25.47036908,-108.0900021,60985.5,Mexico,MX,MEX,Sinaloa
Guasave,Guasave,25.57049217,-108.4699789,82654.5,Mexico,MX,MEX,Sinaloa
El Fuerte,El Fuerte,26.42041445,-108.6199956,8326.5,Mexico,MX,MEX,Sinaloa
Eldorado,Eldorado,24.3304645,-107.3699943,15750.5,Mexico,MX,MEX,Sinaloa
La Cruz,La Cruz,23.92041201,-106.900023,11527.5,Mexico,MX,MEX,Sinaloa
Agua Prieta,Agua Prieta,31.32233746,-109.5630388,77264.5,Mexico,MX,MEX,Sonora
Ciudad Obregon,Ciudad Obregon,27.46660382,-109.9249805,273082,Mexico,MX,MEX,Sonora
Navajoa,Navajoa,27.08189862,-109.4546216,116093,Mexico,MX,MEX,Sonora
Caborca,Caborca,30.71614707,-112.1642495,55126.5,Mexico,MX,MEX,Sonora
Mazatl?n,Mazatlan,29.01710349,-110.1333399,469217,Mexico,MX,MEX,Sonora
Cananea,Cananea,30.99041974,-110.3000481,28625.5,Mexico,MX,MEX,Sonora
Huatabampo,Huatabampo,26.83041526,-109.6300373,27744.5,Mexico,MX,MEX,Sonora
Zacatecas,Zacatecas,22.77043052,-102.5800025,176521.5,Mexico,MX,MEX,Zacatecas
Juan Aldama,Juan Aldama,24.29041526,-103.3899789,13117.5,Mexico,MX,MEX,Zacatecas
Valparaiso,Valparaiso,22.77043052,-103.5699679,7956.5,Mexico,MX,MEX,Zacatecas
Fresnillo,Fresnillo,23.17043194,-102.8599854,102629.5,Mexico,MX,MEX,Zacatecas
Linares,Linares,24.86038047,-99.57003117,52349.5,Mexico,MX,MEX,Nuevo Le?n
Matehuala,Matehuala,23.6603762,-100.6500169,63624.5,Mexico,MX,MEX,San Luis Potos?
Tamuin,Tamuin,21.98037539,-98.7500037,11076.5,Mexico,MX,MEX,San Luis Potos?
Tamazunchale,Tamazunchale,21.27041872,-98.7799502,47108.5,Mexico,MX,MEX,San Luis Potos?
Tula,Tula,23.00039064,-99.71999618,4683,Mexico,MX,MEX,Tamaulipas
Aldama,Aldama,22.92042137,-98.06996769,11367,Mexico,MX,MEX,Tamaulipas
San Fernando,San Fernando,24.85043276,-98.16001388,25596,Mexico,MX,MEX,Tamaulipas
Tecoman,Tecoman,18.92038129,-103.8799748,85450,Mexico,MX,MEX,Colima
Puerto Vallarta,Puerto Vallarta,20.67709576,-105.2449819,183969,Mexico,MX,MEX,Jalisco
La Barca,La Barca,20.28037579,-102.5600037,34897,Mexico,MX,MEX,Jalisco
Ciudad Guzman,Ciudad Guzman,19.71041058,-103.4600004,90480,Mexico,MX,MEX,Jalisco
Lagos de Moreno,Lagos de Moreno,21.37041262,-101.9299905,89402,Mexico,MX,MEX,Jalisco
Morelia,Morelia,19.73338076,-101.189493,618551.5,Mexico,MX,MEX,Michoac?n
Lazaro Cardenas,Lazaro Cardenas,17.95870872,-102.199974,122044,Mexico,MX,MEX,Michoac?n
Zamora,Zamora,19.98036826,-102.2800208,169931.5,Mexico,MX,MEX,Michoac?n
Coalcoman,Coalcoman,18.78038983,-103.1499677,9687.5,Mexico,MX,MEX,Michoac?n
Uruapan,Uruapan,19.42037661,-102.0700078,250919.5,Mexico,MX,MEX,Michoac?n
Tuxpan,Tuxpan,21.93040428,-105.2699675,26115,Mexico,MX,MEX,Nayarit
Tepic,Tepic,21.50539146,-104.8799913,299686.5,Mexico,MX,MEX,Nayarit
Compostela,Compostela,21.23042116,-104.8999901,15192,Mexico,MX,MEX,Nayarit
Tecuala,Tecuala,22.40042727,-105.4599817,12752,Mexico,MX,MEX,Nayarit
Ciudad del Carmen,Ciudad del Carmen,18.65365928,-91.82448019,148751.5,Mexico,MX,MEX,Campeche
Champoton,Champoton,19.35043256,-90.72000289,25722.5,Mexico,MX,MEX,Campeche
Salina Cruz,Salina Cruz,16.16706097,-95.19998784,77355.5,Mexico,MX,MEX,Oaxaca
Puerto Escondido,Puerto Escondido,15.85918031,-97.06588835,15402.5,Mexico,MX,MEX,Oaxaca
Pochutla,Pochutla,15.73039512,-96.46998784,18779.5,Mexico,MX,MEX,Oaxaca
Mitla,Mitla,16.91704103,-96.39999211,4313,Mexico,MX,MEX,Oaxaca
Tlaxiaco,Tlaxiaco,17.27040448,-97.68001734,17999.5,Mexico,MX,MEX,Oaxaca
Huajuapan de Leon,Huajuapan de Leon,17.81037152,-97.78998478,41766.5,Mexico,MX,MEX,Oaxaca
Tehuacan,Tehuacan,18.4503583,-97.37998397,239370.5,Mexico,MX,MEX,Puebla
Teziutlan,Teziutlan,19.82042971,-97.35998519,124307.5,Mexico,MX,MEX,Puebla
Frontera,Frontera,18.5803762,-92.64998845,15014,Mexico,MX,MEX,Tabasco
Tenosique,Tenosique,17.48036582,-91.42998539,24949.5,Mexico,MX,MEX,Tabasco
Salamanca,Salamanca,20.57040977,-101.2000092,168069,Mexico,MX,MEX,Guanajuato
Guanajuato,Guanajuato,21.02040814,-101.2799785,95282,Mexico,MX,MEX,Guanajuato
Taxco,Taxco,18.57037681,-99.6199506,53217,Mexico,MX,MEX,Guerrero
Ayutla,Ayutla,16.90037539,-99.22000086,9897,Mexico,MX,MEX,Guerrero
Ciudad Altamirano,Ciudad Altamirano,18.32039207,-100.6500169,24533,Mexico,MX,MEX,Guerrero
Petatlan,Petatlan,17.52041506,-101.2700308,26474,Mexico,MX,MEX,Guerrero
Pachuca,Pachuca,20.17043418,-98.73003076,310861,Mexico,MX,MEX,Hidalgo
Toluca,Toluca,19.3303821,-99.66999923,1018440.5,Mexico,MX,MEX,M?xico
Zumpango,Zumpango,19.81040448,-99.10998173,188994,Mexico,MX,MEX,M?xico
Minatitlan,Minatitlan,17.9804645,-94.53000289,176398.5,Mexico,MX,MEX,Veracruz
Coatzacoalcos,Coatzacoalcos,18.12040428,-94.4200096,259001,Mexico,MX,MEX,Veracruz
Poza Rica de Hidalgo,Poza Rica de Hidalgo,20.55043683,-97.46997848,214503.5,Mexico,MX,MEX,Veracruz
Cordoba,Cordoba,18.92038129,-96.91998621,177483,Mexico,MX,MEX,Veracruz
Santiago Tuxtla,Santiago Tuxtla,18.47038291,-95.29998173,13598,Mexico,MX,MEX,Veracruz
Tuxpam,Tuxpam,20.9604118,-97.40998214,58690,Mexico,MX,MEX,Veracruz
Panuco,Panuco,22.06044802,-98.18998621,33449.5,Mexico,MX,MEX,Veracruz
Pijijiapan,Pijijiapan,15.69039756,-93.22003117,19388,Mexico,MX,MEX,Chiapas
Isla Mujeres,Isla Mujeres,21.20839057,-86.7114549,12491,Mexico,MX,MEX,Quintana Roo
Felipe Carrillo Puerto,Felipe Carrillo Puerto,19.58039268,-88.04998499,23958,Mexico,MX,MEX,Quintana Roo
Tizimin,Tizimin,21.13042727,-88.14997888,41322.5,Mexico,MX,MEX,Yucat?n
Valladolid,Valladolid,20.67040367,-88.20000167,44071,Mexico,MX,MEX,Yucat?n
Izamal,Izamal,20.93041363,-89.02005497,14570,Mexico,MX,MEX,Yucat?n
Ticul,Ticul,20.40039431,-89.53002385,30400.5,Mexico,MX,MEX,Yucat?n
Ensenada,Ensenada,31.86997845,-116.6199982,238751,Mexico,MX,MEX,Baja California
Saltillo,Saltillo,25.41995872,-101.0049823,679286.5,Mexico,MX,MEX,Coahuila
Ciudad Ju?rez,Ciudad Juarez,31.69037701,-106.4900481,1343000,Mexico,MX,MEX,Chihuahua
Delicias,Delicias,28.19996991,-105.4999793,108876,Mexico,MX,MEX,Chihuahua
Durango,Durango,24.03110292,-104.67003,456368.5,Mexico,MX,MEX,Durango
Los Mochis,Los Mochis,25.78998781,-108.9999982,231824,Mexico,MX,MEX,Sinaloa
Ciudad Victoria,Ciudad Victoria,23.71995913,-99.12998051,272411.5,Mexico,MX,MEX,Tamaulipas
Aguascalientes,Aguascalientes,21.87945992,-102.2904135,763589.5,Mexico,MX,MEX,Aguascalientes
Manzanillo,Manzanillo,19.04958662,-104.3230851,85236.5,Mexico,MX,MEX,Colima
Tehuantepec,Tehuantepec,16.32999676,-95.229986,40082.5,Mexico,MX,MEX,Oaxaca
Villahermosa,Villahermosa,17.99997235,-92.89997319,395482.5,Mexico,MX,MEX,Tabasco
Cuernavaca,Cuernavaca,18.92110476,-99.23999964,591551.5,Mexico,MX,MEX,Morelos
Queretaro,Queretaro,20.63001853,-100.3799817,786392.5,Mexico,MX,MEX,Quer?taro
Tapachula,Tapachula,14.89998069,-92.2699858,209741,Mexico,MX,MEX,Chiapas
Chetumal,Chetumal,18.50001935,-88.29999557,144464.5,Mexico,MX,MEX,Quintana Roo
Progreso,Progreso,21.28331199,-89.66657882,33892.5,Mexico,MX,MEX,Yucat?n
Cabo San Lucas,Cabo San Lucas,22.89275617,-109.9045164,39492.5,Mexico,MX,MEX,Baja California Sur
Monclova,Monclova,26.89999758,-101.4199958,216004,Mexico,MX,MEX,Coahuila
Ometepec,Ometepec,16.68005292,-98.42002385,24036,Mexico,MX,MEX,Guerrero
Cozumel,Cozumel,20.51000002,-86.95000045,67634,Mexico,MX,MEX,Quintana Roo
Mexicali,Mexicali,32.64998252,-115.4800161,736138.5,Mexico,MX,MEX,Baja California
La Paz,La Paz,24.13995933,-110.3199952,180626,Mexico,MX,MEX,Baja California Sur
Torreon,Torreon,25.57005292,-103.4200029,834033,Mexico,MX,MEX,Coahuila
Culiacan,Culiacan,24.82999473,-107.3799679,695734.5,Mexico,MX,MEX,Sinaloa
Nogales,Nogales,31.30500002,-110.9449958,99402,Mexico,MX,MEX,Sonora
Hermosillo,Hermosillo,29.09888145,-110.954065,554373,Mexico,MX,MEX,Sonora
Guaymas,Guaymas,27.93001223,-110.8899862,84496.5,Mexico,MX,MEX,Sonora
San Luis Potosi,San Luis Potosi,22.16997622,-100.9999956,834852,Mexico,MX,MEX,San Luis Potos?
Matamoros,Matamoros,25.87998232,-97.50000248,451394.5,Mexico,MX,MEX,Tamaulipas
Nuevo Laredo,Nuevo Laredo,27.4999868,-99.55000655,255152.5,Mexico,MX,MEX,Tamaulipas
Colima,Colima,19.22997479,-103.7200104,175261,Mexico,MX,MEX,Colima
Campeche,Campeche,19.82998985,-90.49999048,204048.5,Mexico,MX,MEX,Campeche
Oaxaca,Oaxaca,17.08268984,-96.66994979,396647,Mexico,MX,MEX,Oaxaca
Leon,Leon,21.1499868,-101.7000304,1301313,Mexico,MX,MEX,Guanajuato
Tijuana,Tijuana,32.50001752,-117.079996,1464728.5,Mexico,MX,MEX,Baja California
Chihuahua,Chihuahua,28.64498151,-106.0849823,750633.5,Mexico,MX,MEX,Chihuahua
Mazatlan,Mazatlan,23.22110069,-106.4200007,361460.5,Mexico,MX,MEX,Sinaloa
Tampico,Tampico,22.30001996,-97.87000574,578351.5,Mexico,MX,MEX,Tamaulipas
Acapulco,Acapulco,16.84999086,-99.91597905,683860,Mexico,MX,MEX,Guerrero
Veracruz,Veracruz,19.17734235,-96.15998092,573638,Mexico,MX,MEX,Veracruz
Tuxtla Gutierrez,Tuxtla Gutierrez,16.74999697,-93.1500096,473719,Mexico,MX,MEX,Chiapas
Cancun,Cancun,21.16995974,-86.83000777,489452.5,Mexico,MX,MEX,Quintana Roo
Merida,Merida,20.96663881,-89.61663355,841087.5,Mexico,MX,MEX,Yucat?n
Guadalajara,Guadalajara,20.67001609,-103.3300342,2919294.5,Mexico,MX,MEX,Jalisco
Puebla,Puebla,19.04995994,-98.20003727,1793549.5,Mexico,MX,MEX,Puebla
Monterrey,Monterrey,25.66999514,-100.3299848,2417437,Mexico,MX,MEX,Nuevo Le?n
Mexico City,Mexico City,19.44244244,-99.1309882,14919501,Mexico,MX,MEX,Distrito Federal
Dubasari,Dubasari,47.2630556,29.1608333,23254,Moldova,MD,MDA,Transnistria
Balti,Balti,47.75908612,27.90531449,135022.5,Moldova,MD,MDA,Balti
Cahul,Cahul,45.90788129,28.19444413,48949.5,Moldova,MD,MDA,Cahul
Tiraspol,Tiraspol,46.85309491,29.63998897,137097,Moldova,MD,MDA,Bender
Chisinau,Chisinau,47.00502362,28.85771114,662064,Moldova,MD,MDA,Chisinau
Monaco,Monaco,43.73964569,7.406913173,36371,Monaco,MC,MCO,
Suchboatar,Suchboatar,50.24999712,106.2000006,24235,Mongolia,MN,MNG,Selenge
Dzuunmod,Dzuunmod,47.71099805,106.9470006,17738,Mongolia,MN,MNG,T?v
Tsetserleg,Tsetserleg,47.47688112,101.4501794,18056,Mongolia,MN,MNG,Arhangay
Olgiy,Olgiy,48.93369143,89.95000281,31667,Mongolia,MN,MNG,Bayan-?lgiy
Ulaan-Uul,Ulaan-Uul,44.33371381,111.2333032,3726,Mongolia,MN,MNG,Dornogovi
Hodrogo,Hodrogo,48.96642845,96.7832808,10,Mongolia,MN,MNG,Dzavhan
Buyant-Uhaa,Buyant-Uhaa,44.86660118,110.1500101,8776,Mongolia,MN,MNG,Dornogovi
Ondorhaan,Ondorhaan,47.31668418,110.6500313,12433.5,Mongolia,MN,MNG,Hentiy
Bayankhongor,Bayankhongor,46.30000205,100.9833345,26252,Mongolia,MN,MNG,Bayanhongor
Uliastay,Uliastay,47.75001691,96.81671545,8056,Mongolia,MN,MNG,Dzavhan
Altay,Altay,46.39612022,95.8450435,32488,Mongolia,MN,MNG,Govi-Altay
Moron,Moron,49.6452759,100.1544445,24608.5,Mongolia,MN,MNG,H?vsg?l
Ulaangom,Ulaangom,49.98331728,92.0666178,31940.5,Mongolia,MN,MNG,Uvs
Bulgan,Bulgan,48.81059816,103.5317061,17348,Mongolia,MN,MNG,Bulgan
Mandalgovi,Mandalgovi,45.74998395,106.2660095,2984,Mongolia,MN,MNG,Dundgovi
Darhan,Darhan,49.61669883,106.3500354,74738,Mongolia,MN,MNG,Selenge
Dzuunharaa,Dzuunharaa,48.86658958,106.4666174,16074,Mongolia,MN,MNG,Selenge
Arvayheer,Arvayheer,46.24997927,102.7665848,28053,Mongolia,MN,MNG,?v?rhangay
Baruun Urt,Baruun Urt,46.69997764,113.2833073,15805,Mongolia,MN,MNG,S?hbaatar
Dalandzadgad,Dalandzadgad,43.58355288,104.4402811,13491,Mongolia,MN,MNG,?mn?govi
Dund-Us,Dund-Us,48.01664146,91.63325924,26596.5,Mongolia,MN,MNG,Hovd
Choybalsan,Choybalsan,48.06658673,114.5060233,33376,Mongolia,MN,MNG,Dornod
Erdenet,Erdenet,49.05329653,104.118337,79647,Mongolia,MN,MNG,Orhon
Ulaanbaatar,Ulaanbaatar,47.9166734,106.9166158,827306,Mongolia,MN,MNG,Ulaanbaatar
Podgorica,Podgorica,42.46597251,19.26630692,141161.5,Montenegro,ME,MNE,Podgorica
Ksar El Kebir,Ksar El Kebir,35.02038047,-5.909985801,207676.5,Morocco,MA,MAR,Tanger - T?touan
Larache,Larache,35.20042116,-6.160022218,114688,Morocco,MA,MAR,Tanger - T?touan
Taza,Taza,34.22037762,-4.019971966,170761.5,Morocco,MA,MAR,Taza - Al Hoceima - Taounate
Ouezzane,Ouezzane,34.81034161,-5.570006553,64171,Morocco,MA,MAR,Gharb - Chrarda - B?ni Hssen
Kenitra,Kenitra,34.27040041,-6.579996583,459178,Morocco,MA,MAR,Gharb - Chrarda - B?ni Hssen
Settat,Settat,33.01042564,-7.620010622,140415,Morocco,MA,MAR,Chaouia - Ouardigha
Er Rachidia,Er Rachidia,31.94041343,-4.449971559,228489,Morocco,MA,MAR,Mekn?s - Tafilalet
Meknes,Meknes,33.90042299,-5.559981325,621666.5,Morocco,MA,MAR,Mekn?s - Tafilalet
Tiznit,Tiznit,29.71042035,-9.73998458,56398.5,Morocco,MA,MAR,Souss - Massa - Dra?
El Jadida,El Jadida,33.2603587,-8.509982138,164009.5,Morocco,MA,MAR,Doukkala - Abda
Dawra,Dawra,27.46290895,-12.99218917,10,Morocco,MA,MAR,La?youne - Boujdour - Sakia El Hamra
Lemsid,Lemsid,26.54818656,-13.84819219,100,Morocco,MA,MAR,La?youne - Boujdour - Sakia El Hamra
Tan Tan,Tan Tan,28.43039512,-11.10003076,63396,Morocco,MA,MAR,Guelmim - Es-Semara
Bir Anzarane,Bir Anzarane,23.88374758,-14.53330957,6597,Morocco,MA,MAR,Oued el Dahab
Tangier,Tangier,35.74728701,-5.832703696,719208,Morocco,MA,MAR,Tanger - T?touan
Agadir,Agadir,30.43998822,-9.620043581,752031.5,Morocco,MA,MAR,Souss - Massa - Dra?
Goulimine,Goulimine,28.97997398,-10.07001611,106748,Morocco,MA,MAR,Guelmim - Es-Semara
Smara,Smara,26.73328941,-11.68332849,48149,Morocco,MA,MAR,Guelmim - Es-Semara
Ad Dakhla,Ad Dakhla,23.71405588,-15.93681087,82146,Morocco,MA,MAR,Oued el Dahab
Oujda,Oujda,34.69001304,-1.909971559,407322,Morocco,MA,MAR,Oriental
Safi,Safi,32.31997683,-9.239989259,320819.5,Morocco,MA,MAR,Doukkala - Abda
Laayoune,Laayoune,27.14998232,-13.20000594,182224.5,Morocco,MA,MAR,La?youne - Boujdour - Sakia El Hamra
Fez,Fez,34.05459963,-5.000377239,983445.5,Morocco,MA,MAR,F?s - Boulemane
Rabat,Rabat,34.02529909,-6.83613082,1680376.5,Morocco,MA,MAR,Rabat - Sal? - Zemmour - Zaer
Marrakesh,Marrakesh,31.6299931,-7.999987428,855648,Morocco,MA,MAR,Marrakech - Tensift - Al Haouz
Casablanca,Casablanca,33.59997622,-7.616367433,3162954.5,Morocco,MA,MAR,Grand Casablanca
Moatize,Moatize,-16.09954832,33.95001013,40536.5,Mozambique,MZ,MOZ,Tete
Luangwa,Luangwa,-15.61957762,30.41001949,3065,Mozambique,MZ,MOZ,Tete
Manica,Manica,-18.96960569,32.87999792,3713.5,Mozambique,MZ,MOZ,Manica
Espungabera,Espungabera,-20.45013548,32.77003048,393,Mozambique,MZ,MOZ,Manica
Montepuez,Montepuez,-13.11957518,39.0000378,49041,Mozambique,MZ,MOZ,Cabo Delgado
Mocimboa,Mocimboa,-11.31958169,40.34998124,27909,Mozambique,MZ,MOZ,Cabo Delgado
Marrupa,Marrupa,-13.19838174,37.49945756,8762,Mozambique,MZ,MOZ,Nassa
Cuamba,Cuamba,-14.78960244,36.53998124,68204.5,Mozambique,MZ,MOZ,Nassa
Ligonha,Ligonha,-15.17567706,37.74001135,3310.5,Mozambique,MZ,MOZ,Nampula
Macia,Macia,-25.01952065,33.09001094,13095,Mozambique,MZ,MOZ,Gaza
Massangena,Massangena,-21.53730426,32.95637569,634.5,Mozambique,MZ,MOZ,Gaza
Mapai,Mapai,-22.84265094,31.96305131,201,Mozambique,MZ,MOZ,Gaza
Dondo,Dondo,-19.61959186,34.7300142,75217.5,Mozambique,MZ,MOZ,Sofala
Chiramba,Chiramba,-16.89210976,34.65585852,556,Mozambique,MZ,MOZ,Sofala
Mocuba,Mocuba,-16.84958006,38.26003129,68984,Mozambique,MZ,MOZ,Zambezia
Nicuadala,Nicuadala,-17.60767332,36.81970577,6945,Mozambique,MZ,MOZ,Zambezia
Maxixe,Maxixe,-23.86602274,35.38855095,112881.5,Mozambique,MZ,MOZ,Inhambane
Panda,Panda,-24.06288654,34.73027258,602,Mozambique,MZ,MOZ,Inhambane
Quissico,Quissico,-24.72568846,34.765981,1210,Mozambique,MZ,MOZ,Inhambane
Vilanculos,Vilanculos,-21.99954995,35.31659338,177,Mozambique,MZ,MOZ,Inhambane
Matola,Matola,-25.96959186,32.46002356,503368,Mozambique,MZ,MOZ,Maputo
Chimoio,Chimoio,-19.12003579,33.47003943,242538.5,Mozambique,MZ,MOZ,Manica
Lichinga,Lichinga,-13.30002928,35.24000891,94333.5,Mozambique,MZ,MOZ,Nassa
Angoche,Angoche,-16.23003131,39.9100081,57835,Mozambique,MZ,MOZ,Nampula
Mocambique,Mocambique,-15.03989895,40.68218367,40700.5,Mozambique,MZ,MOZ,Nampula
Inhambane,Inhambane,-23.85803973,35.33981752,94830,Mozambique,MZ,MOZ,Inhambane
Tete,Tete,-16.17003497,33.58000688,122183,Mozambique,MZ,MOZ,Tete
Pemba,Pemba,-12.98304604,40.53234737,109690,Mozambique,MZ,MOZ,Cabo Delgado
Nampula,Nampula,-15.13604124,39.29304317,386185.5,Mozambique,MZ,MOZ,Nampula
Xai-Xai,Xai-Xai,-25.03998452,33.64000321,128085.5,Mozambique,MZ,MOZ,Gaza
Quelimane,Quelimane,-17.88000812,36.88998572,179032.5,Mozambique,MZ,MOZ,Zambezia
Nacala,Nacala,-14.51861123,40.71502356,212212.5,Mozambique,MZ,MOZ,Nampula
Beira,Beira,-19.82004474,34.87000565,507196.5,Mozambique,MZ,MOZ,Sofala
Maputo,Maputo,-25.95527749,32.58916296,1318806.5,Mozambique,MZ,MOZ,Maputo
Loikaw,Loikaw,19.66500009,97.20600363,17293,Myanmar,MM,MMR,Kayah
Pa-an,Pa-an,16.8499981,97.61670064,50000,Myanmar,MM,MMR,Kayin
Hakha,Haka,22.6500031,93.6167046,20000,Myanmar,MM,MMR,Chin
Taunggyi,Taunggyi,20.78199907,97.03800065,160115,Myanmar,MM,MMR,Shan
Sagaing,Sagaing,21.87999903,95.9619966,78739,Myanmar,MM,MMR,Sagaing
Myingyan,Myingyan,21.46182823,95.39142777,152762.5,Myanmar,MM,MMR,Mandalay
Letpadan,Letpadan,17.78189781,95.74148393,107753.5,Myanmar,MM,MMR,Bago
Taungoo,Taungoo,18.94828656,96.41792843,105590.5,Myanmar,MM,MMR,Bago
Thongwa,Thongwa,16.75469952,96.51931759,35992.5,Myanmar,MM,MMR,Yangon
Mudon,Mudon,16.26183555,97.72146643,120711.5,Myanmar,MM,MMR,Mon
Ye,Ye,15.25326662,97.86786576,50798,Myanmar,MM,MMR,Mon
Mawlamyine,Mawlamyine,16.50042564,97.67004838,400249,Myanmar,MM,MMR,Mon
Kyaukphyu,Kyaukphyu,19.42901315,93.54940356,4261,Myanmar,MM,MMR,Rakhine
Wakema,Wakema,16.61328697,95.18286169,45555,Myanmar,MM,MMR,Ayeyarwady
Labutta,Labutta,16.16189333,94.70144405,1667,Myanmar,MM,MMR,Ayeyarwady
Phyarpon,Phyarpon,16.29325482,95.68288285,63177,Myanmar,MM,MMR,Ayeyarwady
Yandoon,Yandoon,17.04328656,95.64288529,36172,Myanmar,MM,MMR,Ayeyarwady
Hinthada,Hinthada,17.64826255,95.46785722,157837.5,Myanmar,MM,MMR,Ayeyarwady
Pathein,Pathein,16.77040916,94.74996822,216014.5,Myanmar,MM,MMR,Ayeyarwady
Allanmyo,Allanmyo,19.37831199,95.22792354,48446.5,Myanmar,MM,MMR,Magway
Yaynangyoung,Yaynangyoung,20.46145001,94.88096798,104507.5,Myanmar,MM,MMR,Magway
Chauk,Chauk,20.90847699,94.8230387,85016.5,Myanmar,MM,MMR,Magway
Pakokku,Pakokku,21.33204287,95.08664018,125355.5,Myanmar,MM,MMR,Magway
Namtu,Namtu,23.08374473,97.39998734,48591,Myanmar,MM,MMR,Shan
Dawei,Dawei,14.09796246,98.19497758,141497.5,Myanmar,MM,MMR,Tanintharyi
Shwebo,Shwebo,22.57827171,95.6928564,81758.5,Myanmar,MM,MMR,Sagaing
Bago,Bago,17.32001385,96.51497676,264347,Myanmar,MM,MMR,Bago
Pyu,Pyu,18.477876,96.43787553,37652,Myanmar,MM,MMR,Bago
Pyay,Pyay,18.81645998,95.21143876,124833.5,Myanmar,MM,MMR,Bago
Magway,Magway,20.14454429,94.91957027,111463.5,Myanmar,MM,MMR,Magway
Myitkyina,Myitkyina,25.35962648,97.39275264,114997,Myanmar,MM,MMR,Kachin
Monywa,Monywa,22.1049931,95.14999548,204116.5,Myanmar,MM,MMR,Sagaing
Myeik,Myeik,12.45408347,98.61148962,220009,Myanmar,MM,MMR,Tanintharyi
Mandalay,Mandalay,21.96998842,96.08502885,1167000,Myanmar,MM,MMR,Mandalay
Sittwe,Sittwe,20.13999676,92.88000484,178387.5,Myanmar,MM,MMR,Rakhine
Naypyidaw,Naypyidaw,19.76655703,96.11861853,562412,Myanmar,MM,MMR,Mandalay
Rangoon,Rangoon,16.7833541,96.16667761,3694910,Myanmar,MM,MMR,Yangon
Omaruru,Omaruru,-21.43600193,15.95099754,11547,Namibia,NA,NAM,Erongo
Karibib,Karibib,-21.93900292,15.85299646,6898,Namibia,NA,NAM,Erongo
Otavi,Otavi,-19.63999801,17.34200155,4562,Namibia,NA,NAM,Otjozondjupa
Gobabis,Gobabis,-22.455,18.96300054,16321,Namibia,NA,NAM,Omaheke
Karasburg,Karasburg,-28.01959593,18.73998246,5071.5,Namibia,NA,NAM,Karas
Bethanie,Bethanie,-26.49953367,17.15000199,8122,Namibia,NA,NAM,Karas
Oranjemund,Oranjemund,-28.54948606,16.42999426,7223,Namibia,NA,NAM,Karas
Mariental,Mariental,-24.61959674,17.95992672,12670,Namibia,NA,NAM,Hardap
Rehoboth,Rehoboth,-23.31957273,17.0800321,23298,Namibia,NA,NAM,Hardap
Outjo,Outjo,-20.10953611,16.1400378,6363.5,Namibia,NA,NAM,Kunene
Opuwo,Opuwo,-18.05958372,13.82002437,4857,Namibia,NA,NAM,Kunene
Usakos,Usakos,-21.99954995,15.5800203,5393.5,Namibia,NA,NAM,Erongo
Okahandja,Okahandja,-21.97960285,16.91001664,19691,Namibia,NA,NAM,Otjozondjupa
Otjiwarongo,Otjiwarongo,-20.45954059,16.64000728,23019.5,Namibia,NA,NAM,Otjozondjupa
Oshikango,Oshikango,-17.39952065,15.88000199,7540.5,Namibia,NA,NAM,Ohangwena
Cuangar,Cuangar,-17.60953367,18.61998979,425,Namibia,NA,NAM,Kavango
Katima Mulilo,Katima Mulilo,-17.4996179,24.26000728,21748.5,Namibia,NA,NAM,Caprivi
Keetmanshoop,Keetmanshoop,-26.57389606,18.12999385,16823.5,Namibia,NA,NAM,Karas
Maltah?he,Maltahohe,-24.83999673,16.93998897,2329,Namibia,NA,NAM,Hardap
Swakopmund,Swakopmund,-22.6688631,14.53501949,27269,Namibia,NA,NAM,Erongo
Ongwediva,Ongwediva,-17.78001422,15.77003454,17343,Namibia,NA,NAM,Oshana
Rundu,Rundu,-17.92000568,19.74994665,43485,Namibia,NA,NAM,Kavango
Tsumeb,Tsumeb,-19.24002846,17.71001949,13574.5,Namibia,NA,NAM,Oshikoto
L?deritz,Luderitz,-26.64800006,15.15942582,14216,Namibia,NA,NAM,Karas
Walvis Bay,Walvis Bay,-22.95752765,14.50530554,49504.5,Namibia,NA,NAM,Erongo
Windhoek,Windhoek,-22.57000608,17.0835461,265464,Namibia,NA,NAM,Khomas
Grootfontein,Grootfontein,-19.56662352,18.11655798,19149.5,Namibia,NA,NAM,Otjozondjupa
Salyan,Sallyan,28.35000004,82.18330255,15000,Nepal,NP,NPL,Rapti
Baglung,Baglung,28.26669606,83.58329762,23296,Nepal,NP,NPL,Dhawalagiri
Jumla,Jumla,29.25000013,82.21670162,9073,Nepal,NP,NPL,Karnali
Bhairawa,Bhairawa,27.53330409,83.38329953,63367,Nepal,NP,NPL,Lumbini
Dandeldhura,Dandeldhura,29.30000416,80.60000455,19014,Nepal,NP,NPL,Mahakali
Dhangarhi,Dhangarhi,28.69499706,80.5930026,92294,Nepal,NP,NPL,Achham
Ramechhap,Ramechhap,27.32599808,86.08699853,15000,Nepal,NP,NPL,Janakpur
Bhimphedi,Bhimphedi,27.5509981,85.13000156,15000,Nepal,NP,NPL,Narayani
Rajbiraj,Rajbiraj,26.5332961,86.73329761,33061,Nepal,NP,NPL,Sagarmatha
Ilam,Ilam,26.90800207,87.92600453,17491,Nepal,NP,NPL,Mechi
Lalitpur,Lalitpur,27.66661745,85.3333337,191208.5,Nepal,NP,NPL,Bhaktapur
Hetauda,Hetauda,27.41668439,85.03335201,158554.5,Nepal,NP,NPL,Narayani
Nepalganj,Nepalganj,28.0503408,81.61666134,64400,Nepal,NP,NPL,Banke
Birganj,Birganj,27.00040489,84.86659216,133238,Nepal,NP,NPL,Narayani
Biratnagar,Biratnagar,26.48374392,87.28334387,182324,Nepal,NP,NPL,Bhojpur
Pokhara,Pokhara,28.26399603,83.97199855,200000,Nepal,NP,NPL,Gorkha
Kathmandu,Kathmandu,27.71669191,85.31664221,895000,Nepal,NP,NPL,Bhaktapur
Assen,Assen,53.00000109,6.550002585,62237,Netherlands,NL,NLD,Drenthe
Arnhem,Arnhem,51.98799603,5.922999562,141674,Netherlands,NL,NLD,Gelderland
Maastricht,Maastricht,50.85299707,5.677002477,122378,Netherlands,NL,NLD,Limburg
Zwolle,Zwolle,52.52400009,6.096996529,111805,Netherlands,NL,NLD,Overijssel
Middelburg,Middelburg,51.50199618,3.609999541,46485,Netherlands,NL,NLD,Zeeland
's-Hertogenbosch,'s-Hertogenbosch,51.68333714,5.316660485,134520,Netherlands,NL,NLD,Noord-Brabant
Eindhoven,Eindhoven,51.42997316,5.50001542,303836.5,Netherlands,NL,NLD,Noord-Brabant
Leeuwarden,Leeuwarden,53.25037884,5.783357298,108601,Netherlands,NL,NLD,Friesland
Groningen,Groningen,53.22040651,6.580001179,198941,Netherlands,NL,NLD,Groningen
Utrecht,Utrecht,52.10034568,5.120038614,478224,Netherlands,NL,NLD,Utrecht
Haarlem,Haarlem,52.38043194,4.629991006,248773.5,Netherlands,NL,NLD,Noord-Holland
Rotterdam,Rotterdam,51.9199691,4.479974323,801599.5,Netherlands,NL,NLD,Zuid-Holland
The Hague,The Hague,52.08003684,4.269961302,953862.5,Netherlands,NL,NLD,Zuid-Holland
Amsterdam,Amsterdam,52.34996869,4.916640176,886318,Netherlands,NL,NLD,Noord-Holland
Noumea,Noumea,-22.26252776,166.4442852,89742.5,New Caledonia,NC,NCL,Sud
Greymouth,Greymouth,-42.47274975,171.2087246,9419,New Zealand,NZ,NZL,West Coast
Upper Hutt,Upper Hutt,-41.13548786,175.0290474,34591,New Zealand,NZ,NZL,Manawatu-Wanganui
Masterton,Masterton,-40.94392332,175.6456506,16720.5,New Zealand,NZ,NZL,Manawatu-Wanganui
Levin,Levin,-40.61236733,175.2772493,18764,New Zealand,NZ,NZL,Manawatu-Wanganui
Waitakere,Waitakere,-36.84959959,174.5500069,83400,New Zealand,NZ,NZL,Auckland
Takapuna,Takapuna,-36.7912569,174.7758329,184815.5,New Zealand,NZ,NZL,Auckland
Whakatane,Whakatane,-37.98291543,176.9999865,20665,New Zealand,NZ,NZL,Bay of Plenty
Ashburton,Ashburton,-43.89790322,171.7300756,8895,New Zealand,NZ,NZL,Canterbury
Kaiapoi,Kaiapoi,-43.3776249,172.6400459,7169,New Zealand,NZ,NZL,Canterbury
New Plymouth,New Plymouth,-39.0641931,174.0805265,46289.5,New Zealand,NZ,NZL,Taranaki
Westport,Westport,-41.77443223,171.5666665,1899,New Zealand,NZ,NZL,West Coast
Hokitika,Hokitika,-42.72568188,170.9681006,2139,New Zealand,NZ,NZL,West Coast
Oamaru,Oamaru,-45.09731321,170.9710005,6628,New Zealand,NZ,NZL,Otago
Palmerston North,Palmerston North,-40.35269326,175.6072033,66551.5,New Zealand,NZ,NZL,Manawatu-Wanganui
Wanganui,Wanganui,-39.9311686,175.0288407,35866.5,New Zealand,NZ,NZL,Manawatu-Wanganui
Hastings,Hastings,-39.63821491,176.8367924,39107,New Zealand,NZ,NZL,Gisborne
Gisborne,Gisborne,-38.64478717,178.0152217,30857.5,New Zealand,NZ,NZL,Gisborne
Rotorua,Rotorua,-38.13458576,176.2454073,51497.5,New Zealand,NZ,NZL,Auckland
Taupo,Taupo,-38.69300128,176.0770455,17480.5,New Zealand,NZ,NZL,Auckland
Tauranga,Tauranga,-37.69642129,176.1536299,84730,New Zealand,NZ,NZL,Bay of Plenty
Timaru,Timaru,-44.38159463,171.2185823,23306,New Zealand,NZ,NZL,Canterbury
Nelson,Nelson,-41.29258421,173.2474507,37133,New Zealand,NZ,NZL,Nelson
Whangarei,Whangarei,-35.71995278,174.3100215,53299.5,New Zealand,NZ,NZL,Northland
Queenstown,Queenstown,-45.02997882,168.6625109,5332,New Zealand,NZ,NZL,Otago
Invercargill,Invercargill,-46.40942951,168.3650097,37135.5,New Zealand,NZ,NZL,Southland
Napier,Napier,-39.4900069,176.9150305,56787,New Zealand,NZ,NZL,Gisborne
Manukau,Manukau,-36.99997801,174.8849735,336141.5,New Zealand,NZ,NZL,Auckland
Hamilton,Hamilton,-37.77000853,175.3000386,112145,New Zealand,NZ,NZL,Auckland
Blenheim,Blenheim,-41.52099404,173.9592419,23056.5,New Zealand,NZ,NZL,Marlborough
Dunedin,Dunedin,-45.87995278,170.4799711,92438.5,New Zealand,NZ,NZL,Otago
Wellington,Wellington,-41.29997394,174.7832743,296300,New Zealand,NZ,NZL,Manawatu-Wanganui
Christchurch,Christchurch,-43.53503131,172.6300207,295351.5,New Zealand,NZ,NZL,Canterbury
Auckland,Auckland,-36.850013,174.7649808,759510,New Zealand,NZ,NZL,Auckland
Somoto,Somoto,13.47599712,-86.58299659,20316,Nicaragua,NI,NIC,Madriz
Ocotal,Ocotal,13.62999605,-86.47299861,33928,Nicaragua,NI,NIC,Nueva Segovia
San Carlos,San Carlos,11.1999961,-84.83329749,13451,Nicaragua,NI,NIC,Nicaragua
Jinotepe,Jinotepe,11.84599813,-86.19499748,29507,Nicaragua,NI,NIC,Carazo
Jinotega,Jinotega,13.09100402,-86.00000362,51073,Nicaragua,NI,NIC,Jinotega
Masaya,Masaya,11.96900098,-86.09499852,130113,Nicaragua,NI,NIC,Masaya
San Juan del Sur,San Juan del Sur,11.24999676,-85.86004114,5032,Nicaragua,NI,NIC,Nicaragua
Esteli,Esteli,13.08998781,-86.35998478,102130.5,Nicaragua,NI,NIC,Estel?
Boaco,Boaco,12.46997398,-85.66000167,21572,Nicaragua,NI,NIC,Boaco
Juigalpa,Juigalpa,12.10999595,-85.37996708,35451,Nicaragua,NI,NIC,Chontales
Rivas,Rivas,11.44037274,-85.8199919,31117,Nicaragua,NI,NIC,Nicaragua
San Juan de Nicaragua,San Juan de Nicaragua,10.92040448,-83.69999211,863,Nicaragua,NI,NIC,Nicaragua
Granada,Granada,11.93372764,-85.94998397,97314,Nicaragua,NI,NIC,Granada
Chinandega,Chinandega,12.63037762,-87.13004114,132705,Nicaragua,NI,NIC,Chinandega
Matagalpa,Matagalpa,12.91707847,-85.91665267,106514.5,Nicaragua,NI,NIC,Matagalpa
Puerto Cabezas,Puerto Cabezas,14.03334108,-83.38337061,38318,Nicaragua,NI,NIC,Atl?ntico Norte
Leon,Leon,12.43555747,-86.87943628,154489.5,Nicaragua,NI,NIC,Le?n
Bluefields,Bluefields,11.99997683,-83.76494938,40033,Nicaragua,NI,NIC,Atl?ntico Sur
Managua,Managua,12.15301658,-86.26849166,920000,Nicaragua,NI,NIC,Managua
Goure,Goure,13.98740074,10.2700085,13291.5,Niger,NE,NER,Zinder
Gaya,Gaya,11.88817486,3.446652383,29394.5,Niger,NE,NER,Dosso
Tillaberi,Tillaberi,14.21203819,1.453078978,13812,Niger,NE,NER,Niamey
Ayorou,Ayorou,14.73179974,0.919468138,14001,Niger,NE,NER,Niamey
Birni Nkonni,Birni Nkonni,13.79043601,5.259926716,56677.5,Niger,NE,NER,Tahoua
Madaoua,Madaoua,14.07618085,5.95859208,19954,Niger,NE,NER,Tahoua
Diffa,Diffa,13.31705406,12.60888383,29468,Niger,NE,NER,Diffa
Nguigmi,Nguigmi,14.25317263,13.11081702,15318,Niger,NE,NER,Diffa
Dosso,Dosso,13.05001609,3.200000772,46481.5,Niger,NE,NER,Dosso
Arlit,Arlit,18.81997398,7.32998124,90000,Niger,NE,NER,Agadez
Djado,Djado,21.01498212,12.30750688,10,Niger,NE,NER,Agadez
Maradi,Maradi,13.49164288,7.096403767,198021,Niger,NE,NER,Maradi
Tahoua,Tahoua,14.89998069,5.259926716,98190.5,Niger,NE,NER,Tahoua
Zinder,Zinder,13.79999615,8.983317015,210891,Niger,NE,NER,Zinder
Niamey,Niamey,13.51670595,2.116656045,828895.5,Niger,NE,NER,Niamey
Agadez,Agadez,16.99587343,7.98280961,103165.5,Niger,NE,NER,Agadez
Umuahia,Umuahia,5.532003041,7.486002487,264662,Nigeria,NG,NGA,Abia
Uyo,Uyo,5.007996056,7.849998524,495756,Nigeria,NG,NGA,Akwa Ibom
Owerri,Owerri,5.492997053,7.026003588,215038,Nigeria,NG,NGA,Imo
Dutse,Dutse,11.7991891,9.350334607,17129,Nigeria,NG,NGA,Jigawa
Damaturu,Damaturu,11.74899608,11.96600457,255895,Nigeria,NG,NGA,Yobe
Iwo,Iwo,7.629959329,4.179992634,208688.5,Nigeria,NG,NGA,Osun
Iseyin,Iseyin,7.970016092,3.590002806,98071,Nigeria,NG,NGA,Oyo
Biu,Biu,10.62042279,12.18999467,64619.5,Nigeria,NG,NGA,Borno
Bama,Bama,11.5203937,13.69000647,86410,Nigeria,NG,NGA,Borno
Aba,Aba,5.100397968,7.34998002,874385,Nigeria,NG,NGA,Abia
Opobo,Opobo,4.570404479,7.559993041,34911,Nigeria,NG,NGA,Akwa Ibom
Orlu,Orlu,5.783715433,7.033306843,9351,Nigeria,NG,NGA,Imo
Oturkpo,Oturkpo,7.190399596,8.129984089,68220,Nigeria,NG,NGA,Benue
Calabar,Calabar,4.960406513,8.330023558,354656.5,Nigeria,NG,NGA,Cross River
Wukari,Wukari,7.870409769,9.780012572,74380.5,Nigeria,NG,NGA,Taraba
Jalingo,Jalingo,8.900372741,11.36001949,103773,Nigeria,NG,NGA,Taraba
Kontagora,Kontagora,10.4003587,5.469939737,62144,Nigeria,NG,NGA,Niger
Bida,Bida,9.080413431,6.01001013,172752.5,Nigeria,NG,NGA,Niger
Abeokuta,Abeokuta,7.160427265,3.350017455,441231,Nigeria,NG,NGA,Ogun
Ijebu Ode,Ijebu Ode,6.820448017,3.920008503,204501,Nigeria,NG,NGA,Ogun
Akure,Akure,7.250395934,5.199982054,420594,Nigeria,NG,NGA,Ondo
Ikare,Ikare,7.530430521,5.759999551,899965.5,Nigeria,NG,NGA,Ondo
Owo,Owo,7.200398986,5.589984089,200912,Nigeria,NG,NGA,Ondo
Ondo,Ondo,7.0904057,4.840004027,256444,Nigeria,NG,NGA,Ondo
Ado Ekiti,Ado Ekiti,7.630372741,5.219980834,446749,Nigeria,NG,NGA,Ekiti
Ife,Ife,7.480433572,4.560021117,482365,Nigeria,NG,NGA,Osun
Oshogbo,Oshogbo,7.770364196,4.560021117,408245,Nigeria,NG,NGA,Osun
Oyo,Oyo,7.850436828,3.929982054,475016.5,Nigeria,NG,NGA,Oyo
Awka,Awka,6.210433572,7.06999711,400828.5,Nigeria,NG,NGA,Anambra
Onitsha,Onitsha,6.140412007,6.779988972,73374,Nigeria,NG,NGA,Anambra
Azare,Azare,11.68040977,10.19001339,87912.5,Nigeria,NG,NGA,Bauchi
Bauchi,Bauchi,10.3103642,9.84000891,244350.5,Nigeria,NG,NGA,Bauchi
Gombe,Gombe,10.29044293,11.16995357,260312,Nigeria,NG,NGA,Gombe
Kumo,Kumo,10.04570335,11.21305172,19249,Nigeria,NG,NGA,Gombe
Sapele,Sapele,5.890427265,5.680004434,235424,Nigeria,NG,NGA,Delta
Nsukka,Nsukka,6.867034321,7.383362995,111017,Nigeria,NG,NGA,Enugu
Lokoja,Lokoja,7.800388203,6.739939737,52650.5,Nigeria,NG,NGA,Kogi
Idah,Idah,7.110404479,6.739939737,71895,Nigeria,NG,NGA,Kogi
Lafia,Lafia,8.490423603,8.5200378,79470.5,Nigeria,NG,NGA,Nassarawa
Keffi,Keffi,8.849032205,7.873617308,77056.5,Nigeria,NG,NGA,Nassarawa
Funtua,Funtua,11.5203937,7.320007689,158643,Nigeria,NG,NGA,Katsina
Katsina,Katsina,12.99040733,7.599990599,432149,Nigeria,NG,NGA,Katsina
Gusau,Gusau,12.1704057,6.659996296,185925,Nigeria,NG,NGA,Zamfara
Nguru,Nguru,12.8803882,10.44999752,82481,Nigeria,NG,NGA,Yobe
Gashua,Gashua,12.87049217,11.03998734,74825.5,Nigeria,NG,NGA,Yobe
Potiskum,Potiskum,11.7103821,11.0799849,82733.5,Nigeria,NG,NGA,Yobe
Birnin Kebbi,Birnin Kebbi,12.45041445,4.199939737,102340.5,Nigeria,NG,NGA,Kebbi
Koko,Koko,11.42319033,4.516974649,25792,Nigeria,NG,NGA,Kebbi
Mubi,Mubi,10.2703408,13.2700321,214710,Nigeria,NG,NGA,Adamawa
Numan,Numan,9.460441914,12.04002966,45173,Nigeria,NG,NGA,Adamawa
Ilorin,Ilorin,8.490010192,4.549995889,701742,Nigeria,NG,NGA,Kwara
Minna,Minna,9.619992898,6.550028848,249038,Nigeria,NG,NGA,Niger
Zaria,Zaria,11.0799813,7.710009724,754836.5,Nigeria,NG,NGA,Kaduna
Jos,Jos,9.929973978,8.890041055,737068.5,Nigeria,NG,NGA,Plateau
Yola,Yola,9.209992085,12.48000281,92253,Nigeria,NG,NGA,Adamawa
Benin City,Benin City,6.340477314,5.620008096,929013,Nigeria,NG,NGA,Edo
Maiduguri,Maiduguri,11.84996014,13.16001298,704230,Nigeria,NG,NGA,Borno
Port Harcourt,Port Harcourt,4.810002257,7.010000772,1020000,Nigeria,NG,NGA,Rivers
Makurdi,Makurdi,7.729979064,8.530011351,245367.5,Nigeria,NG,NGA,Benue
Ibadan,Ibadan,7.380026264,3.929982054,2221285,Nigeria,NG,NGA,Oyo
Ogbomosho,Ogbomosho,8.130006326,4.239988972,595063.5,Nigeria,NG,NGA,Oyo
Warri,Warri,5.519958922,5.759999551,683064.5,Nigeria,NG,NGA,Delta
Kaduna,Kaduna,10.52001548,7.440000365,1191296.5,Nigeria,NG,NGA,Kaduna
Enugu,Enugu,6.450031351,7.499996703,688862,Nigeria,NG,NGA,Enugu
Sokoto,Sokoto,13.06001548,5.240031289,648019.5,Nigeria,NG,NGA,Sokoto
Abuja,Abuja,9.083333149,7.533328002,869067.5,Nigeria,NG,NGA,Federal Capital Territory
Kano,Kano,11.99997683,8.5200378,3140000,Nigeria,NG,NGA,Kano
Lagos,Lagos,6.443261653,3.391531071,4733768,Nigeria,NG,NGA,Lagos
Sariwon,Sariwon,38.50700411,125.7620047,154942,North Korea,KP,PRK,Hwanghae-bukto
Sin-Ni,Sin-Ni,39.48800415,125.4639966,19463,North Korea,KP,PRK,P'yongan-namdo
Changyon,Changyon,38.25173362,125.1020691,44176,North Korea,KP,PRK,Hwanghae-namdo
Anbyon,Anbyon,39.02817202,127.5185624,34993.5,North Korea,KP,PRK,Kangwon-do
Munchon,Munchon,39.38130292,127.2517053,73619,North Korea,KP,PRK,Kangwon-do
Kaesong,Kaesong,37.96399925,126.5644087,305333.5,North Korea,KP,PRK,Kaesong
Chosan,Chosan,40.82547833,125.8008378,7786,North Korea,KP,PRK,Chagang-do
Manpo,Manpo,41.14543296,126.2958463,186827,North Korea,KP,PRK,Chagang-do
Sunchon,Sunchon,39.42360008,125.9389689,400629,North Korea,KP,PRK,P'yongan-namdo
Kimhyonggwon,Kimhyonggwon,40.81752016,128.1553194,3839,North Korea,KP,PRK,Ryanggang
Pyongsan,Pyongsan,38.33668968,126.3866418,66260,North Korea,KP,PRK,Hwanghae-bukto
Ongjin,Ongjin,37.93710166,125.3570922,66721,North Korea,KP,PRK,Hwanghae-namdo
Haeju,Haeju,38.039421,125.7143831,223313.5,North Korea,KP,PRK,Hwanghae-namdo
Kilchu,Kilchu,40.96043133,129.3204162,82408.5,North Korea,KP,PRK,Hamgyong-bukto
Musan,Musan,42.23043133,129.2303959,50942.5,North Korea,KP,PRK,Hamgyong-bukto
Sonbong,Sonbong,42.33768577,130.4027274,44097.5,North Korea,KP,PRK,Hamgyong-bukto
Kanggye,Kanggye,40.97322125,126.6032177,254522,North Korea,KP,PRK,Chagang-do
Hungnam,Hungnam,39.82313641,127.6231555,548702,North Korea,KP,PRK,Hamgyong-namdo
Taedong,Taedong,40.61709312,125.4501098,1884,North Korea,KP,PRK,P'yongan-bukto
Chongju,Chongju,39.68128461,125.2163256,85417,North Korea,KP,PRK,P'yongan-bukto
Hyeson,Hyeson,41.39273053,128.1927331,227461,North Korea,KP,PRK,Ryanggang
Nampo,Nampo,38.76692078,125.4524338,791000,North Korea,KP,PRK,Namp'o-si
Chongjin,Chongjin,41.78461875,129.79,499807,North Korea,KP,PRK,Hamgyong-bukto
Kimchaek,Kimchaek,40.67230939,129.202749,187270,North Korea,KP,PRK,Hamgyong-bukto
Hamhung,Hamhung,39.91005617,127.5454341,595670.5,North Korea,KP,PRK,Hamgyong-namdo
Wonsan,Wonsan,39.16048952,127.4308158,322425,North Korea,KP,PRK,Kangwon-do
Sinuiju,Sinuiju,40.08585939,124.4212837,167234,North Korea,KP,PRK,P'yongan-bukto
Pyongyang,Pyongyang,39.0194387,125.7546907,2899398.5,North Korea,KP,PRK,P'yongyang
Kyrenia,Kyrenia,35.3259991,33.33300361,26701,Northern Cyprus,,CYN,
Ammochostos,Ammochostos,35.12502525,33.95001013,33016.5,Northern Cyprus,-99,CYN,
Capitol Hill,Capitol Hill,15.21125368,145.7505761,1764,Northern Mariana Islands,MP,MNP,
Arendal,Arendal,58.46475606,8.766000553,30916,Norway,NO,NOR,Aust-Agder
Vossavangen,Vossavangen,60.63000316,6.441003463,5571,Norway,NO,NOR,Hordaland
Leikanger,Hermansverk,61.18329612,6.849999471,1965,Norway,NO,NOR,Sogn og Fjordane
B?rum,Baerum,59.91348606,11.34723651,113659,Norway,NO,NOR,Akershus
Hamar,Hamar,60.82000207,11.06900156,29479,Norway,NO,NOR,Hedmark
T?nsberg,Tonsberg,59.26400109,10.42100147,38914,Norway,NO,NOR,Vestfold
Finnsnes,Finnsnes,69.24061729,18.00860592,3611,Norway,NO,NOR,Troms
Gj?vik,Gjovik,60.80002138,10.7000081,20157.5,Norway,NO,NOR,Oppland
R?rvik,Rorvik,64.86801597,11.20530025,2615,Norway,NO,NOR,Nord-Tr?ndelag
Harstad,Harstad,68.7879059,16.51557043,19203,Norway,NO,NOR,Troms
?lesund,Alesund,62.54541872,6.388023233,45377,Norway,NO,NOR,M?re og Romsdal
Sandnes,Sandnes,58.84541201,5.690029662,46911,Norway,NO,NOR,Rogaland
Drammen,Drammen,59.75724265,10.19073686,85437.5,Norway,NO,NOR,Buskerud
Moss,Moss,59.43697797,10.66915727,35696.5,Norway,NO,NOR,?stfold
Steinkjer,Steinkjer,64.01706016,11.50001094,11193.5,Norway,NO,NOR,Nord-Tr?ndelag
Svolv?r,Svolvaer,68.23328859,14.56669714,4197,Norway,NO,NOR,Nordland
Mo i Rana,Mo i Rana,66.31660972,14.16666988,19131,Norway,NO,NOR,Nordland
Narvik,Narvik,68.38315025,17.28999345,19236.5,Norway,NO,NOR,Nordland
Bod?,Bodo,67.24677227,14.39901132,31383.5,Norway,NO,NOR,Nordland
Haugesund,Haugesund,59.4119149,5.277496703,36219.5,Norway,NO,NOR,Rogaland
Stavanger,Stavanger,58.97000389,5.680004434,136999,Norway,NO,NOR,Rogaland
Skien,Skien,59.19998985,9.600023558,73330,Norway,NO,NOR,Telemark
Namsos,Namsos,64.48331077,11.50001094,9035,Norway,NO,NOR,Nord-Tr?ndelag
Alta,Alta,69.96664532,23.24167151,12077,Norway,NO,NOR,Finnmark
Vads?,Vadso,70.09659678,29.76574927,5139,Norway,NO,NOR,Finnmark
Molde,Molde,62.74830039,7.183323526,16171.5,Norway,NO,NOR,M?re og Romsdal
Lillehammer,Lillehammer,61.13328269,10.5000203,19319,Norway,NO,NOR,Oppland
Kirkenes,Kirkenes,69.72500633,30.05164343,2728,Norway,NO,NOR,Finnmark
Kristiansand,Kristiansand,58.16664207,8.000017862,58292,Norway,NO,NOR,Vest-Agder
Hammerfest,Hammerfest,70.66127993,23.68800085,9967,Norway,NO,NOR,Finnmark
Troms?,Tromso,69.63507623,18.99202525,48900.5,Norway,NO,NOR,Troms
Trondheim,Trondheim,63.41665753,10.41666622,144336,Norway,NO,NOR,S?r-Tr?ndelag
Bergen,Bergen,60.39100242,5.324522256,200389.5,Norway,NO,NOR,Hordaland
Oslo,Oslo,59.91669029,10.74997921,707500,Norway,NO,NOR,Oslo
Alayat Samail,Alayat Samail,23.3031887,57.97820756,32862.5,Oman,OM,OMN,Ad Dakhliyah
Dawwah,Dawwah,20.63301577,58.90802161,1485.5,Oman,OM,OMN,Ash Sharqiyah
Mirbat,Mirbat,16.99243695,54.69179317,1120,Oman,OM,OMN,Dhofar
Ibri,Ibri,23.22538983,56.51695308,101640,Oman,OM,OMN,Al Dhahira
Salalah,Salalah,17.02545819,54.08521521,183508.5,Oman,OM,OMN,Dhofar
Suhar,Suhar,24.36197335,56.73441896,129811.5,Oman,OM,OMN,Al Batnah
As Sib,As Sib,23.68024579,58.18253617,237816,Oman,OM,OMN,Muscat
Nizwa,Nizwa,22.92638999,57.53141313,70429.5,Oman,OM,OMN,Ad Dakhliyah
Sur,Sur,22.57581708,59.53480505,68738,Oman,OM,OMN,Ash Sharqiyah
Muscat,Muscat,23.61332481,58.59331213,660779,Oman,OM,OMN,Muscat
Parachinar,Parachinar,33.89918276,70.10082678,55685,Pakistan,PK,PAK,F.A.T.A.
Sialkote,Sialkote,32.5200163,74.5600378,477396,Pakistan,PK,PAK,Punjab
Sheikhu Pura,Sheikhu Pura,31.71998761,73.98999508,361303,Pakistan,PK,PAK,Punjab
Gujrat,Gujrat,32.5799868,74.08001542,301506,Pakistan,PK,PAK,Punjab
Sahiwal,Sahiwal,30.67173118,73.11180579,235695,Pakistan,PK,PAK,Punjab
Chiniot,Chiniot,31.71998761,72.97997921,201781,Pakistan,PK,PAK,Punjab
Rahim Yar Khan,Rahimyar Khan,28.4202407,70.29518184,353203,Pakistan,PK,PAK,Punjab
Mansehra,Mansehra,34.3417914,73.19681352,66486,Pakistan,PK,PAK,Khyber-Pakhtunkhwa
Kohat,Kohat,33.60268923,71.43268347,247227,Pakistan,PK,PAK,N.W.F.P.
Abbottabad,Abbottabad,34.1495034,73.19950069,1032323.5,Pakistan,PK,PAK,N.W.F.P.
Mardan,Mardan,34.20004295,72.0399849,300424,Pakistan,PK,PAK,N.W.F.P.
Gwadar,Gwadar,25.13896812,62.32858801,37632.5,Pakistan,PK,PAK,Baluchistan
Zhob,Zhob,31.34897666,69.4385933,69446.5,Pakistan,PK,PAK,Baluchistan
Gilgit,Gilgit,35.91709576,74.30000199,124196.5,Pakistan,PK,PAK,Northern Areas
Kasur,Kasur,31.12537274,74.45503129,290643,Pakistan,PK,PAK,Punjab
Kundian,Kundian,32.45219098,71.47180253,35406,Pakistan,PK,PAK,Punjab
Okara,Okara,30.81040489,73.45002803,223648,Pakistan,PK,PAK,Punjab
Jhang,Jhang,31.2803762,72.32498043,341210,Pakistan,PK,PAK,Punjab
Sargodha,Sargodha,32.08536582,72.6749849,542603,Pakistan,PK,PAK,Punjab
Dera Ghazi Khan,Dera Ghazi Khan,30.06039899,70.63505774,236093,Pakistan,PK,PAK,Punjab
Sadiqabad,Sadiqabad,28.3006356,70.13023067,189876,Pakistan,PK,PAK,Punjab
Nawabshah,Nawabshah,26.24543805,68.40000037,229504,Pakistan,PK,PAK,Sind
Bannu,Bannu,32.98897992,70.59857418,586209.5,Pakistan,PK,PAK,N.W.F.P.
Dera Ismail Khan,Dera Ismail Khan,31.82899904,70.89855587,66676.5,Pakistan,PK,PAK,Khyber-Pakhtunkhwa
Chaman,Chaman,30.92504905,66.44632117,88568,Pakistan,PK,PAK,Baluchistan
Turbat,Turbat,25.99178428,63.07179846,111742.5,Pakistan,PK,PAK,Baluchistan
Faisalabad,Faisalabad,31.40998069,73.10999711,2561797.5,Pakistan,PK,PAK,Punjab
Rawalpindi,Rawalpindi,33.59997622,73.04002722,1800550.5,Pakistan,PK,PAK,Punjab
Bahawalpur,Bahawalpur,29.38997479,71.67499426,552607,Pakistan,PK,PAK,Punjab
Mirput Khas,Mirput Khas,25.53178652,69.01179765,286046,Pakistan,PK,PAK,Sind
Sukkur,Sukkur,27.71356549,68.8485518,417767,Pakistan,PK,PAK,Sind
Saidu,Saidu,34.75003522,72.34999182,1860310,Pakistan,PK,PAK,N.W.F.P.
Gujranwala,Gujranwala,32.16042584,74.18502193,1448735.5,Pakistan,PK,PAK,Punjab
Quetta,Quetta,30.22000165,67.02499385,750837.5,Pakistan,PK,PAK,Baluchistan
Larkana,Larkana,27.56176597,68.20678218,364033,Pakistan,PK,PAK,Sind
Islamabad,Islamabad,33.69999595,73.16663448,690800,Pakistan,PK,PAK,F.C.T.
Multan,Multan,30.19997703,71.45500769,1479615,Pakistan,PK,PAK,Punjab
Hyderabad,Hyderabad,25.379987,68.37498897,1422665,Pakistan,PK,PAK,Sind
Peshawar,Peshawar,34.00501609,71.53500281,1260886.5,Pakistan,PK,PAK,N.W.F.P.
Lahore,Lahore,31.55997154,74.35002478,6443944,Pakistan,PK,PAK,Punjab
Karachi,Karachi,24.86999229,66.99000891,11877109.5,Pakistan,PK,PAK,Sind
Koror,Koror,7.345226355,134.4695009,11200,Palau,PW,PLW,
Melekeok,Melekeok,7.487396173,134.6265485,7026,Palau,PW,PLW,
Ramallah,Ramallah,31.90294475,35.20620938,24599,Palestine,PS,PSE,
Al Khalil,Al Khalil,31.54059287,35.09557328,220395.5,Palestine,PS,PSE,
Nablus,Nablus,32.22148155,35.25442663,173153.5,Palestine,PS,PSE,
Gaza,Gaza,31.52999921,34.44501868,477460.5,Palestine,PS,PSE,
El Porvenir,El Porvenir,9.541686355,-78.97196299,10,Panama,PA,PAN,Kuna Yala
Penonome,Penonome,8.509983133,-80.35998926,20580,Panama,PA,PAN,Cocl?
Chitre,Chitre,7.970016092,-80.42003727,44024,Panama,PA,PAN,Herrera
Jaque,Jaque,7.518958353,-78.16601465,955,Panama,PA,PAN,Dari?n
Bocas del Toro,Bocas del Toro,9.335350084,-82.2474707,6484,Panama,PA,PAN,Bocas del Toro
Almirante,Almirante,9.30001243,-82.3999681,7442.5,Panama,PA,PAN,Bocas del Toro
Las Tablas,Las Tablas,7.760390644,-80.28001998,9964,Panama,PA,PAN,Los Santos
Santiago,Santiago,8.100369892,-80.98333622,45655,Panama,PA,PAN,Veraguas
La Palma,La Palma,8.398181172,-78.14022811,1845,Panama,PA,PAN,Dari?n
Colon,Colon,9.365021382,-79.8749801,170488,Panama,PA,PAN,Col?n
Balboa,Balboa,8.949982116,-79.56665267,62882,Panama,PA,PAN,Panama
Puerto Armuelles,Puerto Armuelles,8.280023009,-82.87001693,22971,Panama,PA,PAN,Chiriqu?
David,David,8.433321146,-82.43332524,96448,Panama,PA,PAN,Chiriqu?
Panama City,Panama City,8.96801719,-79.53303715,844584,Panama,PA,PAN,Panama
Wabag,Wabag,-5.490000005,143.7180037,3958,Papua New Guinea,PG,PNG,Enga
Vanimo,Vanimo,-2.690000936,141.3039966,11204,Papua New Guinea,PG,PNG,Sandaun
Kundiawa,Kundiawa,-6.022997883,144.9600127,9383,Papua New Guinea,PG,PNG,Chimbu
Kerema,Kerema,-7.927001897,145.8379987,5646,Papua New Guinea,PG,PNG,Gulf
Arawa,Arawa,-6.228000033,155.5659907,40266,Papua New Guinea,PG,PNG,North Solomons
Lorengau,Lorengau,-2.032001997,147.2799966,5806,Papua New Guinea,PG,PNG,Manus
Kimbe,Kimbe,-5.55000289,150.1430137,18847,Papua New Guinea,PG,PNG,West New Britain
Daru,Daru,-9.109151958,143.2337226,15214,Papua New Guinea,PG,PNG,
Sohano,Sohano,-5.429742201,154.6711375,2338,Papua New Guinea,PG,PNG,North Solomons
Kieta,Kieta,-6.216275616,155.6333321,5284.5,Papua New Guinea,PG,PNG,North Solomons
Mendi,Mendi,-6.144393698,143.6452266,21685.5,Papua New Guinea,PG,PNG,Southern Highlands
Abau,Abau,-10.04260537,148.5650297,230,Papua New Guinea,PG,PNG,Central
Alotau,Alotau,-10.30207273,150.4590743,11624,Papua New Guinea,PG,PNG,Milne Bay
Popondetta,Popondetta,-8.769194724,148.2484082,25192,Papua New Guinea,PG,PNG,Northern
Hoskins,Hoskins,-5.474615459,150.4099816,871,Papua New Guinea,PG,PNG,West New Britain
Wewak,Wewak,-3.553492412,143.6367,21686.5,Papua New Guinea,PG,PNG,East Sepik
Madang,Madang,-5.224811586,145.785251,44721,Papua New Guinea,PG,PNG,Madang
Kavieng,Kavieng,-2.581284323,150.8129765,17109,Papua New Guinea,PG,PNG,New Ireland
Goroka,Goroka,-6.083312155,145.3854821,29101,Papua New Guinea,PG,PNG,Eastern Highlands
Mt. Hagen,Mt. Hagen,-5.86322223,144.2168196,46343.5,Papua New Guinea,PG,PNG,Western Highlands
Rabaul,Rabaul,-4.205490385,152.1434307,5894,Papua New Guinea,PG,PNG,East New Britain
Lae,Lae,-6.732988262,146.9900354,103653.5,Papua New Guinea,PG,PNG,Morobe
Port Moresby,Port Moresby,-9.464707826,147.1925036,267434.5,Papua New Guinea,PG,PNG,Central
Mariscal Estigarribia,Mariscal Jose F. Estigarribia,-22.03000205,-60.60999555,2250,Paraguay,PY,PRY,Boquer?n
Caacupe,Caacupe,-25.38700191,-57.14000047,21696,Paraguay,PY,PRY,Cordillera
General Eugenio Alejandrino Garay,General Eugenio Alejandrino Garay,-20.51995034,-62.209986,972,Paraguay,PY,PRY,Boquer?n
Arroyos y Esteros,Arroyos y Esteros,-25.04995807,-57.08998845,2755,Paraguay,PY,PRY,Cordillera
Villa Hayes,Villa Hayes,-25.09000731,-57.52998743,15643,Paraguay,PY,PRY,Presidente Hayes
Fortin Falcon,Fortin Falcon,-23.05028685,-59.84994918,-99,Paraguay,PY,PRY,Presidente Hayes
Puerto Pinasco,Puerto Pinasco,-22.64002765,-57.7899974,473.5,Paraguay,PY,PRY,Presidente Hayes
Pozo Colorado,Pozo Colorado,-23.43000527,-58.85998377,2135,Paraguay,PY,PRY,Presidente Hayes
San Pedro,San Pedro,-24.08996499,-57.07998906,7351,Paraguay,PY,PRY,San Pedro
San Lorenzo,San Lorenzo,-25.34001788,-57.52003972,385532,Paraguay,PY,PRY,Asunci?n
Ypacarai,Ypacarai,-25.40998777,-57.27997685,23805.5,Paraguay,PY,PRY,Asunci?n
San Juan Bautista,San Juan Bautista,-26.67998777,-57.15001062,7882,Paraguay,PY,PRY,Misiones
Paraguari,Paraguari,-25.62000079,-57.16001001,14480,Paraguay,PY,PRY,Paraguar?
Nacunday,Nacunday,-26.02002806,-54.76994918,1185,Paraguay,PY,PRY,Alto Paran?
Coronel Oviedo,Coronel Oviedo,-25.44998533,-56.4399506,69693.5,Paraguay,PY,PRY,Caaguaz?
Caazapa,Caazapa,-26.20001707,-56.38000594,5504,Paraguay,PY,PRY,Caazap?
Ype Jhu,Ype Jhu,-23.91002765,-55.45998458,598,Paraguay,PY,PRY,Canindey?
Encarnacion,Encarnacion,-27.34718482,-55.87391878,251813.5,Paraguay,PY,PRY,Itap?a
Coronel Bogado,Coronel Bogado,-27.17003538,-56.25003972,14297,Paraguay,PY,PRY,Itap?a
Fuerte Olimpo,Fuerte Olimpo,-21.06958087,-57.89999068,2475,Paraguay,PY,PRY,Alto Paraguay
Capitan Pablo Lagerenza,Capitan Pablo Lagerenza,-19.91611123,-60.78327722,1200,Paraguay,PY,PRY,Alto Paraguay
La Victoria,La Victoria,-22.28960976,-57.93998824,5000,Paraguay,PY,PRY,Alto Paraguay
Horqueta,Horqueta,-23.33962319,-57.05001673,13351,Paraguay,PY,PRY,Concepci?n
Belen,Belen,-23.46948606,-57.23997929,6490,Paraguay,PY,PRY,Concepci?n
Rosario,Rosario,-24.41960895,-57.10001367,3639,Paraguay,PY,PRY,San Pedro
Ita,Ita,-25.50961994,-57.36002364,29774.5,Paraguay,PY,PRY,Asunci?n
Pilar,Pilar,-26.86948525,-58.29999211,28435,Paraguay,PY,PRY,?eembuc?
Pedro Juan Caballero,Pedro Juan Caballero,-22.54458128,-55.75999211,66029,Paraguay,PY,PRY,Amambay
Bella Vista,Bella Vista,-22.12961953,-56.5199974,11252.5,Paraguay,PY,PRY,Amambay
Abai,Abai,-26.0295882,-55.94000696,2788.5,Paraguay,PY,PRY,Caazap?
Ygatimi,Ygatimi,-24.0796297,-55.49998214,2809,Paraguay,PY,PRY,Canindey?
Hohenau,Hohenau,-27.07954995,-55.74996688,5306,Paraguay,PY,PRY,Itap?a
Concepcion,Concepcion,-23.40638914,-57.43441187,53620.5,Paraguay,PY,PRY,Concepci?n
Villarrica,Villarrica,-25.7500187,-56.43331018,41157,Paraguay,PY,PRY,Guair?
Filadelfia,Filadelfia,-22.33999428,-60.02998987,9259,Paraguay,PY,PRY,Boquer?n
Ciudad del Este,Ciudad del Este,-25.51669961,-54.61605676,320872,Paraguay,PY,PRY,Alto Paran?
Asuncion,Asuncion,-25.29640298,-57.64150517,940846.5,Paraguay,PY,PRY,Asunci?n
Ferrenafe,Ferrenafe,-6.629997133,-79.80002344,42270.5,Peru,PE,PER,Lambayeque
Motupe,Motupe,-6.150026429,-79.71000309,9048,Peru,PE,PER,Lambayeque
Mollendo,Mollendo,-17.02000893,-72.01998153,38993,Peru,PE,PER,Arequipa
Urubamba,Urubamba,-13.30421507,-72.11661646,5985,Peru,PE,PER,Cusco
Santo Tomas,Santo Tomas,-14.46001015,-72.0800037,3695.5,Peru,PE,PER,Cusco
Putina,Putina,-15.47002602,-69.42998458,8118,Peru,PE,PER,Callao
Casma,Casma,-9.440006491,-78.20999129,27421,Peru,PE,PER,Ancash
Tournavista,Tournavista,-8.932182191,-74.70521814,511,Peru,PE,PER,Hu?nuco
Huamachuco,Huamachuco,-7.810028464,-78.04994938,26301.5,Peru,PE,PER,La Libertad
Otuzco,Otuzco,-7.899997133,-78.56999516,8754.5,Peru,PE,PER,La Libertad
Lamas,Lamas,-6.43000934,-76.52001693,13098,Peru,PE,PER,San Mart?n
Nauta,Nauta,-4.570019512,-73.78002914,2308.5,Peru,PE,PER,Loreto
Puquio,Puquio,-14.6999955,-74.12998194,9027.5,Peru,PE,PER,Ayacucho
Chosica,Chosica,-11.93003538,-76.71000533,44572.5,Peru,PE,PER,Lima
Satipo,Satipo,-11.25999876,-74.69002527,15532,Peru,PE,PER,Jun?n
Tarma,Tarma,-11.41001544,-75.72998763,25906,Peru,PE,PER,Jun?n
La Oroya,La Oroya,-11.52003457,-75.94000065,33345,Peru,PE,PER,Jun?n
Huaura,Huaura,-11.06001097,-77.59997685,30561.5,Peru,PE,PER,Lima
Huacho,Huacho,-11.11003375,-77.61994979,67509.5,Peru,PE,PER,Lima
Pimentel,Pimentel,-6.82962319,-79.92998967,14422.5,Peru,PE,PER,Lambayeque
Olmos,Olmos,-5.979597556,-79.74997481,7579.5,Peru,PE,PER,Lambayeque
Sechura,Sechura,-5.55962319,-80.81998702,15811,Peru,PE,PER,Piura
Chulucanas,Chulucanas,-5.089574362,-80.17000086,60435,Peru,PE,PER,Piura
Sullana,Sullana,-4.889586569,-80.67999557,114496.5,Peru,PE,PER,Piura
Abancay,Abancay,-13.63959511,-72.89000594,53981,Peru,PE,PER,Apur?mac
Camana,Camana,-16.61961994,-72.71999048,18695,Peru,PE,PER,Arequipa
Sicuani,Sicuani,-14.28958128,-71.22997807,20924.5,Peru,PE,PER,Cusco
Puno,Puno,-15.83294961,-70.03330693,111350,Peru,PE,PER,Callao
Ayaviri,Ayaviri,-14.87957111,-70.59999068,12524.5,Peru,PE,PER,Callao
Ilave,Ilave,-16.07960122,-69.66999577,16033,Peru,PE,PER,Callao
Desaguadero,Desaguadero,-16.56458453,-69.04499516,5120,Peru,PE,PER,Callao
Huarmey,Huarmey,-10.06958047,-78.15999435,9184,Peru,PE,PER,Ancash
Cajabamba,Cajabamba,-7.619600811,-78.04000167,12036.5,Peru,PE,PER,Cajamarca
Jaen,Jaen,-5.709588197,-78.80998051,49171,Peru,PE,PER,Cajamarca
Chota,Chota,-6.549588604,-78.65004195,13452,Peru,PE,PER,Cajamarca
Tingo Maria,Tingo Maria,-9.289628073,-75.9899976,36138.5,Peru,PE,PER,Hu?nuco
Moyobamba,Moyobamba,-6.049619121,-76.96665633,46005,Peru,PE,PER,San Mart?n
Juanjui,Juanjui,-7.169602438,-76.73997766,27352.5,Peru,PE,PER,San Mart?n
Tocache,Tocache,-8.179618308,-76.52001693,15822.5,Peru,PE,PER,San Mart?n
Sechura,Sechura,-5.235250225,-78.50064539,8602,Peru,PE,PER,Amazonas
Chachapoyas,Chachapoyas,-6.229608135,-77.87001205,23128.5,Peru,PE,PER,Amazonas
Caballococha,Caballococha,-3.916260967,-70.50834253,3195,Peru,PE,PER,Loreto
Puca Urco,Puca Urco,-2.332791729,-71.91668034,10,Peru,PE,PER,Loreto
Andoas,Andoas,-2.902059307,-76.40247888,10,Peru,PE,PER,Loreto
Soldado Bartra,Soldado Bartra,-2.516139711,-75.76660038,10,Peru,PE,PER,Loreto
Nuevo Rocafuerte,Nuevo Rocafuerte,-0.932928854,-75.39998194,40,Peru,PE,PER,Loreto
Requena,Requena,-5.069627259,-73.90999536,17097.5,Peru,PE,PER,Loreto
Huanta,Huanta,-12.94961139,-74.25000045,15534.5,Peru,PE,PER,Ayacucho
Coracora,Coracora,-15.01961424,-73.78997685,6433.5,Peru,PE,PER,Ayacucho
Chincha Alta,Chincha Alta,-13.41960854,-76.13998845,138608,Peru,PE,PER,Ica
Santiago,Santiago,-14.18958738,-75.73996118,10449,Peru,PE,PER,Ica
San Ramon,San Ramon,-11.12961912,-75.34001144,10599,Peru,PE,PER,Jun?n
Junin,Junin,-11.1496179,-76.01002222,11495,Peru,PE,PER,Jun?n
Jauja,Jauja,-11.79960407,-75.50002751,21057,Peru,PE,PER,Jun?n
Pativilca,Pativilca,-10.69961953,-77.79999048,22744,Peru,PE,PER,Lima
Chancay,Chancay,-11.55961871,-77.26997115,18601,Peru,PE,PER,Lima
Chilca,Chilca,-12.5196118,-76.73997766,6556,Peru,PE,PER,Lima
Chiclayo,Chiclayo,-6.762908916,-79.83658452,587083.5,Peru,PE,PER,Lambayeque
Juliaca,Juliaca,-15.49999835,-70.13996708,234428,Peru,PE,PER,Callao
Cerro de Pasco,Cerro de Pasco,-10.69000771,-76.26998051,108071,Peru,PE,PER,Pasco
Tarapoto,Tarapoto,-6.50995278,-76.47996769,936,Peru,PE,PER,San Mart?n
Ayacucho,Ayacucho,-13.17502399,-74.2199506,153173.5,Peru,PE,PER,Ayacucho
Callao,Callao,-12.07002684,-77.13496647,786231.5,Peru,PE,PER,Lima
Paita,Paita,-5.089987774,-81.12002039,47891.5,Peru,PE,PER,Piura
Talara,Talara,-4.579993063,-81.27998478,74760.5,Peru,PE,PER,Piura
Tumbes,Tumbes,-3.570028871,-80.45998316,105783,Peru,PE,PER,Tumbes
Puerto Maldonado,Puerto Maldonado,-12.60002033,-69.18333297,52349,Peru,PE,PER,Madre de Dios
Ilo,Ilo,-17.64002277,-71.34002303,53192,Peru,PE,PER,Moquegua
Moquegua,Moquegua,-17.18997272,-70.93999577,38610,Peru,PE,PER,Moquegua
Huaraz,Huaraz,-9.530026836,-77.53000696,74986.5,Peru,PE,PER,Ancash
Cajamarca,Cajamarca,-7.150017071,-78.53002344,138832.5,Peru,PE,PER,Cajamarca
Huanuco,Huanuco,-9.920028871,-76.24000818,153052,Peru,PE,PER,Hu?nuco
Pacasmayo,Pacasmayo,-7.400647767,-79.57060592,34223.5,Peru,PE,PER,La Libertad
Salaverry,Salaverry,-8.220029278,-78.98999536,7228,Peru,PE,PER,La Libertad
Gueppi,Gueppi,-0.116596254,-75.22996647,10,Peru,PE,PER,Loreto
Contamana,Contamana,-7.340031312,-75.01997929,16403,Peru,PE,PER,Loreto
Huancavelica,Huancavelica,-12.79003457,-74.99000696,42982,Peru,PE,PER,Huancavelica
Pisco,Pisco,-13.71003009,-76.21998356,71538,Peru,PE,PER,Ica
Nasca,Nasca,-14.83001341,-74.94001001,23387,Peru,PE,PER,Ica
Piura,Piura,-5.210032126,-80.62997278,361199,Peru,PE,PER,Piura
Arequipa,Arequipa,-16.41999388,-71.53001144,775785,Peru,PE,PER,Arequipa
Chimbote,Chimbote,-9.070003236,-78.56999516,333406,Peru,PE,PER,Ancash
Pucallpa,Pucallpa,-8.368909079,-74.53499597,304917,Peru,PE,PER,Ucayali
Iquitos,Iquitos,-3.750017884,-73.25000981,448174.5,Peru,PE,PER,Loreto
Huancayo,Huancayo,-12.08000039,-75.20001998,394695,Peru,PE,PER,Jun?n
Cusco,Cusco,-13.52502846,-71.97215499,336661,Peru,PE,PER,Cusco
Tacna,Tacna,-18.00000079,-70.25001205,261042.5,Peru,PE,PER,Tacna
Trujillo,Trujillo,-8.120035381,-79.01996769,521046,Peru,PE,PER,La Libertad
Ica,Ica,-14.06799274,-75.72549178,263132,Peru,PE,PER,Ica
Lima,Lima,-12.04801268,-77.05006209,7385117,Peru,PE,PER,Lima
San Carlos,San Carlos,10.55037539,123.3800036,6353,Philippines,PH,PHL,Negros Occidental
Cadiz,Cadiz,10.95874839,123.3085868,206105,Philippines,PH,PHL,Negros Occidental
Pagadian,Pagadian,7.852968973,123.5070243,159590,Philippines,PH,PHL,Zamboanga Del Sur
Ozamis,Ozamis,8.146206888,123.8444197,95444,Philippines,PH,PHL,Misamis Occidental
Tarlac,Tarlac,15.48379519,120.5833785,183930,Philippines,PH,PHL,Tarlac
Cabanatuan,Cabanatuan,15.50208864,120.9617016,220250,Philippines,PH,PHL,Nueva Ecija
Olongapo,Olongapo,14.82957155,120.2827767,265829,Philippines,PH,PHL,Zambales
Dagupan,Dagupan,16.04789512,120.3408093,163676,Philippines,PH,PHL,Pangasinan
San Pablo,San Pablo,14.06956626,121.3226098,224203.5,Philippines,PH,PHL,Laguna
Quezon City,Quezon City,14.6504352,121.0299662,2761720,Philippines,PH,PHL,Metropolitan Manila
Pasay City,Pasay City,14.5504413,120.9999939,403064,Philippines,PH,PHL,Metropolitan Manila
Iligan,Iligan,8.171244119,124.2153531,464599,Philippines,PH,PHL,Lanao del Norte
Ormac,Ormac,11.0642975,124.6075256,129964.5,Philippines,PH,PHL,Leyte
Tacloban,Tacloban,11.25043601,125.0000081,234548,Philippines,PH,PHL,Leyte
Butuan,Butuan,8.949542866,125.5435925,190557,Philippines,PH,PHL,Agusan del Norte
Tagum,Tagum,7.382144998,125.8016646,6726,Philippines,PH,PHL,Davao del Norte
Surigao,Surigao,9.784298115,125.4888155,64983,Philippines,PH,PHL,Dinagat Islands
Gingoog,Gingoog,8.830377013,125.1299743,218,Philippines,PH,PHL,Misamis Oriental
Legazpi,Legazpi,13.16998293,123.7500069,320081,Philippines,PH,PHL,Albay
Tuguegarao,Tuguegarao,17.61309674,121.7268746,115105,Philippines,PH,PHL,Cagayan
Vigan,Vigan,17.57472699,120.3869047,48545,Philippines,PH,PHL,Ilocos Sur
Bacolod,Bacolod,10.63168825,122.9816817,730587,Philippines,PH,PHL,Negros Occidental
Roxas,Roxas,11.58527346,122.7511014,91880.5,Philippines,PH,PHL,Capiz
Puerto Princesa,Puerto Princesa,9.754267783,118.744384,147882,Philippines,PH,PHL,Palawan
Naga,Naga,13.61915448,123.1813594,458283,Philippines,PH,PHL,Camarines Sur
Angeles,Angeles,15.14505617,120.5450862,314493,Philippines,PH,PHL,Pampanga
Batangas,Batangas,13.78167686,121.021698,330939,Philippines,PH,PHL,Batangas
Cotabato,Cotabato,7.216909606,124.2484261,229476,Philippines,PH,PHL,Shariff Kabunsuan
Calbayog,Calbayog,12.06718203,124.6041666,55015,Philippines,PH,PHL,Samar
Cagayan de Oro,Cagayan de Oro,8.450839456,124.6852986,861824.5,Philippines,PH,PHL,Misamis Oriental
Zamboanga,Zamboanga,6.919976826,122.0800313,615311.5,Philippines,PH,PHL,Zamboanga del Sur
Laoag,Laoag,18.1988491,120.5936104,154576.5,Philippines,PH,PHL,Ilocos Norte
Baguio City,Baguio City,16.42999066,120.5699426,360269,Philippines,PH,PHL,Benguet
General Santos,General Santos,6.110827249,125.1747261,744308,Philippines,PH,PHL,South Cotabato
Cebu,Cebu,10.31997601,123.9000752,806817,Philippines,PH,PHL,Cebu
Iloilo,Iloilo,10.70504295,122.5450158,387681,Philippines,PH,PHL,Iloilo
Davao,Davao,7.110016906,125.6299955,1307252,Philippines,PH,PHL,Davao Del Sur
Manila,Manila,14.60415895,120.9822172,7088787.5,Philippines,PH,PHL,Metropolitan Manila
Olsztyn,Olsztyn,53.80003522,20.48003129,179236.5,Poland,PL,POL,Warmian-Masurian
Elblag,Elblag,54.18995974,19.40268103,124332,Poland,PL,POL,Warmian-Masurian
Inowroclaw,Inowroclaw,52.77994244,18.24998653,78302,Poland,PL,POL,Kuyavian-Pomeranian
Bytom,Bytom,50.35003908,18.90999792,425716.5,Poland,PL,POL,Silesian
Opole,Opole,50.68497988,17.93134965,129544,Poland,PL,POL,Opole
Koszalin,Koszalin,54.2,16.1833333,107450,Poland,PL,POL,West Pomeranian
Elk,Elk,53.83370241,22.34999467,51312.5,Poland,PL,POL,Warmian-Masurian
Gdynia,Gdynia,54.52037884,18.53002112,284197,Poland,PL,POL,Pomeranian
Wroclaw,Wroclaw,51.11043194,17.03000932,622471,Poland,PL,POL,Lower Silesian
Szczecin,Szczecin,53.42039431,14.53000688,390241.5,Poland,PL,POL,West Pomeranian
Zielona Gora,Zielona Gora,51.95040651,15.50002519,113865.5,Poland,PL,POL,Lubusz
Poznan,Poznan,52.4057534,16.89993974,597174.5,Poland,PL,POL,Greater Poland
Grudziadz,Grudziadz,53.48039064,18.75000769,100964.5,Poland,PL,POL,Kuyavian-Pomeranian
Bydgoszcz,Bydgoszcz,53.12041262,18.01000118,366222,Poland,PL,POL,Kuyavian-Pomeranian
Katowice,Katowice,50.26038047,19.02001705,1527362,Poland,PL,POL,Silesian
Gliwice,Gliwice,50.3303762,18.67001257,353252.5,Poland,PL,POL,Silesian
Kielce,Kielce,50.8903937,20.6600203,212165.5,Poland,PL,POL,Swietokrzyskie
Bialystok,Bialystok,53.15035911,23.1699963,288722.5,Poland,PL,POL,Podlachian
Lublin,Lublin,51.25039756,22.57272009,358001,Poland,PL,POL,Lublin
Rzeszow,Rzeszow,50.07046958,22.00004187,202034,Poland,PL,POL,Subcarpathian
L?dz,Lodz,51.77499086,19.45136023,758000,Poland,PL,POL,L?dz
Gdansk,Gdansk,54.3599752,18.64004024,597915,Poland,PL,POL,Pomeranian
Krak?w,Krakow,50.05997927,19.96001135,755525,Poland,PL,POL,Lesser Poland
Warsaw,Warsaw,52.25000063,20.99999955,1704569.5,Poland,PL,POL,Masovian
Aveiro,Aveiro,40.64100311,-8.650997534,54162,Portugal,PT,PRT,Aveiro
Leiria,Leiria,39.73899603,-8.804996462,45112,Portugal,PT,PRT,Leiria
Viana Do Castelo,Viana Do Castelo,41.69623514,-8.844137484,15555,Portugal,PT,PRT,Viana do Castelo
Beja,Beja,38.01400214,-7.86300241,28756,Portugal,PT,PRT,Beja
Evora,Evora,38.55999611,-7.905995561,55620,Portugal,PT,PRT,?vora
Portalegre,Portalegre,39.29000411,-7.423001549,15581,Portugal,PT,PRT,Portalegre
Santarem,Santarem,39.23100008,-8.682002552,29385,Portugal,PT,PRT,Santar?m
Braganca,Braganca,41.80799701,-6.755003426,34375,Portugal,PT,PRT,Bragan?a
Castelo Branco,Castelo Branco,39.81099615,-7.487999559,33479,Portugal,PT,PRT,Castelo Branco
Guarda,Guarda,40.54100414,-7.262000512,32111,Portugal,PT,PRT,Guarda
Viseu,Viseu,40.65699611,-7.910000431,26364,Portugal,PT,PRT,Viseu
Vila Real,Vila Real,41.29399815,-7.73700249,17001,Portugal,PT,PRT,Vila Real
Braga,Braga,41.55499453,-8.421331219,504326,Portugal,PT,PRT,Braga
Covilha,Covilha,40.28334088,-7.499992108,21219,Portugal,PT,PRT,Castelo Branco
Horta,Horta,38.53465595,-28.64475681,6591.5,Portugal,PT,PRT,Azores
Angra do Heroismo,Angra do Heroismo,38.65039146,-27.21666976,11136.5,Portugal,PT,PRT,Azores
Portimao,Portimao,37.13373985,-8.533314048,49856.5,Portugal,PT,PRT,Faro
Faro,Faro,37.0170803,-7.933273154,31259,Portugal,PT,PRT,Faro
Coimbra,Coimbra,40.20037437,-8.41668034,97856.5,Portugal,PT,PRT,Coimbra
Setubal,Setubal,38.52995953,-8.900010011,117542,Portugal,PT,PRT,Lisboa
Porto,Porto,41.15000633,-8.620001263,793316.5,Portugal,PT,PRT,Porto
Funchal,Funchal,32.64998252,-16.88003972,152807,Portugal,PT,PRT,Madeira
Ponta Delgada,Ponta Delgada,37.74830182,-25.6665835,40791,Portugal,PT,PRT,Azores
Lisbon,Lisbon,38.72272288,-9.144866305,1664901,Portugal,PT,PRT,Lisboa
Ponce,Ponce,18.00038576,-66.61664209,156484,Puerto Rico,PR,PRI,
Mayaguez,Mayaguez,18.20151044,-67.13971094,184993,Puerto Rico,PR,PRI,
Arecibo,Arecibo,18.44002301,-66.72999435,59312.5,Puerto Rico,PR,PRI,
San Juan,San Juan,18.44002301,-66.12997929,1437115.5,Puerto Rico,PR,PRI,
Doha,Doha,25.28655601,51.53296789,1090655,Qatar,QA,QAT,Ad Dawhah
Targu Jiu,Targu Jiu,45.04500004,23.27400062,97179,Romania,RO,ROU,Gorj
Slatina,Slatina,44.43499814,24.37100156,78988,Romania,RO,ROU,Olt
Alexandria,Alexandria,43.90163107,25.28670654,49346,Romania,RO,ROU,Teleorman
Targoviste,Targoviste,44.93799913,25.4590025,88435,Romania,RO,ROU,D?mbovita
Giurgiu,Giurgiu,43.92999911,25.8399995,69067,Romania,RO,ROU,Giurgiu
Slobozia,Slobozia,44.56999806,27.38199659,52693,Romania,RO,ROU,Ialomita
Alba Lulia,Alba Lulia,46.07700313,23.58000059,66085,Romania,RO,ROU,Alba
Bistrita,Bistrita,47.13800409,24.51300358,81318,Romania,RO,ROU,Bistrita-Nasaud
Deva,Deva,45.88332304,22.91667357,67802,Romania,RO,ROU,Hunedoara
Zalau,Zalau,47.1750031,23.06300448,63232,Romania,RO,ROU,Salaj
Satu Mare,Satu Mare,47.79199816,22.88500248,112490,Romania,RO,ROU,Satu Mare
Rimnicu Vilcea,Rimnicu Vilcea,45.10999804,24.38299862,107558,Romania,RO,ROU,V?lcea
Sfintu-Gheorghe,Sfintu-Gheorghe,45.86799611,25.79300148,60677,Romania,RO,ROU,Covasna
Miercurea Cuic,Miercurea-Cuic,46.36099808,25.52400051,40004.5,Romania,RO,ROU,Harghita
Piatra-Neamt,Piatra-Neamt,46.94000405,26.38299657,102688,Romania,RO,ROU,Neamt
Braila,Braila,45.29199615,27.96900354,213569,Romania,RO,ROU,Braila
Vaslui,Vaslui,46.63332908,27.73333859,69225,Romania,RO,ROU,Vaslui
Drobeta-Turnu Severin,Drobeta-Turnu Severin,44.64589113,22.6658927,104462,Romania,RO,ROU,Mehedinti
Tulcea,Tulcea,45.19934572,28.79668127,89381.5,Romania,RO,ROU,Constanta
Arad,Arad,46.17000999,21.31998002,159338,Romania,RO,ROU,Arad
Oradea,Oradea,47.04998212,21.91999508,210222,Romania,RO,ROU,Bihor
Sibiu,Sibiu,45.79711285,24.13712073,153729.5,Romania,RO,ROU,Sibiu
Suceava,Suceava,47.63769818,26.25931677,96865.5,Romania,RO,ROU,Suceava
Buzau,Buzau,45.15650596,26.80651851,130826,Romania,RO,ROU,Buzau
Galati,Galati,45.45589337,28.04587439,302621.5,Romania,RO,ROU,Galati
Focsani,Focsani,45.69655052,27.186547,92636.5,Romania,RO,ROU,Vrancea
Craiova,Craiova,44.3262724,23.82587357,301143.5,Romania,RO,ROU,Dolj
Calarasi,Calarasi,44.20627972,27.32591833,71195.5,Romania,RO,ROU,Calarasi
Resita,Resita,45.2969625,21.88650875,82276,Romania,RO,ROU,Caras-Severin
Timisoara,Timisoara,45.75882062,21.22344844,309575,Romania,RO,ROU,Timis
Botosani,Botosani,47.74841494,26.65965409,113359,Romania,RO,ROU,Botosani
Baia Mare,Baia Mare,47.65945396,23.57906693,134630,Romania,RO,ROU,Maramures
Tirgu Mures,Tirgu Mures,46.55820335,24.55781856,148148,Romania,RO,ROU,Mures
Pitesti,Pitesti,44.85631757,24.87583533,169345,Romania,RO,ROU,Arges
Brasov,Brasov,45.64753542,25.6071602,293566,Romania,RO,ROU,Brasov
Ploiesti,Ploiesti,44.94690635,26.036488,230696.5,Romania,RO,ROU,Prahova
Bacau,Bacau,46.57843467,26.91963822,185532,Romania,RO,ROU,Bacau
Cluj-Napoca,Cluj-Napoca,46.78842185,23.5984456,299444.5,Romania,RO,ROU,Cluj
Constanta,Constanta,44.20266237,28.60997432,285112.5,Romania,RO,ROU,Constanta
Iasi,Iasi,47.16834698,27.57494706,325914,Romania,RO,ROU,Iasi
Bucharest,Bucharest,44.4333718,26.09994665,1842097,Romania,RO,ROU,Bucharest
Nazran,Nazran,43.23300312,44.78300151,93357,Russia,RU,RUS,Ingush
Ust' Ordynskiy,Ust' Ordynskiy,52.83299713,104.6999977,14538,Russia,RU,RUS,Ust-Orda Buryat
Maykop,Maykop,44.60997601,40.12002112,143377,Russia,RU,RUS,Adygey
Mozdok,Mozdok,43.75431765,44.65436967,43262.5,Russia,RU,RUS,North Ossetia
Georgievsk,Georgievsk,44.15990013,43.46994584,59158.5,Russia,RU,RUS,Stavropol'
Pyatigorsk,Pyatigorsk,44.07995668,43.09002071,86245.5,Russia,RU,RUS,Stavropol'
Kislovodsk,Kislovodsk,43.90996706,42.72001745,132337,Russia,RU,RUS,Stavropol'
Nevinnomyssk,Nevinnomyssk,44.62005292,41.95003861,134362.5,Russia,RU,RUS,Stavropol'
Enurmino,Enurmino,66.95000775,-171.8166032,297,Russia,RU,RUS,Chukchi Autonomous Okrug
Lavrentiya,Lavrentiya,65.58326947,-171.0249978,660,Russia,RU,RUS,Chukchi Autonomous Okrug
Zvezdnyy,Zvezdnyy,70.9565849,-179.5899789,10,Russia,RU,RUS,Chukchi Autonomous Okrug
Mikhalkino,Mikhalkino,69.42444039,161.4811431,570,Russia,RU,RUS,Koryak
Chernyakhovsk,Chernyakhovsk,54.6316382,21.81085445,42356.5,Russia,RU,RUS,Kaliningrad
Severomorsk,Severomorsk,69.07305646,33.42306555,46709,Russia,RU,RUS,Murmansk
Apatity,Apatity,67.57307049,33.39304154,64046.5,Russia,RU,RUS,Murmansk
Polyarnyy,Polyarnyy,69.20521893,33.45024735,18266,Russia,RU,RUS,Murmansk
Slantsy,Slantsy,59.11159731,28.07465816,27479,Russia,RU,RUS,Leningrad
Kolpino,Kolpino,59.73000917,30.65000484,180938.5,Russia,RU,RUS,City of St. Petersburg
Novozybkov,Novozybkov,52.53481529,31.9448612,43052.5,Russia,RU,RUS,Bryansk
Dyatkovo,Dyatkovo,53.5891437,34.33918534,33363.5,Russia,RU,RUS,Bryansk
Shuya,Shuya,56.85434491,41.36428625,59585.5,Russia,RU,RUS,Ivanovo
Kineshma,Kineshma,57.46996625,42.12997595,91874,Russia,RU,RUS,Ivanovo
Balakhna,Balakhna,56.49434104,43.59438269,62487,Russia,RU,RUS,Nizhegorod
Arzamas,Arzamas,55.39998924,43.80000321,126038,Russia,RU,RUS,Nizhegorod
Rzhev,Rzhev,56.2574046,34.32745479,62830,Russia,RU,RUS,Tver'
Vyshnniy Volochek,Vyshnniy Volochek,57.58303428,34.56309932,50254,Russia,RU,RUS,Tver'
Uglich,Uglich,57.52435569,38.33000118,36355,Russia,RU,RUS,Yaroslavl'
Yelets,Yelets,52.58000633,38.50001664,115803.5,Russia,RU,RUS,Lipetsk
Orekhovo-Zuevo,Orekhovo-Zuevo,55.82001528,38.97998734,130123.5,Russia,RU,RUS,Moskovsskaya
Klin,Klin,56.34305829,36.69873124,72221,Russia,RU,RUS,Moskovsskaya
Sergiyev Posad,Sergiyev Posad,56.33000999,38.17001094,107047.5,Russia,RU,RUS,Moskovsskaya
Kolomna,Kolomna,55.07998293,38.78496049,130324.5,Russia,RU,RUS,Moskovsskaya
Bataysk,Bataysk,47.13682436,39.74485022,106844.5,Russia,RU,RUS,Rostov
Taganrog,Taganrog,47.22999697,38.91999101,254960,Russia,RU,RUS,Rostov
Novocherkassk,Novocherkassk,47.41995953,40.08002356,159470.5,Russia,RU,RUS,Rostov
Kamensk Shakhtinskiy,Kamensk Shakhtinskiy,48.33176434,40.25179602,69037.5,Russia,RU,RUS,Rostov
Novoshakhtinsk,Novoshakhtinsk,47.76998985,39.91998165,82769.5,Russia,RU,RUS,Rostov
Aleksin,Aleksin,54.5143327,37.09436601,59194,Russia,RU,RUS,Tula
Novomoskovsk,Novomoskovsk,54.09001752,38.21998205,74591.5,Russia,RU,RUS,Tula
Shchekino,Shchekino,54.01433738,37.5142887,73394,Russia,RU,RUS,Tula
Nikolayevsk,Nikolayevsk,50.01610598,45.42610551,9803.5,Russia,RU,RUS,Volgograd
Shebekino,Shebekino,50.4143504,36.89437821,41301.5,Russia,RU,RUS,Belgorod
Gubkin,Gubkin,51.27434959,37.38432247,272,Russia,RU,RUS,Belgorod
Apsheronsk,Apsheronsk,44.46871848,39.72872717,43163.5,Russia,RU,RUS,Krasnodar
Kropotkin,Kropotkin,45.44708254,40.58211177,70518,Russia,RU,RUS,Krasnodar
Ruzayevka,Ruzayevka,54.06433433,44.92437903,44635,Russia,RU,RUS,Mordovia
Kirsanov,Kirsanov,52.65739178,42.71743363,17001,Russia,RU,RUS,Tambov
Michurinsk,Michurinsk,52.8999868,40.49999792,93364,Russia,RU,RUS,Tambov
Borisoglebsk,Borisoglebsk,51.36871075,42.08873816,64995,Russia,RU,RUS,Voronezh
Oktyabrskiy,Oktyabrskiy,54.4599691,53.45998205,87793,Russia,RU,RUS,Bashkortostan
Plast,Plast,54.36850181,60.80852576,15480.5,Russia,RU,RUS,Chelyabinsk
Bakal,Bakal,54.94588259,58.79588375,24160.5,Russia,RU,RUS,Chelyabinsk
Verkhniy Ufaley,Verkhniy Ufaley,56.06627932,60.23130001,33562,Russia,RU,RUS,Chelyabinsk
Severnyy,Severnyy,67.60828798,64.12325883,11562,Russia,RU,RUS,Komi
Kirovo-Chepetsk,Kirovo-Chepetsk,58.55437034,50.04437659,71555.5,Russia,RU,RUS,Kirov
Krasnoturinsk,Krasnoturinsk,59.79478558,60.48477291,64878,Russia,RU,RUS,Sverdlovsk
Asbest,Asbest,57.02304262,61.45804683,77915.5,Russia,RU,RUS,Sverdlovsk
Alapayevsk,Alapayevsk,57.84650657,61.69152095,43663.5,Russia,RU,RUS,Sverdlovsk
Krasnouralsk,Krasnouralsk,58.35151451,60.0515177,20571,Russia,RU,RUS,Sverdlovsk
Severouralsk,Severouralsk,60.15652061,59.96154903,34819,Russia,RU,RUS,Sverdlovsk
Novotroitsk,Novotroitsk,51.20001304,58.33002071,90278.5,Russia,RU,RUS,Orenburg
Buguruslan,Buguruslan,53.66301516,52.43301632,51877,Russia,RU,RUS,Orenburg
Chapayevsk,Chapayevsk,52.97432334,49.72434444,88655.5,Russia,RU,RUS,Samara
Syzran,Syzran,53.16999615,48.47997595,171589,Russia,RU,RUS,Samara
Novokuybishevsk,Novokuybishevsk,53.11999921,49.91993974,132067,Russia,RU,RUS,Samara
Naberezhnyye Chelny,Naberezhnyye Chelny,55.69999676,52.31994828,461086,Russia,RU,RUS,Tatarstan
Zelenodolsk,Zelenodolsk,55.84055666,48.65500403,50338.5,Russia,RU,RUS,Tatarstan
Leninogorsk,Leninogorsk,54.59869448,52.44872595,53362,Russia,RU,RUS,Tatarstan
Bugulma,Bugulma,54.55433026,52.79428625,85384,Russia,RU,RUS,Tatarstan
Nefteyugansk,Nefteyugansk,61.07765301,72.70268347,112632,Russia,RU,RUS,Khanty-Mansiy
Leninsk Kuznetsky,Leninsk Kuznetsky,54.66000856,86.16997514,108047.5,Russia,RU,RUS,Kemerovo
Anzhero Sudzhensk,Anzhero Sudzhensk,56.08002525,86.04000891,83109,Russia,RU,RUS,Kemerovo
Kiselevsk,Kiselevsk,54.00002301,86.64002397,87164,Russia,RU,RUS,Kemerovo
Mundybash,Mundybash,53.23327395,87.31667517,5870,Russia,RU,RUS,Kemerovo
Chernogorsk,Chernogorsk,53.8313253,91.22268998,39815.5,Russia,RU,RUS,Khakass
Abaza,Abaza,52.66901898,90.09536861,17638.5,Russia,RU,RUS,Khakass
Iskitim,Iskitim,54.65093935,83.28653357,60806.5,Russia,RU,RUS,Novosibirsk
Toguchin,Toguchin,55.23767356,84.37768144,20087,Russia,RU,RUS,Novosibirsk
Kupina,Kupina,54.35922589,77.27418738,9856.5,Russia,RU,RUS,Novosibirsk
Zaozernyy,Zaozernyy,55.96197044,94.70278764,33865,Russia,RU,RUS,Krasnoyarsk
Bogotol,Bogotol,56.21647687,89.51840124,22559.5,Russia,RU,RUS,Krasnoyarsk
Shilka,Shilka,51.87056643,116.0306331,10561,Russia,RU,RUS,Chita
Sherlovaya Gora,Sherlovaya Gora,50.53059654,116.3006425,411,Russia,RU,RUS,Chita
Petrovsk Zabaykalskiy,Petrovsk Zabaykalskiy,51.28269533,108.8326745,20301,Russia,RU,RUS,Chita
Arsenyev,Arsenyev,44.16230308,133.2823449,56721,Russia,RU,RUS,Primor'ye
Partizansk,Partizansk,43.13487225,133.1349121,40734.5,Russia,RU,RUS,Primor'ye
Dalnerechensk,Dalnerechensk,45.92728579,133.7223181,25917.5,Russia,RU,RUS,Primor'ye
Zemlya Bunge,Zemlya Bunge,74.89830813,142.1050105,10,Russia,RU,RUS,Sakha (Yakutia)
Khorgo,Khorgo,73.48330406,113.6300044,10,Russia,RU,RUS,Sakha (Yakutia)
Put Lenina,Put Lenina,68.51663047,107.7999727,298,Russia,RU,RUS,Sakha (Yakutia)
Obluchye,Obluchye,48.99999229,131.083306,9689.5,Russia,RU,RUS,Yevrey
Vanino,Vanino,49.08732546,140.2424886,15985.5,Russia,RU,RUS,Khabarovsk
Omchak,Omchak,61.63327801,147.9166971,10,Russia,RU,RUS,Maga Buryatdan
Uglegorsk,Uglegorsk,49.08334637,142.0333353,12139.5,Russia,RU,RUS,Sakhalin
Kholmsk,Kholmsk,47.04732078,142.0623775,32796,Russia,RU,RUS,Sakhalin
Solikamsk,Solikamsk,59.669987,56.74996212,97397,Russia,RU,RUS,Perm'
Kizel,Kizel,59.06436505,57.6343009,21971,Russia,RU,RUS,Perm'
Pakhachi,Pakhachi,60.5815851,169.0499808,10,Russia,RU,RUS,Kamchatka
Oymyakon,Oymyakon,0,0,486,Russia,RU,RUS,Sakha (Yakutia)
Timiryazevskiy,Timiryazevskiy,56.49260988,84.90359249,6705.5,Russia,RU,RUS,Tomsk
Asino,Asino,56.99312197,86.16268876,24732.5,Russia,RU,RUS,Tomsk
Strezhevoy,Strezhevoy,60.73315208,77.57768306,38997.5,Russia,RU,RUS,Tomsk
Cherkessk,Cherkessk,44.29040895,42.06000606,101153,Russia,RU,RUS,Karachay-Cherkess
Vladikavkaz,Vladikavkaz,43.05038129,44.66997595,341000,Russia,RU,RUS,North Ossetia
Blagodarnyy,Blagodarnyy,45.10472618,43.43439245,28070.5,Russia,RU,RUS,Stavropol'
Zelenokumsk,Zelenokumsk,44.40910972,43.87870642,35220.5,Russia,RU,RUS,Stavropol'
Mukhomornoye,Mukhomornoye,66.4170687,173.333337,55,Russia,RU,RUS,Chukchi Autonomous Okrug
Beringovskiy,Beringovskiy,63.0654645,179.3066674,1861,Russia,RU,RUS,Chukchi Autonomous Okrug
Bilibino,Bilibino,68.0504057,166.3332991,5757,Russia,RU,RUS,Chukchi Autonomous Okrug
Mys Shmidta,Mys Shmidta,68.93371096,-179.4999844,492,Russia,RU,RUS,Chukchi Autonomous Okrug
Egvekinot,Egvekinot,66.32213166,-179.1837225,2248,Russia,RU,RUS,Chukchi Autonomous Okrug
Sovetsk,Sovetsk,55.07176638,21.88196122,40166.5,Russia,RU,RUS,Kaliningrad
Nikel,Nikel,69.41257062,30.21881669,15731,Russia,RU,RUS,Murmansk
Monchegorsk,Monchegorsk,67.92912111,32.8287349,46934.5,Russia,RU,RUS,Murmansk
Kirovsk,Kirovsk,67.60908897,33.66873531,22949,Russia,RU,RUS,Murmansk
Borovichi,Borovichi,58.39781659,33.89740352,57229,Russia,RU,RUS,Novgorod
Staraya Russa,Staraya Russa,57.99476625,31.35435461,32591.5,Russia,RU,RUS,Novgorod
Volkhov,Volkhov,59.92909263,32.33873897,45366.5,Russia,RU,RUS,Leningrad
Tikhvin,Tikhvin,59.64484641,33.51437781,50793,Russia,RU,RUS,Leningrad
Svetogorsk,Svetogorsk,61.10132082,28.9176558,22924,Russia,RU,RUS,Leningrad
Gatchina,Gatchina,59.5706649,30.13334387,90123.5,Russia,RU,RUS,Leningrad
Luga,Luga,58.7363489,29.83899491,37124.5,Russia,RU,RUS,Leningrad
Klintsy,Klintsy,52.7652405,32.24484289,60885,Russia,RU,RUS,Bryansk
Roslavl,Roslavl,53.95090456,32.86041256,54299,Russia,RU,RUS,Smolensk
Safonovo,Safonovo,55.1464905,33.21610144,44461,Russia,RU,RUS,Smolensk
Vyazma,Vyazma,55.21219708,34.29179805,49118.5,Russia,RU,RUS,Smolensk
Segezha,Segezha,63.75477643,34.32430253,28961,Russia,RU,RUS,Karelia
Vichuga,Vichuga,57.21912884,41.92874792,38093.5,Russia,RU,RUS,Ivanovo
Sharya,Sharya,58.37975568,45.50935624,32666,Russia,RU,RUS,Kostroma
Buy,Buy,58.48468467,41.52437984,25781.5,Russia,RU,RUS,Kostroma
Dzerzhinsk,Dzerzhinsk,56.25037661,43.46002397,235457.5,Russia,RU,RUS,Nizhegorod
Vyska,Vyska,55.32472251,42.16439245,60356,Russia,RU,RUS,Nizhegorod
Kimry,Kimry,56.86912437,37.34437659,50531,Russia,RU,RUS,Tver'
Bezhetsk,Bezhetsk,57.76472862,36.68999792,31425,Russia,RU,RUS,Tver'
Nelidovo,Nelidovo,56.22350486,32.77307939,24973,Russia,RU,RUS,Tver'
Bologoye,Bologoye,57.87216392,34.05176103,21785,Russia,RU,RUS,Tver'
Torzhok,Torzhok,57.02906293,34.97873287,45839,Russia,RU,RUS,Tver'
Sokol,Sokol,59.46477989,40.11438839,35637.5,Russia,RU,RUS,Vologda
Cherepovets,Cherepovets,59.14043276,37.90997514,265606.5,Russia,RU,RUS,Vologda
Rybinsk,Rybinsk,58.05034426,38.81999711,203874.5,Russia,RU,RUS,Yaroslavl'
Rostov,Rostov,57.18915651,39.40430253,33578,Russia,RU,RUS,Yaroslavl'
Kaluga,Kaluga,54.52037884,36.27002356,313733.5,Russia,RU,RUS,Kaluga
Kirov,Kirov,54.08518577,34.30482051,33852,Russia,RU,RUS,Kaluga
Obninsk,Obninsk,55.08044802,36.62002803,66236,Russia,RU,RUS,Kaluga
Lgov,Lgov,51.6947632,35.27437374,16093.5,Russia,RU,RUS,Kursk
Zheleznogorsk,Zheleznogorsk,52.3547746,35.40439164,94212,Russia,RU,RUS,Kursk
Gryazi,Gryazi,52.49476605,39.9343477,46451,Russia,RU,RUS,Lipetsk
Yegoryevsk,Yegoryevsk,55.38479637,39.02939001,87497.5,Russia,RU,RUS,Moskovsskaya
Podolsk,Podolsk,55.38042971,37.52994665,250017.5,Russia,RU,RUS,Moskovsskaya
Solnechnogorsk,Solnechnogorsk,56.18069094,36.98088456,48043,Russia,RU,RUS,Moskovsskaya
Noginsk,Noginsk,55.87042564,38.48001786,172855,Russia,RU,RUS,Moskovsskaya
Serpukhov,Serpukhov,54.93037966,37.43000443,131871,Russia,RU,RUS,Moskovsskaya
Livny,Livny,52.42479616,37.60436072,52277.5,Russia,RU,RUS,Orel
Mtsensk,Mtsensk,53.26474489,36.54716426,24499.5,Russia,RU,RUS,Orel
Salsk,Salsk,46.4775106,41.5420015,54739,Russia,RU,RUS,Rostov
Belaya Kalitva,Belaya Kalitva,48.18650189,40.78613033,47809.5,Russia,RU,RUS,Rostov
Shakhty,Shakhty,47.72038047,40.2700378,206203.5,Russia,RU,RUS,Rostov
Millerovo,Millerovo,48.93785138,40.39742021,32726.5,Russia,RU,RUS,Rostov
Yefremov,Yefremov,53.14911888,38.12153845,44933,Russia,RU,RUS,Tula
Bogoroditsk,Bogoroditsk,53.77468793,38.11435543,34884.5,Russia,RU,RUS,Tula
Kamyshin,Kamyshin,50.08039146,45.40000891,82613,Russia,RU,RUS,Volgograd
Pallasovka,Pallasovka,50.04773195,46.87733476,9960.5,Russia,RU,RUS,Volgograd
Frolovo,Frolovo,49.77219322,43.65179521,40096.5,Russia,RU,RUS,Volgograd
Volzhskiy,Volzhskiy,48.79481101,44.77436234,306022.5,Russia,RU,RUS,Volgograd
Mikhaylovka,Mikhaylovka,50.06785992,43.21745479,57327.5,Russia,RU,RUS,Volgograd
Uryupinsk,Uryupinsk,50.77344993,42.00305863,37993.5,Russia,RU,RUS,Volgograd
Starsy Oskol,Starsy Oskol,51.30042035,37.83995357,200131,Russia,RU,RUS,Belgorod
Alekseyevka,Alekseyevka,50.65348309,38.69307979,38633.5,Russia,RU,RUS,Belgorod
Valuyki,Valuyki,50.20909161,38.09869747,32045,Russia,RU,RUS,Belgorod
Tuapse,Tuapse,44.11476076,39.06437496,81689.5,Russia,RU,RUS,Krasnodar
Gelendzhik,Gelendzhik,44.57475852,38.06438432,53111.5,Russia,RU,RUS,Krasnodar
Labinsk,Labinsk,44.6347807,40.74427242,51594,Russia,RU,RUS,Krasnodar
Armavir,Armavir,45.00039146,41.13003699,191813.5,Russia,RU,RUS,Krasnodar
Timashevsk,Timashevsk,45.62474611,38.94438228,44024,Russia,RU,RUS,Krasnodar
Tikhoretsk,Tikhoretsk,45.85310427,40.13774613,62368.5,Russia,RU,RUS,Krasnodar
Yeysk,Yeysk,46.69878908,38.26339026,76591.5,Russia,RU,RUS,Krasnodar
Saransk,Saransk,54.17037437,45.18002234,303304.5,Russia,RU,RUS,Mordovia
Kamenka,Kamenka,53.19472333,44.04438106,16560,Russia,RU,RUS,Penza
Kuznetsk,Kuznetsk,53.12041262,46.59998734,93027,Russia,RU,RUS,Penza
Serdobsk,Serdobsk,52.46218406,44.22178625,30263,Russia,RU,RUS,Penza
Kasimov,Kasimov,54.9434538,41.39307003,36009,Russia,RU,RUS,Ryazan'
Sasovo,Sasovo,54.34914899,41.90869747,30591.5,Russia,RU,RUS,Ryazan'
Kotovsk,Kotovsk,52.59473411,41.50438106,31221,Russia,RU,RUS,Tambov
Morshansk,Morshansk,53.4547333,41.80436275,46330.5,Russia,RU,RUS,Tambov
Kovrov,Kovrov,56.36036989,41.33002478,153060,Russia,RU,RUS,Vladimir
Murom,Murom,55.57041811,42.04000728,129109,Russia,RU,RUS,Vladimir
Rayevskiy,Rayevskiy,54.06738324,54.92692094,13578.5,Russia,RU,RUS,Bashkortostan
Sibay,Sibay,52.70911989,58.63873572,54696,Russia,RU,RUS,Bashkortostan
Kumertau,Kumertau,52.7747748,55.7843363,48667.5,Russia,RU,RUS,Bashkortostan
Salavat,Salavat,53.37034568,55.92996049,111648,Russia,RU,RUS,Bashkortostan
Belebey,Belebey,54.12913658,54.11870154,57674.5,Russia,RU,RUS,Bashkortostan
Tuymazy,Tuymazy,54.6047923,53.69433467,61826,Russia,RU,RUS,Bashkortostan
Neftekamsk,Neftekamsk,56.08351341,54.26308549,122170,Russia,RU,RUS,Bashkortostan
Troitsk,Troitsk,54.10564964,61.57023637,69919,Russia,RU,RUS,Chelyabinsk
Yemanzhelinsk,Yemanzhelinsk,54.74886619,61.29350907,35936,Russia,RU,RUS,Chelyabinsk
Kartaly,Kartaly,53.04739382,60.6819185,27107,Russia,RU,RUS,Chelyabinsk
Asha,Asha,54.99799827,57.27261755,35944.5,Russia,RU,RUS,Chelyabinsk
Miass,Miass,54.99541445,60.0949259,148834.5,Russia,RU,RUS,Chelyabinsk
Kyshtym,Kyshtym,55.69999676,60.5595487,46268,Russia,RU,RUS,Chelyabinsk
Kurtamysh,Kurtamysh,54.90867556,64.43326575,10006,Russia,RU,RUS,Kurgan
Shadrinsk,Shadrinsk,56.08366844,63.6332629,67303.5,Russia,RU,RUS,Kurgan
Varnek,Varnek,69.73014813,60.06355831,10,Russia,RU,RUS,Nenets
Bugrino,Bugrino,68.80787884,49.30416337,300,Russia,RU,RUS,Nenets
Yamburg,Yamburg,68.35038739,77.13331742,48488,Russia,RU,RUS,Yamal-Nenets
Nakhodka,Nakhodka,67.75039817,77.51996049,159551,Russia,RU,RUS,Yamal-Nenets
Sosnogorsk,Sosnogorsk,63.59476035,53.89432247,24270,Russia,RU,RUS,Komi
Sovetsk,Sovetsk,57.57846092,48.9580863,10020.5,Russia,RU,RUS,Kirov
Slobodskoy,Slobodskoy,58.71849469,50.18803707,40661.5,Russia,RU,RUS,Kirov
Kirs,Kirs,59.31383303,52.24517248,8319,Russia,RU,RUS,Kirov
Omutninsk,Omutninsk,58.6589376,52.1591829,29082,Russia,RU,RUS,Kirov
Kotelnich,Kotelnich,58.30412722,48.31373287,28015.5,Russia,RU,RUS,Kirov
Yoshkar Ola,Yoshkar Ola,56.63539187,47.87494828,301753,Russia,RU,RUS,Mariy-El
Kamensk Uralskiy,Kamensk Uralskiy,56.42046958,61.9350203,176598.5,Russia,RU,RUS,Sverdlovsk
Polevskoy,Polevskoy,56.44341392,60.18804683,42706,Russia,RU,RUS,Sverdlovsk
Tavda,Tavda,58.05365155,65.25827999,32401,Russia,RU,RUS,Sverdlovsk
Artemovskiy,Artemovskiy,57.36519228,61.86975297,39194.5,Russia,RU,RUS,Sverdlovsk
Nevyansk,Nevyansk,57.49024925,60.21476355,27035,Russia,RU,RUS,Sverdlovsk
Verkhnyaya Salda,Verkhnyaya Salda,58.05018923,60.54978186,48525,Russia,RU,RUS,Sverdlovsk
Nizhnyaya Tura,Nizhnyaya Tura,58.64364138,59.7982515,56084,Russia,RU,RUS,Sverdlovsk
Karpinsk,Karpinsk,59.76016237,60.00981482,30438.5,Russia,RU,RUS,Sverdlovsk
Ivdel,Ivdel,60.69364545,60.41325273,11466.5,Russia,RU,RUS,Sverdlovsk
Krasnoufimsk,Krasnoufimsk,56.59911501,57.7586344,40208.5,Russia,RU,RUS,Sverdlovsk
Sarapul,Sarapul,56.47914817,53.79872107,92622.5,Russia,RU,RUS,Udmurt
Mozhga,Mozhga,56.4547569,52.18434932,43098,Russia,RU,RUS,Udmurt
Votkinsk,Votkinsk,57.03040651,53.99002722,91248,Russia,RU,RUS,Udmurt
Glazov,Glazov,58.12320803,52.62876664,93352,Russia,RU,RUS,Udmurt
Kanash,Kanash,55.50912986,47.46866817,49011.5,Russia,RU,RUS,Chuvash
Shumerlya,Shumerlya,55.4848161,46.42439083,35225,Russia,RU,RUS,Chuvash
Alatyr,Alatyr,54.8503587,46.59998734,44291.5,Russia,RU,RUS,Chuvash
Sol-lletsk,Sol-lletsk,51.1602997,54.99988806,25155,Russia,RU,RUS,Orenburg
Dombarovskiy,Dombarovskiy,50.75458803,59.54002437,5564,Russia,RU,RUS,Orenburg
Mednogorsk,Mednogorsk,51.41912111,57.57874874,27274,Russia,RU,RUS,Orenburg
Gay,Gay,51.47472495,58.45430253,39710,Russia,RU,RUS,Orenburg
Buzuluk,Buzuluk,52.78211285,52.26176062,84762,Russia,RU,RUS,Orenburg
Otradnyy,Otradnyy,53.37781293,51.34739783,46400,Russia,RU,RUS,Samara
Tolyatti,Tolyatti,53.48039064,49.53004106,648622,Russia,RU,RUS,Samara
Engels,Engels,51.50040814,46.12001664,183221,Russia,RU,RUS,Saratov
Pugachev,Pugachev,52.01476951,48.79437537,26690,Russia,RU,RUS,Saratov
Volsk,Volsk,52.03471661,47.37430701,62027,Russia,RU,RUS,Saratov
Atkarsk,Atkarsk,51.87645754,44.99610592,23315.5,Russia,RU,RUS,Saratov
Balashov,Balashov,51.55350568,43.16309119,84107,Russia,RU,RUS,Saratov
Almetyevsk,Almetyevsk,54.90040733,52.31994828,117971,Russia,RU,RUS,Tatarstan
Chistopol,Chistopol,55.36477175,50.64067094,52232.5,Russia,RU,RUS,Tatarstan
Nizhnekamsk,Nizhnekamsk,55.64043968,51.82003048,210363,Russia,RU,RUS,Tatarstan
Dimitrovgrad,Dimitrovgrad,54.25042116,49.56001339,121213.5,Russia,RU,RUS,Ul'yanovsk
Peregrebnoye,Peregrebnoye,62.96699506,65.08593909,10,Russia,RU,RUS,Khanty-Mansiy
Saranpaul,Saranpaul,64.25045677,60.97001461,2985,Russia,RU,RUS,Khanty-Mansiy
Uray,Uray,60.14013918,64.75479651,20361,Russia,RU,RUS,Khanty-Mansiy
Laryak,Laryak,61.10119163,80.25136999,10,Russia,RU,RUS,Khanty-Mansiy
Kogalym,Kogalym,62.04462242,74.49409867,58192,Russia,RU,RUS,Khanty-Mansiy
Megion,Megion,61.06075482,76.0953446,47650.5,Russia,RU,RUS,Khanty-Mansiy
Cherlak,Cherlak,54.16047833,74.82002193,7060.5,Russia,RU,RUS,Omsk
Kalachinsk,Kalachinsk,55.04866701,74.56825435,20506.5,Russia,RU,RUS,Omsk
Nazyvayevsk,Nazyvayevsk,55.56695579,71.35000118,10938.5,Russia,RU,RUS,Omsk
Isikul,Isikul,54.92870017,71.26824906,21136,Russia,RU,RUS,Omsk
Ishim,Ishim,56.15022768,69.44980709,60798,Russia,RU,RUS,Tyumen'
Golyshmanovo,Golyshmanovo,56.3819448,68.37147497,8708.5,Russia,RU,RUS,Tyumen'
Yalutorovsk,Yalutorovsk,56.67363243,66.29826819,31580,Russia,RU,RUS,Tyumen'
Biysk,Biysk,52.53406598,85.18000972,209796.5,Russia,RU,RUS,Altay
Zmeinogorsk,Zmeinogorsk,51.15709576,82.19502397,10471.5,Russia,RU,RUS,Altay
Aleysk,Aleysk,52.49176882,82.77767574,22477.5,Russia,RU,RUS,Altay
Novoaltaysk,Novoaltaysk,53.39925865,83.95884395,76218,Russia,RU,RUS,Altay
Kamenna Obi,Kamenna Obi,53.7936015,81.33879716,40883,Russia,RU,RUS,Altay
Gornyak,Gornyak,50.98808799,81.48767696,9567,Russia,RU,RUS,Altay
Kulunda,Kulunda,52.58266766,78.94726355,8831.5,Russia,RU,RUS,Altay
Slavgorod,Slavgorod,53.00494163,78.6695544,27651,Russia,RU,RUS,Altay
Tashtagol,Tashtagol,52.79175051,87.86770097,21902,Russia,RU,RUS,Kemerovo
Guryevsk,Guryevsk,54.29814435,85.93768957,31878.5,Russia,RU,RUS,Kemerovo
Yurga,Yurga,55.72575747,84.88540238,72495.5,Russia,RU,RUS,Kemerovo
Topki,Topki,55.28017743,85.61083614,24672,Russia,RU,RUS,Kemerovo
Mariinsk,Mariinsk,56.21076662,87.76036902,41344.5,Russia,RU,RUS,Kemerovo
Shira,Shira,54.49144004,89.95305172,4836,Russia,RU,RUS,Khakass
Cherepanovo,Cherepanovo,54.23362632,83.36880245,15094.5,Russia,RU,RUS,Novosibirsk
Kargat,Kargat,55.19594484,80.28113562,5861,Russia,RU,RUS,Novosibirsk
Ob,Ob,54.99804995,82.70765417,32093.5,Russia,RU,RUS,Novosibirsk
Karasuk,Karasuk,53.72730064,78.02189368,26758.5,Russia,RU,RUS,Novosibirsk
Barabinsk,Barabinsk,55.35727867,78.35189937,29888.5,Russia,RU,RUS,Novosibirsk
Tatarsk,Tatarsk,55.22193809,75.96651526,24182,Russia,RU,RUS,Novosibirsk
Kaspiysk,Kaspiysk,42.87473309,47.62436926,61451.5,Russia,RU,RUS,Dagestan
Derbent,Derbent,42.05780621,48.27740434,97259,Russia,RU,RUS,Dagestan
Buynaksk,Buynaksk,42.8334953,47.11303096,75800,Russia,RU,RUS,Dagestan
Yessey,Yessey,68.48373842,102.1666215,10,Russia,RU,RUS,Evenk
Ulkan,Ulkan,55.90039797,107.7833329,10,Russia,RU,RUS,Irkutsk
Kirensk,Kirensk,57.78573509,108.1119433,6759,Russia,RU,RUS,Irkutsk
Zheleznogorsk Ilimskiy,Zheleznogorsk Ilimskiy,56.57624819,104.1226778,27291,Russia,RU,RUS,Irkutsk
Vikhorevka,Vikhorevka,56.09309938,101.2426985,166,Russia,RU,RUS,Irkutsk
Biryusinsk,Biryusinsk,55.96065269,97.81443233,8199.5,Russia,RU,RUS,Irkutsk
Kodinskiy,Kodinskiy,58.69805666,99.17765662,15670,Russia,RU,RUS,Krasnoyarsk
Artemovsk,Artemovsk,54.34873557,93.43552649,4948,Russia,RU,RUS,Krasnoyarsk
Uyar,Uyar,55.81037762,94.31531775,12370,Russia,RU,RUS,Krasnoyarsk
Uzhur,Uzhur,55.32916669,89.82070837,17424.5,Russia,RU,RUS,Krasnoyarsk
Sayanogorsk,Sayanogorsk,53.0894326,91.40040523,52790.5,Russia,RU,RUS,Krasnoyarsk
Podkamennaya,Podkamennaya,61.59950747,90.12363562,10,Russia,RU,RUS,Krasnoyarsk
Igarka,Igarka,67.46710797,86.58333492,6262,Russia,RU,RUS,Krasnoyarsk
Agapa,Agapa,71.45037905,89.24999385,10,Russia,RU,RUS,Taymyr
Boyarka,Boyarka,70.76698407,97.50003292,35968,Russia,RU,RUS,Taymyr
Nordvik,Nordvik,74.01650148,111.5100305,0,Russia,RU,RUS,Taymyr
Chelyuskin,Chelyuskin,77.71697329,104.2500085,885,Russia,RU,RUS,Taymyr
Taksimo,Taksimo,56.33153444,114.8899792,10359,Russia,RU,RUS,Buryat
Gusinoozyorsk,Gusinoozyorsk,51.28075747,106.5003621,20498.5,Russia,RU,RUS,Buryat
Aginskoye,Aginskoye,51.10306805,114.5228182,11491,Russia,RU,RUS,Aga Buryat
Progress,Progress,49.75038576,129.6166772,146,Russia,RU,RUS,Amur
Belogorsk,Belogorsk,50.91909995,128.4637243,69057,Russia,RU,RUS,Amur
Nyukzha,Nyukzha,56.53121218,121.613083,10,Russia,RU,RUS,Amur
Nerchinsk,Nerchinsk,52.00895591,116.548586,11979.5,Russia,RU,RUS,Chita
Kavalerovo,Kavalerovo,44.27020347,135.0497823,17801,Russia,RU,RUS,Primor'ye
Spassk Dalniy,Spassk Dalniy,44.60015749,132.8197892,44861,Russia,RU,RUS,Primor'ye
Shalaurova,Shalaurova,73.22037437,143.1833427,10,Russia,RU,RUS,Sakha (Yakutia)
Logashkino,Logashkino,70.85038983,153.9000012,0,Russia,RU,RUS,Sakha (Yakutia)
Ust Kuyga,Ust Kuyga,70.01705568,135.6000329,1517,Russia,RU,RUS,Sakha (Yakutia)
Pokrovsk,Pokrovsk,61.49344159,129.1272497,8065.5,Russia,RU,RUS,Sakha (Yakutia)
Verkhnevilyuysk,Verkhnevilyuysk,63.44569969,120.3167281,6341,Russia,RU,RUS,Sakha (Yakutia)
Vitim,Vitim,59.45149904,112.5578218,3843,Russia,RU,RUS,Sakha (Yakutia)
Olyokminsk,Olyokminsk,60.50319195,120.3925891,9743.5,Russia,RU,RUS,Sakha (Yakutia)
Tunguskhaya,Tunguskhaya,64.90044293,125.2500187,10,Russia,RU,RUS,Sakha (Yakutia)
Natara,Natara,68.41061627,123.9255,10,Russia,RU,RUS,Sakha (Yakutia)
Zhilinda,Zhilinda,70.13368939,114.0000077,10,Russia,RU,RUS,Sakha (Yakutia)
Trofimovsk,Trofimovsk,72.59968874,127.0336824,10,Russia,RU,RUS,Sakha (Yakutia)
Tukchi,Tukchi,57.36697512,139.5000016,10,Russia,RU,RUS,Khabarovsk
Amursk,Amursk,50.22283754,136.8974214,45901.5,Russia,RU,RUS,Khabarovsk
Bikin,Bikin,46.82025454,134.2649206,19264.5,Russia,RU,RUS,Khabarovsk
Vyazemskiy,Vyazemskiy,47.5328467,134.7474751,14191,Russia,RU,RUS,Khabarovsk
Chegdomyn,Chegdomyn,51.11779584,133.0241178,7485.5,Russia,RU,RUS,Khabarovsk
Siglan,Siglan,59.03372093,152.4165775,10,Russia,RU,RUS,Maga Buryatdan
Karamken,Karamken,60.20041974,151.166628,10,Russia,RU,RUS,Maga Buryatdan
Strelka,Strelka,61.86698468,152.2501794,10,Russia,RU,RUS,Maga Buryatdan
Severo Kurilsk,Severo Kurilsk,50.69048342,156.0850358,2422,Russia,RU,RUS,Sakhalin
Krasnogorsk,Krasnogorsk,48.4615497,142.0899727,3304,Russia,RU,RUS,Sakhalin
Poronaysk,Poronaysk,49.24155377,143.0850024,15555,Russia,RU,RUS,Sakhalin
Makarov,Makarov,48.63373557,142.8000069,4571.5,Russia,RU,RUS,Sakhalin
Dolinsk,Dolinsk,47.35042889,142.8000069,11791.5,Russia,RU,RUS,Sakhalin
Nevelsk,Nevelsk,46.68028892,141.8699344,16754.5,Russia,RU,RUS,Sakhalin
Kudymkar,Kudymkar,59.01617678,54.63303707,32009.5,Russia,RU,RUS,Komi-Permyak
Kungur,Kungur,57.4347746,56.95434241,59911.5,Russia,RU,RUS,Perm'
Krasnokamsk,Krasnokamsk,58.07473553,55.74428707,50382,Russia,RU,RUS,Perm'
Chusovoy,Chusovoy,58.2934302,57.81304968,61159,Russia,RU,RUS,Perm'
Gubakha,Gubakha,58.86913149,57.58872229,18716.5,Russia,RU,RUS,Perm'
Utkholok,Utkholok,57.55040061,157.2333378,10,Russia,RU,RUS,Kamchatka
Bol'sheretsk,Bol'sheretsk,52.43898134,156.3593859,10,Russia,RU,RUS,Kamchatka
Il'pyrskiy,Il'pyrskiy,59.96738829,164.1720053,10,Russia,RU,RUS,Kamchatka
Korf,Korf,60.33206545,165.8183435,400,Russia,RU,RUS,Kamchatka
Kolpashevo,Kolpashevo,58.30040651,82.99538855,27876,Russia,RU,RUS,Tomsk
Omolon,Omolon,65.24998232,160.5000118,1050,Russia,RU,RUS,Chukchi Autonomous Okrug
Pevek,Pevek,69.70082176,170.3133146,4837,Russia,RU,RUS,Chukchi Autonomous Okrug
Umba,Umba,66.68139366,34.34554154,6128,Russia,RU,RUS,Murmansk
Kovda,Kovda,66.690282,32.87023108,20,Russia,RU,RUS,Murmansk
Velikiy Novgorod,Velikiy Novgorod,58.4999809,31.33001501,218717,Russia,RU,RUS,Novgorod
Velikiye Luki,Velikiye Luki,56.31995892,30.52003861,93243,Russia,RU,RUS,Pskov
Belomorsk,Belomorsk,64.52522036,34.76582597,12165,Russia,RU,RUS,Karelia
Kem,Kem,64.95359214,34.56837032,13829,Russia,RU,RUS,Karelia
Krasino,Krasino,70.73144845,54.420799,10,Russia,RU,RUS,Arkhangel'sk
Matochkin Shar,Matochkin Shar,73.26999163,56.44969682,10,Russia,RU,RUS,Arkhangel'sk
Severodvinsk,Severodvinsk,64.57002382,39.83001298,182077.5,Russia,RU,RUS,Arkhangel'sk
Kursk,Kursk,51.73998008,36.19002844,398742,Russia,RU,RUS,Kursk
Tula,Tula,54.19995913,37.62994055,479155.5,Russia,RU,RUS,Tula
Tambov,Tambov,52.73002301,41.43001868,296207.5,Russia,RU,RUS,Tambov
Sterlitamak,Sterlitamak,53.62999392,55.96003617,220040,Russia,RU,RUS,Bashkortostan
Kurgan,Kurgan,55.45995974,65.34499304,329399.5,Russia,RU,RUS,Kurgan
Indiga,Indiga,67.68975404,49.01659483,10,Russia,RU,RUS,Nenets
Shoyna,Shoyna,67.86664431,44.13336788,300,Russia,RU,RUS,Nenets
Novy Port,Novyy Port,67.69833417,72.92830277,1790,Russia,RU,RUS,Yamal-Nenets
Salekhard,Salekhard,66.53502016,66.60998043,32427,Russia,RU,RUS,Yamal-Nenets
Gyda,Gyda,70.88142153,78.46610429,10,Russia,RU,RUS,Yamal-Nenets
Tazovskiy,Tazovskiy,67.46666872,78.69999182,5981,Russia,RU,RUS,Yamal-Nenets
Novy Urengoy,Novy Urengoy,66.08331647,76.63324459,47357.5,Russia,RU,RUS,Yamal-Nenets
Nadym,Nadym,65.5298102,72.51478796,26723,Russia,RU,RUS,Yamal-Nenets
Noyabrsk,Noyabrsk,63.1665436,75.61651078,110572,Russia,RU,RUS,Yamal-Nenets
Syktyvkar,Syktyvkar,61.65999473,50.81998816,230524.5,Russia,RU,RUS,Komi
Ukhta,Ukhta,63.55998212,53.68999385,96396.5,Russia,RU,RUS,Komi
Serov,Serov,59.61497744,60.58497351,91831,Russia,RU,RUS,Sverdlovsk
Cheboksary,Cheboksary,56.12997052,47.25002519,444027.5,Russia,RU,RUS,Chuvash
Orsk,Orsk,51.21001243,58.62731523,159353,Russia,RU,RUS,Orenburg
Balakovo,Balakovo,52.02998822,47.80001745,172821.5,Russia,RU,RUS,Saratov
Igrim,Igrim,63.19331199,64.41941646,9545,Russia,RU,RUS,Khanty-Mansiy
Nyagan,Nyagan,62.14652834,65.38142493,46238.5,Russia,RU,RUS,Khanty-Mansiy
Khanty Mansiysk,Khanty Mansiysk,61.00153363,69.00151404,48114,Russia,RU,RUS,Khanty-Mansiy
Nizhenvartovsk,Nizhenvartovsk,60.93497438,76.58001786,136385,Russia,RU,RUS,Khanty-Mansiy
Numto,Numto,63.66671979,71.33330969,10,Russia,RU,RUS,Khanty-Mansiy
Tara,Tara,56.89824404,74.37824011,24130.5,Russia,RU,RUS,Omsk
Tobolsk,Tobolsk,58.1997925,68.26481482,87877.5,Russia,RU,RUS,Tyumen'
Rubtsovsk,Rubtsovsk,51.52001935,81.21001949,159133,Russia,RU,RUS,Altay
Gorno Altaysk,Gorno Altaysk,51.96133608,85.95768835,57392.5,Russia,RU,RUS,Gorno-Altay
Prokopyevsk,Prokopyevsk,53.89997744,86.70999385,242547,Russia,RU,RUS,Kemerovo
Makhachkala,Makhachkala,42.98002382,47.49998409,526470,Russia,RU,RUS,Dagestan
Tura,Tura,64.28329714,100.2500459,5444,Russia,RU,RUS,Evenk
Noginsk,Noginsk,64.48331077,91.23333533,229731,Russia,RU,RUS,Evenk
Yerema,Yerema,60.38079632,107.7794055,745,Russia,RU,RUS,Irkutsk
Tayshet,Tayshet,55.92770896,97.98770341,44975,Russia,RU,RUS,Irkutsk
Usolye Sibirskoye,Usolye Sibirskoye,52.76498212,103.6449808,85012,Russia,RU,RUS,Irkutsk
Slyudyanka,Slyudyanka,51.65383547,103.6988277,14920.5,Russia,RU,RUS,Irkutsk
Cheremkhovo,Cheremkhovo,53.15880821,103.0738529,51686.5,Russia,RU,RUS,Irkutsk
Zima,Zima,53.93305035,102.0330896,46781,Russia,RU,RUS,Irkutsk
Tulun,Tulun,54.56533734,100.5653755,48407,Russia,RU,RUS,Irkutsk
Nizhneudinsk,Nizhneudinsk,54.89766848,99.02769161,41024.5,Russia,RU,RUS,Irkutsk
Ust Kut,Ust Kut,56.76497052,105.7599939,25388,Russia,RU,RUS,Irkutsk
Bodaybo,Bodaybo,57.96497479,114.3289799,15933,Russia,RU,RUS,Irkutsk
Komsa,Komsa,61.86804405,89.25774532,10,Russia,RU,RUS,Krasnoyarsk
Kansk,Kansk,56.19001853,95.71001298,94420.5,Russia,RU,RUS,Krasnoyarsk
Achinsk,Achinsk,56.26998781,90.49999508,112541.5,Russia,RU,RUS,Krasnoyarsk
Yeniseysk,Yeniseysk,58.4515084,92.15653479,15407.5,Russia,RU,RUS,Krasnoyarsk
Lesosibirsk,Lesosibirsk,58.24325238,92.48328487,65629,Russia,RU,RUS,Krasnoyarsk
Turukhansk,Turukhansk,65.83816347,87.95498246,4774,Russia,RU,RUS,Krasnoyarsk
Vorontsovo,Vorontsovo,71.69832257,83.56419104,100,Russia,RU,RUS,Taymyr
Starorybnoye,Starorybnoye,72.76660362,104.8000008,10,Russia,RU,RUS,Taymyr
Mikhaylova,Mikhaylova,75.09498863,86.98243201,10,Russia,RU,RUS,Taymyr
Dudinka,Dudinka,69.41820335,86.22501054,22913,Russia,RU,RUS,Taymyr
Teli,Teli,51.03330487,90.23329301,3732,Russia,RU,RUS,Tuva
Novyy Uoyin,Novyy Uoyin,56.13498313,111.7338928,4184,Russia,RU,RUS,Buryat
Bagdarin,Bagdarin,54.43330406,113.6000321,4676,Russia,RU,RUS,Buryat
Severobaykalsk,Severobaykalsk,55.63400596,109.3129553,25800,Russia,RU,RUS,Buryat
Kyakhta,Kyakhta,50.35267458,106.4526648,12368,Russia,RU,RUS,Buryat
Svobodnyy,Svobodnyy,51.40617617,128.1311865,62318.5,Russia,RU,RUS,Amur
Zeya,Zeya,53.75001243,127.2665881,26999,Russia,RU,RUS,Amur
Magdagachi,Magdagachi,53.44997906,125.8000109,8070.5,Russia,RU,RUS,Amur
Shimanovsk,Shimanovsk,52.00244468,127.6974662,16574.5,Russia,RU,RUS,Amur
Skovorodino,Skovorodino,53.98330568,123.9166634,6485.5,Russia,RU,RUS,Amur
Tynda,Tynda,55.17426658,124.7075712,33187,Russia,RU,RUS,Amur
Olovyannaya,Olovyannaya,50.94997662,115.5666304,5281.5,Russia,RU,RUS,Chita
Mogocha,Mogocha,53.73332094,119.7665808,10636.5,Russia,RU,RUS,Chita
Krasnokamensk,Krasnokamensk,50.0664905,118.0264803,52308,Russia,RU,RUS,Chita
Borzya,Borzya,50.38856386,116.518562,29653,Russia,RU,RUS,Chita
Khilok,Khilok,51.35000389,110.4500435,6540.5,Russia,RU,RUS,Chita
Nakhodka,Nakhodka,42.83744855,132.8874336,153235.5,Russia,RU,RUS,Primor'ye
Ussuriysk,Ussuriysk,43.80002545,132.019993,140673.5,Russia,RU,RUS,Primor'ye
Lesozavodsk,Lesozavodsk,45.47475527,133.4297778,39241.5,Russia,RU,RUS,Primor'ye
Kavache,Kavache,70.73329104,136.2166361,-99,Russia,RU,RUS,Sakha (Yakutia)
Verkhoyansk,Verkhoyansk,67.54470013,133.3849743,1388,Russia,RU,RUS,Sakha (Yakutia)
Cherskiy,Cherskiy,68.75005292,161.3300386,3707,Russia,RU,RUS,Sakha (Yakutia)
Srednekolymsk,Srednekolymsk,67.45000307,153.7100386,3459,Russia,RU,RUS,Sakha (Yakutia)
Zyryanka,Zyryanka,65.73597333,150.890004,3627,Russia,RU,RUS,Sakha (Yakutia)
Eldikan,Eldikan,60.80002138,135.1833142,1516,Russia,RU,RUS,Sakha (Yakutia)
Chagda,Chagda,60.10001243,133.8999816,10,Russia,RU,RUS,Sakha (Yakutia)
Khandyga,Khandyga,62.66600568,135.6000329,6796,Russia,RU,RUS,Sakha (Yakutia)
Ust Maya,Ust Maya,60.45657981,134.5433016,3062,Russia,RU,RUS,Sakha (Yakutia)
Neryungri,Neryungri,56.67404584,124.7103617,33364,Russia,RU,RUS,Sakha (Yakutia)
Chernyshevskiy,Chernyshevskiy,63.01275454,112.4714188,5137,Russia,RU,RUS,Sakha (Yakutia)
Terbyas,Terbyas,64.37608217,120.5468949,10,Russia,RU,RUS,Sakha (Yakutia)
Vilyuysk,Vilyuysk,63.75526735,121.6247619,5543.5,Russia,RU,RUS,Sakha (Yakutia)
Sangar,Sangar,63.92414593,127.4739139,4633,Russia,RU,RUS,Sakha (Yakutia)
Menkere,Menkere,67.98860069,123.3504964,10,Russia,RU,RUS,Sakha (Yakutia)
Saskylakh,Saskylakh,71.91662966,114.0833101,1920,Russia,RU,RUS,Sakha (Yakutia)
Govorovo,Govorovo,70.21135907,125.9932808,943,Russia,RU,RUS,Sakha (Yakutia)
Sagastyr,Sagastyr,73.37793312,126.5923521,10,Russia,RU,RUS,Sakha (Yakutia)
Ust Olensk,Ust Olensk,72.99778302,119.7729295,10,Russia,RU,RUS,Sakha (Yakutia)
Suntar,Suntar,62.14440961,117.6319307,4716,Russia,RU,RUS,Sakha (Yakutia)
Olenek,Olenek,68.52500205,112.4500248,10,Russia,RU,RUS,Sakha (Yakutia)
Udachnyy,Udachnyy,66.42316652,112.3965397,15266,Russia,RU,RUS,Sakha (Yakutia)
Birobidzhan,Birobidzhan,48.79742067,132.9507889,75022.5,Russia,RU,RUS,Yevrey
Khakhar,Khakhar,57.66659507,135.4300175,10,Russia,RU,RUS,Khabarovsk
De Kastri,De Kastri,51.46658592,140.7833341,3615,Russia,RU,RUS,Khabarovsk
Chumikan,Chumikan,54.7113945,135.3145141,1305,Russia,RU,RUS,Khabarovsk
Komsomolsk na Amure,Komsomolsk na Amure,50.55498781,137.0199979,264374,Russia,RU,RUS,Khabarovsk
Ayan,Ayan,56.45424113,138.1673305,1286,Russia,RU,RUS,Khabarovsk
Nikolayevsk na Amure,Nikolayevsk na Amure,53.14963564,140.730004,27113,Russia,RU,RUS,Khabarovsk
Savetskaya Gavan,Savetskaya Gavan,48.96989077,140.2748897,27882,Russia,RU,RUS,Khabarovsk
Evensk,Evensk,61.94997703,159.2333191,2024,Russia,RU,RUS,Maga Buryatdan
Palatka,Palatka,60.10001243,150.8999776,12993,Russia,RU,RUS,Maga Buryatdan
Omsukchan,Omsukchan,62.53327476,155.8000402,4201,Russia,RU,RUS,Maga Buryatdan
Susuman,Susuman,62.78333701,148.1667594,7367,Russia,RU,RUS,Maga Buryatdan
Nogliki,Nogliki,51.83328188,143.1667028,10098,Russia,RU,RUS,Sakhalin
Aleksandrovsk Sakhalinskiy,Aleksandrovsk Sakhalinskiy,50.89749921,142.1561185,9263.5,Russia,RU,RUS,Sakhalin
Korsakov,Korsakov,46.64243593,142.777476,33165.5,Russia,RU,RUS,Sakhalin
Manily,Manily,62.54999208,165.3000288,10,Russia,RU,RUS,Kamchatka
Oktyabrskiy,Oktyabrskiy,52.66359296,156.2387215,67386,Russia,RU,RUS,Kamchatka
Klyuchi,Klyuchi,56.29996014,160.8500162,1089,Russia,RU,RUS,Kamchatka
Ust Kamchatsk,Ust Kamchatsk,56.21350547,162.4349841,4939,Russia,RU,RUS,Kamchatka
Provideniya,Provideniya,64.4234953,-173.2257937,1746.5,Russia,RU,RUS,Chukchi Autonomous Okrug
Uelen,Uelen,66.15413931,-169.8105835,776,Russia,RU,RUS,Chukchi Autonomous Okrug
Kandalaksha,Kandalaksha,67.16433575,32.41439327,72614.5,Russia,RU,RUS,Murmansk
Vyborg,Vyborg,60.70387738,28.75492672,97917,Russia,RU,RUS,Leningrad
Kondopoga,Kondopoga,62.20872093,34.28869747,31952,Russia,RU,RUS,Karelia
Rusanovo,Rusanovo,70.59807362,56.37229099,10,Russia,RU,RUS,Arkhangel'sk
Mezen,Mezen,65.85221946,44.24002803,2460.5,Russia,RU,RUS,Arkhangel'sk
Velsk,Velsk,61.06739524,42.0974198,25729,Russia,RU,RUS,Arkhangel'sk
Kotlas,Kotlas,61.26306805,46.66308427,59529.5,Russia,RU,RUS,Arkhangel'sk
Onega,Onega,63.92714317,38.0771484,20447.5,Russia,RU,RUS,Arkhangel'sk
Ivanovo,Ivanovo,57.01002016,41.00999263,417527,Russia,RU,RUS,Ivanovo
Kostroma,Kostroma,57.77002545,40.94002274,256955.5,Russia,RU,RUS,Kostroma
Velikiy Ustyug,Velikiy Ustyug,60.76870546,46.29866207,32939.5,Russia,RU,RUS,Vologda
Lipetsk,Lipetsk,52.62000389,39.63999874,502144,Russia,RU,RUS,Lipetsk
Orel,Orel,52.96995668,36.06998409,329376,Russia,RU,RUS,Orel
Volgodonsk,Volgodonsk,47.50997988,42.15994828,122434.5,Russia,RU,RUS,Rostov
Belgorod,Belgorod,50.62999615,36.5999259,328004.5,Russia,RU,RUS,Belgorod
Novorossiysk,Novorossiysk,44.72996869,37.76993201,229927,Russia,RU,RUS,Krasnodar
Vladimir,Vladimir,56.12997052,40.4099259,314336,Russia,RU,RUS,Vladimir
Birsk,Birsk,55.42438051,55.54435095,33903,Russia,RU,RUS,Bashkortostan
Zlatoust,Zlatoust,55.17499005,59.64999182,176285,Russia,RU,RUS,Chelyabinsk
Amderma,Amderma,69.76301434,61.66769812,282,Russia,RU,RUS,Nenets
Naryan Mar,Naryan Mar,67.64740704,53.05742265,19849.5,Russia,RU,RUS,Nenets
Inta,Inta,66.03742779,60.16742794,12410.5,Russia,RU,RUS,Komi
Usinsk,Usinsk,65.92304201,57.40299719,42913.5,Russia,RU,RUS,Komi
Pechora,Pechora,65.15874758,57.20874548,45957,Russia,RU,RUS,Komi
Pervouralsk,Pervouralsk,56.91002626,59.9550378,127236,Russia,RU,RUS,Sverdlovsk
Izhevsk,Izhevsk,56.85002993,53.23002193,611230,Russia,RU,RUS,Udmurt
Akhtubinsk,Akhtubinsk,48.27871848,46.16869584,38179,Russia,RU,RUS,Astrakhan'
Elista,Elista,46.32865664,44.20871212,99728,Russia,RU,RUS,Kalmyk
Krasnoarmeysk,Krasnoarmeysk,51.01738853,45.69740678,20625.5,Russia,RU,RUS,Saratov
Berezniki,Berezniki,59.42000226,56.75998734,153305,Russia,RU,RUS,Perm'
Naltchik,Naltchik,43.4981059,43.61794714,290333,Russia,RU,RUS,Kabardin-Balkar
Stavropol,Stavropol,45.05000083,41.98001094,350795.5,Russia,RU,RUS,Stavropol'
Ugolnye Kopi,Ugolnyye Kopi,64.73329551,177.6999955,3367,Russia,RU,RUS,Chukchi Autonomous Okrug
Kaliningrad,Kaliningrad,54.70000612,20.49734289,403226.5,Russia,RU,RUS,Kaliningrad
Pskov,Pskov,57.82999595,28.32993974,189979.5,Russia,RU,RUS,Pskov
Bryansk,Bryansk,53.25999066,34.42998083,426510,Russia,RU,RUS,Bryansk
Smolensk,Smolensk,54.78268841,32.04733557,311954.5,Russia,RU,RUS,Smolensk
Petrozavodsk,Petrozavodsk,61.84998313,34.28001583,248350.5,Russia,RU,RUS,Karelia
Tver,Tver,56.85997764,35.88999508,382043,Russia,RU,RUS,Tver'
Vologda,Vologda,59.20998924,39.91998165,251692,Russia,RU,RUS,Vologda
Yaroslavl,Yaroslavl,57.61998293,39.87001054,571154,Russia,RU,RUS,Yaroslavl'
Rostov,Rostov,47.23464785,39.7126558,1032567,Russia,RU,RUS,Rostov
Sochi,Sochi,43.59001243,39.72996741,326639,Russia,RU,RUS,Krasnodar
Krasnodar,Krasnodar,45.01997683,39.0000378,601191.5,Russia,RU,RUS,Krasnodar
Penza,Penza,53.18002138,44.99998165,491943,Russia,RU,RUS,Penza
Ryazan,Ryazan,54.61995933,39.71999385,502373,Russia,RU,RUS,Ryazan'
Voronezh,Voronezh,51.72998069,39.26999548,569734.5,Russia,RU,RUS,Voronezh
Magnitogorsk,Magnitogorsk,53.42269391,58.98000688,308724.5,Russia,RU,RUS,Chelyabinsk
Chelyabinsk,Chelyabinsk,55.15499127,61.43866817,1018802,Russia,RU,RUS,Chelyabinsk
Vorkuta,Vorkuta,67.50000002,64.00998409,71261.5,Russia,RU,RUS,Komi
Kirov,Kirov,58.59005292,49.66998083,457410,Russia,RU,RUS,Kirov
Nizhny Tagil,Nizhny Tagil,57.9200163,59.9749849,374343.5,Russia,RU,RUS,Sverdlovsk
Astrakhan,Astrakhan,46.34865541,48.05498897,493363.5,Russia,RU,RUS,Astrakhan'
Orenburg,Orenburg,51.77997764,55.11001054,530820.5,Russia,RU,RUS,Orenburg
Saratov,Saratov,51.57998985,46.0299963,814586.5,Russia,RU,RUS,Saratov
Ulyanovsk,Ulyanovsk,54.32997703,48.41000606,571553.5,Russia,RU,RUS,Ul'yanovsk
Omsk,Omsk,54.98998842,73.39995357,1089201.5,Russia,RU,RUS,Omsk
Tyumen,Tyumen,57.14001223,65.52999467,460952,Russia,RU,RUS,Tyumen'
Novokuznetsk,Novokuznetsk,53.75001243,87.11498205,530325.5,Russia,RU,RUS,Kemerovo
Kemerovo,Kemerovo,55.33996706,86.08998002,470684.5,Russia,RU,RUS,Kemerovo
Groznyy,Groznyy,43.31868532,45.69869869,221237.5,Russia,RU,RUS,Chechnya
Ust-Ulimsk,Ust-Ulimsk,57.98996035,102.6333113,68812,Russia,RU,RUS,Irkutsk
Angarsk,Angarsk,52.56000755,103.9200028,231719,Russia,RU,RUS,Irkutsk
Abakan,Abakan,53.70368451,91.44500199,161377,Russia,RU,RUS,Krasnoyarsk
Norilsk,Norilsk,69.34001691,88.22499182,153336.5,Russia,RU,RUS,Taymyr
Khatanga,Khatanga,72.04114402,102.4650012,3205,Russia,RU,RUS,Taymyr
Kyzyl,Kyzyl,51.70670046,94.38306555,106310.5,Russia,RU,RUS,Tuva
Ulan Ude,Ulan Ude,51.82498781,107.6249963,354127,Russia,RU,RUS,Buryat
Blagoveshchensk,Blagoveshchensk,50.26660748,127.5333418,206711,Russia,RU,RUS,Amur
Bukachacha,Bukachacha,52.98334088,116.9166255,1934.5,Russia,RU,RUS,Chita
Dalnegorsk,Dalnegorsk,44.5372156,135.5172473,8123,Russia,RU,RUS,Primor'ye
Ambarchik,Ambarchik,69.65100568,162.3335949,0,Russia,RU,RUS,Sakha (Yakutia)
Batagay,Batagay,67.65598533,134.6350272,4266,Russia,RU,RUS,Sakha (Yakutia)
Chokurdakh,Chokurdakh,70.61831097,147.8945796,2506,Russia,RU,RUS,Sakha (Yakutia)
Ust Nera,Ust Nera,64.56658734,143.1999825,9148,Russia,RU,RUS,Sakha (Yakutia)
Lensk,Lensk,60.72527142,114.94703,24641.5,Russia,RU,RUS,Sakha (Yakutia)
Aldan,Aldan,58.60299786,125.38939,18571.5,Russia,RU,RUS,Sakha (Yakutia)
Mirnyy,Mirnyy,62.54001853,113.9613537,30535.5,Russia,RU,RUS,Sakha (Yakutia)
Zhigansk,Zhigansk,66.76970868,123.3711153,3237,Russia,RU,RUS,Sakha (Yakutia)
Okhotsk,Okhotsk,59.38300193,143.2170357,5570,Russia,RU,RUS,Khabarovsk
Khabarovsk,Khabarovsk,48.4549868,135.1200105,562705.5,Russia,RU,RUS,Khabarovsk
Okha,Okha,53.57389915,142.9478531,25461,Russia,RU,RUS,Sakhalin
Yuzhno Sakhalinsk,Yuzhno Sakhalinsk,46.96497438,142.7400105,174685,Russia,RU,RUS,Sakhalin
Tomsk,Tomsk,56.494987,84.97500932,471950,Russia,RU,RUS,Tomsk
Anadyr,Anadyr,64.73699038,177.4749963,10332,Russia,RU,RUS,Chukchi Autonomous Okrug
Murmansk,Murmansk,68.96998781,33.10003617,271758,Russia,RU,RUS,Murmansk
Archangel,Archangel,64.57495892,40.5450081,295186.5,Russia,RU,RUS,Arkhangel'sk
Nizhny Novgorod,Nizhny Novgorod,56.33300722,44.00009436,1246463,Russia,RU,RUS,Nizhegorod
Volgograd,Volgograd,48.71000999,44.49996049,801827.5,Russia,RU,RUS,Volgograd
Ufa,Ufa,54.78997479,56.04003129,969378,Russia,RU,RUS,Bashkortostan
Yekaterinburg,Yekaterinburg,56.85002993,60.59995967,1270488,Russia,RU,RUS,Sverdlovsk
Samara,Samara,53.19500755,50.15129512,996595,Russia,RU,RUS,Samara
Kazan,Kazan,55.74994204,49.12634477,1013635,Russia,RU,RUS,Tatarstan
Surgut,Surgut,61.25994163,73.42501664,353351.5,Russia,RU,RUS,Khanty-Mansiy
Barnaul,Barnaul,53.35499778,83.74500688,569711,Russia,RU,RUS,Altay
Novosibirsk,Novosibirsk,55.02996014,82.96004187,1213100.5,Russia,RU,RUS,Novosibirsk
Bratsk,Bratsk,56.15699729,101.6150272,133905,Russia,RU,RUS,Irkutsk
Irkutsk,Irkutsk,52.31997052,104.2450476,572325,Russia,RU,RUS,Irkutsk
Krasnoyarsk,Krasnoyarsk,56.01398277,92.86600053,613605,Russia,RU,RUS,Krasnoyarsk
Dickson,Dickson,73.50697186,80.54509884,1113,Russia,RU,RUS,Taymyr
Chita,Chita,52.05502545,113.4650016,293153.5,Russia,RU,RUS,Chita
Vladivostok,Vladivostok,43.13001467,131.9100256,586617,Russia,RU,RUS,Primor'ye
Nizhneyansk,Nizhneyansk,71.43332583,136.0666194,395.5,Russia,RU,RUS,Sakha (Yakutia)
Yakutsk,Yakutsk,62.03495892,129.7350162,220813,Russia,RU,RUS,Sakha (Yakutia)
Tiksi,Tiksi,71.62688552,128.8349668,5700,Russia,RU,RUS,Sakha (Yakutia)
Magadan,Magadan,59.57497988,150.8100089,91221.5,Russia,RU,RUS,Maga Buryatdan
Perm,Perm,57.99995974,56.24999263,924154,Russia,RU,RUS,Perm'
Palana,Palana,59.08400209,159.9500195,3671,Russia,RU,RUS,Kamchatka
Petropavlovsk Kamchatskiy,Petropavlovsk Kamchatskiy,53.06199241,158.6230204,182270.5,Russia,RU,RUS,Kamchatka
St. Petersburg,St. Petersburg,59.93901451,30.31602006,4023106,Russia,RU,RUS,City of St. Petersburg
Moscow,Moscow,55.75216412,37.61552283,10452000,Russia,RU,RUS,Moskva
Gikongoro,Gikongoro,-2.483297945,29.5667016,15000,Rwanda,RW,RWA,Southern
Kibuye,Kibuye,-2.050001985,29.34999959,48024,Rwanda,RW,RWA,Western
Kibungo,Kibungo,-2.166695932,30.53330158,46240,Rwanda,RW,RWA,Eastern
Nyanza,Nyanza,-2.349586569,29.74003454,225209,Rwanda,RW,RWA,Southern
Gitarama,Gitarama,-2.069603659,29.75998165,87613,Rwanda,RW,RWA,Southern
Butare,Butare,-2.589623597,29.73000932,77000,Rwanda,RW,RWA,Southern
Gisenyi,Gisenyi,-1.684665915,29.26290605,83623,Rwanda,RW,RWA,Western
Cyangugu,Cyangugu,-2.479604473,28.89998246,19900,Rwanda,RW,RWA,Western
Byumba,Byumba,-1.579556052,30.06001501,70593,Rwanda,RW,RWA,Northern
Ruhengeri,Ruhengeri,-1.499612611,29.63001542,86685,Rwanda,RW,RWA,Northern
Kigali,Kigali,-1.953590069,30.06053178,802630.5,Rwanda,RW,RWA,Kigali City
Basseterre,Basseterre,17.30203046,-62.71700932,18693.5,Saint Kitts and Nevis,KN,KNA,
Castries,Castries,14.00197349,-61.00000818,24298.5,Saint Lucia,LC,LCA,
Kingstown,Kingstown,13.14827883,-61.21206242,37001.5,Saint Vincent and the Grenadines,VC,VCT,
Apia,Apia,-13.84154504,-171.7386416,49812,Samoa,WS,WSM,
San Marino,San Marino,43.91715008,12.46667029,29289.5,San Marino,SM,SMR,
Santo Antonio,Santo Antonio,1.645002051,7.412004483,1156,Sao Tome and Principe,ST,STP,
Sao Tome,Sao Tome,0.333402119,6.733325153,72192.5,Sao Tome and Principe,ST,STP,
An Nabk,An Nabk,31.33330205,37.33329653,7500,Saudi Arabia,SA,SAU,Al Jawf
Sakakah,Sakakah,29.99999706,40.13330454,128332,Saudi Arabia,SA,SAU,Al Jawf
Yanbu al Bahr,Yanbu al Bahr,24.09427736,38.0492948,233875.5,Saudi Arabia,SA,SAU,Al Madinah
Dawmat al Jandal,Dawmat al Jandal,29.81529767,39.86639319,22583,Saudi Arabia,SA,SAU,Al Jawf
Qal at Bishah,Qal at Bishah,20.00868695,42.59868119,85059.5,Saudi Arabia,SA,SAU,`Asir
At Taif,At Taif,21.26222801,40.38227901,594065,Saudi Arabia,SA,SAU,Makkah
Najran,Najran,17.50653994,44.1315592,314091,Saudi Arabia,SA,SAU,Najran
Al Quwayiyah,Al Quwayiyah,24.07371014,45.28063635,8712,Saudi Arabia,SA,SAU,Ar Riyad
Al Hillah,Al Hillah,23.4894564,46.75636023,594605,Saudi Arabia,SA,SAU,Ar Riyad
Al Mubarraz,Al Mubarraz,25.42905377,49.5659045,294682,Saudi Arabia,SA,SAU,Ash Sharqiyah
Al-Qatif,Al-Qatif,26.5196332,50.01151037,233575.5,Saudi Arabia,SA,SAU,Ash Sharqiyah
Az Zahran,Az Zahran,26.29143007,50.15832312,54373,Saudi Arabia,SA,SAU,Ash Sharqiyah
Buraydah,Buraydah,26.36638674,43.96283565,394958.5,Saudi Arabia,SA,SAU,Al Quassim
Hail,Hail,27.52357709,41.70007971,385257,Saudi Arabia,SA,SAU,Ha'il
Arar,Arar,30.99000633,41.02068966,185278,Saudi Arabia,SA,SAU,Al Hudud ash Shamaliyah
Rafha,Rafha,29.62021914,43.4948022,64755,Saudi Arabia,SA,SAU,Al Hudud ash Shamaliyah
Al Kharj,Al Kharj,24.15556561,47.3120369,298428,Saudi Arabia,SA,SAU,Ar Riyad
Ad Damman,Ad Damman,26.42819175,50.09967037,1411656,Saudi Arabia,SA,SAU,Ash Sharqiyah
Hafar al Batin,Hafar al Batin,28.43365074,45.96007808,249194,Saudi Arabia,SA,SAU,Ash Sharqiyah
Al Jubayl,Al Jubayl,27.00464235,49.64600297,235237,Saudi Arabia,SA,SAU,Ash Sharqiyah
Al Qunfudhah,Al Qunfudhah,19.12636354,41.07887732,157,Saudi Arabia,SA,SAU,Makkah
Al Hufuf,Al Hufuf,25.3487486,49.58559322,518694.5,Saudi Arabia,SA,SAU,Ash Sharqiyah
Al Wajh,Al Wajh,26.23241559,36.4635518,34936.5,Saudi Arabia,SA,SAU,Tabuk
Abha,Abha,18.2300875,42.50013424,207802.5,Saudi Arabia,SA,SAU,`Asir
Jizan,Jizan,16.90655072,42.5565649,100397,Saudi Arabia,SA,SAU,Jizan
As Sulayyil,As Sulayyil,20.462251,45.57224646,20858.5,Saudi Arabia,SA,SAU,Ar Riyad
Medina,Medina,24.49998903,39.5800024,1010000,Saudi Arabia,SA,SAU,Al Madinah
Tabuk,Tabuk,28.38383465,36.55496741,501703.5,Saudi Arabia,SA,SAU,Tabuk
Jeddah,Jeddah,21.51688946,39.21919755,2939723,Saudi Arabia,SA,SAU,Makkah
Makkah,Makkah,21.43002138,39.82003943,1354312,Saudi Arabia,SA,SAU,Makkah
Riyadh,Riyadh,24.64083315,46.77274166,4335480.5,Saudi Arabia,SA,SAU,Ar Riyad
Fatick,Fatick,14.3440021,-16.41599952,24243,Senegal,SM,SEN,Fatick
Diourbel,Diourbel,14.66038291,-16.24000126,148024,Senegal,SM,SEN,Diourbel
Louga,Louga,15.61037661,-16.25000065,85075,Senegal,SM,SEN,Louga
Thies,Thies,14.8103996,-16.93001083,293001,Senegal,SM,SEN,Thi?s
Kolda,Kolda,12.91043805,-14.95002832,64038,Senegal,SM,SEN,Kolda
Tambacounda,Tambacounda,13.78035911,-13.68002832,89212,Senegal,SM,SEN,Tambacounda
Kedougou,Kedougou,12.56043357,-12.17999068,18074,Senegal,SM,SEN,Tambacounda
Ziguinchor,Ziguinchor,12.58999249,-16.28999821,175747,Senegal,SM,SEN,Ziguinchor
Kaolack,Kaolack,14.14997479,-16.10000981,277812,Senegal,SM,SEN,Kaolack
Kaedi,Kaedi,16.15000775,-13.49998763,21656,Senegal,SM,SEN,Matam
Dakar,Dakar,14.71583173,-17.47313013,2540200,Senegal,SM,SEN,Dakar
Subotica,Subotica,46.07001609,19.68002844,96704,Serbia,RS,SRB,Severno-Backi
Kragujevac,Kragujevac,44.01996035,20.92000443,159335,Serbia,RS,SRB,?umadijski
Zrenjanin,Zrenjanin,45.3786371,20.39946773,64053,Serbia,RS,SRB,Srednje-Banatski
Pec,Pec,43.88973574,20.33011796,137332.5,Serbia,RS,SRB,Moravicki
Nis,Nis,43.33041587,21.8999963,230444,Serbia,RS,SRB,Ni?avski
Novi Sad,Novi Sad,45.2503762,19.84994055,220428.5,Serbia,RS,SRB,Ju?no-Backi
Belgrade,Belgrade,44.81864545,20.46799068,1099000,Serbia,RS,SRB,Grad Beograd
Victoria,Victoria,-4.616631654,55.44998979,28228.5,Seychelles,SC,SYC,
Makeni,Makeni,8.880425638,-12.04997278,83116,Sierra Leone,SL,SLE,Northern
Koidu,Koidu,8.440478331,-10.84999435,45307.5,Sierra Leone,SL,SLE,Eastern
Kenema,Kenema,7.880409158,-11.18997359,133918.5,Sierra Leone,SL,SLE,Eastern
Bo,Bo,7.970016092,-11.74001754,170690.5,Sierra Leone,SL,SLE,Southern
Freetown,Freetown,8.470011412,-13.23421574,420384,Sierra Leone,SL,SLE,Western
Singapore,Singapore,1.293033466,103.8558207,4236614.5,Singapore,SG,SGP,
Banska Bystrica,Banska Bystrica,48.73329022,19.14998328,80784,Slovakia,SK,SVK,Banskobystrick?
Trnava,Trnava,48.36659426,17.60000036,60919,Slovakia,SK,SVK,Trnavsk?
Zvolen,Zvolen,48.58373863,19.13324011,38276.5,Slovakia,SK,SVK,Banskobystrick?
Zilina,Zilina,49.21982383,18.74938757,86805,Slovakia,SK,SVK,?ilinsk?
Kosice,Kosice,48.73044802,21.25001013,210316.5,Slovakia,SK,SVK,Ko?ick?
Presov,Presov,48.99973391,21.23936479,85368.5,Slovakia,SK,SVK,Pre?ov
Bratislava,Bratislava,48.15001833,17.11698075,398712,Slovakia,SK,SVK,Bratislavsk?
Maribor,Maribor,46.54047833,15.65004187,101642,Slovenia,SI,SVN,Maribor
Ljubljana,Ljubljana,46.05528831,14.51496903,284961,Slovenia,SI,SVN,Osrednjeslovenska
Gizo,Gizo,-8.09962319,156.8350158,6154,Solomon Islands,SB,SLB,Choiseul
Lata,Lata,-10.73801832,165.8567353,553,Solomon Islands,SB,SLB,Temotu
Honiara,Honiara,-9.437994295,159.9497657,66313,Solomon Islands,SB,SLB,Guadalcanal
Hudur,Xuddur,4.183298973,43.86670261,1639,Somalia,SO,SOM,Bakool
Garbahaarey,Garbahaarey,3.327003116,42.22700164,12652,Somalia,SO,SOM,Gedo
Bu'aale,Bu'aale,1.083303017,42.58330253,1490,Somalia,SO,SOM,Jubbada Dhexe
Dhuusa Mareeb,Dhuusa Mareeb,5.741999984,46.5080045,447,Somalia,SO,SOM,Galguduud
Buurhakaba,Buurhakaba,2.783717671,44.08329342,29529.5,Somalia,SO,SOM,Bay
Luuq,Luuq,3.800477314,42.55000199,33820,Somalia,SO,SOM,Gedo
Mandera,Mandera,3.940442931,41.86001827,44480.5,Somalia,SO,SOM,Gedo
Ferfer,Ferfer,5.085411803,45.16503617,5205.5,Somalia,SO,SOM,Hiiraan
Jawhar,Jawhar,2.767000345,45.51659094,86654,Somalia,SO,SOM,Shabeellaha Dhexe
Hurdiyo,Hurdiyo,10.5820272,51.12332882,176,Somalia,SO,SOM,Bari
Qardho,Qardho,9.500413634,49.16598059,1341,Somalia,SO,SOM,Bari
Caluula,Caluula,11.96695559,50.75001827,513,Somalia,SO,SOM,Bari
Buur Gaabo,Buur Gaabo,-1.200869868,41.85195979,3096,Somalia,SO,SOM,Jubbada Hoose
Baydhabo,Baydhabo,3.119976216,43.64998653,128830,Somalia,SO,SOM,Bay
Marka,Marka,1.776569843,44.85327226,1958,Somalia,SO,SOM,Shabeellaha Hoose
Mereeg,Mereeg,3.766577575,47.2999963,548,Somalia,SO,SOM,Galguduud
Beledweyne,Beledweyne,4.739980691,45.20002112,59177.5,Somalia,SO,SOM,Hiiraan
Boosaaso,Boosaaso,11.28002077,49.1799849,46969,Somalia,SO,SOM,Bari
Bandarbeyla,Bandarbeyla,9.483308735,50.81668087,13753,Somalia,SO,SOM,Bari
Gaalkacyo,Gaalkacyo,6.769960143,47.4300142,57350.5,Somalia,SO,SOM,Mudug
Eyl,Eyl,7.983348611,49.83327836,9636.5,Somalia,SO,SOM,Nugaal
Garoowe,Garoowe,8.399989847,48.50002641,2568,Somalia,SO,SOM,Nugaal
Jamaame,Jamaame,0.072177754,42.75055823,156923.5,Somalia,SO,SOM,Jubbada Hoose
Kismaayo,Kismaayo,-0.356633282,42.51832434,184901.5,Somalia,SO,SOM,Jubbada Hoose
Mogadishu,Mogadishu,2.066681334,45.36667761,987694,Somalia,SO,SOM,Banaadir
Laascaanood,Laascaanood,8.43329714,47.31669964,60100,Somaliland,,SOL,
Ceerigaabo,Ceerigaabo,10.58329807,47.33330461,165000,Somaliland,,SOL,
Boorama,Boorama,9.940412617,43.18004106,67664,Somaliland,-99,SOL,
Burco,Burco,9.520386575,45.54000037,102931.5,Somaliland,-99,SOL,
Maydh,Maydh,10.98009076,47.09752803,30000,Somaliland,-99,SOL,
Berbera,Berbera,10.43555035,45.01641475,178407,Somaliland,-99,SOL,
Hargeysa,Hargeysa,9.560022399,44.06531002,362447,Somaliland,-99,SOL,
Qacha's Nek,Qacha's Nek,-30.11726692,28.70199951,25573,South Africa,ZA,ZAF,Eastern Cape
Colesberg,Colesberg,-30.71953449,25.10000769,7491,South Africa,ZA,ZAF,Northern Cape
Poffader,Poffader,-29.13291299,19.38335404,4220,South Africa,ZA,ZAF,Northern Cape
Carnarvon,Carnarvon,-30.94959796,22.13331539,5785,South Africa,ZA,ZAF,Northern Cape
Prieska,Prieska,-29.65954751,22.73002315,7640.5,South Africa,ZA,ZAF,Northern Cape
Kuruman,Kuruman,-27.4495532,23.42000688,9549.5,South Africa,ZA,ZAF,Northern Cape
Knysna,Knysna,-34.03292397,23.03331213,33887,South Africa,ZA,ZAF,Western Cape
Swellendam,Swellendam,-34.01959145,20.4300085,8954,South Africa,ZA,ZAF,Western Cape
Hermanus,Hermanus,-34.40959349,19.22992672,16274.5,South Africa,ZA,ZAF,Western Cape
Paarl,Paarl,-33.69955931,18.96002071,159791.5,South Africa,ZA,ZAF,Western Cape
Bredasdorp,Bredasdorp,-34.52953449,20.02998124,8453,South Africa,ZA,ZAF,Western Cape
Beaufort West,Beaufort West,-32.34961587,22.56998124,28070.5,South Africa,ZA,ZAF,Western Cape
Brits,Brits,-25.62961261,27.77999914,81222,South Africa,ZA,ZAF,North West
Bloemhof,Bloemhof,-27.64959267,25.59000362,10662.5,South Africa,ZA,ZAF,North West
Potchefstroom,Potchefstroom,-26.69957314,27.09998897,103741.5,South Africa,ZA,ZAF,North West
Brandfort,Brandfort,-28.69955442,26.47000159,6190,South Africa,ZA,ZAF,Orange Free State
Bethlehem,Bethlehem,-28.21958372,28.29996741,66373,South Africa,ZA,ZAF,Orange Free State
Springs,Springs,-26.26957355,28.43003699,211238.5,South Africa,ZA,ZAF,Gauteng
Volksrust,Volksrust,-27.35958453,29.88999955,25394.5,South Africa,ZA,ZAF,Mpumalanga
Mbombela,Nelspruit,-25.46962238,30.98001054,184839,South Africa,ZA,ZAF,Mpumalanga
Komatipoort,Komatipoort,-25.40957436,31.94000362,10333.5,South Africa,ZA,ZAF,Mpumalanga
Middelburg,Middelburg,-25.75963051,29.47002519,124248,South Africa,ZA,ZAF,Mpumalanga
Bethal,Bethal,-26.46961302,29.45002641,96184.5,South Africa,ZA,ZAF,Mpumalanga
Standerton,Standerton,-26.93950682,29.24001339,46057,South Africa,ZA,ZAF,Mpumalanga
Lebowakgomo,Lebowakgomo,-24.19962238,29.49999752,16852.5,South Africa,ZA,ZAF,Limpopo
Tzaneen,Tzaneen,-23.81954222,30.16998246,42099.5,South Africa,ZA,ZAF,Limpopo
Ulundi,Ulundi,-28.32960285,31.41001013,13167,South Africa,ZA,ZAF,KwaZulu-Natal
Ladysmith,Ladysmith,-28.54948606,29.7800321,47375,South Africa,ZA,ZAF,KwaZulu-Natal
Port Shepstone,Port Shepstone,-30.71953449,30.4599906,37325.5,South Africa,ZA,ZAF,KwaZulu-Natal
Ubomba,Ubomba,-27.56608356,32.08330237,564,South Africa,ZA,ZAF,KwaZulu-Natal
Cradock,Cradock,-32.19954751,25.6100024,32898,South Africa,ZA,ZAF,Eastern Cape
Uitenhage,Uitenhage,-33.75960732,25.39001583,217839,South Africa,ZA,ZAF,Eastern Cape
Port Alfred,Port Alfred,-33.59951373,26.8800024,9377,South Africa,ZA,ZAF,Eastern Cape
Grahamstown,Grahamstown,-33.29958372,26.52002437,70315.5,South Africa,ZA,ZAF,Eastern Cape
Port St. Johns,Port St. Johns,-31.62785114,29.5283162,5939,South Africa,ZA,ZAF,Eastern Cape
Aliwal North,Aliwal North,-30.68956216,26.71003861,26423,South Africa,ZA,ZAF,Eastern Cape
Queenstown,Queenstown,-31.89961749,26.8800024,96274.5,South Africa,ZA,ZAF,Eastern Cape
Benoni,Benoni,-26.14958087,28.32993974,1795672,South Africa,ZA,ZAF,Gauteng
Vereeniging,Vereeniging,-26.64960203,27.95998816,774340.5,South Africa,ZA,ZAF,Gauteng
De Aar,De Aar,-30.64997801,24.00002315,18669.5,South Africa,ZA,ZAF,Northern Cape
Alexander Bay,Alexander Bay,-28.60834552,16.50332312,1476,South Africa,ZA,ZAF,Northern Cape
Kimberley,Kimberley,-28.74683836,24.77000199,153676.5,South Africa,ZA,ZAF,Northern Cape
Oudtshoorn,Oudtshoorn,-33.58003172,22.19000443,62353,South Africa,ZA,ZAF,Western Cape
Vanhynsdorp,Vanhynsdorp,-31.61663735,18.7333162,3331,South Africa,ZA,ZAF,Western Cape
Saldanha,Saldanha,-33.01004067,17.93000606,37469,South Africa,ZA,ZAF,Western Cape
Mossel Bay,Mossel Bay,-34.17002155,22.1300081,16743,South Africa,ZA,ZAF,Western Cape
Vryburg,Vryburg,-26.96002236,24.73000443,31589,South Africa,ZA,ZAF,North West
Rustenburg,Rustenburg,-25.6500248,27.2400321,145020,South Africa,ZA,ZAF,North West
Mmabatho,Mmabatho,-25.83001382,25.6100024,90591,South Africa,ZA,ZAF,North West
Klerksdorp,Klerksdorp,-26.88002724,26.62001827,163362.5,South Africa,ZA,ZAF,North West
Kroonstad,Kroonstad,-27.66003131,27.2100081,88413.5,South Africa,ZA,ZAF,Orange Free State
Polokwane,Polokwane,-23.89002887,29.45002641,171897,South Africa,ZA,ZAF,Limpopo
Thohoyandou,Thohoyandou,-22.95003457,30.48004106,156876.5,South Africa,ZA,ZAF,Limpopo
Musina,Musina,-22.33999428,30.02999101,11848,South Africa,ZA,ZAF,Limpopo
Vryheid,Vryheid,-27.76002521,30.7899963,108364.5,South Africa,ZA,ZAF,KwaZulu-Natal
Pietermaritzburg,Pietermaritzburg,-29.61004148,30.39002071,620898,South Africa,ZA,ZAF,KwaZulu-Natal
Umtata,Umtata,-31.57999876,28.79001501,108217.5,South Africa,ZA,ZAF,Eastern Cape
Graaff Reinet,Graaff Reinet,-32.30000649,24.54004187,32958.5,South Africa,ZA,ZAF,Eastern Cape
Bhisho,Bhisho,-32.86999754,27.38999711,149142,South Africa,ZA,ZAF,Eastern Cape
Springbok,Springbok,-29.66673053,17.88329057,6623.5,South Africa,ZA,ZAF,Northern Cape
Upington,Upington,-28.46003416,21.23001135,62086,South Africa,ZA,ZAF,Northern Cape
Worcester,Worcester,-33.64002806,19.43993974,109200,South Africa,ZA,ZAF,Western Cape
George,George,-33.95003497,22.45004024,143915,South Africa,ZA,ZAF,Western Cape
Welkom,Welkom,-27.96998655,26.72998572,279011.5,South Africa,ZA,ZAF,Orange Free State
East London,East London,-32.97004311,27.87001949,338627,South Africa,ZA,ZAF,Eastern Cape
Middelburg,Middelburg,-31.50000364,25.00998734,10964,South Africa,ZA,ZAF,Eastern Cape
Bloemfontein,Bloemfontein,-29.11999388,26.22991288,459866.5,South Africa,ZA,ZAF,Orange Free State
Pretoria,Pretoria,-25.70692055,28.22942908,1338000,South Africa,ZA,ZAF,Gauteng
Port Elizabeth,Port Elizabeth,-33.97003375,25.60002885,830527,South Africa,ZA,ZAF,Eastern Cape
Durban,Durban,-29.865013,30.98001054,2729000,South Africa,ZA,ZAF,KwaZulu-Natal
Johannesburg,Johannesburg,-26.17004474,28.03000972,2730734.5,South Africa,ZA,ZAF,Gauteng
Cape Town,Cape Town,-33.92001097,18.43498816,2823929,South Africa,ZA,ZAF,Western Cape
Grytviken,Grytviken,-54.28057697,-36.50798893,99,South Georgia and the Islands,GS,SGS,
Eumseong,Eumseong,36.93525067,127.6897147,10077,South Korea,KR,KOR,Chungcheongbuk-do
Cheongju,Cheongju,36.64389895,127.5011991,719420.5,South Korea,KR,KOR,Chungcheongbuk-do
Wonju,Wonju,37.35514752,127.9396219,240898,South Korea,KR,KOR,Gangwon-do
Chuncheon,Chuncheon,37.87470237,127.7341565,218127.5,South Korea,KR,KOR,Gangwon-do
Ansan,Ansan,37.34806785,126.8595328,695110.5,South Korea,KR,KOR,Gyeonggi-do
Iksan,Iksan,35.94097027,126.9454191,261545,South Korea,KR,KOR,Jeollabuk-do
Gyeongju,Gyeongju,35.84275922,129.211689,148852.5,South Korea,KR,KOR,Daegu
Changwon,Masan,35.21910219,128.583562,1081499,South Korea,KR,KOR,Gyeongsangnam-do
Yeosu,Yeosu,34.73678021,127.7458353,302142,South Korea,KR,KOR,Gwangju
Andong,Andong,36.56591921,128.7250004,123920.5,South Korea,KR,KOR,Daegu
Jeju,Jeju,33.51013674,126.5219307,361258,South Korea,KR,KOR,Jeju
Gangneung,Gangneung,37.75587242,128.8961527,173797,South Korea,KR,KOR,Gangwon-do
Sokcho,Sokcho,38.20871299,128.5911584,85430,South Korea,KR,KOR,Gangwon-do
Jeonju,Jeonju,35.83141624,127.1403942,679948.5,South Korea,KR,KOR,Jeollabuk-do
Gunsan,Gunsan,35.98176575,126.7160215,243743,South Korea,KR,KOR,Jeollabuk-do
Mokpo,Mokpo,34.80680178,126.3958402,264210,South Korea,KR,KOR,Gwangju
Puch'on,Puch'on,37.4988889,126.7830556,866000,South Korea,KR,KOR,Gyeonggi-do
Songnam,Songnam,37.4386111,127.1377778,986967.5,South Korea,KR,KOR,Gyeonggi-do
Goyang,Goyang,37.65273586,126.8372485,903000,South Korea,KR,KOR,Gyeonggi-do
Suwon,Suwon,37.25778912,127.0108931,1078000,South Korea,KR,KOR,Gyeonggi-do
Pohang,Pohang,36.02086204,129.3715242,435266,South Korea,KR,KOR,Daegu
Ulsan,Ulsan,35.54673077,129.3169539,1011932.5,South Korea,KR,KOR,Ulsan
Daegu,Daegu,35.86678876,128.6069714,2460000,South Korea,KR,KOR,Taegu-gwangyoksi
Incheon,Incheon,37.47614789,126.6422334,2550000,South Korea,KR,KOR,Inch'on-gwangyoksi
Daejeon,Daejeon,36.33554567,127.425028,1458165,South Korea,KR,KOR,Daejeon
Gwangju,Gwangju,35.1709656,126.9104341,1428469,South Korea,KR,KOR,Kwangju-gwangyoksi
Busan,Busan,35.09505292,129.0100476,3480000,South Korea,KR,KOR,Busan
Seoul,Seoul,37.5663491,126.999731,9796000,South Korea,KR,KOR,Seoul
Bentiu,Bentiu,9.2333333,29.8333333,7653,South Sudan,SS,SSD,Unity
Maridi,Maridi,4.91511212,29.47694983,7757.5,South Sudan,SS,SSD,West Equatoria
Yei,Yei,4.090382099,30.68002885,112691,South Sudan,SS,SSD,Central Equatoria
Melut,Melut,10.43369,32.20003943,6407,South Sudan,SS,SSD,Upper Nile
Nasir,Nasir,8.600391051,33.06660152,1741,South Sudan,SS,SSD,Upper Nile
Gogrial,Gogrial,8.533728454,28.1166711,44318.5,South Sudan,SS,SSD,Warap
Kapoeta,Kapoeta,4.772123432,33.59023881,5021,South Sudan,SS,SSD,East Equatoria
Aweil,Aweil,8.766556619,27.40002234,42725,South Sudan,SS,SSD,North Bahr-al-Ghazal
Rumbek,Rumbek,6.800009988,29.68329382,17772.5,South Sudan,SS,SSD,Lakes
Yambio,Yambio,4.57053367,28.41634273,24420.5,South Sudan,SS,SSD,West Equatoria
Bor,Bor,6.207203795,31.55914831,26782,South Sudan,SS,SSD,Jungoli
Nimule,Nimule,3.599998595,32.05002274,242,South Sudan,SS,SSD,East Equatoria
Juba,Juba,4.829975198,31.58002559,111975,South Sudan,SS,SSD,Central Equatoria
Malakal,Malakal,9.536897195,31.65598995,160765,South Sudan,SS,SSD,Upper Nile
Wau,Wau,7.699980895,27.98996049,99158,South Sudan,SS,SSD,West Bahr-al-Ghazal
Merida,Merida,38.91200402,-6.337997512,52423,Spain,ES,ESP,Extremadura
Marbella,Marbella,36.51661989,-4.88333012,153069.5,Spain,ES,ESP,Andaluc?a
Linares,Linares,38.08332013,-3.633354738,49549.5,Spain,ES,ESP,Andaluc?a
Algeciras,Algeciras,36.12671215,-5.466530363,106687.5,Spain,ES,ESP,Andaluc?a
Leon,Leon,42.57997072,-5.570006553,135014,Spain,ES,ESP,Castilla y Le?n
Mataro,Mataro,41.53995668,2.45002071,149826,Spain,ES,ESP,Catalu?a
Gijon,Gijon,43.53001609,-5.670000449,303712,Spain,ES,ESP,Principado de Asturias
Vitoria,Vitoria,42.84998008,-2.669976849,199109.5,Spain,ES,ESP,Pa?s Vasco
Almeria,Almeria,36.83034751,-2.429991497,152032.5,Spain,ES,ESP,Andaluc?a
Malaga,Malaga,36.7204059,-4.419999228,539381.5,Spain,ES,ESP,Andaluc?a
Ja?n,Jaen,37.77039349,-3.799985394,92909,Spain,ES,ESP,Andaluc?a
Huelva,Huelva,37.25037355,-6.929949383,119732,Spain,ES,ESP,Andaluc?a
Albacete,Albacete,39.00034426,-1.869999839,127597,Spain,ES,ESP,Castilla-La Mancha
Toledo,Toledo,39.86703554,-4.016716351,53878.5,Spain,ES,ESP,Castilla-La Mancha
Guadalajara,Guadalajara,40.63370709,-3.166587363,51906.5,Spain,ES,ESP,Castilla-La Mancha
Santander,Santander,43.3804645,-3.799985394,196025.5,Spain,ES,ESP,Cantabria
Salamanca,Salamanca,40.97040489,-5.670000449,160456.5,Spain,ES,ESP,Castilla y Le?n
Burgos,Burgos,42.35039817,-3.67996688,150251,Spain,ES,ESP,Castilla y Le?n
Tarragona,Tarragona,41.12036989,1.249990599,107957.5,Spain,ES,ESP,Catalu?a
Lorca,Lorca,37.68856386,-1.698511598,56541.5,Spain,ES,ESP,Regi?n de Murcia
Cartagena,Cartagena,37.60042971,-0.980028322,166276.5,Spain,ES,ESP,Regi?n de Murcia
Oviedo,Oviedo,43.35049217,-5.829990683,223524.5,Spain,ES,ESP,Principado de Asturias
Santiago de Compostela,Santiago de Compostela,42.88289797,-8.541091351,87721,Spain,ES,ESP,Galicia
Badajoz,Badajoz,38.8804291,-6.96997278,115638.5,Spain,ES,ESP,Extremadura
Logrono,Logrono,42.47036501,-2.429991497,123918.5,Spain,ES,ESP,La Rioja
San Sebasti?n,San Sebastian,43.32039064,-1.979993125,270498,Spain,ES,ESP,Pa?s Vasco
Alicante,Alicante,38.3512199,-0.483640721,296345,Spain,ES,ESP,Comunidad Valenciana
Castello,Castello,39.97041424,-0.05000757,176360,Spain,ES,ESP,Comunidad Valenciana
Arrecife,Arrecife,28.96904923,-13.53783283,47182.5,Spain,ES,ESP,
Cadiz,Cadiz,36.53499086,-6.225005332,153932.5,Spain,ES,ESP,Andaluc?a
Granada,Granada,37.16497825,-3.585011435,313269,Spain,ES,ESP,Andaluc?a
Murcia,Murcia,37.9799931,-1.12996749,368322.5,Spain,ES,ESP,Regi?n de Murcia
Ceuta,Ceuta,35.88898378,-5.30699935,78674,Spain,ES,ESP,Ceuta
La Coru?a,La Coruna,43.32997662,-8.419987632,306614.5,Spain,ES,ESP,Galicia
Ourense,Ourense,42.32996014,-7.869995363,113095,Spain,ES,ESP,Galicia
Pamplona,Pamplona,42.82000775,-1.649987428,233855.5,Spain,ES,ESP,Comunidad Foral de Navarra
Valladolid,Valladolid,41.65000165,-4.750030763,299373.5,Spain,ES,ESP,Castilla y Le?n
Melilla,Melilla,35.30000165,-2.950011435,107384,Spain,ES,ESP,Melilla
Palma,Palma,39.57426271,2.65424597,319951,Spain,ES,ESP,Islas Baleares
Zaragoza,Zaragoza,41.65000165,-0.889982138,548955.5,Spain,ES,ESP,Arag?n
Santa Cruz de Tenerife,Santa Cruz de Tenerife,28.46997927,-16.25000065,279125.5,Spain,ES,ESP,
Cordoba,Cordoba,37.87999921,-4.770003704,300512,Spain,ES,ESP,Andaluc?a
Vigo,Vigo,42.22001853,-8.729994549,335848.5,Spain,ES,ESP,Galicia
Bilbao,Bilbao,43.24998151,-2.929986818,614369.5,Spain,ES,ESP,Pa?s Vasco
Las Palmas,Las Palmas,28.09997601,-15.42999902,364718,Spain,ES,ESP,
Seville,Seville,37.40501528,-5.980007366,957533,Spain,ES,ESP,Andaluc?a
Valencia,Valencia,39.48501752,-0.400012046,806652,Spain,ES,ESP,Comunidad Valenciana
Barcelona,Barcelona,41.38329958,2.183370319,3250797.5,Spain,ES,ESP,Catalu?a
Madrid,Madrid,40.40002626,-3.683351686,2808718.5,Spain,ES,ESP,Comunidad de Madrid
Trincomalee,Trincomalee,8.568999036,81.23300155,108420,Sri Lanka,LK,LKA,Trincomalee
Puttalan,Puttalan,8.033004084,79.82600454,45661,Sri Lanka,LK,LKA,Puttalam
Ratnapura,Ratnapura,6.693003132,80.38600257,47832,Sri Lanka,LK,LKA,Ratnapura
Batticaloa,Batticaloa,7.717008279,81.70001542,107982,Sri Lanka,LK,LKA,Batticaloa
Kilinochchi,Kilinochchi,9.400419738,80.39993974,64358.5,Sri Lanka,LK,LKA,Kilinochchi
Matara,Matara,5.948976663,80.5427734,68244,Sri Lanka,LK,LKA,Matara
Badulla,Badulla,6.983693867,81.0499259,44908.5,Sri Lanka,LK,LKA,Badulla
Moratuwa,Moratuwa,6.780398782,79.88002315,188595,Sri Lanka,LK,LKA,Colombo
Galle,Galle,6.030005309,80.24000118,96298,Sri Lanka,LK,LKA,Galle
Anuradhapura,Anuradhapura,8.349992898,80.38329993,89622.5,Sri Lanka,LK,LKA,Anuradhapura
Jaffna,Jaffna,9.675002461,80.00502844,169069,Sri Lanka,LK,LKA,Jaffna
Kandy,Kandy,7.279980691,80.67000077,111701,Sri Lanka,LK,LKA,Kandy
Sri Jawewardenepura Kotte,Sri Jawewardenepura Kotte,6.900003885,79.94999304,115826,Sri Lanka,LK,LKA,Colombo
Colombo,Colombo,6.931965758,79.85775061,217000,Sri Lanka,LK,LKA,Colombo
Ad Damazin,Ed Damazin,11.77040428,34.34998572,114030,Sudan,SD,SDN,Blue Nile
Haiya,Haiya,18.33623089,36.3841768,17409,Sudan,SD,SDN,Red Sea
El Manaqil,El Manaqil,14.2503821,32.97999182,140062,Sudan,SD,SDN,Gezira
Shendi,Shendi,16.68049217,33.42001664,120089.5,Sudan,SD,SDN,River Nile
Berber,Berber,18.01702557,33.98328975,35975.5,Sudan,SD,SDN,River Nile
Kerma,Kerma,19.63369692,30.4165824,3928,Sudan,SD,SDN,Northern
Ed Dueim,Ed Dueim,13.99039797,32.29998165,54825.5,Sudan,SD,SDN,White Nile
Umm Ruwaba,Umm Ruwaba,12.91043805,31.19999711,35999.5,Sudan,SD,SDN,North Kurdufan
En Nuhud,En Nuhud,12.69042564,28.42001176,84623.5,Sudan,SD,SDN,South Kordofan
Muglad,Muglad,11.03373089,27.73333533,17344,Sudan,SD,SDN,South Kordofan
Tokar,Tokar,18.43333091,37.73329342,47726,Sudan,SD,SDN,Red Sea
Medani,Medani,14.39995953,33.52001054,308540.5,Sudan,SD,SDN,Gezira
Gedaref,Gedaref,14.03998151,35.38000036,201282,Sudan,SD,SDN,Gedarif
EdDamer,EdDamer,17.58997154,33.95998368,94398.5,Sudan,SD,SDN,River Nile
Atbara,Atbara,17.70999005,33.97998246,138271,Sudan,SD,SDN,River Nile
Wadi Halfa,Wadi Halfa,21.80002464,31.34996212,17121,Sudan,SD,SDN,Northern
Merowe,Merowe,18.48330202,31.81665198,7405,Sudan,SD,SDN,Northern
Kosti,Kosti,13.16998293,32.66001135,274463,Sudan,SD,SDN,White Nile
Sennar,Sennar,13.54995974,33.60000565,103308,Sudan,SD,SDN,Sennar
El Fasher,El Fasher,13.62998069,25.35001827,220906,Sudan,SD,SDN,Northern Darfur
Kadugli,Kadugli,11.00995974,29.70003699,132298.5,Sudan,SD,SDN,South Kordufan
Babanusa,Babanusa,11.33335085,27.79999792,19700,Sudan,SD,SDN,South Kordofan
Geneina,Geneina,13.45001752,22.44001501,161145.5,Sudan,SD,SDN,West Darfur
Omdurman,Omdurman,15.61668113,32.48002234,2289428.5,Sudan,SD,SDN,Khartoum
El Obeid,El Obeid,13.18328961,30.21669796,331367.5,Sudan,SD,SDN,North Kurdufan
Port Sudan,Port Sudan,19.61579103,37.21642574,489725,Sudan,SD,SDN,Red Sea
Niyala,Niyala,12.05997316,24.88999467,392373,Sudan,SD,SDN,South Darfur
Dongola,Dongola,19.16659365,30.48329667,26404,Sudan,SD,SDN,Northern
Kassala,Kassala,15.45997235,36.39001623,370499,Sudan,SD,SDN,Kassala
Khartoum,Khartoum,15.58807823,32.53417924,3364323.5,Sudan,SD,SDN,Khartoum
Onverwacht,Onverwacht,5.599998125,-55.19999648,2105,Suriname,SR,SUR,Para
Groningen,Groningen,5.796998975,-55.48100346,3216,Suriname,SR,SUR,Saramacca
Brownsweg,Brownsweg,5.020015278,-55.1699506,3639,Suriname,SR,SUR,Brokopondo
Moengo,Moengo,5.630003885,-54.40999699,7420,Suriname,SR,SUR,Marowijne
Nieuw Amsterdam,Nieuw Amsterdam,5.909986795,-55.07000838,4935,Suriname,SR,SUR,Commewijne
Nieuw Nickerie,Nieuw Nickerie,5.950423603,-56.98999455,14567.5,Suriname,SR,SUR,Nickerie
Brokopondo,Brokopondo,5.040375792,-55.02001144,6170,Suriname,SR,SUR,Brokopondo
Totness,Totness,5.890427265,-56.31998377,1468,Suriname,SR,SUR,Coronie
Cottica,Cottica,3.850009175,-54.23328943,24605,Suriname,SR,SUR,Sipaliwini
Paramaribo,Paramaribo,5.83503013,-55.16703089,238963,Suriname,SR,SUR,Paramaribo
Longyearbyen,Longyearbyen,78.21668439,15.5499963,1232,Svalbard and Jan Mayen Islands,SJ,SJM,Svalbard
Piggs Peak,Piggs Peak,-25.96100399,31.2470015,5750,Swaziland,SZ,SWZ,Hhohho
Siteki,Siteki,-26.45499604,31.95199862,6152,Swaziland,SZ,SWZ,Lubombo
Manzini,Manzini,-26.49500106,31.3880045,110537,Swaziland,SZ,SWZ,Manzini
Hlatikulu,Hlatikulu,-26.99999993,31.41669655,2748,Swaziland,SZ,SWZ,Shiselweni
Golela,Golela,-27.29617755,31.90000606,3695,Swaziland,SZ,SWZ,Shiselweni
Lobamba,Lobamba,-26.46666746,31.19999711,7169.5,Swaziland,SZ,SWZ,Manzini
Mbabane,Mbabane,-26.31665078,31.13333451,83178,Swaziland,SZ,SWZ,Hhohho
Falun,Falun,60.61300204,15.64700455,36477,Sweden,SE,SWE,Dalarna
Nykoping,Nykoping,58.76399718,17.01500451,27582,Sweden,SE,SWE,S?dermanland
Harnosand,Harnosand,62.63399704,17.93400362,17016,Sweden,SE,SWE,V?sternorrland
Karlskrona,Karlskrona,56.20300219,15.29600461,35212,Sweden,SE,SWE,Blekinge
Mariestad,Mariestad,58.70500209,13.82799659,14891,Sweden,SE,SWE,V?stra G?taland
Vannersborg,Vannersborg,58.36300214,12.33000061,21835,Sweden,SE,SWE,V?stra G?taland
Borl?nge,Borlange,60.48332237,15.4166711,38974.5,Sweden,SE,SWE,Dalarna
V?ster?s,Vasteraas,59.63001528,16.54001339,100186.5,Sweden,SE,SWE,V?stmanland
Bolln?s,Bollnas,61.35200319,16.36658728,12771.5,Sweden,SE,SWE,G?vleborg
G?vle,Gavle,60.66698041,17.1666418,68235.5,Sweden,SE,SWE,G?vleborg
Kalmar,Kalmar,56.66701784,16.36658728,34884,Sweden,SE,SWE,Kalmar
V?xj?,Vaxjo,56.88369712,14.81670772,53067.5,Sweden,SE,SWE,Kronoberg
?rebro,Orebro,59.2803467,15.2199906,95932,Sweden,SE,SWE,Orebro
Norrk?ping,Norrkoping,58.59542727,16.17869177,85771,Sweden,SE,SWE,?sterg?tland
Halmstad,Halmstad,56.67177207,12.85558712,55433,Sweden,SE,SWE,Halland
Karlstad,Karlstad,59.36713727,13.49994055,66703.5,Sweden,SE,SWE,V?rmland
Skellefte?,Skelleftea,64.77207867,20.95002844,31075,Sweden,SE,SWE,V?sterbotten
Visby,Visby,57.63365135,18.30000932,22281.5,Sweden,SE,SWE,Gotland
Trollh?ttan,Trollhattan,58.26710105,12.29996212,44532.5,Sweden,SE,SWE,V?stra G?taland
Bor?s,Boras,57.7304413,12.91997595,64115.5,Sweden,SE,SWE,V?stra G?taland
Kristianstad,Kristianstad,56.03367149,14.1332869,26763.5,Sweden,SE,SWE,Sk?ne
Helsingborg,Helsingborg,56.05049217,12.70004106,91164.5,Sweden,SE,SWE,Sk?ne
J?nk?ping,Jonkoping,57.7713432,14.16501623,86491,Sweden,SE,SWE,J?nk?ping
?rnsk?ldsvik,Ornskoldsvik,63.31800722,18.71667639,26406,Sweden,SE,SWE,V?sternorrland
Link?ping,Linkoping,58.41001223,15.62993974,94111.5,Sweden,SE,SWE,?sterg?tland
?stersund,Ostersund,63.1833126,14.64999955,44559,Sweden,SE,SWE,J?mtland
Kiruna,Kiruna,67.8500045,20.21663651,13302,Sweden,SE,SWE,Norrbotten
Ume?,Umea,63.82999147,20.23999426,76101,Sweden,SE,SWE,V?sterbotten
Uppsala,Uppsala,59.86005292,17.63999792,130425.5,Sweden,SE,SWE,Uppsala
G?teborg,Goteborg,57.75000083,12.0000321,520940.5,Sweden,SE,SWE,V?stra G?taland
Lule?,Lulea,65.59663477,22.15837833,47094.5,Sweden,SE,SWE,Norrbotten
Sundsvall,Sundsvall,62.40005292,17.31665849,60926,Sweden,SE,SWE,V?sternorrland
Malm?,Malmo,55.58333722,13.03330237,265448.5,Sweden,SE,SWE,Sk?ne
Stockholm,Stockholm,59.35075995,18.09733473,1258654.5,Sweden,SE,SWE,Stockholm
Delemont,Delemont,47.36999713,7.344999488,11315,Switzerland,CH,CHE,Jura
Neuchatel,Neuchatel,46.99899914,6.922998615,31270,Switzerland,CH,CHE,Neuch?tel
Aarau,Aarau,47.3900041,8.03400361,15501,Switzerland,CH,CHE,Aargau
Stans,Stans,46.95000307,8.383302547,7475,Switzerland,CH,CHE,Nidwalden
Sion,Sion,46.23900303,7.353999482,28045,Switzerland,CH,CHE,Valais
Herisau,Herisau,47.38329903,9.283302472,15438,Switzerland,CH,CHE,Appenzell Ausserrhoden
Saint Gallen,Saint Gallen,47.42299807,9.361998557,70572,Switzerland,CH,CHE,Sankt Gallen
Bellinzona,Bellinzona,46.19700013,9.019998609,16572,Switzerland,CH,CHE,Ticino
Glarus,Glarus,47.05000204,9.066699587,5681,Switzerland,CH,CHE,Glarus
Schaffhausen,Schaffhausen,47.70600309,8.632998523,33863,Switzerland,CH,CHE,Schaffhausen
Schwyz,Schwyz,47.01999604,8.648001603,14177,Switzerland,CH,CHE,Schwyz
Frauenfeld,Frauenfeld,47.56799717,9.108000502,21979,Switzerland,CH,CHE,Thurgau
Altdorf,Altdorf,46.87900214,8.638002584,8678,Switzerland,CH,CHE,Uri
Zug,Zug,47.17899903,8.487000565,23435,Switzerland,CH,CHE,Zug
Fribourg,Fribourg,46.80000008,7.149996522,32827,Switzerland,CH,CHE,Fribourg
Liestal,Liestal,47.48300112,7.737003468,12832,Switzerland,CH,CHE,Basel-Landschaft
Solothurn,Solothurn,47.2120021,7.536996608,14853,Switzerland,CH,CHE,Solothurn
Sarnen,Sarnen,46.89900002,8.243001529,9410,Switzerland,CH,CHE,Obwalden
Appenzell,Appenzell,47.3333041,9.416700505,5649,Switzerland,CH,CHE,Appenzell Innerrhoden
Chur,Chur,46.85002016,9.500029662,35361,Switzerland,CH,CHE,Graub?nden
Biel,Biel,47.16658999,7.2500378,63661,Switzerland,CH,CHE,Bern
Luzern,Luzern,47.05042137,8.280000772,163745.5,Switzerland,CH,CHE,Lucerne
Lugano,Lugano,46.0003821,8.966677204,65876.5,Switzerland,CH,CHE,Ticino
Lausanne,Lausanne,46.53042727,6.650022744,191226.5,Switzerland,CH,CHE,Vaud
Basel,Basel,47.58038902,7.590017048,500317.5,Switzerland,CH,CHE,Basel-Stadt
Bern,Bern,46.91668276,7.466975462,198480,Switzerland,CH,CHE,Bern
Z?rich,Zurich,47.37998781,8.55001013,724865,Switzerland,CH,CHE,Z?rich
Geneva,Geneva,46.21000755,6.140028034,716192.5,Switzerland,CH,CHE,Gen?ve
Dar'a,Dar'a,32.62500014,36.10500351,122225,Syria,SY,SYR,Dar`a
Al Ladhiqiyah,Al Ladhiqiyah,35.539987,35.77997595,439664,Syria,SY,SYR,Lattakia (Al Ladhiqiyah)
Madinat ath Thawrah,Madinat ath Thawrah,35.8366614,38.54807572,85590,Syria,SY,SYR,Ar Raqqah
Izaz,Izaz,36.58878603,37.04408484,31534,Syria,SY,SYR,Aleppo (Halab)
Manbij,Manbij,36.52664512,37.9563289,94528.5,Syria,SY,SYR,Aleppo (Halab)
Idlib,Idlib,35.92970481,36.63165523,115785.5,Syria,SY,SYR,Idlib
Al Qamishli,Al Qamishli,37.03002525,41.22997921,104107,Syria,SY,SYR,Hasaka (Al Haksa)
Al Hasakah,Al Hasakah,36.48328859,40.7500085,104819.5,Syria,SY,SYR,Hasaka (Al Haksa)
Douma,Duma,33.5833364,36.39998979,406912,Syria,SY,SYR,Damascus
Tartus,Tartus,34.88463448,35.88658405,139374.5,Syria,SY,SYR,Tartus
Ar Raqqah,Ar Raqqah,35.93037661,39.0199849,175600.5,Syria,SY,SYR,Ar Raqqah
Hamah,Hamah,35.1503467,36.72999548,439796,Syria,SY,SYR,Hamah
Tadmur,Tadmur,34.55040916,38.28333736,53063,Syria,SY,SYR,Homs (Hims)
Abu Kamal,Abu Kamal,34.45041526,40.9186287,69190,Syria,SY,SYR,Dayr Az Zawr
Dayr az Zawr,Dayr az Zawr,35.33038739,40.12999467,275853,Syria,SY,SYR,Dayr Az Zawr
As Suwayda,As Suwayda,32.70041872,36.5665946,65650,Syria,SY,SYR,As Suwayda'
Ad Nabk,Ad Nabk,34.01703086,36.73330277,49775,Syria,SY,SYR,Damascus
Al Qunaytirah,Al Qunaytirah,33.12566408,35.82359086,2235.5,Syria,SY,SYR,Golan
Hims,Hims,34.72995892,36.72002193,890202,Syria,SY,SYR,Homs (Hims)
Aleppo,Aleppo,36.22997072,37.1700203,2170132,Syria,SY,SYR,Aleppo (Halab)
Damascus,Damascus,33.500034,36.29999589,2466000,Syria,SY,SYR,Damascus
Bade,Bade,24.9575,121.2988889,172065,Taiwan,TW,TWN,Taoyuan
Pingzhen,Pingzhen,24.94388889,121.2161111,201632,Taiwan,TW,TWN,Taoyuan
Taibao,Taibao,23.45,120.3333333,34665,Taiwan,TW,TWN,Chiayi
Taoyuan,Taoyuan,24.98888889,121.3111111,451007,Taiwan,TW,TWN,Taoyuan
Yangmei,Yangmei,24.91666667,121.15,162511,Taiwan,TW,TWN,Taoyuan
Yilan,Yilan,24.75,121.75,122915.5,Taiwan,TW,TWN,Yilan
Zhubei,Zhubei,24.83333333,121.0119444,174003,Taiwan,TW,TWN,Hsinchu
Douliou,Douliou,23.7075,120.5438889,105688,Taiwan,TW,TWN,Yunlin
Zhongli,Zhongli,24.96502525,121.2167765,1001193,Taiwan,TW,TWN,Taoyuan
Keelung,Keelung,25.13325787,121.7332824,443603.5,Taiwan,TW,TWN,Keelung City
Nantou,Nantou,23.91666667,120.6833333,134349,Taiwan,TW,TWN,Nantou
Puzi,Puzi,23.46111111,120.2419444,47042,Taiwan,TW,TWN,Chiayi
Changhua,Changhua,24.07340008,120.5134086,493294,Taiwan,TW,TWN,Changhua
Chiayi,Chiayi,23.47545209,120.4350671,387106,Taiwan,TW,TWN,Chiayi City
Hsinchu,Hsinchu,24.8167914,120.9767395,582778.5,Taiwan,TW,TWN,Hsinchu City
Miaoli,Miaoli,24.57,120.82,120494,Taiwan,TW,TWN,Miaoli
Pingtung,Pingtung,22.68170209,120.4816792,359752.5,Taiwan,TW,TWN,Pingtung
Hualien,Hualien,23.98374147,121.6000089,229563,Taiwan,TW,TWN,Hualien
New Taipei,New Taipei,25.01277778,121.465,2821870,Taiwan,TW,TWN,New Taipei City
Tainan,Tainan,23.00000307,120.2000427,1319156,Taiwan,TW,TWN,Tainan City
Taitung,Taitung,22.75539268,121.140037,142292,Taiwan,TW,TWN,Taitung
Magong,Magong,23.56666667,119.5833333,56435,Taiwan,TW,TWN,Penghu
Taichung,Taichung,24.15207745,120.681667,1835024,Taiwan,TW,TWN,Taichung City
Kaohsiung,Kaohsiung,22.63330711,120.2666019,2144391.5,Taiwan,TW,TWN,Kaohsiung City
Taipei,Taipei,25.03583333,121.5683333,4759522.5,Taiwan,TW,TWN,Taipei City
Leninobod,Leninobod,39.75000301,69.00000365,11468,Tajikistan,TJ,TJK,Leninabad
Qurghonteppa,Qurghonteppa,37.83731447,68.77134721,188287,Tajikistan,TJ,TJK,Khatlon
Konibodom,Konibodom,40.29215171,70.42716345,155117.5,Tajikistan,TJ,TJK,Leninabad
Kuybyshevskiy,Kuybyshevskiy,37.97939882,68.68897497,8925,Tajikistan,TJ,TJK,Khatlon
Kulob,Kulob,37.92115948,69.77573035,96975,Tajikistan,TJ,TJK,Khatlon
Uroteppa,Uroteppa,39.92191591,69.00146236,104736,Tajikistan,TJ,TJK,Leninabad
Khorugh,Khorugh,37.4875167,71.54756018,21017.5,Tajikistan,TJ,TJK,Gorno-Badakhshan
Khujand,Khujand,40.2899813,69.6199259,291274.5,Tajikistan,TJ,TJK,Leninabad
Dushanbe,Dushanbe,38.56003522,68.77387935,882822,Tajikistan,TJ,TJK,Tadzhikistan Territories
Wete,Wete,-5.063463959,39.725799,26450,Tanzania,TZ,TZA,Kaskazini-Pemba
Kibaha,Kibaha,-6.766703953,38.9167026,23651,Tanzania,TZ,TZA,Pwani
Mkokotoni,Mkokotoni,-5.878997975,39.25999862,2572,Tanzania,TZ,TZA,Kaskazini-Unguja
Tunduma,Tunduma,-9.284615459,32.77493974,27543,Tanzania,TZ,TZA,Mbeya
Tukuyu,Tukuyu,-9.249578838,33.64000321,77984,Tanzania,TZ,TZA,Mbeya
Sumbawanga,Sumbawanga,-7.959580059,31.62002315,76546.5,Tanzania,TZ,TZA,Rukwa
Mpanda,Mpanda,-6.359574362,31.0500321,73338,Tanzania,TZ,TZA,Rukwa
Kipili,Kipili,-7.432893861,30.59998205,1533,Tanzania,TZ,TZA,Rukwa
Karema,Karema,-6.816187318,30.43327388,14507.5,Tanzania,TZ,TZA,Rukwa
Geita,Geita,-2.866195863,32.16660478,1536,Tanzania,TZ,TZA,Mwanza
Nyahanga,Nyahanga,-2.382917868,33.55003454,16092,Tanzania,TZ,TZA,Mwanza
Kahama,Kahama,-3.819574362,32.58001623,35279,Tanzania,TZ,TZA,Shinyanga
Shinyanga,Shinyanga,-3.659584128,33.42001664,93794,Tanzania,TZ,TZA,Shinyanga
Nzega,Nzega,-4.209628073,33.18003129,18325,Tanzania,TZ,TZA,Tabora
Sikonge,Sikonge,-5.629541403,32.77003048,14549.5,Tanzania,TZ,TZA,Tabora
Biharamulo,Biharamulo,-2.629621156,31.31001623,21817.5,Tanzania,TZ,TZA,Kagera
Bukoba,Bukoba,-1.319623597,31.79996049,85566,Tanzania,TZ,TZA,Kagera
Ngara,Ngara,-2.469527569,30.65000484,10744,Tanzania,TZ,TZA,Kagera
Kakonko,Kakonko,-3.279607321,30.96001176,16319,Tanzania,TZ,TZA,Kigoma
Kasulu,Kasulu,-4.579579652,30.10001257,31218.5,Tanzania,TZ,TZA,Kigoma
Kanyato,Kanyato,-4.456538067,30.26139807,232,Tanzania,TZ,TZA,Kigoma
Uvinza,Uvinza,-5.119598369,30.39002071,52500,Tanzania,TZ,TZA,Kigoma
Kigoma,Kigoma,-4.879613018,29.61001664,164268,Tanzania,TZ,TZA,Kigoma
Mikumi,Mikumi,-7.399614239,36.98000606,12471,Tanzania,TZ,TZA,Morogoro
Ifakara,Ifakara,-8.129595521,36.68002437,27929.5,Tanzania,TZ,TZA,Morogoro
Kilosa,Kilosa,-6.839596742,36.99003129,52558,Tanzania,TZ,TZA,Morogoro
Chake Chake,Chake Chake,-5.239539369,39.77001664,35822.5,Tanzania,TZ,TZA,Kusini-Pemba
Kibiti,Kibiti,-7.729619935,38.95001501,15553,Tanzania,TZ,TZA,Pwani
Bagamoyo,Bagamoyo,-6.439621156,38.89001868,41609.5,Tanzania,TZ,TZA,Pwani
Kilindoni,Kilindoni,-7.916275209,39.65002397,7994.5,Tanzania,TZ,TZA,Pwani
Mpwapwa,Mpwapwa,-6.349600811,36.4799849,10093.5,Tanzania,TZ,TZA,Dodoma
Njombe,Njombe,-9.329625632,34.77001176,42017.5,Tanzania,TZ,TZA,Iringa
Iringa,Iringa,-7.769617494,35.69000728,103290,Tanzania,TZ,TZA,Iringa
Masasi,Masasi,-10.72959186,38.79994665,31549.5,Tanzania,TZ,TZA,Mtwara
Mtwara,Mtwara,-10.26961994,40.18999101,91674,Tanzania,TZ,TZA,Mtwara
Tunduru,Tunduru,-11.08956989,37.3700081,600,Tanzania,TZ,TZA,Ruvuma
Mbamba Bay,Mbamba Bay,-11.2829431,34.76660111,8997,Tanzania,TZ,TZA,Ruvuma
Manyoni,Manyoni,-5.779609763,34.90002966,310,Tanzania,TZ,TZA,Singida
Itigi,Itigi,-5.699614646,34.48000362,11534,Tanzania,TZ,TZA,Singida
Singida,Singida,-4.81961668,34.74003943,47749.5,Tanzania,TZ,TZA,Singida
Ngorongoro,Ngorongoro,-3.249583314,35.51999182,10836,Tanzania,TZ,TZA,Arusha
Oldeani,Oldeani,-3.349628887,35.55001583,7300.5,Tanzania,TZ,TZA,Arusha
Mbulu,Mbulu,-3.849598369,35.53001705,10421,Tanzania,TZ,TZA,Arusha
Babati,Babati,-4.219549948,35.75000362,19117,Tanzania,TZ,TZA,Arusha
Same,Same,-4.069584942,37.72001257,9768,Tanzania,TZ,TZA,Kilimanjaro
Moshi,Moshi,-3.339603659,37.33998409,463873,Tanzania,TZ,TZA,Kilimanjaro
Musoma,Musoma,-1.489587383,33.79999345,127137.5,Tanzania,TZ,TZA,Mara
Korogwe,Korogwe,-5.089574362,38.5400142,47000,Tanzania,TZ,TZA,Tanga
Tabora,Tabora,-5.020017884,32.80000281,145893.5,Tanzania,TZ,TZA,Tabora
Lindi,Lindi,-10.00002399,39.69999508,27953.5,Tanzania,TZ,TZA,Lindi
Songea,Songea,-10.68003416,35.65000972,120923,Tanzania,TZ,TZA,Ruvuma
Tanga,Tanga,-5.070040671,39.09000647,217155.5,Tanzania,TZ,TZA,Tanga
Mwanza,Mwanza,-2.520015443,32.93002071,465372.5,Tanzania,TZ,TZA,Mwanza
Morogoro,Morogoro,-6.820011374,37.66001623,242718.5,Tanzania,TZ,TZA,Morogoro
Dodoma,Dodoma,-6.183306052,35.75000362,199405,Tanzania,TZ,TZA,Dodoma
Arusha,Arusha,-3.36001585,36.66999914,330605,Tanzania,TZ,TZA,Arusha
Mbeya,Mbeya,-8.890014222,33.43004187,261855.5,Tanzania,TZ,TZA,Mbeya
Zanzibar,Zanzibar,-6.159999981,39.20002559,388439,Tanzania,TZ,TZA,Zanzibar West
Dar es Salaam,Dar es Salaam,-6.800012595,39.26834184,2814326,Tanzania,TZ,TZA,Dar-Es-Salaam
Mae Hong Son,Mae Hong Son,19.30100405,97.96899665,9109,Thailand,TH,THA,Mae Hong Son
Phangnga,Phangnga,8.451000086,98.53399857,9676,Thailand,TH,THA,Phangnga
Ranong,Ranong,9.962001095,98.63800257,24561,Thailand,TH,THA,Ranong
Krabi,Krabi,8.052003097,98.91199867,31219,Thailand,TH,THA,Krabi
Phatthalung,Phatthalung,7.61499898,100.0809996,43522,Thailand,TH,THA,Phatthalung
Satun,Satun,6.616701099,100.0666986,34544,Thailand,TH,THA,Satun
Lamphun,Lamphun,18.50300114,99.07399856,14030,Thailand,TH,THA,Lamphun
Kamphaeng Phet,Kamphaeng Phet,16.47299704,99.52900267,58787,Thailand,TH,THA,Kamphaeng Phet
Phichit,Phichit,16.43900405,100.3490017,35760,Thailand,TH,THA,Phichit
Phetchabun,Phetchabun,16.41899707,101.1590017,50656,Thailand,TH,THA,Phetchabun
Supham Buri,Supham Buri,14.47100105,100.1289966,53399,Thailand,TH,THA,Suphan Buri
Ang Thong,Ang Thong,14.58330306,100.4499997,13738,Thailand,TH,THA,Ang Thong
Chainat,Chainat,15.17900402,100.1259997,15469,Thailand,TH,THA,Chai Nat
Nakhon Nayok,Nakhon Nayok,14.20000203,101.2159987,21309,Thailand,TH,THA,Nakhon Nayok
Sing Buri,Sing Buri,14.886999,100.4010036,20046,Thailand,TH,THA,Sing Buri
Nakhon Pathom,Nakhon Pathom,13.81799707,100.0639986,117927,Thailand,TH,THA,Nakhon Pathom
Prachuap Khiri Khan,Prachuap Khiri Khan,11.80299605,99.80000169,33521,Thailand,TH,THA,Prachuap Khiri Khan
Samut Sakhon,Samut Sakhon,13.536,100.2740046,63498,Thailand,TH,THA,Samut Sakhon
Samut Songkhram,Samut Songkhram,13.41299699,100.0009986,35065,Thailand,TH,THA,Samut Songkhram
Yasothon,Yasothon,15.78799812,104.1509977,21643,Thailand,TH,THA,Yasothon
Chachoengsao,Chachoengsao,13.67900105,101.0760037,49741,Thailand,TH,THA,Chachoengsao
Trat,Trat,12.23700309,102.5090016,21590,Thailand,TH,THA,Trat
Kalasin,Kalasin,16.42799707,103.5090007,55102,Thailand,TH,THA,Kalasin
Maha Sarakham,Maha Sarakham,16.18399803,103.2980045,51584,Thailand,TH,THA,Maha Sarakham
Roi Et,Roi Et,16.050996,103.6549986,39328,Thailand,TH,THA,Roi Et
Pattani,Pattani,6.864003023,101.2500006,96815.5,Thailand,TH,THA,Pattani
Chumphon,Chumphon,10.51267743,99.18721676,70760.5,Thailand,TH,THA,Chumphon
Thung Song,Thung Song,8.153958353,99.72863074,26037.5,Thailand,TH,THA,Nakhon Si Thammarat
Trang,Trang,7.563400084,99.60801794,103728.5,Thailand,TH,THA,Trang
Yala,Yala,6.550490335,101.2850732,120849,Thailand,TH,THA,Yala
Chiang Rai,Chiang Rai,19.91187115,99.82645422,97941.5,Thailand,TH,THA,Chiang Rai
Lampang,Lampang,18.29155662,99.48125565,180110,Thailand,TH,THA,Lampang
Nan,Nan,18.78684938,100.7714611,53576.5,Thailand,TH,THA,Nan
Phayao,Phayao,19.17070192,99.90830969,20088,Thailand,TH,THA,Phayao
Phrae,Phrae,18.15329632,100.1629195,28254.5,Thailand,TH,THA,Phrae
Phitsanulok,Phitsanulok,16.8283126,100.2728869,133722,Thailand,TH,THA,Phitsanulok
Sukhothai,Sukhothai,17.01186729,99.7515234,10276,Thailand,TH,THA,Sukhothai
Uttaradit,Uttaradit,17.63162274,100.0971871,67471.5,Thailand,TH,THA,Uttaradit
Kanchanaburi,Kanchanaburi,14.01742474,99.52202836,63699,Thailand,TH,THA,Kanchanaburi
Mae Sot,Mae Sot,16.71617474,98.57076859,45172,Thailand,TH,THA,Tak
Tak,Tak,16.88474326,99.12933915,28647.5,Thailand,TH,THA,Tak
Uthai Thani,Uthai Thani,15.38186342,100.026442,19233,Thailand,TH,THA,Uthai Thani
Lop Buri,Lop Buri,14.80401756,100.6186023,42130.5,Thailand,TH,THA,Lop Buri
Prachin Buri,Prachin Buri,14.0572156,101.3767989,56178.5,Thailand,TH,THA,Prachin Buri
Ayutthaya,Ayutthaya,14.35879925,100.5684244,113788.5,Thailand,TH,THA,Phra Nakhon Si Ayutthaya
Pathum Thani,Pathum Thani,14.01711468,100.5333361,154412,Thailand,TH,THA,Pathum Thani
Saraburi,Saraburi,14.53036501,100.8799816,70769,Thailand,TH,THA,Saraburi
Nonthaburi,Nonthaburi,13.83368919,100.4833134,258550,Thailand,TH,THA,Nonthaburi
Phetchaburi,Phetchaburi,13.11329388,99.9411759,68549,Thailand,TH,THA,Phetchaburi
Hua Hin,Hua Hin,12.56970949,99.94432816,33963,Thailand,TH,THA,Prachuap Khiri Khan
Ratchaburi,Ratchaburi,13.54189821,99.82154496,99722,Thailand,TH,THA,Ratchaburi
Samut Prakan,Samut Prakan,13.60690716,100.6114709,388920,Thailand,TH,THA,Samut Prakan
Sisaket,Sisaket,15.12025148,104.3298486,42856,Thailand,TH,THA,Si Sa Ket
Si Racha,Si Racha,13.15902753,100.9286608,94204.5,Thailand,TH,THA,Chon Buri
Chon Buri,Chon Buri,13.40040814,100.9999743,221340.5,Thailand,TH,THA,Chon Buri
Chanthaburi,Chanthaburi,12.61327272,102.0978918,94950.5,Thailand,TH,THA,Chanthaburi
Aranyaprathet,Aranyaprathet,13.68235476,102.4969372,21354,Thailand,TH,THA,Sa Kaeo
Rayong,Rayong,12.67184796,101.2814559,37035,Thailand,TH,THA,Rayong
Buriram,Buriram,15.00043968,103.116641,47292,Thailand,TH,THA,Buri Ram
Chaiyaphum,Chaiyaphum,15.8040082,102.0386189,55191,Thailand,TH,THA,Chaiyaphum
Bua Yai,Bua Yai,15.58402163,102.4185957,17550.5,Thailand,TH,THA,Nakhon Ratchasima
Surin,Surin,14.88682904,103.4914502,54604.5,Thailand,TH,THA,Surin
Loei,Loei,17.49188967,101.7315059,29908,Thailand,TH,THA,Loei
Nong Khai,Nong Khai,17.87326174,102.747878,84057,Thailand,TH,THA,Nong Khai
Sakhon Nakhon,Sakhon Nakhon,17.16790428,104.1478959,67755.5,Thailand,TH,THA,Sakon Nakhon
Udon Thani,Udon Thani,17.4047632,102.7893225,239192,Thailand,TH,THA,Udon Thani
Nakhon Phanom,Nakhon Phanom,17.39447959,104.76946,44986,Thailand,TH,THA,Nakhon Phanom
Narathiwat,Narathiwat,6.431841246,101.8214229,57941.5,Thailand,TH,THA,Narathiwat
Khon Kaen,Khon Kaen,16.42004295,102.8300435,199317.5,Thailand,TH,THA,Khon Kaen
Phuket,Phuket,7.876533426,98.3815295,108595.5,Thailand,TH,THA,Phuket
Nakhon Si Thammarat,Nakhon Si Thammarat,8.399989847,99.97001135,176585.5,Thailand,TH,THA,Nakhon Si Thammarat
Songkhla,Songkhla,7.209959126,100.5600012,48616,Thailand,TH,THA,Songkhla (Songkhla Lake)
Hat Yai,Hat Yai,6.996432107,100.4714278,254825,Thailand,TH,THA,Songkhla
Nakhon Sawan,Nakhon Sawan,15.70003522,100.0700052,111915,Thailand,TH,THA,Nakhon Sawan
Ubon Ratchathani,Ubon Ratchathani,15.24995933,104.8300248,198213,Thailand,TH,THA,Ubon Ratchathani
Surat Thani,Surat Thani,9.1500991,99.34012732,142414,Thailand,TH,THA,Surat Thani
Chiang Mai,Chiang Mai,18.7999752,98.98004594,299081.5,Thailand,TH,THA,Chiang Mai
Nakhon Ratchasima,Nakhon Ratchasima,15.00002626,102.1000105,271882.5,Thailand,TH,THA,Nakhon Ratchasima
Bangkok,Bangkok,13.74999921,100.5166447,5904238,Thailand,TH,THA,Bangkok Metropolis
Freeport,Freeport,26.53327578,-78.70001306,25383,The Bahamas,BS,BHS,
Nassau,Nassau,25.08339012,-77.35004378,194453,The Bahamas,BS,BHS,
Georgetown,Georgetown,13.55100308,-14.76700152,3584,The Gambia,GM,GMB,Maccarthy Island
Basse Santa Su,Basse Santa Su,13.31000112,-14.2229965,14380,The Gambia,GM,GMB,Upper River
Kerewan,Kerewan,13.49399711,-16.09499647,2751,The Gambia,GM,GMB,Lower River
Mansa Konko,Mansa Konko,13.3773121,-15.67856644,18672,The Gambia,GM,GMB,Lower River
Bansang,Bansang,13.43363609,-14.65002079,4646.5,The Gambia,GM,GMB,Maccarthy Island
Brikama,Brikama,13.28036379,-16.65994979,136418,The Gambia,GM,GMB,Banjul
Banjul,Banjul,13.45387646,-16.59170149,38841.5,The Gambia,GM,GMB,Banjul
Bassar,Bassar,9.261000068,0.789003574,61845,Togo,TG,TGO,Kara
Sotouboua,Sotouboua,8.557002133,0.984996462,21054,Togo,TG,TGO,Centre
Kpalime,Kpalime,6.900391458,0.630028441,98226.5,Togo,TG,TGO,Plateaux
Sokode,Sokode,8.9904706,1.149996703,99725.5,Togo,TG,TGO,Centre
Mango,Mango,10.35956016,0.470813353,40187,Togo,TG,TGO,Savanes
Atakpame,Atakpame,7.530042947,1.120024372,74757,Togo,TG,TGO,Plateaux
Lome,Lome,6.131937072,1.222757119,1100850,Togo,TG,TGO,Maritime
Neiafu,Neiafu,-18.64957355,-173.9832927,5855.5,Tonga,TO,TON,
Nukualofa,Nukualofa,-21.13851236,-175.2205645,33139,Tonga,TO,TON,
San Fernando,San Fernando,10.28046166,-61.45937678,166039,Trinidad and Tobago,TT,TTO,San Fernando
Port-of-Spain,Port-of-Spain,10.65199709,-61.51703089,171982.5,Trinidad and Tobago,TT,TTO,Port of Spain
Medenine,Medemine,33.399999,10.41669956,61705,Tunisia,TN,TUN,M?denine
Kebili,Kebili,33.68999703,8.971002538,19875,Tunisia,TN,TUN,Kebili
Tataouine,Tataouine,33.00000315,10.46670359,62577,Tunisia,TN,TUN,Tataouine
L'Ariana,L'Ariana,36.86667315,10.19999755,97687,Tunisia,TN,TUN,Manubah
Jendouba,Jendouba,36.50000406,8.749998615,51408,Tunisia,TN,TUN,Jendouba
Kasserine,Kasserine,35.2167031,8.716698503,76243,Tunisia,TN,TUN,Kass?rine
Sdid Bouzid,Sdid Bouzid,35.01669608,9.500004482,42098,Tunisia,TN,TUN,Sidi Bou Zid
Siliana,Siliana,36.08330413,9.3833016,26960,Tunisia,TN,TUN,Siliana
Mahdia,Mahdia,35.48391304,11.04087662,45977,Tunisia,TN,TUN,Mahdia
Monastir,Monasir,35.73070214,10.76729456,56473,Tunisia,TN,TUN,Monastir
Zaghouan,Zaghouan,36.39999616,10.14699661,16911,Tunisia,TN,TUN,Zaghouan
Ben Gardane,Ben Gardane,33.14039187,11.22002803,16603.5,Tunisia,TN,TUN,M?denine
Zarzis,Zarzis,33.51039512,11.09998368,119238.5,Tunisia,TN,TUN,M?denine
Dehibat,Dehibat,32.01704958,10.7000081,3525,Tunisia,TN,TUN,Tataouine
Tozeur,Tozeur,33.93042116,8.129984089,37223.5,Tunisia,TN,TUN,Tozeur
Beja,Beja,36.73040529,9.190022744,58400,Tunisia,TN,TUN,B?ja
Bizerte,Bizerte,37.29042279,9.854995075,127555.5,Tunisia,TN,TUN,Bizerte
Nabeul,Nabeul,36.46034426,10.7300321,115149,Tunisia,TN,TUN,Nabeul
El Kef,El Kef,36.18263511,8.714754597,42303.5,Tunisia,TN,TUN,Le Kef
Qasserine,Qasserine,35.18039654,8.829993041,80072.5,Tunisia,TN,TUN,Kass?rine
Gabes,Gabes,33.90042299,10.09999304,164796,Tunisia,TN,TUN,Gab?s
Gafsa,Gafsa,34.42044293,8.780021931,104017.5,Tunisia,TN,TUN,Gafsa
Qairouan,Qairouan,35.68039187,10.09999304,132158,Tunisia,TN,TUN,Kairouan
Sfax,Sfax,34.75003522,10.72000688,365164,Tunisia,TN,TUN,Sfax
Sousse,Sousse,35.82999514,10.62502559,245563.5,Tunisia,TN,TUN,Sousse
Tunis,Tunis,36.80277814,10.1796781,1570476.5,Tunisia,TN,TUN,Tunis
Kirklareli,Kirklareli,41.74299917,27.22599962,58223,Turkey,TR,TUR,Kirklareli
Bilecik,Bilecik,40.14999902,29.9829966,40285,Turkey,TR,TUR,Bilecik
Sakarya,Sakarya,40.76666114,30.40000251,286787,Turkey,TR,TUR,Sakarya
Kastamonu,Kastamonu,41.38900215,33.78300349,70402,Turkey,TR,TUR,Kastamonu
Burdur,Burdur,37.71666011,30.28333554,66158,Turkey,TR,TUR,Burdur
Kirsehir,Kirsehir,39.14199917,34.1710026,94336,Turkey,TR,TUR,Kirsehir
Nevsehir,Nevsehir,38.62400404,34.72399852,75527,Turkey,TR,TUR,Nevsehir
Antioch,Antioch,36.23333409,36.11667656,154803,Turkey,TR,TUR,Hatay
Giresun,Giresun,40.91300115,38.39000452,98864,Turkey,TR,TUR,Giresun
Sinop,Sinop,42.02299802,35.1530015,34834,Turkey,TR,TUR,Sinop
Tokat,Tokat,40.30599617,36.56300452,129702,Turkey,TR,TUR,Tokat
Artvin,Coruh,41.18300114,41.81799654,27899.5,Turkey,TR,TUR,Artvin
Bingol,Bingol,38.88500404,40.49800256,80568,Turkey,TR,TUR,Bing?l
Bitlis,Bitlis,38.39400012,42.12299765,52960,Turkey,TR,TUR,Bitlis
Cankiri,Cankiri,40.60700101,33.62100359,71379,Turkey,TR,TUR,?ankiri
Nigde,Nigde,37.97600412,34.69400163,91039,Turkey,TR,TUR,Nigde
Yozgat,Yozgat,39.81799809,34.81499749,87881,Turkey,TR,TUR,Yozgat
Gumushane,Gumushane,40.46400013,39.48399962,32250,Turkey,TR,TUR,G?m?shane
Siirt,Siirt,37.94400007,41.93299858,114034,Turkey,TR,TUR,Siirt
Tunceli,Tunceli,39.11670002,39.5333015,29062,Turkey,TR,TUR,Tunceli
Aydin,Aydin,37.8499752,27.85002071,180939.5,Turkey,TR,TUR,Aydin
Luleburgaz,Luleburgaz,41.40665733,27.35521887,67989.5,Turkey,TR,TUR,Kirklareli
Isparta,Isparta,37.76998008,30.52996049,161089,Turkey,TR,TUR,Isparta
Kutahya,Kutahya,39.42000856,29.92999711,168459.5,Turkey,TR,TUR,K?tahya
Mugla,Mugla,37.21637046,28.36389115,44488.5,Turkey,TR,TUR,Mugla
Elazig,Elazig,38.67997622,39.22999792,271492,Turkey,TR,TUR,Elazig
Kahramanmaras,Kahramanmaras,37.60998985,36.94502112,374745.5,Turkey,TR,TUR,K. Maras
Icel,Icel,36.79998761,34.61999508,577416,Turkey,TR,TUR,Mersin
Corum,Corum,40.5199931,34.95000077,168544,Turkey,TR,TUR,?orum
Rize,Rize,41.02084108,40.52185705,187976.5,Turkey,TR,TUR,Rize
Tatvan,Tatvan,38.50657595,42.2815946,68436.5,Turkey,TR,TUR,Bitlis
Polatli,Polatli,39.58415875,32.14722611,72631.5,Turkey,TR,TUR,Ankara
Karabuk,Karabuk,41.20000327,32.60001501,113022.5,Turkey,TR,TUR,Zinguldak
Nusaybin,Nusaybin,37.07498374,41.21835201,120822.5,Turkey,TR,TUR,Mardin
Hakkari,Hakkari,37.57443646,43.7408337,42385,Turkey,TR,TUR,Hakkari
Soke,Soke,37.75122154,27.41025427,72785.5,Turkey,TR,TUR,Aydin
Balikesir,Balikesir,39.6503821,27.89001827,249833.5,Turkey,TR,TUR,Balikesir
Canakkale,Canakkale,40.14593325,26.4063879,74667,Turkey,TR,TUR,?anakkale
Edirne,Edirne,41.67043968,26.56999548,114424,Turkey,TR,TUR,Edirne
Tekirdag,Tekirdag,40.99086875,27.50998979,108266,Turkey,TR,TUR,Tekirdag
Izmit,Kocaeli,40.77602399,29.93061723,383557.5,Turkey,TR,TUR,Kocaeli
Bolu,Bolu,40.73625897,31.60612219,96489,Turkey,TR,TUR,Bolu
Afyon,Afyon,38.75038535,30.55001094,151564,Turkey,TR,TUR,Afyon
Denizli,Denizli,37.77039349,29.08002315,342791,Turkey,TR,TUR,Denizli
Manisa,Manisa,38.63039268,27.43996822,237700,Turkey,TR,TUR,Manisa
Adiyaman,Adiyaman,37.77039349,38.27992672,195497,Turkey,TR,TUR,Adiyaman
Malatya,Malatya,38.37043439,38.30002885,451689.5,Turkey,TR,TUR,Malatya
Tarsus,Tarsus,36.9203937,34.87997921,566297,Turkey,TR,TUR,Mersin
Samandagi,Samandagi,36.11705772,35.93329993,93638,Turkey,TR,TUR,Hatay
Hatay,Hatay,36.2303583,36.12000688,305564,Turkey,TR,TUR,Hatay
Iskenderun,Iskenderun,36.58041445,36.17002966,228954,Turkey,TR,TUR,Hatay
Amasya,Amasya,40.65368003,35.83304765,77700.5,Turkey,TR,TUR,Amasya
Ordu,Ordu,41.00042889,37.8699259,135952.5,Turkey,TR,TUR,Ordu
Sivas,Sivas,39.74541506,37.03498979,245801.5,Turkey,TR,TUR,Sivas
Bafra,Bafra,41.56817202,35.90689327,95198,Turkey,TR,TUR,Samsun
Erzurum,Erzurum,39.92039146,41.29002722,391804,Turkey,TR,TUR,Erzurum
Erzincan,Erzincan,39.75264976,39.49277258,121717,Turkey,TR,TUR,Erzincan
Agri,Agri,39.71983522,43.05131506,87854,Turkey,TR,TUR,Agri
Diyarbakir,Diyarbakir,37.92043601,40.23004024,640586.5,Turkey,TR,TUR,Diyarbakir
Mus,Mus,38.74901593,41.49693966,80541,Turkey,TR,TUR,Mus
Zonguldak,Zonguldak,41.43037681,31.78001339,128573.5,Turkey,TR,TUR,Zinguldak
Eregli,Eregli,37.50627525,34.05165767,86563,Turkey,TR,TUR,Konya
Karaman,Karaman,37.18154055,33.21501623,103619.5,Turkey,TR,TUR,Karaman
Usak,Usak,38.68036379,29.4200024,147190.5,Turkey,TR,TUR,Usak
Kilis,Kilis,36.7204059,37.11999752,73320,Turkey,TR,TUR,Gaziantep
Kirikkale,Kirikkale,39.85036989,33.52998409,208554.5,Turkey,TR,TUR,Kinkkale
Kars,Kars,40.60846315,43.09746212,62793,Turkey,TR,TUR,Kars
Mardin,Mardin,37.31150677,40.74272213,64479.5,Turkey,TR,TUR,Mardin
Batman,Batman,37.89041201,41.14001054,276337.5,Turkey,TR,TUR,Batman
Van,Van,38.49543968,43.39997595,326262,Turkey,TR,TUR,Van
Adapazari,Adapazari,40.79997601,30.4150321,260109,Turkey,TR,TUR,Sakarya
Trabzon,Trabzon,40.97999086,39.71999385,497556.5,Turkey,TR,TUR,Trabzon
Sanliurfa,Sanliurfa,37.16999086,38.79498572,431407.5,Turkey,TR,TUR,Sanliurfa
Eskisehir,Eskisehir,39.7949986,30.52996049,490644.5,Turkey,TR,TUR,Eskisehir
Antalya,Antalya,36.88998212,30.69997595,703468.5,Turkey,TR,TUR,Antalya
Kayseri,Kayseri,38.73495994,35.49001949,562215.5,Turkey,TR,TUR,Kayseri
Gaziantep,Gaziantep,37.07498374,37.38499426,943262,Turkey,TR,TUR,Gaziantep
Izmir,Izmir,38.43614968,27.15179401,2454909,Turkey,TR,TUR,Izmir
Bursa,Bursa,40.1999868,29.06999792,1425544.5,Turkey,TR,TUR,Bursa
Samsun,Samsun,41.27999839,36.34366247,573722.5,Turkey,TR,TUR,Samsun
Konya,Konya,37.87501243,32.47500972,718680,Turkey,TR,TUR,Konya
Adana,Adana,36.99498863,35.32000403,1245445,Turkey,TR,TUR,Adana
Ankara,Ankara,39.92723859,32.86439164,3511689.5,Turkey,TR,TUR,Ankara
Istanbul,Istanbul,41.10499615,29.01000159,10003305,Turkey,TR,TUR,Istanbul
Gyzlarbat,Gyzlarbat,38.97553957,56.27779455,30229,Turkmenistan,TM,TKM,Balkan
Celeken,Celeken,39.43615488,53.12259119,1206,Turkmenistan,TM,TKM,Balkan
Tejen,Tejen,37.37860862,60.49603837,62649.5,Turkmenistan,TM,TKM,Ahal
Buzmeyin,Buzmeyin,38.05166831,58.21002803,40147,Turkmenistan,TM,TKM,Ahal
Koneurgench,Koneurgench,42.31665346,59.16666215,30700,Turkmenistan,TM,TKM,Tashauz
Balkanabat,Balkanabat,39.51238019,54.36493974,99324.5,Turkmenistan,TM,TKM,Balkan
Kaka,Kaka,37.35034161,59.60002071,28463,Turkmenistan,TM,TKM,Ahal
Atamyrat,Atamyrat,37.82480878,65.19973059,32205,Turkmenistan,TM,TKM,Chardzhou
Dasoguz,Dasoguz,41.83999005,59.96495967,183962,Turkmenistan,TM,TKM,Tashauz
Turkmenbasy,Turkmenbasy,40.02304669,52.96967606,66722,Turkmenistan,TM,TKM,Balkan
Turkmenabat,Turkmenabat,39.11000165,63.58003617,231665.5,Turkmenistan,TM,TKM,Chardzhou
Mary,Mary,37.6000163,61.83332108,146694,Turkmenistan,TM,TKM,Mary
Ashgabat,Ashgabat,37.94999493,58.38329911,652841,Turkmenistan,TM,TKM,Ahal
Grand Turk,Grand Turk,21.46642743,-71.13597864,4760.5,Turks and Caicos Islands,TC,TCA,
Funafuti,Funafuti,-8.516651999,179.2166471,4749,Tuvalu,TV,TUV,
Kalangala,Kalangala,-0.3088889,32.225,5200,Uganda,UG,UGA,Kalangala
Kumi,Kumi,1.4608333,33.9361111,13000,Uganda,UG,UGA,Kumi
Kaberamaido,Kaberamaido,1.7388889,33.1594444,3400,Uganda,UG,UGA,Kaberamaido
Kayunga,Kayunga,0.7025,32.8886111,21704,Uganda,UG,UGA,Kayunga
Iganga,Iganga,0.6091667,33.4686111,45024,Uganda,UG,UGA,Iganga
Kamuli,Kamuli,0.9472222,33.1197222,12764,Uganda,UG,UGA,Kamuli
Pallisa,Pallisa,1.145,33.7094444,30745,Uganda,UG,UGA,Pallisa
Mpigi,Mpigi,0.225,32.3136111,11082,Uganda,UG,UGA,Mpigi
Adjumani,Adjumani,3.3613889,31.8097222,34700,Uganda,UG,UGA,Adjumani
Nebbi,Nebbi,2.4758333,31.1025,30354,Uganda,UG,UGA,Nebbi
Kiboga,Kiboga,0.9161111,31.7741667,14512,Uganda,UG,UGA,Kiboga
Nakasongola,Nakasongola,1.3088889,32.4563889,6921,Uganda,UG,UGA,Nakasongola
Bombo,Bombo,0.583299106,32.53329952,48000,Uganda,UG,UGA,Bamunanika
Masindi,Masindi,1.6744444,31.715,31486,Uganda,UG,UGA,Masindi
Fort Portal,Fort Portal,0.671004121,30.27500162,42670,Uganda,UG,UGA,Kabarole
Kibale,Kibale,0.8,31.0666667,5200,Uganda,UG,UGA,Kibale
Sironko,Sironko,1.25,34.3,14100,Uganda,UG,UGA,Budadiri
Busia,Busia,0.4544444,34.0758333,47100,Uganda,UG,UGA,Busia
Katakwi,Katakwi,1.8911111,33.9661111,8400,Uganda,UG,UGA,Usuk
Ntungamo,Ntungamo,-0.8794444,30.2641667,16400,Uganda,UG,UGA,Ntungamo
Kisoro,Kisoro,-1.3538889,29.6983333,12900,Uganda,UG,UGA,Kisoro
Jinja,Jinja,0.44042401,33.19992672,195659.5,Uganda,UG,UGA,Jinja
Soroti,Soroti,1.710398172,33.60000565,1038,Uganda,UG,UGA,Soroti
Arua,Arua,3.020369892,30.90001542,154700,Uganda,UG,UGA,Arua Municipality
Pakwach,Pakwach,2.470377623,31.47998002,17541,Uganda,UG,UGA,Nebbi
Moyo,Moyo,3.650408955,31.72001705,22434,Uganda,UG,UGA,Moyo
Entebbe,Entebbe,0.060395527,32.46002356,127414,Uganda,UG,UGA,Wakiso
Mubende,Mubende,0.590440693,31.37001257,9556,Uganda,UG,UGA,Mubende
Mityana,Mityana,0.400426452,32.05002274,37420.5,Uganda,UG,UGA,Busujju
Kitgum,Kitgum,3.300404479,32.87002437,32785.5,Uganda,UG,UGA,Kitgum
Lira,Lira,2.260390441,32.89002315,127384,Uganda,UG,UGA,Lira
Masindi-Port,Masindi-Port,1.700398782,32.06991817,8073.5,Uganda,UG,UGA,Masindi
Mbale,Mbale,1.090410175,34.1699967,247084,Uganda,UG,UGA,Bungokho
Tororo,Tororo,0.710381692,34.1699967,96850,Uganda,UG,UGA,Tororo
Kaabong,Kaabong,3.520391051,34.12002559,1137,Uganda,UG,UGA,Kaabong
Moroto,Moroto,2.540347513,34.63999385,371,Uganda,UG,UGA,Moroto
Masaka,Masaka,-0.329606507,31.7299906,65373,Uganda,UG,UGA,Masaka
Katwe,Katwe,-0.129618715,29.92002356,1957,Uganda,UG,UGA,Kasese
Mbarara,Mbarara,-0.599615866,30.65000484,83700,Uganda,UG,UGA,Kashari
Kabale,Kabale,-1.249602032,29.97996822,44600,Uganda,UG,UGA,Kabale
Kasese,Kasese,0.232478047,29.98828813,67269,Uganda,UG,UGA,Kasese
Gulu,Gulu,2.779996967,32.28003454,144430.5,Uganda,UG,UGA,Aswa
Kampala,Kampala,0.316658955,32.58332353,1386594.5,Uganda,UG,UGA,Kampala
Mykolayiv,Mykolayiv,46.96773907,31.984342,352917.5,Ukraine,UA,UKR,Mykolayiv
Chernihiv,Chernihiv,51.50492983,31.3015413,293656.5,Ukraine,UA,UKR,Chernihiv
Khmelnytskyy,Khmelnytskyy,49.42492759,27.00154537,322093,Ukraine,UA,UKR,Khmel'nyts'kyy
Kamyanets-Podilskyy,Kamyanets-Podilskyy,48.68430096,26.58089921,107329,Ukraine,UA,UKR,Khmel'nyts'kyy
Drohobych,Drohobych,49.34436403,23.49938188,101837.5,Ukraine,UA,UKR,L'viv
Uzhgorod,Uzhgorod,48.62998903,22.25000077,134355,Ukraine,UA,UKR,Transcarpathia
Uman,Uman,48.75429669,30.2109102,87620,Ukraine,UA,UKR,Cherkasy
Brovary,Brovary,50.49431968,30.78090124,77355.5,Ukraine,UA,UKR,Kiev
Bila Tserkva,Bila Tserkva,49.77431195,30.13091508,192418.5,Ukraine,UA,UKR,Kiev
Illichivsk,Illichivsk,46.30000205,30.66659298,53906,Ukraine,UA,UKR,Odessa
Konotop,Konotop,51.24238771,33.20902177,97672.5,Ukraine,UA,UKR,Sumy
Kryvyy Rih,Kryvyy Rih,47.92832644,33.34498246,571643.5,Ukraine,UA,UKR,Dnipropetrovs'k
Makiyivka,Makiyivka,48.02966392,37.97462235,318882.5,Ukraine,UA,UKR,Donets'k
Horlivka,Horlivka,48.29964744,38.05466915,337717.5,Ukraine,UA,UKR,Donets'k
Kramatorsk,Kramatorsk,48.71936342,37.53439083,178902.5,Ukraine,UA,UKR,Donets'k
Berdyansk,Berdyansk,46.75682172,36.78683956,88409,Ukraine,UA,UKR,Zaporizhzhya
Dzhankoy,Dzhankoy,45.71704022,34.4000085,42805,Ukraine,UA,UKR,Crimea
Yevpatoriya,Yevpatoriya,45.19689109,33.36306921,90588,Ukraine,UA,UKR,Crimea
Kerch,Kerch,45.36850852,36.4880981,133972,Ukraine,UA,UKR,Crimea
Simferopol,Simferopol,44.94915428,34.0987349,305882.5,Ukraine,UA,UKR,Crimea
Kherson,Kherson,46.63253718,32.60066489,278578.5,Ukraine,UA,UKR,Crimea
Voznesensk,Voznesensk,47.55036501,31.33332231,43122,Ukraine,UA,UKR,Mykolayiv
Nizhyn,Nizhyn,51.0540788,31.89029089,95893.5,Ukraine,UA,UKR,Chernihiv
Rivne,Rivne,50.61658612,26.25280554,253261,Ukraine,UA,UKR,Rivne
Chernivtsi,Chernivtsi,48.30530601,25.92155961,267250.5,Ukraine,UA,UKR,Chernivtsi
Ivano-Frankivsk,Ivano-Frankivsk,48.93475079,24.70938554,222719.5,Ukraine,UA,UKR,Ivano-Frankivs'k
Ternopil,Ternopil,49.53598024,25.5821488,240222,Ukraine,UA,UKR,Ternopil'
Lutsk,Lutsk,50.7471983,25.33337846,211980,Ukraine,UA,UKR,Volyn
Kovel,Kovel,51.21706626,24.71662024,68850.5,Ukraine,UA,UKR,Volyn
Cherkasy,Cherkasy,49.43472028,32.07090002,285694.5,Ukraine,UA,UKR,Cherkasy
Kirovohrad,Kirovohrad,48.50405357,32.26029415,243573.5,Ukraine,UA,UKR,Kirovohrad
Izmayil,Izmayil,45.35034426,28.83735063,82839.5,Ukraine,UA,UKR,Odessa
Vinnytsya,Vinnytsya,49.22537905,28.48155839,349627,Ukraine,UA,UKR,Vinnytsya
Korosten,Korosten,50.95041587,28.65002356,68992,Ukraine,UA,UKR,Zhytomyr
Shostka,Shostka,51.87340863,33.47965124,91128.5,Ukraine,UA,UKR,Sumy
Nikopol,Nikopol,47.56659141,34.40620967,119110,Ukraine,UA,UKR,Dnipropetrovs'k
Kupyansk,Kupyansk,49.72178286,37.59805619,78870,Ukraine,UA,UKR,Kharkiv
Lysychansk,Lysychansk,48.92041058,38.42735958,118010.5,Ukraine,UA,UKR,Luhans'k
Luhansk,Luhansk,48.56976015,39.33438432,408931,Ukraine,UA,UKR,Luhans'k
Poltava,Poltava,49.57403994,34.57028235,302217.5,Ukraine,UA,UKR,Poltava
Kremenchuk,Kremenchuk,49.08352724,33.42962846,209496.5,Ukraine,UA,UKR,Poltava
Melitopol,Melitopol,46.83782452,35.37746822,135850,Ukraine,UA,UKR,Zaporizhzhya
Zaporizhzhya,Zaporizhzhya,47.85729718,35.17680863,600778.5,Ukraine,UA,UKR,Zaporizhzhya
Yalta,Yalta,44.49931093,34.15940303,76814.5,Ukraine,UA,UKR,Crimea
Chernobyl,Chernobyl,51.38940716,30.09887569,0,Ukraine,UA,UKR,Kiev
Sumy,Sumy,50.92429344,34.78086381,289801,Ukraine,UA,UKR,Sumy
Mariupol,Mariupol,47.09618085,37.55619828,416435,Ukraine,UA,UKR,Donets'k
Lvov,Lvov,49.83498008,24.02999548,760841.5,Ukraine,UA,UKR,L'viv
Odessa,Odessa,46.4900163,30.71000118,847500.5,Ukraine,UA,UKR,Odessa
Zhytomyr,Zhytomyr,50.24557517,28.66216752,278581,Ukraine,UA,UKR,Zhytomyr
Dnipropetrovsk,Dnipropetrovsk,48.47997235,35.00002356,949424.5,Ukraine,UA,UKR,Dnipropetrovs'k
Donetsk,Donetsk,48.00000165,37.82998002,874137.5,Ukraine,UA,UKR,Donets'k
Kharkiv,Kharkiv,49.99998293,36.25002478,1338063.5,Ukraine,UA,UKR,Kharkiv
Sevastapol,Sevastapol,44.59997662,33.46497514,346832.5,Ukraine,UA,UKR,Crimea
Kiev,Kiev,50.43336733,30.51662797,2185754,Ukraine,UA,UKR,Kiev
Umm al Qaywayn,Umm al Qaywayn,25.56527285,55.55334265,38531,United Arab Emirates,AE,ARE,Umm Al Qaywayn
Sharjah,Sharjah,25.37138287,55.40647823,952015.5,United Arab Emirates,AE,ARE,Sharjah
Jabal Ali,Jabal Ali,24.97623903,55.01074011,55817,United Arab Emirates,AE,ARE,Dubay
Ras al Khaymah,Ras al Khaymah,25.79153811,55.94277624,138399,United Arab Emirates,AE,ARE,Ras Al Khaymah
Al Fujayrah,Al Fujayrah,25.12343935,56.33748083,78289,United Arab Emirates,AE,ARE,Fujayrah
Al Ayn,Al Ayn,24.2304706,55.73999792,352500.5,United Arab Emirates,AE,ARE,Abu Dhabi
Abu Dhabi,Abu Dhabi,24.46668357,54.36659338,581861,United Arab Emirates,AE,ARE,Abu Dhabi
Dubai,Dubai,25.22999615,55.27997432,1258173.5,United Arab Emirates,AE,ARE,Dubay
Greenock,Greenock,55.93329002,-4.750030763,59065,United Kingdom,GB,GBR,Inverclyde
Sunderland,Sunderland,54.92001853,-1.380029746,315449.5,United Kingdom,GB,GBR,Tyne and Wear
Southampton,Southampton,50.90003135,-1.399976849,384417,United Kingdom,GB,GBR,Southampton
Bristol,Bristol,51.44999778,-2.583315472,492120.5,United Kingdom,GB,GBR,Bristol
Bournemouth,Bournemouth,50.72999005,-1.900049684,295272.5,United Kingdom,GB,GBR,Bournemouth
Omagh,Omagh,54.60001223,-7.300004315,18691,United Kingdom,GB,GBR,Omagh
Chester,Chester,53.20002016,-2.919987428,83285.5,United Kingdom,GB,GBR,Cheshire
Swansea,Swansea,51.6299868,-3.950002077,232611,United Kingdom,GB,GBR,Swansea
Carlisle,Carlisle,54.87999514,-2.929986818,69270,United Kingdom,GB,GBR,Cumbria
Southend-on-Sea,Southend,51.55001752,0.71999711,395993,United Kingdom,GB,GBR,Southend-on-Sea
Reading,Reading,51.46997072,-0.980028322,257752,United Kingdom,GB,GBR,Oxfordshire
Leicester,Leicester,52.62997744,-1.133248943,398611,United Kingdom,GB,GBR,Leicester
Bradford,Bradford,53.80003522,-1.749981325,397708.5,United Kingdom,GB,GBR,West Yorkshire
Sheffield,Sheffield,53.36667666,-1.499996583,922800,United Kingdom,GB,GBR,South Yorkshire
Fort William,Fort William,56.81647795,-5.112075806,9652,United Kingdom,GB,GBR,Highland
Ayr,Ayr,55.4503996,-4.61667973,57277.5,United Kingdom,GB,GBR,South Ayrshire
Aberdeen,Aberdeen,57.17039797,-2.079987021,186577,United Kingdom,GB,GBR,Aberdeen
Perth,Perth,56.40034161,-3.469979697,39654,United Kingdom,GB,GBR,Perthshire and Kinross
Dundee,Dundee,56.47038902,-3.000008384,151013.5,United Kingdom,GB,GBR,Dundee
Middlesbrough,Middlesbrough,54.58037518,-1.230013063,279374.5,United Kingdom,GB,GBR,Stockton-on-Tees
Coventry,Coventry,52.42040367,-1.499996583,348292,United Kingdom,GB,GBR,West Midlands
Bath,Bath,51.3837486,-2.350022218,92679,United Kingdom,GB,GBR,Bath and North East Somerset
Exeter,Exeter,50.70040529,-3.529950197,108242,United Kingdom,GB,GBR,Devon
Cambridge,Cambridge,52.20039125,0.116623086,128488,United Kingdom,GB,GBR,Cambridgeshire
Kingston upon Hull,Kingston upon Hull,53.75042584,-0.32999048,297398.5,United Kingdom,GB,GBR,Kingston upon Hull
Londonderry,Londonderry,55.00037539,-7.333283937,82635,United Kingdom,GB,GBR,Derry
Lisburn,Lisburn,54.52037884,-6.670016929,12899,United Kingdom,GB,GBR,Dungannon
Penzance,Penzance,50.13372154,-5.550033611,18150.5,United Kingdom,GB,GBR,Cornwall
York,York,53.97038658,-1.080022218,151574.5,United Kingdom,GB,GBR,York
Blackpool,Blackpool,53.83039512,-3.050005332,207946.5,United Kingdom,GB,GBR,Lancashire
Dumfries,Dumfries,55.06708966,-3.550000652,31044,United Kingdom,GB,GBR,Dumfries and Galloway
Scarborough,Scarborough,54.28039349,-0.429984376,70571,United Kingdom,GB,GBR,North Yorkshire
Plymouth,Plymouth,50.38538576,-4.159989259,239436,United Kingdom,GB,GBR,Plymouth
Ipswich,Ipswich,52.07034751,1.169995482,139012,United Kingdom,GB,GBR,Suffolk
Norwich,Norwich,52.63036501,1.300013386,184196,United Kingdom,GB,GBR,Norfolk
Brighton,Brighton,50.83034568,-0.169974407,321004.5,United Kingdom,GB,GBR,Brighton and Hove
Kirkwall,Kirkwall,58.96698081,-2.950011435,5826.5,United Kingdom,GB,GBR,Moray
Inverness,Inverness,57.46712404,-4.23326644,42956.5,United Kingdom,GB,GBR,Highland
Oxford,Oxford,51.7704175,-1.249986004,173681,United Kingdom,GB,GBR,Oxfordshire
Luton,Luton,51.88035911,-0.420010825,214813.5,United Kingdom,GB,GBR,Luton
Portsmouth,Portsmouth,50.80034751,-1.080022218,323676,United Kingdom,GB,GBR,Portsmouth
Peterborough,Peterborough,52.58041974,-0.249995363,140141,United Kingdom,GB,GBR,Peterborough
Nottingham,Nottingham,52.97034426,-1.170016725,565650,United Kingdom,GB,GBR,Nottingham
Stoke,Stoke,53.00036826,-2.180006756,325610,United Kingdom,GB,GBR,Stoke-on-Trent
Dover,Dover,51.13371218,1.300013386,32270,United Kingdom,GB,GBR,Kent
Edinburgh,Edinburgh,55.94832786,-3.219090618,470378.5,United Kingdom,GB,GBR,Edinburgh
Newcastle,Newcastle,55.00037539,-1.59999048,537191,United Kingdom,GB,GBR,Tyne and Wear
Liverpool,Liverpool,53.41600181,-2.917997886,639972.5,United Kingdom,GB,GBR,Merseyside
Cardiff,Cardiff,51.49999473,-3.22500757,603750,United Kingdom,GB,GBR,Cardiff
Wick,Wick,58.43329246,-3.083362469,7147,United Kingdom,GB,GBR,Highland
Leeds,Leeds,53.83000755,-1.580017539,992061.5,United Kingdom,GB,GBR,West Yorkshire
Lerwick,Lerwick,60.15003522,-1.149992108,5604,United Kingdom,GB,GBR,Aberdeen
Manchester,Manchester,53.50041526,-2.247987103,1312757.5,United Kingdom,GB,GBR,Manchester
Birmingham,Birmingham,52.47497398,-1.919996787,1634666.5,United Kingdom,GB,GBR,West Midlands
Belfast,Belfast,54.60001223,-5.960034425,362588,United Kingdom,GB,GBR,Belfast
Glasgow,Glasgow,55.87440472,-4.250707236,885134,United Kingdom,GB,GBR,Glasgow
London,London,51.49999473,-0.116721844,7994104.5,United Kingdom,GB,GBR,Westminster
Faribault,Faribault,44.29048647,-93.26801274,24004.5,United States of America,US,USA,Minnesota
Mankato,Mankato,44.16362083,-93.99915674,45731.5,United States of America,US,USA,Minnesota
Albert Lea,Albert Lea,43.64778668,-93.36870427,19063.5,United States of America,US,USA,Minnesota
Willmar,Willmar,45.12188275,-95.04330489,18432,United States of America,US,USA,Minnesota
Brainerd,Brainerd,46.35800885,-94.20084986,21202.5,United States of America,US,USA,Minnesota
Crookston,Crookston,47.77376223,-96.60773137,8215.5,United States of America,US,USA,Minnesota
Hardin,Hardin,45.731768,-107.612486,3975.5,United States of America,US,USA,Montana
Glendive,Glendive,47.10858319,-104.7104926,5277.5,United States of America,US,USA,Montana
Dillon,Dillon,45.21567548,-112.6839852,4213.5,United States of America,US,USA,Montana
Polson,Polson,47.68800519,-114.156686,5079,United States of America,US,USA,Montana
Devils Lake,Devils Lake,48.11221702,-98.85968693,7312,United States of America,US,USA,North Dakota
Burley,Burley,42.53581321,-113.7918763,11644.5,United States of America,US,USA,Idaho
Wallace,Wallace,47.47421979,-115.9268881,1028,United States of America,US,USA,Idaho
Kennewick,Kennewick,46.21137697,-119.1360979,82331,United States of America,US,USA,Washington
Centralia,Centralia,46.71641075,-122.9529708,16993.5,United States of America,US,USA,Washington
Glendale,Glendale,33.58194114,-112.1958238,363360.5,United States of America,US,USA,Arizona
Safford,Safford,32.83382143,-109.7068801,9746.5,United States of America,US,USA,Arizona
Casa Grande,Casa Grande,32.87937421,-111.7566258,38396.5,United States of America,US,USA,Arizona
Mesa,Mesa,33.42391461,-111.7360844,762217.5,United States of America,US,USA,Arizona
Lake Havasu City,Lake Havasu City,34.49829348,-114.3082789,55442.5,United States of America,US,USA,Arizona
Berkeley,Berkeley,37.87390139,-122.271152,298257,United States of America,US,USA,California
National City,National City,32.67194501,-117.0980052,104291,United States of America,US,USA,California
Mendocino,Mendocino,39.30776735,-123.7994308,548,United States of America,US,USA,California
Paso Robles,Paso Robles,35.6265967,-120.6899823,26221,United States of America,US,USA,California
Riverside,Riverside,33.94194501,-117.3980386,297554,United States of America,US,USA,California
Delano,Delano,35.76193728,-119.2430681,42396.5,United States of America,US,USA,California
San Mateo,San Mateo,37.55691815,-122.3130616,361806.5,United States of America,US,USA,California
Vallejo,Vallejo,38.11194887,-122.258052,133367.5,United States of America,US,USA,California
Glenwood Springs,Glenwood Springs,39.54658999,-107.3247,11272,United States of America,US,USA,Colorado
Aurora,Aurora,39.69585736,-104.808497,431966.5,United States of America,US,USA,Colorado
Greeley,Greeley,40.41919822,-104.739974,106142.5,United States of America,US,USA,Colorado
Tonopah,Tonopah,38.06699038,-117.2289791,1993,United States of America,US,USA,Nevada
Deming,Deming,32.26109153,-107.7557848,15523,United States of America,US,USA,New Mexico
Truth or Consequences,Truth or Consequences,33.13359641,-107.2528956,6479,United States of America,US,USA,New Mexico
Las Vegas,Las Vegas,35.59701194,-105.2225027,15521,United States of America,US,USA,New Mexico
Farmington,Farmington,36.75415061,-108.1860944,42917.5,United States of America,US,USA,New Mexico
Springfield,Springfield,44.05194806,-122.9780339,55531.5,United States of America,US,USA,Oregon
Tillamook,Tillamook,45.45524742,-123.8425031,6351.5,United States of America,US,USA,Oregon
Ontario,Ontario,44.02662661,-116.9618895,11578,United States of America,US,USA,Oregon
La Grande,La Grande,45.32468691,-118.0866012,13646,United States of America,US,USA,Oregon
Richfield,Richfield,38.77247703,-112.0832984,7308.5,United States of America,US,USA,Utah
Nephi,Nephi,39.71027508,-111.8354841,4960,United States of America,US,USA,Utah
Lander,Lander,42.83300437,-108.7325985,6742,United States of America,US,USA,Wyoming
Powell,Powell,44.75867495,-108.7584367,6054,United States of America,US,USA,Wyoming
Paragould,Paragould,36.05708722,-90.50288436,22886,United States of America,US,USA,Arkansas
Iowa City,Iowa City,41.66108624,-91.52997929,81343,United States of America,US,USA,Iowa
Ottumwa,Ottumwa,41.01288291,-92.414809,25287.5,United States of America,US,USA,Iowa
Spencer,Spencer,43.14528505,-95.14717452,10938.5,United States of America,US,USA,Iowa
Ft. Dodge,Ft. Dodge,42.50682273,-94.1802568,26284,United States of America,US,USA,Iowa
Hutchinson,Hutchinson,38.06549176,-97.92349085,42536.5,United States of America,US,USA,Kansas
Kansas City,Kansas City,39.11358052,-94.63014638,324221.5,United States of America,US,USA,Kansas
Lawrence,Lawrence,38.95975242,-95.25522994,88020,United States of America,US,USA,Kansas
Garden City,Garden City,37.97521303,-100.8640866,27494.5,United States of America,US,USA,Kansas
Manhattan,Manhattan,39.19402753,-96.59243514,51289,United States of America,US,USA,Kansas
Hays,Hays,38.87936973,-99.322191,20638.5,United States of America,US,USA,Kansas
Goodland,Goodland,39.34848838,-101.7110374,4258.5,United States of America,US,USA,Kansas
Independence,Independence,39.09111391,-94.41528121,130695,United States of America,US,USA,Missouri
Kirksville,Kirksville,40.19368227,-92.58280908,18083,United States of America,US,USA,Missouri
Kearney,Kearney,40.70070559,-99.08114628,30155.5,United States of America,US,USA,Nebraska
Grand Island,Grand Island,40.92226829,-98.35798629,45208.5,United States of America,US,USA,Nebraska
Alliance,Alliance,42.10139528,-102.8701915,8269,United States of America,US,USA,Nebraska
Bartlesville,Bartlesville,36.74720013,-95.98058618,24935,United States of America,US,USA,Oklahoma
Enid,Enid,36.39554201,-97.8780931,45963.5,United States of America,US,USA,Oklahoma
Ardmore,Ardmore,34.1810777,-97.12940495,24467.5,United States of America,US,USA,Oklahoma
McAlester,McAlester,34.93299562,-95.76597396,19894,United States of America,US,USA,Oklahoma
Stillwater,Stillwater,36.13535118,-97.06829757,45212,United States of America,US,USA,Oklahoma
Lead,Lead,44.35084454,-103.7657699,2311,United States of America,US,USA,South Dakota
Slidell,Slidell,30.27495953,-89.78109379,56019,United States of America,US,USA,Louisiana
Lake Charles,Lake Charles,30.22638369,-93.21718897,77065,United States of America,US,USA,Louisiana
Metairie,Metairie,29.98386619,-90.15277653,270171,United States of America,US,USA,Louisiana
New Iberia,New Iberia,30.00358075,-91.81830794,34985,United States of America,US,USA,Louisiana
Bryan,Bryan,30.67418581,-96.36968388,108156.5,United States of America,US,USA,Texas
San Marcos,San Marcos,29.88307131,-97.94111251,58553.5,United States of America,US,USA,Texas
Longview,Longview,32.50053428,-94.74027429,75658,United States of America,US,USA,Texas
McAllen,McAllen,26.20303754,-98.22972538,243291,United States of America,US,USA,Texas
Harlingen,Harlingen,26.19755983,-97.69019759,86749,United States of America,US,USA,Texas
Alice,Alice,27.75046246,-98.07048446,21122,United States of America,US,USA,Texas
New Braunfels,New Braunfels,29.6978113,-98.12632084,45270,United States of America,US,USA,Texas
Cleburne,Cleburne,32.35152529,-97.39248967,32263,United States of America,US,USA,Texas
Brownwood,Brownwood,31.70789532,-98.98231511,20261,United States of America,US,USA,Texas
Alpine,Alpine,30.36071657,-103.6650009,6429.5,United States of America,US,USA,Texas
Van Horn,Van Horn,31.04248374,-104.8322423,1797,United States of America,US,USA,Texas
Big Spring,Big Spring,32.24318565,-101.4751862,23987,United States of America,US,USA,Texas
Vernon,Vernon,34.15105369,-99.29038416,11574.5,United States of America,US,USA,Texas
Childress,Childress,34.4248871,-100.2139195,5662,United States of America,US,USA,Texas
Hereford,Hereford,34.82191713,-102.3985924,15023.5,United States of America,US,USA,Texas
Dalhart,Dalhart,36.06080792,-102.5186109,6763.5,United States of America,US,USA,Texas
Texas City,Texas City,29.41087791,-94.96276717,55717.5,United States of America,US,USA,Texas
Pasadena,Pasadena,29.66086265,-95.14774296,388767.5,United States of America,US,USA,Texas
Baytown,Baytown,29.75584393,-94.96772811,76687.5,United States of America,US,USA,Texas
Arlington,Grand Prairie,32.68476076,-97.02023849,545107.5,United States of America,US,USA,Texas
New London,New London,41.3555235,-72.10002832,61236,United States of America,US,USA,Connecticut
Stamford,Stamford,41.05334556,-73.53919112,434781.5,United States of America,US,USA,Connecticut
Waterbury,Waterbury,41.55000775,-73.05002202,174236,United States of America,US,USA,Connecticut
New Bedford,New Bedford,41.6561253,-70.94469833,115082.5,United States of America,US,USA,Massachusetts
Springfield,Springfield,42.12002464,-72.57999903,287003.5,United States of America,US,USA,Massachusetts
Salem,Salem,42.5224989,-70.88309175,188982,United States of America,US,USA,Massachusetts
Pittsfield,Pittsfield,42.44819582,-73.25982833,45202,United States of America,US,USA,Massachusetts
Montpelier,Montpelier,44.25997154,-72.57581323,8183,United States of America,US,USA,Vermont
Auburn,Auburn,32.60970074,-85.48083948,61881,United States of America,US,USA,Alabama
Florence,Florence,34.79969627,-87.67724288,40806.5,United States of America,US,USA,Alabama
Winter Haven,Winter Haven,28.02191876,-81.73300623,68435,United States of America,US,USA,Florida
Melbourne,Melbourne,28.08331036,-80.60832035,170870,United States of America,US,USA,Florida
Homestead,Homestead,25.46830202,-80.47778569,60673,United States of America,US,USA,Florida
Sanford,Sanford,28.78995974,-81.27998478,189374.5,United States of America,US,USA,Florida
Miami Beach,Miami Beach,25.80991953,-80.13178111,248538,United States of America,US,USA,Florida
Coral Springs,Coral Springs,26.27083701,-80.27082158,185548,United States of America,US,USA,Florida
Port Charlotte,Port Charlotte,27.00004315,-82.10569666,56806,United States of America,US,USA,Florida
Spring Hill,Spring Hill,28.47894513,-82.54771102,91887.5,United States of America,US,USA,Florida
Palm Coast,Palm Coast,29.53800193,-81.22329574,45030,United States of America,US,USA,Florida
Palatka,Palatka,29.64768516,-81.65130579,16094.5,United States of America,US,USA,Florida
Leesburg,Leesburg,28.81050112,-81.88333297,33929,United States of America,US,USA,Florida
Lake City,Lake City,30.18971926,-82.63974675,20159.5,United States of America,US,USA,Florida
Crestview,Crestview,30.75420677,-86.57260746,19552.5,United States of America,US,USA,Florida
Panama City,Panama City,30.15861005,-85.65527328,68852.5,United States of America,US,USA,Florida
Dalton,Dalton,34.76972394,-84.97030217,45077.5,United States of America,US,USA,Georgia
Marietta,Marietta,33.95561342,-84.54324813,61360,United States of America,US,USA,Georgia
Waycross,Waycross,31.21381695,-82.35490625,17445.5,United States of America,US,USA,Georgia
La Grange,La Grange,33.03647056,-85.03187464,28887,United States of America,US,USA,Georgia
Southaven,Southaven,34.96891075,-90.00345748,79923,United States of America,US,USA,Mississippi
Meridian,Meridian,32.36418601,-88.70361434,40863.5,United States of America,US,USA,Mississippi
Laurel,Laurel,31.69737917,-89.1392725,23366,United States of America,US,USA,Mississippi
Spartanburg,Spartanburg,34.94942873,-81.93227055,81059,United States of America,US,USA,South Carolina
Orangeburg,Orangeburg,33.49680422,-80.86223251,24192.5,United States of America,US,USA,South Carolina
Galesburg,Galesburg,40.94777061,-90.37108362,32078.5,United States of America,US,USA,Illinois
Joliet,Joliet,41.52998313,-88.10667403,362946.5,United States of America,US,USA,Illinois
Cape Girardeau,Cape Girardeau,37.30582237,-89.51808659,38165.5,United States of America,US,USA,Illinois
Rockford,Rockford,42.26970542,-89.06969019,204371.5,United States of America,US,USA,Illinois
Evanston,Evanston,42.04834943,-87.69995467,212243,United States of America,US,USA,Illinois
Rock Island,Rock Island,41.49339622,-90.53461369,102055.5,United States of America,US,USA,Illinois
Elgin,Elgin,42.03946108,-88.28991866,244050,United States of America,US,USA,Illinois
Richmond,Richmond,39.82889833,-84.89028121,41015.5,United States of America,US,USA,Indiana
Terre Haute,Terre Haute,39.46664654,-87.41387394,65149.5,United States of America,US,USA,Indiana
Lafayette,Lafayette,40.41720868,-86.87824772,98104,United States of America,US,USA,Indiana
Marion,Marion,40.55833701,-85.65917485,34249,United States of America,US,USA,Indiana
South Bend,South Bend,41.68330711,-86.25001734,171791,United States of America,US,USA,Indiana
New Albany,New Albany,38.3108773,-85.82128382,78381.5,United States of America,US,USA,Indiana
Elkhart,Elkhart,41.68294537,-85.96879419,100295,United States of America,US,USA,Indiana
Hopkinsville,Hopkinsville,36.86548749,-87.4886239,31630,United States of America,US,USA,Kentucky
London,London,37.12888226,-84.08335372,7844,United States of America,US,USA,Kentucky
Madisonville,Madisonville,37.33274579,-87.5022148,20858.5,United States of America,US,USA,Kentucky
Rocky Mount,Rocky Mount,35.93799888,-77.79076624,57179,United States of America,US,USA,North Carolina
Salisbury,Salisbury,35.67078005,-80.4744784,33907,United States of America,US,USA,North Carolina
Durham,Durham,35.99995892,-78.91999964,257114.5,United States of America,US,USA,North Carolina
Lumberton,Lumberton,34.62720034,-79.01190617,27049.5,United States of America,US,USA,North Carolina
Zanesville,Zanesville,39.94028688,-82.01332503,32514,United States of America,US,USA,Ohio
Mansfield,Mansfield,40.75832481,-82.51554244,64039,United States of America,US,USA,Ohio
Bowling Green,Bowling Green,41.37474713,-83.65139042,33147.5,United States of America,US,USA,Ohio
Springfield,Springfield,39.92000388,-83.799986,74450.5,United States of America,US,USA,Ohio
Lancaster,Lancaster,39.71921511,-82.6053044,42356,United States of America,US,USA,Ohio
Johnson City,Johnson City,36.31332481,-82.35361434,68070.5,United States of America,US,USA,Tennessee
Kingsport,Kingsport,36.54832338,-82.56194788,50709.5,United States of America,US,USA,Tennessee
Columbia,Columbia,35.61499534,-87.03526656,74866,United States of America,US,USA,Tennessee
Barlett,Barlett,35.22290041,-89.84109013,164843.5,United States of America,US,USA,Tennessee
Blacksburg,Blacksburg,37.22941876,-80.41419784,53845.5,United States of America,US,USA,Virginia
Harrisonburg,Harrisonburg,38.44942181,-78.86917586,42131.5,United States of America,US,USA,Virginia
Petersburg,Petersburg,37.22776512,-77.40223698,76158.5,United States of America,US,USA,Virginia
Hampton,Hampton,37.03002525,-76.34994979,256601.5,United States of America,US,USA,Virginia
Sheboygan,Sheboygan,43.75082949,-87.71442407,51148,United States of America,US,USA,Wisconsin
Waukesha,Waukesha,43.0116498,-88.23136926,159012,United States of America,US,USA,Wisconsin
La Crosse,La Crosse,43.80136904,-91.23942855,69599.5,United States of America,US,USA,Wisconsin
Eau Claire,Eau Claire,44.81135907,-91.49835331,71296,United States of America,US,USA,Wisconsin
Tomah,Tomah,43.98505292,-90.50389205,10796.5,United States of America,US,USA,Wisconsin
Janesville,Janesville,42.68262596,-89.02157943,65476.5,United States of America,US,USA,Wisconsin
Appleton,Appleton,44.26867902,-88.40050623,136888.5,United States of America,US,USA,Wisconsin
Parkersburg,Parkersburg,39.26665875,-81.56164718,46749.5,United States of America,US,USA,West Virginia
White Sulphur Springs,White Sulphur Springs,37.79388043,-80.30348108,2154,United States of America,US,USA,West Virginia
Clarksburg,Clarksburg,39.28327272,-80.33691573,22502.5,United States of America,US,USA,West Virginia
Dover,Dover,39.15808657,-75.524703,54662.5,United States of America,US,USA,Delaware
St. Charles,St. Charles,38.60305585,-76.93893193,52792,United States of America,US,USA,Maryland
Annapolis,Annapolis,38.9783301,-76.49249923,58776,United States of America,US,USA,Maryland
Hagerstown,Hagerstown,39.64164878,-77.72027958,58487.5,United States of America,US,USA,Maryland
Paterson,Paterson,40.91999453,-74.17000533,151205,United States of America,US,USA,New Jersey
Saratoga Springs,Saratoga Springs,43.08296328,-73.78501591,41891,United States of America,US,USA,New York
Poughkeepsie,Poughkeepsie,41.70023114,-73.92141585,100670.5,United States of America,US,USA,New York
Plattsburg,Plattsburg,44.69498374,-73.45798161,24233.5,United States of America,US,USA,New York
Beaver Falls,Beaver Falls,40.75194277,-80.31942326,64814.5,United States of America,US,USA,Pennsylvania
Altoona,Altoona,40.51859784,-78.39496708,62784.5,United States of America,US,USA,Pennsylvania
Williamsport,Williamsport,41.24108604,-77.0013829,43791.5,United States of America,US,USA,Pennsylvania
Lancaster,Lancaster,40.03777447,-76.30576644,209489,United States of America,US,USA,Pennsylvania
Allentown,Allentown,40.59998822,-75.50002751,300980.5,United States of America,US,USA,Pennsylvania
Waterville,Waterville,44.5518917,-69.64578536,20529,United States of America,US,USA,Maine
Calais,Calais,45.16598859,-67.24239201,1781.5,United States of America,US,USA,Maine
Houlton,Houlton,46.12551658,-67.83971989,6051.5,United States of America,US,USA,Maine
Benton Harbor,Benton Harbor,42.11663983,-86.45419092,34637.5,United States of America,US,USA,Michigan
Battle Creek,Battle Creek,42.32109764,-85.17974675,62454,United States of America,US,USA,Michigan
Bay City,Bay City,43.5944566,-83.88889531,51558.5,United States of America,US,USA,Michigan
Alpena,Alpena,45.06160219,-83.43269576,14524,United States of America,US,USA,Michigan
Iron Mountain,Iron Mountain,45.82246014,-88.06409265,12011,United States of America,US,USA,Michigan
Ironwood,Ironwood,46.4558065,-90.15939112,6400,United States of America,US,USA,Michigan
Sand Point,Sand Point,55.33970868,-160.4971908,667,United States of America,US,USA,Alaska
Hydaburg,Hydaburg,55.21397992,-132.8006385,382,United States of America,US,USA,Alaska
Mekoryuk,Mekoryuk,60.38864671,-166.1899372,99,United States of America,US,USA,Alaska
Atqasuk,Atqasuk,70.4693795,-157.395778,201,United States of America,US,USA,Alaska
Port Heiden,Port Heiden,56.94909365,-158.6268915,102,United States of America,US,USA,Alaska
Perryville,Perryville,55.91861391,-159.1511489,113,United States of America,US,USA,Alaska
Dillingham,Dillingham,59.05656031,-158.4803121,1710,United States of America,US,USA,Alaska
Goodnews Bay,Goodnews Bay,59.12099265,-161.5871302,230,United States of America,US,USA,Alaska
Nyac,Nyac,61.00414329,-159.9404806,75,United States of America,US,USA,Alaska
Tununak,Tununak,60.58548667,-165.2557892,352,United States of America,US,USA,Alaska
Mountain Village,Mountain Village,62.08552431,-163.729009,755,United States of America,US,USA,Alaska
Emmonak,Emmonak,62.77698081,-164.5229916,100,United States of America,US,USA,Alaska
Kaltag,Kaltag,64.32719627,-158.7218986,190,United States of America,US,USA,Alaska
Teller,Teller,65.26359906,-166.3607864,83,United States of America,US,USA,Alaska
Koyukuk,Koyukuk,64.88028912,-157.7008499,101,United States of America,US,USA,Alaska
Kobuk,Kobuk,66.9072455,-156.8809774,151,United States of America,US,USA,Alaska
Selawik,Selawik,66.60387901,-160.0093911,832,United States of America,US,USA,Alaska
Talkeetna,Talkeetna,62.3237785,-150.1094269,1078,United States of America,US,USA,Alaska
Whittier,Whittier,60.78415672,-148.6776797,177,United States of America,US,USA,Alaska
Montana,Montana,62.07968487,-150.0727625,10,United States of America,US,USA,Alaska
Lake Minchumina,Lake Minchumina,63.88283063,-152.3121865,32,United States of America,US,USA,Alaska
Cantwell,Cantwell,63.39159446,-148.9507896,222,United States of America,US,USA,Alaska
Gulkana,Gulkana,62.27135276,-145.3821961,119,United States of America,US,USA,Alaska
Eagle,Eagle,64.78799501,-141.1999966,104,United States of America,US,USA,Alaska
Nenana,Nenana,64.56379681,-149.0930032,75,United States of America,US,USA,Alaska
Big Delta,Big Delta,64.15252993,-145.8421939,591,United States of America,US,USA,Alaska
Allakaket,Allakaket,66.56548342,-152.6454995,97,United States of America,US,USA,Alaska
Tanana,Tanana,65.17187339,-152.0787899,291.5,United States of America,US,USA,Alaska
Virginia,Virginia,47.52367413,-92.53640365,8709,United States of America,US,USA,Minnesota
Winona,Winona,44.0504236,-91.63919743,29757.5,United States of America,US,USA,Minnesota
Rochester,Rochester,44.02205324,-92.46968937,102433,United States of America,US,USA,Minnesota
Lakeville,Lakeville,44.65010276,-93.24251042,156151,United States of America,US,USA,Minnesota
Ely,Ely,47.90042116,-91.82569767,3687,United States of America,US,USA,Minnesota
Moorhead,Moorhead,46.87430808,-96.74219344,34332.5,United States of America,US,USA,Minnesota
St. Cloud,St. Cloud,45.56120994,-94.16222172,85974,United States of America,US,USA,Minnesota
Miles City,Miles City,46.4088843,-105.8399844,8399.5,United States of America,US,USA,Montana
Bozeman,Bozeman,45.68009157,-111.0378325,39049.5,United States of America,US,USA,Montana
Glasgow,Glasgow,48.18396975,-106.6352588,3144,United States of America,US,USA,Montana
Dickinson,Dickinson,46.88399742,-102.7888011,15987.5,United States of America,US,USA,North Dakota
Jamestown,Jamestown,46.90601158,-98.70297815,14954.5,United States of America,US,USA,North Dakota
Williston,Williston,48.15678794,-103.6280005,12767.5,United States of America,US,USA,North Dakota
Lihue,Lihue,21.98151227,-159.3710063,10694.5,United States of America,US,USA,Hawaii
Wahiawa,Wahiawa,21.50309186,-158.0236209,95336,United States of America,US,USA,Hawaii
Wailuku,Wailuku,20.89147544,-156.5047213,32769.5,United States of America,US,USA,Hawaii
Montpelier,Montpelier,42.32262209,-111.2969123,2775.5,United States of America,US,USA,Idaho
Twin Falls,Twin Falls,42.5609538,-114.4605693,42958.5,United States of America,US,USA,Idaho
Caldwell,Caldwell,43.66096417,-116.6705378,83403,United States of America,US,USA,Idaho
Salmon,Salmon,45.17567792,-113.8949966,3297,United States of America,US,USA,Idaho
Coeur d'Alene,Coeur d'Alene,47.67808331,-116.7794458,34514,United States of America,US,USA,Idaho
Richland,Richland,46.29181134,-119.2911013,39940.5,United States of America,US,USA,Washington
Bellingham,Bellingham,48.76013613,-122.4869269,86565.5,United States of America,US,USA,Washington
Longview,Longview,46.13871991,-122.9369511,51290,United States of America,US,USA,Washington
Walla Walla,Walla Walla,46.06515851,-118.3418828,37864,United States of America,US,USA,Washington
Aberdeen,Aberdeen,46.97489626,-123.8143911,24400,United States of America,US,USA,Washington
Bremerton,Bremerton,47.57359552,-122.6420175,82039.5,United States of America,US,USA,Washington
Everett,Everett,47.9604175,-122.1999677,291948,United States of America,US,USA,Washington
Bullhead City,Bullhead City,35.14817629,-114.5674878,37989,United States of America,US,USA,Arizona
Winslow,Winslow,35.28470542,-110.7006954,9931,United States of America,US,USA,Arizona
Gila Bend,Gila Bend,32.95037762,-112.7246546,2012,United States of America,US,USA,Arizona
Tombstone,Tombstone,31.71314048,-110.066884,1396.5,United States of America,US,USA,Arizona
Willcox,Willcox,32.25321088,-109.8313945,4451.5,United States of America,US,USA,Arizona
Scottsdale,Scottsdale,33.69234784,-111.8680402,15401,United States of America,US,USA,Arizona
Kingman,Kingman,35.18987917,-114.0522221,33306.5,United States of America,US,USA,Arizona
Grand Canyon,Grand Canyon,36.05478762,-112.1385922,1068.5,United States of America,US,USA,Arizona
Arcata,Arcata,40.88519045,-124.0882245,19052,United States of America,US,USA,California
Stockton,Stockton,37.95813397,-121.289739,488506.5,United States of America,US,USA,California
Barstow,Barstow,34.89901837,-117.0218858,21119,United States of America,US,USA,California
Victorville,Victoriaville,34.5365082,-117.2903191,83496,United States of America,US,USA,California
Pasadena,Pasadena,34.16038129,-118.1388719,144618,United States of America,US,USA,California
Visalia,Visalia,36.32502952,-119.3160094,114699.5,United States of America,US,USA,California
El Centro,El Centro,32.79237693,-115.5580475,41661.5,United States of America,US,USA,California
San Luis Obispo,San Luis Obispo,35.28318097,-120.6585889,54759,United States of America,US,USA,California
Merced,Merced,37.30261843,-120.481933,84355,United States of America,US,USA,California
Yuba City,Yuba City,39.14103334,-121.6157656,84324.5,United States of America,US,USA,California
Redding,Redding,40.58704327,-122.3905762,93871.5,United States of America,US,USA,California
Santa Rosa,Santa Rosa,38.45040367,-122.6999889,193455,United States of America,US,USA,California
Oceanside,Oceanside,33.2204645,-117.3349675,396474.5,United States of America,US,USA,California
Modesto,Modesto,37.65541343,-120.9899899,269697,United States of America,US,USA,California
Irvine,Irvine,33.68041058,-117.8299502,1611303.5,United States of America,US,USA,California
Ukiah,Ukiah,39.15423667,-123.2108621,21826.5,United States of America,US,USA,California
Needles,Needles,34.84842714,-114.6133507,6246.5,United States of America,US,USA,California
Bishop,Bishop,37.36395835,-118.394076,4249,United States of America,US,USA,California
Palm Springs,Palm Springs,33.77735557,-116.5330526,216461,United States of America,US,USA,California
Santa Maria,Santa Maria,34.94012697,-120.4366386,98092.5,United States of America,US,USA,California
Tulare,Tulare,36.20702639,-119.3441213,53005.5,United States of America,US,USA,California
Mt. Shasta,Mt. Shasta,41.3103583,-122.3093925,3742.5,United States of America,US,USA,California
Crescent City,Crescent City,41.7564551,-124.2004916,9439.5,United States of America,US,USA,California
Fort Collins,Fort Collins,40.56068829,-105.0588693,178818.5,United States of America,US,USA,Colorado
Pueblo,Pueblo,38.2803882,-104.6300066,108244,United States of America,US,USA,Colorado
Lamar,Lamar,38.08649823,-102.6194058,8567,United States of America,US,USA,Colorado
Trinidad,Trinidad,37.17133445,-104.5063965,8701.5,United States of America,US,USA,Colorado
Gunnison,Gunnison,38.54476483,-106.92829,6273,United States of America,US,USA,Colorado
Durango,Durango,37.27564333,-107.8799891,19127.5,United States of America,US,USA,Colorado
Montrose,Montrose,38.47727541,-107.8655197,18463.5,United States of America,US,USA,Colorado
Craig,Craig,40.51728009,-107.5503968,9315.5,United States of America,US,USA,Colorado
Boulder,Boulder,40.03844627,-105.246093,106897.5,United States of America,US,USA,Colorado
Boulder City,Boulder City,35.97895245,-114.8315802,15072.5,United States of America,US,USA,Nevada
Winnemucca,Winnemucca,40.97337628,-117.7346847,7997.5,United States of America,US,USA,Nevada
Roswell,Roswell,33.39453656,-104.5224679,45082.5,United States of America,US,USA,New Mexico
Clovis,Clovis,34.40506919,-103.2047706,33477.5,United States of America,US,USA,New Mexico
Las Cruces,Las Cruces,32.31261293,-106.7778083,97675.5,United States of America,US,USA,New Mexico
Hobbs,Hobbs,32.71261436,-103.1406143,28375.5,United States of America,US,USA,New Mexico
Socorro,Socorro,34.06211855,-106.8989895,8117,United States of America,US,USA,New Mexico
Gallup,Gallup,35.52407066,-108.7339938,21627,United States of America,US,USA,New Mexico
Raton,Raton,36.89739768,-104.439889,6820,United States of America,US,USA,New Mexico
Tucumcari,Tucumcari,35.16980288,-103.725514,5259.5,United States of America,US,USA,New Mexico
Roseburg,Roseburg,43.21843304,-123.3560987,25454.5,United States of America,US,USA,Oregon
Pendleton,Pendleton,45.67259849,-118.7874886,16669,United States of America,US,USA,Oregon
John Day,John Day,44.41652529,-118.9520264,1437.5,United States of America,US,USA,Oregon
Grants Pass,Grants Pass,42.43954002,-123.3271857,36690,United States of America,US,USA,Oregon
Corvallis,Corvallis,44.57235557,-123.2799793,54865.5,United States of America,US,USA,Oregon
Albany,Albany,44.62049217,-123.086942,48066.5,United States of America,US,USA,Oregon
Astoria,Astoria,46.18838096,-123.8299974,9773,United States of America,US,USA,Oregon
Logan,Logan,41.73593955,-111.8335979,58664,United States of America,US,USA,Utah
Parowan,Parowan,37.84253379,-112.8272065,2533,United States of America,US,USA,Utah
Kanab,Kanab,37.04738853,-112.5254936,2861,United States of America,US,USA,Utah
Monticello,Monticello,37.87178265,-109.3421995,1811.5,United States of America,US,USA,Utah
Moab,Moab,38.57370363,-109.5491895,5309,United States of America,US,USA,Utah
Price,Price,39.59979087,-110.8100169,9175,United States of America,US,USA,Utah
Cedar City,Cedar City,37.67742759,-113.061094,25371.5,United States of America,US,USA,Utah
Vernal,Vernal,40.45539756,-109.5280022,11175.5,United States of America,US,USA,Utah
Ogden,Ogden,41.23237856,-111.9680341,227774,United States of America,US,USA,Utah
Green River,Green River,41.51455772,-109.4649827,10239.5,United States of America,US,USA,Wyoming
Rawlins,Rawlins,41.7906649,-107.234292,8458,United States of America,US,USA,Wyoming
Douglas,Douglas,42.75647158,-105.3845341,5838,United States of America,US,USA,Wyoming
Riverton,Riverton,43.02816042,-108.3950481,10350,United States of America,US,USA,Wyoming
Thermopolis,Thermopolis,43.64597801,-108.2146715,3195,United States of America,US,USA,Wyoming
Gillette,Gillette,44.28317425,-105.5052503,26107,United States of America,US,USA,Wyoming
Jonesboro,Jonesboro,35.84257835,-90.70416406,58322,United States of America,US,USA,Arkansas
Texarkana,Texarkana,33.44210472,-94.03747481,52169,United States of America,US,USA,Arkansas
Pine Bluff,Pine Bluff,34.22869753,-92.00305119,51472,United States of America,US,USA,Arkansas
Hot Springs,Hot Springs,34.50395205,-93.05500248,40826,United States of America,US,USA,Arkansas
Fort Smith,Fort Smith,35.38622377,-94.39835718,87986.5,United States of America,US,USA,Arkansas
Fayetteville,Fayetteville,36.06297833,-94.15720911,108267.5,United States of America,US,USA,Arkansas
Conway,Conway,35.09128054,-92.4513184,56759.5,United States of America,US,USA,Arkansas
El Dorado,El Dorado,33.21392743,-92.66251998,21384.5,United States of America,US,USA,Arkansas
Davenport,Davenport,41.55398684,-90.58753036,178282.5,United States of America,US,USA,Iowa
Burlington,Burlington,40.80793418,-91.11276961,27690.5,United States of America,US,USA,Iowa
Dubuque,Dubuque,42.50093162,-90.66445073,59834,United States of America,US,USA,Iowa
Waterloo,Waterloo,42.49315432,-92.34279789,82091.5,United States of America,US,USA,Iowa
Sioux City,Sioux City,42.50038902,-96.39999211,87090,United States of America,US,USA,Iowa
Council Bluffs,Council Bluffs,41.26227338,-95.86080021,80284.5,United States of America,US,USA,Iowa
Ames,Ames,42.05385297,-93.61972254,56855,United States of America,US,USA,Iowa
Mason City,Mason City,43.15401837,-93.20083338,27327,United States of America,US,USA,Iowa
Emporia,Emporia,38.40423077,-96.18137496,27796.5,United States of America,US,USA,Kansas
Salina,Salina,38.82467023,-97.6071794,46877,United States of America,US,USA,Kansas
Dodge City,Dodge City,37.76005821,-100.018195,25237.5,United States of America,US,USA,Kansas
Coffeyville,Coffeyville,37.03806093,-95.6263184,10955,United States of America,US,USA,Kansas
St. Charles,St. Charles,38.78428509,-90.50616581,213139.5,United States of America,US,USA,Missouri
Poplar Bluff,Poplar Bluff,36.76019676,-90.40268376,18575,United States of America,US,USA,Missouri
Joplin,Joplin,37.08459556,-94.51307886,60290.5,United States of America,US,USA,Missouri
Columbia,Columbia,38.95207847,-92.33390955,244754,United States of America,US,USA,Missouri
St. Joseph,St. Joseph,39.76903119,-94.84639185,74878.5,United States of America,US,USA,Missouri
McCook,McCook,40.20559369,-100.6261683,8003,United States of America,US,USA,Nebraska
Norfolk,Norfolk,42.02871238,-97.43359827,24562,United States of America,US,USA,Nebraska
North Platte,North Platte,41.13628623,-100.7705005,24709.5,United States of America,US,USA,Nebraska
Sidney,Sidney,41.13980023,-102.9782727,6221.5,United States of America,US,USA,Nebraska
Scottsbluff,Scottsbluff,41.86750775,-103.6606859,20172,United States of America,US,USA,Nebraska
Chadron,Chadron,42.82791424,-103.0030774,5686.5,United States of America,US,USA,Nebraska
Lawton,Lawton,34.59903668,-98.40997278,85795.5,United States of America,US,USA,Oklahoma
Norman,Norman,35.22791302,-97.34414636,113525,United States of America,US,USA,Oklahoma
Muskogee,Muskogee,35.74821718,-95.36943486,38995.5,United States of America,US,USA,Oklahoma
Ponca City,Ponca City,36.7073576,-97.08527328,24843,United States of America,US,USA,Oklahoma
Shawnee,Shawnee,35.34278973,-96.93378382,29160,United States of America,US,USA,Oklahoma
Woodward,Woodward,36.43342084,-99.39769027,12339.5,United States of America,US,USA,Oklahoma
Guymon,Guymon,36.68580853,-101.4795012,10843.5,United States of America,US,USA,Oklahoma
Yankton,Yankton,42.88201947,-97.39248967,14495,United States of America,US,USA,South Dakota
Brookings,Brookings,44.30676455,-96.78803044,20313.5,United States of America,US,USA,South Dakota
Mitchell,Mitchell,43.71429425,-98.02619776,14973,United States of America,US,USA,South Dakota
Aberdeen,Aberdeen,45.46511761,-98.48640222,24854,United States of America,US,USA,South Dakota
Mobridge,Mobridge,45.54012596,-100.4347071,3083.5,United States of America,US,USA,South Dakota
Houma,Houma,29.59593121,-90.71948613,48196,United States of America,US,USA,Louisiana
Monroe,Monroe,32.50960349,-92.11919397,76674.5,United States of America,US,USA,Louisiana
Conroe,Conroe,30.31206321,-95.45586369,41643,United States of America,US,USA,Texas
Nacogdoches,Nacogdoches,31.60374147,-94.65526656,30691,United States of America,US,USA,Texas
Eagle Pass,Eagle Pass,28.71102399,-100.4892774,39683,United States of America,US,USA,Texas
Edinburg,Edinburg,26.30318646,-98.1599622,114573.5,United States of America,US,USA,Texas
Kingsville,Kingsville,27.51595481,-97.8558464,24560.5,United States of America,US,USA,Texas
Port Arthur,Port Arthur,29.89898765,-93.92859257,54972,United States of America,US,USA,Texas
Huntsville,Huntsville,30.72376935,-95.55058659,34444.5,United States of America,US,USA,Texas
Killeen,Killeen,31.11728538,-97.72748214,120464,United States of America,US,USA,Texas
Lufkin,Lufkin,31.33843467,-94.72887964,38465.5,United States of America,US,USA,Texas
Del Rio,Del Rio,29.36294802,-100.8963843,35803.5,United States of America,US,USA,Texas
San Angelo,San Angelo,31.4640084,-100.4366966,87297.5,United States of America,US,USA,Texas
Sherman,Sherman,33.63599469,-96.60858403,38696,United States of America,US,USA,Texas
Beaumont,Beaumont,30.08626304,-94.10168278,107455.5,United States of America,US,USA,Texas
Bay City,Bay City,28.98111086,-95.96435978,17487,United States of America,US,USA,Texas
Port Lavaca,Port Lavaca,28.61601687,-96.62969385,10715.5,United States of America,US,USA,Texas
Falfurrias,Falfurrias,27.22690269,-98.14489852,5152.5,United States of America,US,USA,Texas
Beeville,Beeville,28.40597801,-97.75083989,11748,United States of America,US,USA,Texas
Fort Stockton,Fort Stockton,30.89169191,-102.8849968,7434,United States of America,US,USA,Texas
Pecos,Pecos,31.41579429,-103.4998947,7991,United States of America,US,USA,Texas
Dumas,Dumas,35.86239626,-101.9668875,13551.5,United States of America,US,USA,Texas
Denton,Denton,33.21576194,-97.12883651,138952.5,United States of America,US,USA,Texas
Midland,Midland,32.030718,-102.0974996,98141.5,United States of America,US,USA,Texas
Temple,Temple,31.10209251,-97.36300826,58432,United States of America,US,USA,Texas
New Haven,New Haven,41.33038291,-72.90000533,707883,United States of America,US,USA,Connecticut
Lowell,Lowell,42.63368837,-71.31669112,415074,United States of America,US,USA,Massachusetts
Worcester,Worcester,42.27042889,-71.80002079,232290.5,United States of America,US,USA,Massachusetts
Manchester,Manchester,42.99599184,-71.45528731,153221.5,United States of America,US,USA,New Hampshire
Newport,Newport,41.49039899,-71.31335799,35893,United States of America,US,USA,Rhode Island
Dothan,Dothan,31.22345461,-85.39058659,61715,United States of America,US,USA,Alabama
Tuscaloosa,Tuscaloosa,33.22511538,-87.54417607,100594.5,United States of America,US,USA,Alabama
Gadsden,Gadsden,34.01455039,-86.00664718,39265,United States of America,US,USA,Alabama
Enterprise,Enterprise,31.32781516,-85.84399561,23388.5,United States of America,US,USA,Alabama
Selma,Selma,32.40756838,-87.0211589,19553,United States of America,US,USA,Alabama
Coral Gables,Coral Gables,25.71541872,-80.29107874,98700.5,United States of America,US,USA,Florida
Cape Coral,Cape Coral,26.60290977,-81.97968368,117387.5,United States of America,US,USA,Florida
Naples,Naples,26.14205935,-81.79499211,141902,United States of America,US,USA,Florida
Fort Pierce,Fort Pierce,27.44678591,-80.3258053,132984,United States of America,US,USA,Florida
Kissimmee,Kissimmee,28.29205731,-81.4077806,144589.5,United States of America,US,USA,Florida
Titusville,Titusville,28.61234784,-80.80779138,47505.5,United States of America,US,USA,Florida
St. Augustine,St. Augustine,29.89487937,-81.31471135,44214,United States of America,US,USA,Florida
Ocala,Ocala,29.1873515,-82.14026819,95470,United States of America,US,USA,Florida
Fort Lauderdale,Fort Lauderdale,26.13606488,-80.14178552,1103781.5,United States of America,US,USA,Florida
Apalachicola,Apalachicola,29.72561322,-84.99252303,2134,United States of America,US,USA,Florida
Vero Beach,Vero Beach,27.64225201,-80.39112431,51650.5,United States of America,US,USA,Florida
Valdosta,Valdosta,30.8328583,-83.27859664,53420,United States of America,US,USA,Georgia
Albany,Albany,31.57873008,-84.15582992,82280,United States of America,US,USA,Georgia
Athens,Athens,33.96129783,-83.3780221,78017.5,United States of America,US,USA,Georgia
Macon,Macon,32.85038373,-83.63004806,104932.5,United States of America,US,USA,Georgia
Columbus,Columbus,32.47043276,-84.98001734,202225,United States of America,US,USA,Georgia
Douglas,Douglas,31.50777834,-82.85068994,12159,United States of America,US,USA,Georgia
Dublin,Dublin,32.53745709,-82.91828272,19258.5,United States of America,US,USA,Georgia
Gulfport,Gulfport,30.3675637,-89.09276371,76646,United States of America,US,USA,Mississippi
Hattiesburg,Hattiesburg,31.32727256,-89.2902452,53498.5,United States of America,US,USA,Mississippi
Tupelo,Tupelo,34.25792055,-88.70333012,33928,United States of America,US,USA,Mississippi
Greenville,Greenville,33.41037539,-91.06168746,36539.5,United States of America,US,USA,Mississippi
Natchez,Natchez,31.55480389,-91.38750737,20490.5,United States of America,US,USA,Mississippi
Florence,Florence,34.19567629,-79.76279057,43977.5,United States of America,US,USA,South Carolina
Greenville,Greenville,34.85292299,-82.3941545,203256.5,United States of America,US,USA,South Carolina
Sumter,Sumter,33.92065432,-80.34172164,27012,United States of America,US,USA,South Carolina
Anderson,Anderson,34.50374534,-82.6502629,43475.5,United States of America,US,USA,South Carolina
Aiken,Aiken,33.5494625,-81.72060388,36716.5,United States of America,US,USA,South Carolina
Beaufort,Beaufort,32.43216636,-80.68950403,21941,United States of America,US,USA,South Carolina
Rock Hill,Rock Hill,34.94038535,-81.03000004,77165,United States of America,US,USA,South Carolina
Decatur,Decatur,39.8407064,-88.95473596,74967.5,United States of America,US,USA,Illinois
Alton,Alton,38.89099693,-90.18422164,57386,United States of America,US,USA,Illinois
Quincy,Quincy,39.9359719,-91.40972823,43419.5,United States of America,US,USA,Illinois
Urbana,Urbana,40.10999229,-88.20418746,91792.5,United States of America,US,USA,Illinois
Bloomington,Bloomington,40.48459475,-88.99359664,99842.5,United States of America,US,USA,Illinois
Kankakee,Kankakee,41.12036989,-87.86110763,48115.5,United States of America,US,USA,Illinois
Waukegan,Waukegan,42.36404075,-87.8447262,144539,United States of America,US,USA,Illinois
Aurora,Aurora,41.76539512,-88.29999557,273949.5,United States of America,US,USA,Illinois
Carbondale,Carbondale,37.72683026,-89.22024947,28473,United States of America,US,USA,Illinois
Belleville,Belleville,38.52515362,-90.0002277,92409.5,United States of America,US,USA,Illinois
Bloomington,Bloomington,39.16565716,-86.52640873,85781.5,United States of America,US,USA,Indiana
Muncie,Muncie,40.19375979,-85.38637496,75388,United States of America,US,USA,Indiana
Kokomo,Kokomo,40.48676516,-86.13364201,53674,United States of America,US,USA,Indiana
Gary,Gary,41.58039349,-87.33000309,335737,United States of America,US,USA,Indiana
Fort Wayne,Fort Wayne,41.08039817,-85.12998234,264793,United States of America,US,USA,Indiana
Covington,Covington,39.0840084,-84.50859908,313064.5,United States of America,US,USA,Kentucky
Bowling Green,Bowling Green,36.99069948,-86.44364893,61349,United States of America,US,USA,Kentucky
Paducah,Paducah,37.08371706,-88.60000309,33812,United States of America,US,USA,Kentucky
Owensboro,Owensboro,37.77457928,-87.11332381,61151.5,United States of America,US,USA,Kentucky
Jacksonville,Jacksonville,34.75432436,-77.43055567,72651.5,United States of America,US,USA,North Carolina
Goldsboro,Goldsboro,35.38513857,-77.99305363,42922.5,United States of America,US,USA,North Carolina
Greenville,Greenville,35.61287661,-77.3666836,81661,United States of America,US,USA,North Carolina
Fayetteville,Fayetteville,35.06293601,-78.88359359,184040.5,United States of America,US,USA,North Carolina
Hickory,Hickory,35.7334894,-81.34140222,64898,United States of America,US,USA,North Carolina
Asheville,Asheville,35.60119773,-82.55414474,105775,United States of America,US,USA,North Carolina
Winston-Salem,Winston-Salem,36.10543052,-80.25999536,237491.5,United States of America,US,USA,North Carolina
Kitty Hawk,Kitty Hawk,36.07731854,-75.70471786,2109.5,United States of America,US,USA,North Carolina
Akron,Akron,41.07039878,-81.51999597,451155,United States of America,US,USA,Ohio
Lima,Lima,40.74287355,-84.10526453,54135,United States of America,US,USA,Ohio
Oak Ridge,Oak Ridge,36.01065594,-84.26972477,30471.5,United States of America,US,USA,Tennessee
Murfreesboro,Murfreesboro,35.84596315,-86.39026717,100237,United States of America,US,USA,Tennessee
Clarksville,Clarksville,36.5300816,-87.35943282,122115,United States of America,US,USA,Tennessee
Jackson,Jackson,35.61486615,-88.81389185,62638,United States of America,US,USA,Tennessee
Alexandria,Alexandria,38.82043276,-77.09998153,127273,United States of America,US,USA,Virginia
Fredericksburg,Fredericksburg,38.30351341,-77.46078638,76848,United States of America,US,USA,Virginia
Roanoke,Roanoke,37.27119916,-79.94161686,144669.5,United States of America,US,USA,Virginia
Danville,Danville,36.58625388,-79.39531946,43176,United States of America,US,USA,Virginia
Winchester,Winchester,39.1787313,-78.16663477,39418,United States of America,US,USA,Virginia
Bristol,Bristol,36.61152366,-82.17600244,31276.5,United States of America,US,USA,Virginia
Superior,Superior,46.72124249,-92.10389775,27474,United States of America,US,USA,Wisconsin
West Bend,West Bend,43.42570721,-88.18333602,31980.5,United States of America,US,USA,Wisconsin
Fond du Lac,Fond du Lac,43.77343793,-88.44691166,48079.5,United States of America,US,USA,Wisconsin
Oshkosh,Oshkosh,44.02510215,-88.54251306,67857.5,United States of America,US,USA,Wisconsin
Rhinelander,Rhinelander,45.63991315,-89.41207239,9633,United States of America,US,USA,Wisconsin
Racine,Racine,42.72771364,-87.81183415,105458.5,United States of America,US,USA,Wisconsin
Marinette,Marinette,45.10038535,-87.63047571,19170,United States of America,US,USA,Wisconsin
Wheeling,Wheeling,40.06431032,-80.72107833,40940,United States of America,US,USA,West Virginia
Morgantown,Morgantown,39.62981488,-79.95606043,43882.5,United States of America,US,USA,West Virginia
Huntington,Huntington,38.41957867,-82.44528833,66957,United States of America,US,USA,West Virginia
Beckley,Beckley,37.78018618,-81.18301396,27358,United States of America,US,USA,West Virginia
Wilmington,Wilmington,39.74626772,-75.54689803,116205.5,United States of America,US,USA,Delaware
Cumberland,Cumberland,39.65317263,-78.76277409,20831.5,United States of America,US,USA,Maryland
Atlantic City,Atlantic City,39.36463727,-74.4233232,58563.5,United States of America,US,USA,New Jersey
Newark,Newark,40.70042137,-74.17000533,280123,United States of America,US,USA,New Jersey
Schenectady,Schenectady,42.81458173,-73.93996769,104767.5,United States of America,US,USA,New York
Binghamton,Binghamton,42.09901817,-75.91832239,92687.5,United States of America,US,USA,New York
Utica,Utica,43.10117922,-75.23306706,81870,United States of America,US,USA,New York
Watertown,Watertown,43.97515688,-75.91106185,30938,United States of America,US,USA,New York
Niagara Falls,Niagara Falls,43.09482302,-79.0369434,117567,United States of America,US,USA,New York
Jamestown,Jamestown,42.09736452,-79.23553593,37916.5,United States of America,US,USA,New York
Elmira,Elmira,42.09012982,-76.80803552,46201,United States of America,US,USA,New York
York,York,39.96292116,-76.72804041,128798.5,United States of America,US,USA,Pennsylvania
Johnstown,Johnstown,40.32708498,-78.92222172,45821.5,United States of America,US,USA,Pennsylvania
Scranton,Scranton,41.40929283,-75.66267908,114701,United States of America,US,USA,Pennsylvania
State College,State College,40.79372316,-77.8602452,64880.5,United States of America,US,USA,Pennsylvania
Erie,Erie,42.12992067,-80.08499313,138991.5,United States of America,US,USA,Pennsylvania
Wilkes Barre,Wilkes Barre,41.24904421,-75.87793726,99824.5,United States of America,US,USA,Pennsylvania
Bar Harbor,Bar Harbor,44.38789654,-68.20437464,4483.5,United States of America,US,USA,Maine
Lewiston,Lewiston,44.10070477,-70.21525965,46689,United States of America,US,USA,Maine
Presque Isle,Presque Isle,46.79340863,-68.00216476,9466,United States of America,US,USA,Maine
Ann Arbor,Ann Arbor,42.30037539,-83.71999089,189893,United States of America,US,USA,Michigan
Kalamazoo,Kalamazoo,42.29215883,-85.58718958,128759.5,United States of America,US,USA,Michigan
Muskegon,Muskegon,43.23458193,-86.24836369,70644.5,United States of America,US,USA,Michigan
Flint,Flint,43.0128642,-83.68753809,206235,United States of America,US,USA,Michigan
Grand Rapids,Grand Rapids,42.96371991,-85.66994938,361934.5,United States of America,US,USA,Michigan
Pontiac,Pontiac,42.65185264,-83.29022384,67994,United States of America,US,USA,Michigan
Cadillac,Cadillac,44.25121238,-85.41360844,12177.5,United States of America,US,USA,Michigan
Traverse City,Traverse City,44.76844179,-85.62217452,28807,United States of America,US,USA,Michigan
Petoskey,Petoskey,45.37375368,-84.95518681,9424,United States of America,US,USA,Michigan
Escanaba,Escanaba,45.7456948,-87.06436039,14970,United States of America,US,USA,Michigan
Marquette,Marquette,46.54673118,-87.40658757,23711,United States of America,US,USA,Michigan
Hancock,Hancock,47.12729006,-88.5808053,10322.5,United States of America,US,USA,Michigan
Wrangell,Wrangell,56.47126752,-132.3715949,1658.5,United States of America,US,USA,Alaska
Shishmaref,Shishmaref,66.25697512,-166.0718893,254,United States of America,US,USA,Alaska
Hoonah,Hoonah,58.11540489,-135.438617,361,United States of America,US,USA,Alaska
Atka,Atka,52.19648968,-174.2004887,61,United States of America,US,USA,Alaska
Nikolski,Nikolski,52.93843406,-168.8676876,18,United States of America,US,USA,Alaska
Karluk,Karluk,57.57228558,-154.4550273,96,United States of America,US,USA,Alaska
False Pass,False Pass,54.85121136,-163.415023,35,United States of America,US,USA,Alaska
Kivalina,Kivalina,67.73149224,-164.4859034,374,United States of America,US,USA,Alaska
Newhalen,Newhalen,59.72034568,-154.8971967,160,United States of America,US,USA,Alaska
Pilot Point,Pilot Point,57.56455996,-157.5691266,68,United States of America,US,USA,Alaska
Chignik,Chignik,56.295671,-158.4022282,118,United States of America,US,USA,Alaska
King Salmon,King Salmon,58.68870323,-156.6613784,292,United States of America,US,USA,Alaska
Quinhagak,Quinhagak,59.74923281,-161.9157864,250,United States of America,US,USA,Alaska
Aniak,Aniak,61.5787077,-159.5221857,501,United States of America,US,USA,Alaska
Kotlit,Kotlit,63.03458783,-163.5532833,1002,United States of America,US,USA,Alaska
Unalakleet,Unalakleet,63.87342552,-160.7880516,741,United States of America,US,USA,Alaska
Koyuk,Koyuk,64.94026874,-161.1574717,254,United States of America,US,USA,Alaska
McGrath,McGrath,62.9568148,-155.5957845,138,United States of America,US,USA,Alaska
Hughes,Hughes,66.04918418,-154.2549878,78,United States of America,US,USA,Alaska
Ambler,Ambler,67.08648521,-157.8514091,258,United States of America,US,USA,Alaska
Wales,Wales,65.60959861,-168.0875027,99,United States of America,US,USA,Alaska
Kotzebue,Kotzebue,66.89869305,-162.5965975,2873.5,United States of America,US,USA,Alaska
Wasilla,Wasilla,61.58173077,-149.439442,8521,United States of America,US,USA,Alaska
Circle,Circle,65.82589032,-144.0605197,100,United States of America,US,USA,Alaska
Denali Park,Denali Park,63.73309816,-148.9140994,1063,United States of America,US,USA,Alaska
Yakutat,Yakutat,59.54730715,-139.7272183,109,United States of America,US,USA,Alaska
Homer,Homer,59.64293439,-151.5482797,5021.5,United States of America,US,USA,Alaska
Tanacross,Tanacross,63.38570335,-143.346403,136,United States of America,US,USA,Alaska
Wiseman,Wiseman,67.4104706,-150.1074891,14,United States of America,US,USA,Alaska
Kailua-Kona,Kailua-Kona,19.6405556,-155.9955556,9870,United States of America,US,USA,Hawaii
Butte,Butte,46.0038961,-112.5338394,31478,United States of America,US,USA,Montana
Grand Forks,Grand Forks,47.92527753,-97.0324858,53496,United States of America,US,USA,North Dakota
Pocatello,Pocatello,42.87134829,-112.4447234,57327,United States of America,US,USA,Idaho
Tacoma,Tacoma,47.21131594,-122.5150131,460273,United States of America,US,USA,Washington
Yuma,Yuma,32.68527753,-114.6236084,88402.5,United States of America,US,USA,Arizona
Prescott,Prescott,34.59001914,-112.4477723,47587,United States of America,US,USA,Arizona
Long Beach,Long Beach,33.78696739,-118.1580439,1249195.5,United States of America,US,USA,California
Grand Junction,Grand Junction,39.09385276,-108.5499998,75076,United States of America,US,USA,Colorado
Ely,Ely,39.24702171,-114.887675,3911,United States of America,US,USA,Nevada
Carson City,Carson City,39.16384849,-119.7663953,53767,United States of America,US,USA,Nevada
Carlsbad,Carlsbad,32.420565,-104.2282998,25240,United States of America,US,USA,New Mexico
Alamogordo,Alamogordo,32.89947634,-105.9597187,33710.5,United States of America,US,USA,New Mexico
Medford,Medford,42.32662701,-122.8744227,89081.5,United States of America,US,USA,Oregon
Klamath Falls,Klamath Falls,42.22500531,-121.7805359,31090.5,United States of America,US,USA,Oregon
St. George,St. George,37.10415509,-113.583336,79988,United States of America,US,USA,Utah
Provo,Provo,40.24889854,-111.63777,231238,United States of America,US,USA,Utah
Laramie,Laramie,41.31136599,-105.5905681,25587.5,United States of America,US,USA,Wyoming
Little Rock,Little Rock,34.73608258,-92.33109318,227555,United States of America,US,USA,Arkansas
Wichita,Wichita,37.71998313,-97.32998702,378543.5,United States of America,US,USA,Kansas
Jefferson City,Jefferson City,38.57662335,-92.17332503,45511,United States of America,US,USA,Missouri
Rapid City,Rapid City,44.08055096,-103.2305571,67760,United States of America,US,USA,South Dakota
Lafayette,Lafayette,30.19997703,-92.01994938,135205.5,United States of America,US,USA,Louisiana
Galveston,Galveston,29.301143,-94.7974801,62516,United States of America,US,USA,Texas
Freeport,Freeport,28.95948427,-95.35687748,43762,United States of America,US,USA,Texas
Victoria,Victoria,28.80499758,-97.00334029,63126.5,United States of America,US,USA,Texas
Odessa,Odessa,31.84556134,-102.3672248,98655,United States of America,US,USA,Texas
Wichita Falls,Wichita Falls,33.91362632,-98.49306848,97429,United States of America,US,USA,Texas
Waco,Waco,31.54917116,-97.14638066,143157,United States of America,US,USA,Texas
Lubbock,Lubbock,33.58000327,-101.8799677,212343.5,United States of America,US,USA,Texas
Hartford,Hartford,41.77002016,-72.67996708,518509.5,United States of America,US,USA,Connecticut
Providence,Providence,41.82110231,-71.4149797,663726.5,United States of America,US,USA,Rhode Island
Birmingham,Birmingham,33.53000633,-86.82499516,670142,United States of America,US,USA,Alabama
Mobile,Mobile,30.68002525,-88.04998499,221870,United States of America,US,USA,Alabama
Pensacola,Pensacola,30.42112632,-87.21693506,145319.5,United States of America,US,USA,Florida
St. Petersburg,St. Petersburg,27.77053876,-82.67938257,523314.5,United States of America,US,USA,Florida
Biloxi,Biloxi,30.39580487,-88.88530868,43857,United States of America,US,USA,Mississippi
Springfield,Springfield,39.82000999,-89.65001652,125345,United States of America,US,USA,Illinois
Frankfort,Frankfort,38.2008065,-84.87335718,32214.5,United States of America,US,USA,Kentucky
Greensboro,Greensboro,36.07000633,-79.80002344,310328,United States of America,US,USA,North Carolina
Dayton,Dayton,39.750376,-84.19998743,466067,United States of America,US,USA,Ohio
Virginia Beach,Virginia Beach,36.85321433,-75.97831873,877475.5,United States of America,US,USA,Virginia
Madison,Madison,43.07301556,-89.40111699,276036,United States of America,US,USA,Wisconsin
Green Bay,Green Bay,44.5299809,-88.00001388,149811.5,United States of America,US,USA,Wisconsin
Trenton,Trenton,40.2169625,-74.74335535,225713,United States of America,US,USA,New Jersey
Lansing,Lansing,42.73352724,-84.54673629,198821.5,United States of America,US,USA,Michigan
Gambell,Gambell,63.77971031,-171.7310787,681,United States of America,US,USA,Alaska
Palmer,Palmer,61.59971417,-149.1126919,9848,United States of America,US,USA,Alaska
Seward,Seward,60.1261607,-149.4699827,2900,United States of America,US,USA,Alaska
Duluth,Duluth,46.78333173,-92.10637822,82026.5,United States of America,US,USA,Minnesota
Bemidji,Bemidji,47.47357383,-94.88018823,14063.5,United States of America,US,USA,Minnesota
Havre,Havre,48.54523968,-109.6776829,10266.5,United States of America,US,USA,Montana
Kalispell,Kalispell,48.19776735,-114.3159786,25040,United States of America,US,USA,Montana
Idaho Falls,Idaho Falls,43.46668662,-112.0333014,65787,United States of America,US,USA,Idaho
Lewiston,Lewiston,46.41660992,-117.016589,40096.5,United States of America,US,USA,Idaho
Yakima,Yakima,46.60223167,-120.5046965,93846,United States of America,US,USA,Washington
Wenatchee,Wenatchee,47.42362856,-120.3090237,45892,United States of America,US,USA,Washington
Douglas,Douglas,31.35864016,-109.5483627,23438.5,United States of America,US,USA,Arizona
Bakersfield,Bakersfield,35.36997154,-119.0199809,367259,United States of America,US,USA,California
Oakland,Oakland,37.76892071,-122.2211034,953044,United States of America,US,USA,California
Lancaster,Lancaster,34.69804873,-118.135823,225799,United States of America,US,USA,California
Chico,Chico,39.72862022,-121.8363982,83226.5,United States of America,US,USA,California
Monterey,Monterey,36.6002582,-121.8935781,77297.5,United States of America,US,USA,California
Salinas,Salinas,36.68221702,-121.6416555,152737.5,United States of America,US,USA,California
Los Alamos,Los Alamos,35.89110252,-106.2977084,11997,United States of America,US,USA,New Mexico
Eugene,Eugene,44.05001019,-123.1000161,195183,United States of America,US,USA,Oregon
Coos Bay,Coos Bay,43.36661521,-124.2165888,23685,United States of America,US,USA,Oregon
Bend,Bend,44.071921,-121.3099962,70598.5,United States of America,US,USA,Oregon
Cody,Cody,44.52321128,-109.0571007,8976.5,United States of America,US,USA,Wyoming
Cedar Rapids,Cedar Rapids,41.96998212,-91.66002303,149338.5,United States of America,US,USA,Iowa
Springfield,Springfield,37.18001609,-93.31999923,180691,United States of America,US,USA,Missouri
Lincoln,Lincoln,40.81997479,-96.68000086,244146,United States of America,US,USA,Nebraska
Alexandria,Alexandria,31.31109784,-92.44501388,60876,United States of America,US,USA,Louisiana
Abilene,Abilene,32.4486253,-99.73278609,108008,United States of America,US,USA,Texas
Brownsville,Brownsville,25.91997988,-97.50000248,174707,United States of America,US,USA,Texas
Tyler,Tyler,32.35108604,-95.30078272,101561.5,United States of America,US,USA,Texas
Concord,Concord,43.20807192,-71.53804712,42646.5,United States of America,US,USA,New Hampshire
Huntsville,Huntsville,34.71995953,-86.60999536,185474.5,United States of America,US,USA,Alabama
Key West,Key West,24.55523114,-81.78274479,27011.5,United States of America,US,USA,Florida
West Palm Beach,West Palm Beach,26.74501996,-80.12362126,675521.5,United States of America,US,USA,Florida
Sarasota,Sarasota,27.33612083,-82.53078699,321223.5,United States of America,US,USA,Florida
Daytona Beach,Daytona Beach,29.21055422,-81.0230754,140775.5,United States of America,US,USA,Florida
Gainesville,Gainesville,29.65138002,-82.32503727,158390.5,United States of America,US,USA,Florida
Ft. Myers,Ft. Myers,26.64029767,-81.86049199,120810.5,United States of America,US,USA,Florida
Brunswick,Brunswick,31.1496865,-81.49165145,31785.5,United States of America,US,USA,Georgia
Augusta,Augusta,33.46081158,-81.98498051,152895.5,United States of America,US,USA,Georgia
Vicksburg,Vicksburg,32.3524813,-90.8777452,24669.5,United States of America,US,USA,Mississippi
Myrtle Beach,Myrtle Beach,33.68891136,-78.8869784,37333.5,United States of America,US,USA,South Carolina
Charleston,Charleston,32.79237693,-79.99210474,254295,United States of America,US,USA,South Carolina
Peoria,Peoria,40.69998212,-89.67004114,142622,United States of America,US,USA,Illinois
Evansville,Evansville,37.97469627,-87.5558291,144788,United States of America,US,USA,Indiana
Louisville,Louisville,38.22501691,-85.74870427,595819.5,United States of America,US,USA,Kentucky
Lexington,Lexington,38.05001467,-84.50002079,244972,United States of America,US,USA,Kentucky
Charlotte,Charlotte,35.20499453,-80.83003809,943574.5,United States of America,US,USA,North Carolina
Youngstown,Youngstown,41.09969932,-80.64973902,194765,United States of America,US,USA,Ohio
Canton,Canton,40.79886497,-81.37863509,168410,United States of America,US,USA,Ohio
Toledo,Toledo,41.67002626,-83.57997359,388449,United States of America,US,USA,Ohio
Columbus,Columbus,39.97997438,-82.9900096,1003418,United States of America,US,USA,Ohio
Chattanooga,Chattanooga,35.06998985,-85.25000086,206571.5,United States of America,US,USA,Tennessee
Charlottesville,Charlottesville,38.02918907,-78.47692591,61314,United States of America,US,USA,Virginia
Lynchburg,Lynchburg,37.4136194,-79.14246668,84581,United States of America,US,USA,Virginia
Wausau,Wausau,44.95915367,-89.6299919,56100.5,United States of America,US,USA,Wisconsin
Albany,Albany,42.67001691,-73.81994918,484286,United States of America,US,USA,New York
Ithaca,Ithaca,42.44057355,-76.4969434,45544.5,United States of America,US,USA,New York
Harrisburg,Harrisburg,40.27359987,-76.88474919,289210,United States of America,US,USA,Pennsylvania
Bangor,Bangor,44.80115297,-68.77834477,40843,United States of America,US,USA,Maine
Portland,Portland,43.67216158,-70.2455274,99504,United States of America,US,USA,Maine
Saginaw,Saginaw,43.4194802,-83.95082951,89457.5,United States of America,US,USA,Michigan
Ketchikan,Ketchikan,55.3562193,-131.6639895,8121,United States of America,US,USA,Alaska
Unalaska,Unalaska,53.868584,-166.5316028,1938.5,United States of America,US,USA,Alaska
Togiak,Togiak,59.07036101,-160.3783234,236,United States of America,US,USA,Alaska
Red Devil,Red Devil,61.76099632,-157.3125273,24,United States of America,US,USA,Alaska
Hooper Bay,Hooper Bay,61.53108787,-166.0965648,623,United States of America,US,USA,Alaska
Wainwright,Wainwright,70.63688865,-160.0383041,174,United States of America,US,USA,Alaska
Galena,Galena,64.73329551,-156.9269953,485,United States of America,US,USA,Alaska
Kaktovik,Kaktovik,70.08785552,-143.6029132,101,United States of America,US,USA,Alaska
Skagway,Skagway,59.45832033,-135.3138959,955,United States of America,US,USA,Alaska
Cordova,Cordova,60.5427761,-145.7574962,1622.5,United States of America,US,USA,Alaska
Kenai,Kenai,60.55435162,-151.2580131,6580.5,United States of America,US,USA,Alaska
Fort Yukon,Fort Yukon,66.56468243,-145.2737789,833,United States of America,US,USA,Alaska
Santa Cruz,Santa Cruz,36.97194629,-122.0263904,101530.5,United States of America,US,USA,California
San Bernardino,San Bernardino,34.12038373,-117.3000342,973690.5,United States of America,US,USA,California
Bridgeport,Bridgeport,41.17997866,-73.19996118,578545,United States of America,US,USA,Connecticut
Rochester,Rochester,43.17042564,-77.61994979,483177,United States of America,US,USA,New York
International Falls,International Falls,48.60112775,-93.4108464,10832,United States of America,US,USA,Minnesota
St. Paul,St. Paul,44.94398663,-93.08497481,509961,United States of America,US,USA,Minnesota
Billings,Billings,45.78830202,-108.5400004,102151.5,United States of America,US,USA,Montana
Great Falls,Great Falls,47.50029055,-111.299987,61316.5,United States of America,US,USA,Montana
Missoula,Missoula,46.87224103,-113.9930526,68010,United States of America,US,USA,Montana
Minot,Minot,48.23249392,-101.2958173,37162,United States of America,US,USA,North Dakota
Fargo,Fargo,46.8772278,-96.7894257,127472.5,United States of America,US,USA,North Dakota
Hilo,Hilo,19.69999778,-155.0900273,47720.5,United States of America,US,USA,Hawaii
Olympia,Olympia,47.03804486,-122.899434,100950,United States of America,US,USA,Washington
Spokane,Spokane,47.66999595,-117.4199494,272483.5,United States of America,US,USA,Washington
Vancouver,Vancouver,45.63030133,-122.6399925,343796.5,United States of America,US,USA,Washington
Flagstaff,Flagstaff,35.19809572,-111.6505083,60779.5,United States of America,US,USA,Arizona
Tucson,Tucson,32.20499676,-110.8899862,670953.5,United States of America,US,USA,Arizona
Santa Barbara,Santa Barbara,34.43498985,-119.7199899,135021,United States of America,US,USA,California
Fresno,Fresno,36.7477169,-119.7729841,540768,United States of America,US,USA,California
Eureka,Eureka,40.80222394,-124.1474974,34012,United States of America,US,USA,California
Colorado Springs,Colorado Springs,38.86296246,-104.7919863,427272,United States of America,US,USA,Colorado
Reno,Reno,39.52997601,-119.8200096,265363.5,United States of America,US,USA,Nevada
Elko,Elko,40.83250633,-115.7619886,17537,United States of America,US,USA,Nevada
Albuquerque,Albuquerque,35.10497479,-106.6413308,725723,United States of America,US,USA,New Mexico
Salem,Salem,44.92807029,-123.0238967,187966,United States of America,US,USA,Oregon
Casper,Casper,42.86661989,-106.3124878,56149,United States of America,US,USA,Wyoming
Topeka,Topeka,39.05000531,-95.66998499,126830.5,United States of America,US,USA,Kansas
Kansas City,Kansas City,39.10708851,-94.60409422,955272.5,United States of America,US,USA,Missouri
Tulsa,Tulsa,36.12000327,-95.93002079,669434,United States of America,US,USA,Oklahoma
Sioux Falls,Sioux Falls,43.54998903,-96.7299978,148030,United States of America,US,USA,South Dakota
Shreveport,Shreveport,32.50001752,-93.77002344,224099,United States of America,US,USA,Louisiana
Baton Rouge,Baton Rouge,30.45794578,-91.14015812,322710.5,United States of America,US,USA,Louisiana
Ft. Worth,Ft. Worth,32.73997703,-97.34003809,1090830,United States of America,US,USA,Texas
Corpus Christi,Corpus Christi,27.74281435,-97.40189478,249977.5,United States of America,US,USA,Texas
Austin,Austin,30.26694969,-97.74277836,919684,United States of America,US,USA,Texas
Amarillo,Amarillo,35.22998008,-101.8299966,178526,United States of America,US,USA,Texas
El Paso,El Paso,31.77998395,-106.5099952,658331,United States of America,US,USA,Texas
Laredo,Laredo,27.50613629,-99.50721847,322768.5,United States of America,US,USA,Texas
Burlington,Burlington,44.47579816,-73.21246688,66204,United States of America,US,USA,Vermont
Montgomery,Montgomery,32.36160219,-86.27918868,194491.5,United States of America,US,USA,Alabama
Tallahassee,Tallahassee,30.44998761,-84.28003422,187402.5,United States of America,US,USA,Florida
Orlando,Orlando,28.50997683,-81.38003036,778985,United States of America,US,USA,Florida
Jacksonville,Jacksonville,30.33002077,-81.66998682,904953.5,United States of America,US,USA,Florida
Savannah,Savannah,32.02110618,-81.10999516,155848.5,United States of America,US,USA,Georgia
Columbia,Columbia,34.0399752,-80.89998214,257185.5,United States of America,US,USA,South Carolina
Indianapolis,Indianapolis,39.74998842,-86.17004806,1104641.5,United States of America,US,USA,Indiana
Wilmington,Wilmington,34.22551943,-77.94502039,126992,United States of America,US,USA,North Carolina
Knoxville,Knoxville,35.97001243,-83.92003036,417137,United States of America,US,USA,Tennessee
Richmond,Richmond,37.55001935,-77.449986,551443,United States of America,US,USA,Virginia
Charleston,Charleston,38.34973798,-81.63272811,87113,United States of America,US,USA,West Virginia
Baltimore,Baltimore,39.29999005,-76.61998499,1432946,United States of America,US,USA,Maryland
Syracuse,Syracuse,43.04999371,-76.15001367,403873.5,United States of America,US,USA,New York
Augusta,Augusta,44.31056276,-69.77998906,21301,United States of America,US,USA,Maine
Sault Ste. Marie,Sault Ste. Marie,46.49526145,-84.34527572,50173.5,United States of America,US,USA,Michigan
Sitka,Sitka,57.06039769,-135.3275494,8110,United States of America,US,USA,Alaska
Helena,Helena,46.59274904,-112.035291,33032.5,United States of America,US,USA,Montana
Bismarck,Bismarck,46.80831728,-100.7833163,60288.5,United States of America,US,USA,North Dakota
Boise,Boise,43.60859011,-116.2274899,242029,United States of America,US,USA,Idaho
San Jose,San Jose,37.29998293,-121.8499891,1281471.5,United States of America,US,USA,California
Sacramento,Sacramento,38.57502138,-121.4700381,1035949,United States of America,US,USA,California
Las Vegas,Las Vegas,36.20999778,-115.2200061,1150717,United States of America,US,USA,Nevada
Santa Fe,Santa Fe,35.68692893,-105.9372394,80943,United States of America,US,USA,New Mexico
Portland,Portland,45.52002382,-122.6799901,1207756.5,United States of America,US,USA,Oregon
Salt Lake City,Salt Lake City,40.7750163,-111.9300519,572013,United States of America,US,USA,Utah
Cheyenne,Cheyenne,41.14000694,-104.8197107,64185,United States of America,US,USA,Wyoming
Des Moines,Des Moines,41.57998008,-93.61998092,286917.5,United States of America,US,USA,Iowa
Omaha,Omaha,41.24000083,-96.00999007,643034,United States of America,US,USA,Nebraska
Oklahoma City,Oklahoma City,35.47004295,-97.51868351,660475,United States of America,US,USA,Oklahoma
Pierre,Pierre,44.36833701,-100.350552,13734.5,United States of America,US,USA,South Dakota
San Antonio,San Antonio,29.48733319,-98.50730534,1364905,United States of America,US,USA,Texas
Jackson,Jackson,32.29881533,-90.18499679,213799,United States of America,US,USA,Mississippi
Raleigh,Raleigh,35.81878135,-78.64469344,789991.5,United States of America,US,USA,North Carolina
Cleveland,Cleveland,41.4699868,-81.69499821,1169757,United States of America,US,USA,Ohio
Cincinnati,Cincinnati,39.16188479,-84.45692265,971191,United States of America,US,USA,Ohio
Nashville,Nashville,36.16997438,-86.77998499,703926,United States of America,US,USA,Tennessee
Memphis,Memphis,35.1199868,-89.99999516,753843.5,United States of America,US,USA,Tennessee
Norfolk,Norfolk,36.84995872,-76.28000574,645336,United States of America,US,USA,Virginia
Milwaukee,Milwaukee,43.05265505,-87.91996708,983590,United States of America,US,USA,Wisconsin
Buffalo,Buffalo,42.87997825,-78.88000208,647778.5,United States of America,US,USA,New York
Pittsburgh,Pittsburgh,40.4299986,-79.99998539,1535267.5,United States of America,US,USA,Pennsylvania
Kodiak,Kodiak,57.78999839,-152.4069869,7804.5,United States of America,US,USA,Alaska
Cold Bay,Cold Bay,55.20000144,-162.7150916,154,United States of America,US,USA,Alaska
Bethel,Bethel,60.79330345,-161.7557961,5440.5,United States of America,US,USA,Alaska
Point Hope,Point Hope,68.34772605,-166.8080201,461,United States of America,US,USA,Alaska
Barrow,Barrow,71.29056968,-156.78858,3412,United States of America,US,USA,Alaska
Nome,Nome,64.50610008,-165.4063744,3021,United States of America,US,USA,Alaska
Valdez,Valdez,61.13599571,-146.348287,3283,United States of America,US,USA,Alaska
Juneau,Juneau,58.31412661,-134.419997,26172,United States of America,US,USA,Alaska
Fairbanks,Fairbanks,64.83698427,-147.7106586,43608.5,United States of America,US,USA,Alaska
Prudhoe Bay,Prudhoe Bay,70.29218101,-148.6693598,2337,United States of America,US,USA,Alaska
Minneapolis,Minneapolis,44.97997927,-93.25178634,1491886.5,United States of America,US,USA,Minnesota
Honolulu,Honolulu,21.30687644,-157.8579979,578828.5,United States of America,US,USA,Hawaii
Seattle,Seattle,47.57000205,-122.339985,1821684.5,United States of America,US,USA,Washington
Phoenix,Phoenix,33.53997988,-112.0699917,2436022.5,United States of America,US,USA,Arizona
San Diego,San Diego,32.82002382,-117.1799899,1938570.5,United States of America,US,USA,California
St. Louis,St. Louis,38.63501772,-90.23998051,1259958,United States of America,US,USA,Missouri
New Orleans,New Orleans,29.99500246,-90.03996688,527428.5,United States of America,US,USA,Louisiana
Dallas,Dallas,32.82002382,-96.84001693,3004852,United States of America,US,USA,Texas
Boston,Boston,42.32996014,-71.07001367,2528070.5,United States of America,US,USA,Massachusetts
Tampa,Tampa,27.94698793,-82.45862085,1319232.5,United States of America,US,USA,Florida
Philadelphia,Philadelphia,39.99997316,-75.16999597,3504775,United States of America,US,USA,Pennsylvania
Detroit,Detroit,42.32996014,-83.08005579,2526135,United States of America,US,USA,Michigan
Anchorage,Anchorage,61.21996991,-149.9002149,252068,United States of America,US,USA,Alaska
San Francisco,San Francisco,37.74000775,-122.4599777,2091036,United States of America,US,USA,California
Denver,Denver,39.73918805,-104.984016,1930799.5,United States of America,US,USA,Colorado
Houston,Houston,29.81997438,-95.33997929,4053287,United States of America,US,USA,Texas
Miami,Miami,25.7876107,-80.22410608,2983947,United States of America,US,USA,Florida
Atlanta,Atlanta,33.83001385,-84.39994938,2464454,United States of America,US,USA,Georgia
Chicago,Chicago,41.82999066,-87.75005497,5915976,United States of America,US,USA,Illinois
Los Angeles,Los Angeles,33.98997825,-118.1799805,8097410,United States of America,US,USA,California
"Washington, D.C.","Washington, D.C.",38.89954938,-77.00941858,2445216.5,United States of America,US,USA,District of Columbia
New York,New York,40.74997906,-73.98001693,13524139,United States of America,US,USA,New York
Christiansted,Christiansted,17.75037518,-64.749986,32543,United States Virgin Islands,VI,VIR,
Colonia del Sacramento,Colonia del Sacramento,-34.47999901,-57.84000247,21714,Uruguay,UY,URY,Colonia
Trinidad,Trinidad,-33.54399894,-56.90099656,21093,Uruguay,UY,URY,Flores
Fray Bentos,Fray Bentos,-33.13899903,-58.30399747,23279,Uruguay,UY,URY,R?o Negro
Canelones,Canelones,-34.53800401,-56.28400149,19698,Uruguay,UY,URY,Canelones
Florida,Florida,-34.09900201,-56.21499845,32234,Uruguay,UY,URY,Florida
Artigas,Artigas,-30.41598712,-56.48602014,32072.5,Uruguay,UY,URY,Artigas
Baltasar Brum,Baltasar Brum,-30.7300248,-57.31997441,2432,Uruguay,UY,URY,Artigas
Tranqueras,Tranqueras,-31.20002195,-55.74996688,4775.5,Uruguay,UY,URY,Rivera
Tacuarembo,Tacuarembo,-31.70996499,-55.98000452,53065.5,Uruguay,UY,URY,Tacuaremb?
Paso de los Toros,Paso de los Toros,-32.8100012,-56.51004968,11450,Uruguay,UY,URY,Tacuaremb?
Vergara,Vergara,-32.92999388,-53.94999923,3749,Uruguay,UY,URY,Treinta y Tres
Treinta y Tres,Treinta y Tres,-33.23002724,-54.38002466,26668.5,Uruguay,UY,URY,Treinta y Tres
Santa Lucia,Santa Lucia,-34.47000324,-56.39997888,15264.5,Uruguay,UY,URY,Canelones
Jose Batlle y Ordonez,Jose Batlle y Ordonez,-33.47001259,-55.12000533,2438,Uruguay,UY,URY,Lavalleja
Minas,Minas,-34.37000934,-55.23002446,39602.5,Uruguay,UY,URY,Lavalleja
Maldonado,Maldonado,-34.91002806,-54.95998926,51877.5,Uruguay,UY,URY,Maldonado
Punta del Este,Punta del Este,-34.96997272,-54.94998987,84140,Uruguay,UY,URY,Maldonado
Aigua,Aigua,-34.19999388,-54.75000208,2622,Uruguay,UY,URY,Maldonado
La Paloma,La Paloma,-34.66999103,-54.1699858,2897,Uruguay,UY,URY,Rocha
Carmelo,Carmelo,-33.98961912,-58.29999211,15113.5,Uruguay,UY,URY,Colonia
Bella Union,Bella Union,-30.25961424,-57.59995732,17947,Uruguay,UY,URY,Artigas
Mercedes,Mercedes,-33.25953449,-58.02998275,41951.5,Uruguay,UY,URY,Soriano
Melo,Melo,-32.35948606,-54.17998519,53258.5,Uruguay,UY,URY,Cerro Largo
Rivera,Rivera,-30.89957518,-55.56000431,132232.5,Uruguay,UY,URY,Rivera
Lascano,Lascano,-33.66958698,-54.20000981,5215.5,Uruguay,UY,URY,Rocha
Castillos,Castillos,-34.16960814,-53.82998071,7686,Uruguay,UY,URY,Rocha
San Jose de Mayo,San Jose de Mayo,-34.34995888,-56.7099858,36462,Uruguay,UY,URY,San Jos?
Rocha,Rocha,-34.48297402,-54.33302494,26194.5,Uruguay,UY,URY,Rocha
Paysandu,Paysandu,-32.32997882,-58.0799797,76132.5,Uruguay,UY,URY,Paysand?
Salto,Salto,-31.39034625,-57.9686945,102756.5,Uruguay,UY,URY,Salto
Durazno,Durazno,-33.41001626,-56.51004968,33981.5,Uruguay,UY,URY,Durazno
Montevideo,Montevideo,-34.85804157,-56.17105229,759162,Uruguay,UY,URY,Montevideo
Khujayli,Khujayli,42.4047101,59.45165767,55200.5,Uzbekistan,UZ,UZB,Karakalpakstan
Urgut,Urgut,39.40070742,67.26069006,73524,Uzbekistan,UZ,UZB,Samarkand
Kattaqorgon,Kattaqorgon,39.90070274,66.2607511,153247.5,Uzbekistan,UZ,UZB,Samarkand
Denow,Denow,38.27715843,67.88716345,143134,Uzbekistan,UZ,UZB,Surkhandarya
Guliston,Guliston,40.49573102,68.79072587,74446.5,Uzbekistan,UZ,UZB,Sirdaryo
Iskandar,Iskandar,41.55073122,69.68074906,111634.5,Uzbekistan,UZ,UZB,Tashkent
Chirchiq,Chirchiq,41.45497479,69.55998124,155093.5,Uzbekistan,UZ,UZB,Tashkent
Kogon,Kogon,39.72107546,64.54576534,85093,Uzbekistan,UZ,UZB,Bukhoro
Khiwa,Khiwa,41.39112856,60.35573686,102659,Uzbekistan,UZ,UZB,Khorezm
Chimboy,Chimboy,42.93113792,59.77075964,34277.5,Uzbekistan,UZ,UZB,Karakalpakstan
Qunghirot,Qunghirot,43.0704059,58.90001176,57758,Uzbekistan,UZ,UZB,Karakalpakstan
Zarafshon,Zarafshon,41.58222801,64.20180701,55292.5,Uzbekistan,UZ,UZB,Navoi
Navoi,Navoi,40.1104057,65.35496659,172276.5,Uzbekistan,UZ,UZB,Navoi
Shahrisabz,Shahrisabz,39.06178754,66.83146562,277798,Uzbekistan,UZ,UZB,Kashkadarya
Qarshi,Qarshi,38.87042971,65.80000403,304629.5,Uzbekistan,UZ,UZB,Kashkadarya
Qoqon,Qoqon,40.54040529,70.94000037,271250,Uzbekistan,UZ,UZB,Ferghana
Jizzax,Jizzax,40.10038047,67.83000932,193997,Uzbekistan,UZ,UZB,Jizzakh
Angren,Angren,41.03037539,70.15493201,164513.5,Uzbekistan,UZ,UZB,Tashkent
Olmaliq,Olmaliq,40.85043805,69.59501786,119768,Uzbekistan,UZ,UZB,Tashkent
Muynoq,Muynoq,43.76832196,59.0213997,13000,Uzbekistan,UZ,UZB,Karakalpakstan
Termiz,Termiz,37.23293276,67.27293738,159036,Uzbekistan,UZ,UZB,Surkhandarya
Fargona,Fargona,40.3899752,71.78000077,482000,Uzbekistan,UZ,UZB,Ferghana
Namangan,Namangan,41.00001548,71.66998165,599600,Uzbekistan,UZ,UZB,Namangan
Urgentch,Urgentch,41.5599813,60.64000891,126476.5,Uzbekistan,UZ,UZB,Khorezm
Bukhara,Bukhara,39.78001243,64.43001013,283560,Uzbekistan,UZ,UZB,Bukhoro
Nukus,Nukus,42.47000327,59.61500688,228211,Uzbekistan,UZ,UZB,Karakalpakstan
Andijon,Andijon,40.79000246,72.33996659,486950,Uzbekistan,UZ,UZB,Andijon
Samarqand,Samarqand,39.67001914,66.94499874,652150,Uzbekistan,UZ,UZB,Samarkand
Tashkent,Tashkent,41.31170188,69.29493282,2081014,Uzbekistan,UZ,UZB,Tashkent
Luganville,Luganville,-15.51255573,167.1766068,10634.5,Vanuatu,VU,VUT,Sanma
Port Vila,Port-Vila,-17.7333504,168.3166406,39970.5,Vanuatu,VU,VUT,Shefa
Vatican City,Vatican City,41.90001223,12.44780839,832,Vatican (Holy Sea),VA,VAT,Lazio
San Carlos,San Carlos,9.657999007,-68.58999854,77192,Venezuela,VE,VEN,Cojedes
San Felipe,San Felipe,10.33599598,-68.74599552,76766,Venezuela,VE,VEN,Yaracuy
San Juan De Los Morros,San Juan De Los Morros,9.900999019,-67.35400159,87739,Venezuela,VE,VEN,Gu?rico
La Asuncion,La Asuncion,11.03333403,-63.8833315,35084,Venezuela,VE,VEN,Nueva Esparta
Guasdualito,Guasdualito,7.239983133,-70.73998214,28287.5,Venezuela,VE,VEN,Apure
Barinas,Barinas,8.59997764,-70.25001205,261405.5,Venezuela,VE,VEN,Barinas
Valera,Valera,9.319959533,-70.6200153,142461.5,Venezuela,VE,VEN,Trujillo
Cabimas,Cabimas,10.42999514,-71.44999048,320956,Venezuela,VE,VEN,Trujillo
Carora,Carora,10.18998395,-70.07999658,121749.5,Venezuela,VE,VEN,Lara
Guanare,Guanare,9.049976012,-69.75001673,131964,Venezuela,VE,VEN,Portuguesa
Puerto la Cruz,Puerto la Cruz,10.16995933,-64.68001612,500464,Venezuela,VE,VEN,Anzo?tegui
Anaco,Anaco,9.440003885,-64.4600037,100118,Venezuela,VE,VEN,Anzo?tegui
Los Teques,Los Teques,10.41996991,-67.02002832,303470,Venezuela,VE,VEN,Distrito Capital
Valle de la Pascua,Valle de la Pascua,9.209992085,-66.019986,86273.5,Venezuela,VE,VEN,Gu?rico
Ocumare del Tuy,Ocumare del Tuy,10.11998822,-66.77999129,130824,Venezuela,VE,VEN,Miranda
Carupano,Carupano,10.67000633,-63.23000126,119187.5,Venezuela,VE,VEN,Sucre
Trujillo,Trujillo,9.38039512,-70.44000045,44231.5,Venezuela,VE,VEN,Trujillo
Santa Rita,Santa Rita,10.53182698,-71.50394902,21095,Venezuela,VE,VEN,Trujillo
Machiques,Machiques,10.07043052,-72.54994918,44936.5,Venezuela,VE,VEN,Zulia
San Carlos del Zulia,San Carlos del Zulia,9.010391865,-71.91998763,76935,Venezuela,VE,VEN,Zulia
Puerto Cabello,Puerto Cabello,10.47043194,-68.17000981,174000,Venezuela,VE,VEN,Carabobo
Acarigua,Acarigua,9.580382913,-69.20002446,202312.5,Venezuela,VE,VEN,Portuguesa
Upata,Upata,8.020426452,-62.40999964,53474.5,Venezuela,VE,VEN,Bol?var
El Manteco,El Manteco,7.35038983,-62.53332544,2215,Venezuela,VE,VEN,Bol?var
Chaguaramas,Chaguaramas,9.215934874,-63.75226913,12500,Venezuela,VE,VEN,Anzo?tegui
Barcelona,Barcelona,10.13037518,-64.72001367,361430,Venezuela,VE,VEN,Anzo?tegui
El Tigre,El Tigre,8.890347513,-64.26001591,174219.5,Venezuela,VE,VEN,Anzo?tegui
Maiquetia,Maiquetia,10.60039817,-66.9699797,184003,Venezuela,VE,VEN,Vargas
Calabozo,Calabozo,8.930396748,-67.43997685,110907,Venezuela,VE,VEN,Gu?rico
Zaraza,Zaraza,9.340397562,-65.32000289,35279.5,Venezuela,VE,VEN,Gu?rico
Altagracia de Orituco,Altagracia de Orituco,9.85041811,-66.37998987,34427,Venezuela,VE,VEN,Gu?rico
Tucupita,Tucupita,9.060492166,-62.05999516,49704,Venezuela,VE,VEN,Monagas
Porlamar,Porlamar,10.9603762,-63.84998926,142027,Venezuela,VE,VEN,Nueva Esparta
San Fernando de Apure,San Fernando de Apure,7.899994526,-67.46994918,100740,Venezuela,VE,VEN,Apure
Barquisimeto,Barquisimeto,10.04999249,-69.29996668,962745,Venezuela,VE,VEN,Lara
Maturin,Maturin,9.749959126,-63.17003076,357707.5,Venezuela,VE,VEN,Monagas
Cumana,Cumana,10.44999392,-64.18002079,287693,Venezuela,VE,VEN,Sucre
Coro,Coro,11.42001223,-69.67999516,184098,Venezuela,VE,VEN,Falc?n
Punto Fijo,Punto Fijo,11.71999392,-70.21001449,183260,Venezuela,VE,VEN,Falc?n
La Esmeralda,La Esmeralda,3.173823058,-65.54660405,149.5,Venezuela,VE,VEN,Amazonas
Ciudad Bolivar,Ciudad Bolivar,8.099982319,-63.60000452,317971.5,Venezuela,VE,VEN,Bol?var
El Dorado,El Dorado,6.733295714,-61.6333287,2383,Venezuela,VE,VEN,Bol?var
Maracay,Maracay,10.2468797,-67.59580713,1007000,Venezuela,VE,VEN,Aragua
Merida,Merida,8.399989847,-71.13001001,275184,Venezuela,VE,VEN,M?rida
Puerto Ayacucho,Puerto Ayacucho,5.663903624,-67.62360905,51622.5,Venezuela,VE,VEN,Amazonas
San Cristobal,San Cristobal,7.770002461,-72.24996749,342690.5,Venezuela,VE,VEN,T?chira
Valencia,Valencia,10.22998151,-67.9800214,1569526.5,Venezuela,VE,VEN,Carabobo
Ciudad Guayana,Ciudad Guayana,8.370017516,-62.61998682,634317.5,Venezuela,VE,VEN,Bol?var
Maracaibo,Maracaibo,10.72997683,-71.65997766,1764650,Venezuela,VE,VEN,Zulia
Caracas,Caracas,10.50099855,-66.91703719,2400339.5,Venezuela,VE,VEN,Distrito Capital
Tay Ninh,Tay Ninh,11.32299911,106.1469997,126370,Vietnam,VN,VNM,T?y Ninh
Luan Chau,Luan Chau,21.74000399,103.3430047,7335,Vietnam,VN,VNM,?i?n Bi?n
Bac Kan,Bac Kan,22.1333333,105.8333333,29227,Vietnam,VN,VNM,Bac Kan
Lang Son,Lang Son,21.8459971,106.7570016,148000,Vietnam,VN,VNM,L?ng S?n
Son La,Son La,21.32800214,103.9100047,19054,Vietnam,VN,VNM,Son La
Tuyen Quang,Tuyen Quang,21.8179981,105.2109996,36430,Vietnam,VN,VNM,Tuy?n Quang
Yen Bai,Yen Bai,21.70500304,104.8750026,96540,Vietnam,VN,VNM,Y?n B?i
Hai Duong,Hai Duong,20.94200108,106.3310046,58030,Vietnam,VN,VNM,H?i D??ng 
Thai Binh,Thai Binh,20.45030412,106.3330296,210000,Vietnam,VN,VNM,Th?i B?nh
Tuy Hoa,Tuy Hoa,13.08200402,109.3159987,69596,Vietnam,VN,VNM,Ph? Y?n
Thu Dau Mot,Thu Dau Mot,10.96907408,106.6527455,244277,Vietnam,VN,VNM,B?nh Duong
Dong Ha,Dong Ha,16.8499981,107.1333007,17662,Vietnam,VN,VNM,Qu?ng Tr? 
Cao Lanh,Cao Lanh,10.46700013,105.6359976,149837,Vietnam,VN,VNM,??ng Th?p 
Truc Giang,Truc Giang,10.234998,106.3749966,59442,Vietnam,VN,VNM,B?n Tre 
Tra Vinh,Tra Vinh,9.934002087,106.3340017,131360,Vietnam,VN,VNM,Tr? Vinh
Vinh Long,Vinh Long,10.256004,105.9640026,103314,Vietnam,VN,VNM,Vinh Long
Cao Bang,Cao Bang,22.66399806,106.2680046,41112,Vietnam,VN,VNM,Cao B?ng
Hong Gai,Hong Gai,20.9604118,107.1000154,160490.5,Vietnam,VN,VNM,Qu?ng Ninh 
Cam Pha,Cam Pha,21.04043276,107.320002,75925.5,Vietnam,VN,VNM,Qu?ng Ninh 
Lao Chi,Lao Chi,22.50135134,103.9659948,51854,Vietnam,VN,VNM,L?o Cai
Hoa Binh,Hoa Binh,20.81370241,105.3383142,102381,Vietnam,VN,VNM,H?a B?nh
Son Tay,Son Tay,21.13817873,105.5050223,115091.5,Vietnam,VN,VNM,H? T?y
Ninh Binh,Ninh Binh,20.25430503,105.9750195,130517,Vietnam,VN,VNM,Ninh B?nh
Viet Tri,Viet Tri,21.33041506,105.4299882,305144,Vietnam,VN,VNM,Ph? Th? 
Bac Giang,Bac Giang,21.26700808,106.2000187,53728,Vietnam,VN,VNM,B?c Giang 
Ha Tinh,Ha Tinh,18.33377626,105.900037,165396,Vietnam,VN,VNM,Ha Tinh
Buon Me Thuot,Buon Me Thuot,12.66704205,108.0499833,248460,Vietnam,VN,VNM,Dak Lak
Da Lat,Da Lat,11.93042035,108.4199865,193698,Vietnam,VN,VNM,L?m ??ng 
Phan Rang,Phan Rang,11.56703168,108.9833113,135646.5,Vietnam,VN,VNM,Ninh Thu?n 
Hon Quan,Hon Quan,11.65038576,106.6000459,40279,Vietnam,VN,VNM,B?nh Ph??c 
Kon Tum,Kon Tum,14.38375897,107.9833207,76449,Vietnam,VN,VNM,Kon Tum
Quang Ngai,Quang Ngai,15.15043052,108.8299873,184625.5,Vietnam,VN,VNM,Qu?ng Ng?i? 
Quang Tri,Quang Tri,16.7503587,107.2000093,72722,Vietnam,VN,VNM,Qu?ng Tr? 
Vung Tau,Vung Tau,10.35537437,107.0849776,229225,Vietnam,VN,VNM,B? R?a?V?ng T?u 
Phan Thiet,Phan Thiet,10.933737,108.1000577,248749,Vietnam,VN,VNM,B?nh Thu?n 
Long Xuyen,Long Xuyen,10.38038576,105.4200146,254076.5,Vietnam,VN,VNM,An Giang
Chau Doc,Chau Doc,10.70039207,105.1166739,70239,Vietnam,VN,VNM,An Giang
Rach Gia,Rach Gia,10.01539512,105.0913525,252830,Vietnam,VN,VNM,Ki?n Giang
Tan An,Tan An,10.53373557,106.416698,101149.5,Vietnam,VN,VNM,Long An
My Tho,My Tho,10.35041343,106.3500354,123226.5,Vietnam,VN,VNM,Ti?n Giang 
Bac Lieu,Bac Lieu,9.280375385,105.7199963,187500,Vietnam,VN,VNM,B?c Li?u 
Ca Mau,Ca Mau,9.177358418,105.1500052,280765.5,Vietnam,VN,VNM,C? Mau
Soc Trang,Soc Trang,9.603740661,105.9800321,236961,Vietnam,VN,VNM,S?c Trang
Ha Giang,Ha Giang,22.83365664,104.9833488,35526,Vietnam,VN,VNM,H? Giang
Thai Nguyen,Thai Nguyen,21.59995933,105.8300154,415000,Vietnam,VN,VNM,Th?i Nguy?n
Thanh Hoa,Thanh Hoa,19.8200163,105.7999914,197551,Vietnam,VN,VNM,Thanh H?a
Nam Dinh,Nam Dinh,20.42003135,106.2000187,243186,Vietnam,VN,VNM,Nam ??nh 
Vinh,Vinh,18.6999813,105.6799987,514426.5,Vietnam,VN,VNM,Ngh? An 
Dong Hoi,Dong Hoi,17.48333722,106.6000459,110152.5,Vietnam,VN,VNM,Qu?ng B?nh 
Play Ku,Play Ku,13.98329246,108.0000122,128562.5,Vietnam,VN,VNM,Gia Lai
Nha Trang,Nha Trang,12.25003908,109.1700183,347498.5,Vietnam,VN,VNM,Kh?nh H?a
Cam Ranh,Cam Ranh,11.90202415,109.2206612,85327,Vietnam,VN,VNM,Kh?nh H?a
Qui Nhon,Qui Nhon,13.77997154,109.1800435,543095,Vietnam,VN,VNM,B?nh ??nh 
Hue,Hue,16.46998822,107.5800378,645000,Vietnam,VN,VNM,Th?a Thi?n?Hu? 
Bien Hoa,Bien Hoa,10.97001385,106.8300577,652646,Vietnam,VN,VNM,??ng Nai 
Can Tho,Can Tho,10.04999249,105.7700191,690299,Vietnam,VN,VNM,Can Tho
Haiphong,Haiphong,20.83000633,106.6800927,1285847.5,Vietnam,VN,VNM,Qu?ng Ninh
Da Nang,Da Nang,16.06003908,108.2499711,943534.5,Vietnam,VN,VNM,Da Nang
Hanoi,Hanoi,21.03332725,105.8500142,2904635,Vietnam,VN,VNM,Th?i Nguy?n
Ho Chi Minh City,Ho Chi Minh City,10.78002545,106.6950272,4390665.5,Vietnam,VN,VNM,Ho Chi Minh City
Bir Lehlou,Bir Lehlou,26.11916669,-9.652522218,350,Western Sahara,EH,SAH,
Al Bayda,Al Bayda,13.9789981,45.57400265,37821,Yemen,YE,YEM,Al Bayda'
'Ataq,'Ataq,14.55000311,46.80000058,37315,Yemen,YE,YEM,Shabwah
Marib,Marib,15.42099607,45.33399954,16794,Yemen,YE,YEM,Ma'rib
Dhamar,Dhamar,14.5574693,44.3874609,191259,Yemen,YE,YEM,Dhamar
Ibb,Ibb,13.97585105,44.17088497,234837,Yemen,YE,YEM,Ibb
Ash Shihr,Ash Shihr,14.75931744,49.60915767,54274,Yemen,YE,YEM,Hadramawt
Zabid,Zabid,14.19508832,43.31553666,102547,Yemen,YE,YEM,Al Hudaydah
Hajjah,Hajjah,15.69174115,43.60213415,125918,Yemen,YE,YEM,Hajjah
Lahij,Lahij,13.05818097,44.88376135,44831.5,Yemen,YE,YEM,Lahij
Al Ghaydah,Al Ghaydah,16.23940798,52.1637821,23702,Yemen,YE,YEM,Al Mahrah
Rida,Rida,14.42949261,44.8341003,45233,Yemen,YE,YEM,Al Bayda'
Hadiboh,Hadiboh,12.65187502,54.02392696,9970.5,Yemen,YE,YEM,Hadramawt
Saywun,Saywun,15.94299196,48.78734737,68747,Yemen,YE,YEM,Hadramawt
Sadah,Sadah,16.93977867,43.84976762,105542,Yemen,YE,YEM,Sa`dah
Al Hudaydah,Al Hudaydah,14.79794558,42.95297481,627610.5,Yemen,YE,YEM,Al Hudaydah
Sayhut,Sayhut,15.21050437,51.24544023,189,Yemen,YE,YEM,Al Mahrah
Al Mukalla,Al Mukalla,14.54116538,49.12593135,194080.5,Yemen,YE,YEM,Hadramawt
Taizz,Taizz,13.60445253,44.03942012,683111,Yemen,YE,YEM,Ta`izz
Aden,Aden,12.77972251,45.00949011,775301,Yemen,YE,YEM,`Adan
Sanaa,Sanaa,15.3547333,44.20659338,1921926.5,Yemen,YE,YEM,Amanat Al Asimah
Kawambwa,Kawambwa,-9.779520651,29.08002315,20355,Zambia,ZM,ZMB,Luapula
Nchelenge,Nchelenge,-9.349572735,28.73001868,15904,Zambia,ZM,ZMB,Luapula
Chinsali,Chinsali,-10.54960285,32.0599963,7482.5,Zambia,ZM,ZMB,Northern
Kasama,Kasama,-10.19959837,31.17994665,156500,Zambia,ZM,ZMB,Northern
Kapiri Mposhi,Kapiri Mposhi,-13.96960081,28.65999711,30078,Zambia,ZM,ZMB,Central
Mumbwa,Mumbwa,-14.97961668,27.07001664,14408.5,Zambia,ZM,ZMB,Central
Chingola,Chingola,-12.53961058,27.85002071,165289.5,Zambia,ZM,ZMB,Copperbelt
Chililabombwe,Chililabombwe,-12.36959511,27.8199967,69698,Zambia,ZM,ZMB,Copperbelt
Nyimba,Nyimba,-14.54951373,30.80999508,814,Zambia,ZM,ZMB,Eastern
Lundazi,Lundazi,-12.28954832,33.17000606,9540.5,Zambia,ZM,ZMB,Eastern
Chipata,Chipata,-13.62956989,32.64001257,82455,Zambia,ZM,ZMB,Eastern
Mwinilunga,Mwinilunga,-11.73955605,24.4399963,8336.5,Zambia,ZM,ZMB,North-Western
Kasempa,Kasempa,-13.4596061,25.82001542,5622,Zambia,ZM,ZMB,North-Western
Solwezi,Solwezi,-12.17958087,26.39998002,51793.5,Zambia,ZM,ZMB,North-Western
Choma,Choma,-16.80947915,26.97002274,42324,Zambia,ZM,ZMB,Southern
Mongu,Mongu,-15.27959837,23.12002519,45098.5,Zambia,ZM,ZMB,Western
Kaoma,Kaoma,-14.77962889,24.79997432,7259,Zambia,ZM,ZMB,Western
Sesheke,Sesheke,-17.46954222,24.30000484,10177.5,Zambia,ZM,ZMB,Western
Lukulu,Lukulu,-14.38957518,23.24001786,3349,Zambia,ZM,ZMB,Western
Kalabo,Kalabo,-14.98959023,22.68000036,7731,Zambia,ZM,ZMB,Western
Senanga,Senanga,-16.11959878,23.27004187,10005,Zambia,ZM,ZMB,Western
Mansa,Mansa,-11.20000242,28.89000891,31357,Zambia,ZM,ZMB,Luapula
Mpika,Mpika,-11.83004148,31.45998124,17242.5,Zambia,ZM,ZMB,Northern
Mbala,Mbala,-8.840043112,31.37001257,18384,Zambia,ZM,ZMB,Northern
Luanshya,Luanshya,-13.13332111,28.40001298,132679,Zambia,ZM,ZMB,Copperbelt
Ndola,Ndola,-12.99994424,28.65002356,395428.5,Zambia,ZM,ZMB,Copperbelt
Zambezi,Zambezi,-13.54001463,23.10994828,4987.5,Zambia,ZM,ZMB,North-Western
Kafue,Kafue,-15.78003294,28.18002641,25725.5,Zambia,ZM,ZMB,Southern
Mazabuka,Mazabuka,-15.86002806,27.76000036,57874.5,Zambia,ZM,ZMB,Southern
Kabwe,Kabwe,-14.44001137,28.44998409,188667,Zambia,ZM,ZMB,Central
Mufulira,Mufulira,-12.54999754,28.25996985,137062,Zambia,ZM,ZMB,Copperbelt
Kitwe,Kitwe,-12.81003335,28.22002397,402907.5,Zambia,ZM,ZMB,Copperbelt
Livingstone,Livingstone,-17.86000934,25.86001298,137341.5,Zambia,ZM,ZMB,Southern
Lusaka,Lusaka,-15.41664427,28.28332759,1297720,Zambia,ZM,ZMB,Lusaka
Mazowe,Mazowe,-17.51961668,30.97003699,9966,Zimbabwe,ZW,ZWE,Mashonaland Central
Shamva,Shamva,-17.31962889,31.57000036,8521,Zimbabwe,ZW,ZWE,Mashonaland Central
Victoria Falls,Victoria Falls,-17.92961749,25.8400142,23964.5,Zimbabwe,ZW,ZWE,Matabeleland North
Zvishavane,Zvishavane,-20.32957436,30.04998979,34557.5,Zimbabwe,ZW,ZWE,Midlands
Kwekwe,Kwekwe,-18.92960814,29.79997921,80788,Zimbabwe,ZW,ZWE,Midlands
Plumtree,Plumtree,-20.47953937,27.8199967,1959.5,Zimbabwe,ZW,ZWE,Matabeleland South
Beitbridge,Beitbridge,-22.20961465,29.98999345,13759.5,Zimbabwe,ZW,ZWE,Matabeleland South
Gwanda,Gwanda,-20.93961465,29.01000159,8252.5,Zimbabwe,ZW,ZWE,Matabeleland South
Chiredzi,Chiredzi,-21.04958209,31.66002071,17816.5,Zimbabwe,ZW,ZWE,Masvingo
Masvingo,Masvingo,-20.05961668,30.8200203,76300.5,Zimbabwe,ZW,ZWE,Masvingo
Karoi,Karoi,-16.81955605,29.67998653,13194,Zimbabwe,ZW,ZWE,Mashonaland West
Chinhoyi,Chinhoyi,-17.35962645,30.18000769,52812,Zimbabwe,ZW,ZWE,Mashonaland West
Kariba,Kariba,-16.52959959,28.80004024,23133.5,Zimbabwe,ZW,ZWE,Mashonaland West
Hwange,Hwange,-18.37000405,26.50002559,33599.5,Zimbabwe,ZW,ZWE,Matabeleland North
Gweru,Gweru,-19.45004148,29.82002966,164715.5,Zimbabwe,ZW,ZWE,Midlands
Mutare,Mutare,-18.97001911,32.6500378,216785,Zimbabwe,ZW,ZWE,Manicaland
Kadoma,Kadoma,-18.33000649,29.90994665,56400,Zimbabwe,ZW,ZWE,Mashonaland West
Chitungwiza,Chitungwiza,-18.00000079,31.10000321,331071,Zimbabwe,ZW,ZWE,Harare
Harare,Harare,-17.81778969,31.04470943,1557406.5,Zimbabwe,ZW,ZWE,Harare
Bulawayo,Bulawayo,-20.16999754,28.58000199,697096,Zimbabwe,ZW,ZWE,Bulawayo
'''
