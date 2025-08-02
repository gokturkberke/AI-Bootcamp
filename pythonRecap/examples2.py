text = "The Goal is to turn data into information, and information into insight."
a = text.upper()
splitted_text = a.replace(","," ").replace(".","").split()
print(splitted_text)

lst = ["D","A","T","A","S","C","I","E","N","C","E"]
print(len(lst))
print(lst[0],lst[10])
print(lst[0:4])
lst.pop(8)
lst.append("N")
lst.insert(8,"N")
print(lst)

dict = {'Christian' : ["America",18],
        'Daisy' : ["England",12],
        'Antonio' : ["Spain",22],
        'Dante' : ["Italy",25]}

print(dict.keys())
print(dict.values())

dict['Daisy'][1] =13

# yeni eleman ekleme
dict['Ahmet']= ["Turkey", 24]
print(dict)

print(dict.keys())

dict.pop('Antonio')
print(dict)

# liste icerisindeki tek be cift sayilari ayirma
l = [2,13,18,93,22]

def func(list):
    even = []
    odd = []
    for i in list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd

print(func(l))

# dereceye giren ogrenci isimleri var ilk 3 muhendis son uc tip enumarete kullanarak derecelerini fakulte ozelinde yazdirin
students = ["Ahmet", "Mehmet", "Ayse", "Fatma", "Ali", "Zeynep"]

for i,x in enumerate(students):
    if i < 3:
        i += 1
        print(f"{i}. Mühendis: {x}")
    else:
        i -= 2
        print(f"{i}. Tıp: {x}")
# Normal bir for döngüsünde sadece listedeki elemanları alırsınız. enumerate kullandığınızda ise döngünün her adımında (sıra_numarası, eleman) şeklinde bir çift alırsınız.
# Bu sayede sayaç tutmak için fazladan bir değişken oluşturmanıza gerek kalmaz.

# 3 adet lsite verilmis zip kullanara kdersleri birleştirip derslerin isimlerini ve notlarını yazdırın
ders_kodu = ["MAT101", "FIZ102", "KIM103"]
kredi = [3, 4, 2]
kontenjan = [30, 25, 20]

for a,b,c in zip(ders_kodu, kredi, kontenjan):
    print(f"Ders Kodu: {a}, Kredi: {b}, Kontenjan: {c}")
    
    
# asagida 2 adet set verilmistir istenilen eger 1.kume 2.kumeyi kapsiyor ise ortak elemanlari kapsamiyor ise 2.kumenin 1.kumeden farkini yazdiracak fonksiyon yaziniz
kume1 = set(["data", "python"])
kume2 = set(["data","function","qcut","lambda","python","miuul"])

def kume_kontrol(k1,k2):
    if k1.issubset(k2):
        ortak = k1.intersection(k2)
        print(f"Ortak Elemanlar: {ortak}")
    else:
        fark = k2.difference(k1)
        print(f"2. Kümenin 1. Kümeden Farkı: {fark}")
        
kume_kontrol(kume1, kume2)
        