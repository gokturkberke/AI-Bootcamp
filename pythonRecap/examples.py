# İsminizi içeren bir string değişkeni oluşturun.
# Bu stringin ilk ve son karakterini yazdırın. Ayrıca tüm harfleri büyük yaparak ekrana yazdırın.
name = "Berke"
print("İlk karakter:", name[0])
print("Son karakter:", name[-1])
print("Tüm harfler büyük:", name.upper())


#Aşağıdaki string içinde "veri" kelimesi geçiyor mu kontrol edin.
# Ardından bu stringi boşluklardan bölerek liste haline getirin.

sentence = "Veri bilimi yapay zeka ile birleştiğinde güçlü sonuçlar doğurabilir."
print("veri" in sentence)
print(sentence.split())

liste1 = ["berke",21,True]
print(len(liste1))
liste1.append("yeni eleman")
liste1.pop(1)
print(liste1)


# iki parametre alan bir fonksiyon tanımlayın. ortalam donsun
def ortalama(a,b):
    return (a + b) / 2

def age_check(age):
    if age < 18:
        return "Cok gencsin"
    elif age > 18 and age < 40:
        return "guzel yasindasin"
    else:
        return "cok yaslisin"
    
# icersiinde sayilar olan bir liste icindeki saytilari dolasarak iki katini ekrana yazdirin
liste2 = [1, 2, 3, 4, 5]
for sayi in liste2:
    print(sayi * 2)
    
# 1 den baslayarak 20 dahil olacak skeidle cift sayilari yazdirin while dongusu ile
while sayi <=20:
    if sayi % 2 == 0:
        print(sayi)
    sayi += 1
    
# haftalik maasi hesaplayan bir fonksiyon tanimlayin.
def calculate_wage(hourly_wage, total_hours):
    if total_hours >= 40:
        overtime_hours = total_hours - 40
        total_wage = hourly_wage * 40 + (overtime_hours * 1.5 * hourly_wage)
        return total_wage
    else:
        total_wage = hourly_wage * total_hours
    return total_wage

# -----------------------------------------------------
import pandas as pd
import numpy as np
import seaborn as sns

# 1d ve 2d arrayler olusturun
a = np.array([1, 2, 3, 4, 5,6])
b = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)
print(b.shape)
print(a.ndim)
print(b.ndim)
print(a.size)  
print(b.size)

# 5 elemanli rastgele sayilardan olusan array olstur
c = np.random.randint(1, 100, size=5)
print(c.mean())
print(c.std())
print(np.median(c))

# 0 ile 1 arasinda 10 esit aralikli sayi uretin
d = np.linspace(0, 1, 10)
#0.5ten buyuk olanlari yazdirin
print(d[d > 0.5])

#pandas serisi ikle bir seri olusturun yaslari tutan yas ortalamasi ve en kucuk yasi bulun
ages = pd.Series([25, 30, 22, 28, 35])
print("ages ortalaması:", ages.mean())
print("en küçük yaş:", ages.min())

#seaborn icinden diamonds veri setini alin
# sadece carat ve price sutunlarini iceren ilk 5 satiri yazdirin
df = sns.load_dataset('diamonds')
df[['carat', 'price']].head()

# fiyati 15000den fazla olan elmas sayisi
expensive_diamonds = df[df['price'] > 15000]
print("Fiyatı 15000'den fazla olan elmas sayısı:", expensive_diamonds.shape[0])

# cut sutundaki her bir kesim tipi icin ortalam fiyat hesaplayin
average_price_by_cut = df.groupby('cut')['price'].mean()
print("Ortalama fiyatlar:\n", average_price_by_cut)

#pivot table kullanarak her cut tipi icin hem ortalama carat hem de price degerlerini gosterin
pivot_table = df.pivot_table(index="cut",values=["carat", "price"], aggfunc="mean")
print("Pivot Table:\n", pivot_table)

# color sutunundaki kac farkli renk oldugunu bulun her rengin kac kez gectigini yazdirin
color_counts = df['color'].value_counts()
print("Renk sayıları:\n", color_counts)
print("Toplam renk sayısı:", len(color_counts))

# cut ve clarity kombinasyonlarina gore ortalama fiyatlari hesaplayin
average_price_by_cut_clarity = df.groupby(['cut', 'clarity'])['price'].mean()